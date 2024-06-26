# SimpleUID
SimpleUID - "sequential" IDs at scale

## Features
- auto-incrementable
- variable namespace size and value size
- ID obfuscation/deobfuscation for opaque layers

  
## Formats
SimpleUID is not a fixed size until initialized.  It takes a shape parameter to define:
- Namespace size
- ID size

For example, a 32x64 SimpleUID has a 2^32-1 amount of namespaces and 2^64-1 IDs available within the namespace.
```
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                   32 bit uint (namespace)                     |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                       64 bit uint                             |
    |                          (value)                              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

bits=96
namespace_max=2^32-1
id_max=2^64-1
total_max=namespace_max * id_max
```


```
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    | 16bit uint (namespace)      |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                       64 bit uint                             |
    |                          (value)                              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
bits=80
namespace_max=2^16-1
id_max=2^64-1
total_max=namespace_max * id_max
```


### Format Examples

Given a SimpleUID-32x64 `100000000000000000001`, it can be broken down into two sections: namespace and value:
- namespace: 1
- value: 1

Given a SimpleUID-32x64 `2100000000000000003818`:
- namespace: 21
- value: 3818 

Note that value is left padded to 20 places to provide uniqueness (even though it is an unsigned integer) and the namespace does not require any padding.

Example breakdown:
```yaml
namespace: 1
    id: 1
        output: 100000000000000000001
    id: 2
        output: 100000000000000000002

namespace: 2
    id: 1
        output: 200000000000000000001
    id: 2
        output: 200000000000000000002
```


## Python Example
```
➜  SimpleUID git:(main) ✗ python simpleuid.py
Running tests...
100000000000000000001 0AKUeoy8ISdmw6GQaku4EOYis2CMWgr 100000000000000000001
200000000000000000001 0AKUeoy8ISemw6GQaku4EOYis2CMWgr 200000000000000000001
100000000000000001001 0AKUeoy8ISdmw6GQaku4EOYis2CNWgr 100000000000000001001
200000000000000001001 0AKUeoy8ISemw6GQaku4EOYis2CNWgr 200000000000000001001
100000000000000002001 0AKUeoy8ISdmw6GQaku4EOYis2COWgr 100000000000000002001
200000000000000002001 0AKUeoy8ISemw6GQaku4EOYis2COWgr 200000000000000002001
100000000000000003001 0AKUeoy8ISdmw6GQaku4EOYis2CPWgr 100000000000000003001
200000000000000003001 0AKUeoy8ISemw6GQaku4EOYis2CPWgr 200000000000000003001
100000000000000004001 0AKUeoy8ISdmw6GQaku4EOYis2CQWgr 100000000000000004001
200000000000000004001 0AKUeoy8ISemw6GQaku4EOYis2CQWgr 200000000000000004001
100000000000000005001 0AKUeoy8ISdmw6GQaku4EOYis2CRWgr 100000000000000005001
200000000000000005001 0AKUeoy8ISemw6GQaku4EOYis2CRWgr 200000000000000005001
100000000000000006001 0AKUeoy8ISdmw6GQaku4EOYis2CSWgr 100000000000000006001
200000000000000006001 0AKUeoy8ISemw6GQaku4EOYis2CSWgr 200000000000000006001
100000000000000007001 0AKUeoy8ISdmw6GQaku4EOYis2CTWgr 100000000000000007001
200000000000000007001 0AKUeoy8ISemw6GQaku4EOYis2CTWgr 200000000000000007001
100000000000000008001 0AKUeoy8ISdmw6GQaku4EOYis2CUWgr 100000000000000008001
200000000000000008001 0AKUeoy8ISemw6GQaku4EOYis2CUWgr 200000000000000008001
100000000000000009001 0AKUeoy8ISdmw6GQaku4EOYis2CVWgr 100000000000000009001
200000000000000009001 0AKUeoy8ISemw6GQaku4EOYis2CVWgr 200000000000000009001
in 0.09967562500969507 seconds:
 - generated 20000 ids
 - obfuscated 20000 ids
 - deobfuscated and asserted 20000 ids
speedtest took 0.0050337910070084035 seconds:
 - generated 20000 ids (3973148.0/s)

```
