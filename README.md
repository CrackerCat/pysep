# pysep
Split 64 bits sep-firmware images

```
λ ~ » python3 pysep.py AppleSEPOS-1134.0.0.100.1
name : boot         start : 0x0          end : 0x4000       size : 0x4001
name : kernel       start : 0x4000       end : 0x2d8000     size : 0x2d4001
name : SEPOS        start : 0x2d8000     end : 0x2f4000     size : 0x1c001
name : SEPD         start : 0x2f4000     end : 0x304000     size : 0x10001
name : AESSEP       start : 0x304000     end : 0x334000     size : 0x30001
name : sepS         start : 0x334000     end : 0x348000     size : 0x14001
name : sskg         start : 0x348000     end : 0x350000     size : 0x8001
name : ARTMate      start : 0x350000     end : 0x3e0000     size : 0x90001
name : sks          start : 0x3e0000     end : 0x3ec000     size : 0xc001
name : pass         start : 0x3ec000     end : 0x3f4000     size : 0x8001
name : test         start : 0x3f4000     end : 0x404000     size : 0x10001
name : unit_test    start : 0x404000     end : 0x430000     size : 0x2c001
name : pairing      start : 0x430000     end : 0x444000     size : 0x14001
name : xART         start : 0x444000     end : 0x450000     size : 0xc001
name : hdcp         start : 0x450000     end : 0x484000     size : 0x34001
name : sse          start : 0x484000     end : 0x4ac000     size : 0x28001
name : scrd         start : 0x4ac000     end : 0x5e4000     size : 0x138001
name : eispAppl_d4x   start : 0x5e4000     end : 0x698000     size : 0xb4001
name : sprl_d4x     start : 0x698000     end : 0x6b0000     size : 0x18001
```
