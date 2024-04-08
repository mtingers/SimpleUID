# SimpleUID
SimpleUID - sequential IDs at scale

## Features
- sharding/clustering ready (via namespace)
- auto-incrementing (per namespace)
- 4,294,967,295 unique namespaces available (aka shards/nodes)
- ID obfuscation/deobfuscation for opaque layers

    
## Format
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                   32 bit uint (namespace)                      |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                       64 bit uint                             |
    |                          (value)                              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

### Format Examples

Given a SimpleUID `100000000000000000001`, it can be broken down into two sections: namespace and value:
- namespace: 1
- value: 1

Given a SimpleUID `2100000000000000003818`:
- namespace: 21
- value: 3818 

Note that value is left padded to 20 places to provide uniqueness (even though it is an unsigned integer) and the namespace does not require any padding.

Example breakdown:
```yaml
namespace: 1
    - id: 1
        - output: 100000000000000000001
    - id: 2
        - output: 100000000000000000002

namespace: 2
    - id: 1
        - output: 200000000000000000001
    - id: 2
        - output: 200000000000000000002
```
