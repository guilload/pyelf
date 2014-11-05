from .flag import Flag


class SH_FLAG(Flag):
    flags = (('SHF_WRITE', 0x1, 'W'),
             ('SHF_ALLOC', 0x2, 'A'),
             ('SHF_EXECINSTR', 0x4, 'X'),
             ('SHF_MASKPROC', 0xf0000000, ''))
