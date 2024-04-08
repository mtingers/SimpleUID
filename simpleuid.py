"""
A naive Python example implementation.
"""


class Obfuscator:
    """
    Singleton pattern to avoid multiple runs of init_obfuscator()
    """

    _instance = None
    _obfuscate_map: list[dict[str, str]] = []
    _obfuscate_map_r: list[dict[str, str]] = []

    def __new__(cls):
        if cls._instance is None:
            # cls._instance = cls.__new__(cls)
            cls._instance = super(Obfuscator, cls).__new__(cls)
            cls.init_obfuscator()

        return cls._instance

    @classmethod
    def init_obfuscator(cls):
        keys = "0123456789"
        options = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        option_idx = 0
        # 2**32-1 +  2**64-1 = 30 chars
        # maxlen = 31
        for _ in range(0, 31):
            cur_map = {}
            cur_map_r = {}
            for o in keys:
                cur_map[o] = options[option_idx]
                cur_map_r[options[option_idx]] = o
                option_idx += 1
                if option_idx >= len(options):
                    option_idx = 0
            cls._obfuscate_map.append(cur_map)
            cls._obfuscate_map_r.append(cur_map_r)

    def obfuscate(self, simple_id: int) -> str:
        x = list(str(simple_id).zfill(31))
        out = []
        for i in range(len(x)):
            c = self._obfuscate_map[i]
            out.append(c[x[i]])
        return "".join(out)

    def deobfuscate(self, obfuscated_id: str) -> int:
        x = []
        for i in range(len(obfuscated_id)):
            c = self._obfuscate_map_r[i]
            x.append(c[obfuscated_id[i]])
        return int("".join(x))


class SimpleUid:
    def __init__(self, namespace_id: int, start_id: int = 0):
        self.namespace_id = namespace_id
        id_str = str(start_id).zfill(20)
        self.latest_id = int(f"{self.namespace_id}{id_str}")
        self.obfuscator = Obfuscator()

    def next_id(self, previous_id: int) -> int:
        previous_id = int(str(previous_id).split(str(self.namespace_id), 1)[1])
        id_str = str(previous_id + 1).zfill(20)
        self.latest_id = int(f"{self.namespace_id}{id_str}")
        return self.latest_id

    def obfuscate(self, simple_id: int) -> str:
        return self.obfuscator.obfuscate(simple_id)

    def deobfuscate(self, obfuscated_id: str) -> int:
        return self.obfuscator.deobfuscate(obfuscated_id)


def example():
    print("Running example...")
    limit = 10000

    simple_id = SimpleUid(1, start_id=0)
    simple_id2 = SimpleUid(2, start_id=0)

    import time

    tstart = time.monotonic()
    for i in range(limit):
        cur_id = simple_id.next_id(simple_id.latest_id)
        obf_id = simple_id.obfuscate(cur_id)
        deobf_id = simple_id.deobfuscate(obf_id)
        assert cur_id == deobf_id
        if i % 1000 == 0:
            print(cur_id, obf_id, deobf_id)

        cur_id = simple_id2.next_id(simple_id2.latest_id)
        obf_id = simple_id2.obfuscate(cur_id)
        deobf_id = simple_id2.deobfuscate(obf_id)
        assert cur_id == deobf_id
        if i % 1000 == 0:
            print(cur_id, obf_id, deobf_id)

    tdiff = time.monotonic() - tstart
    print(f"in {tdiff} seconds:")
    print(f" - generated {limit*2} ids ({limit*2//tdiff}/s)")
    print(f" - obfuscated {limit*2} ids")
    print(f" - deobfuscated and asserted {limit*2} ids")


if __name__ == "__main__":
    example()
