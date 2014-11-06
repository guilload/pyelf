from .flag import Flag


class SH_FLAG(Flag):
    flags = (('SHF_WRITE', 0x1, 'W'),
             ('SHF_ALLOC', 0x2, 'A'),
             ('SHF_EXECINSTR', 0x4, 'X'),
             ('SHF_MERGE', 0x10, 'M'),
             ('SHF_STRINGS', 0x20, 'S'),
             ('SHF_INFO_LINK', 0x40, 'I'),
             ('SHF_LINK_ORDER', 0x80, 'L'),
             ('SHF_OS_NONCONFORMING', 0x100, 'O'),
             ('SHF_GROUP', 0x200, 'G'),
             ('SHF_TLS', 0x400, 'TLS'),
             ('SHF_MASKOS', 0x0ff00000, 'o'),
             ('SHF_EXCLUDE', 0x80000000, 'E'),
             ('SHF_MASKPROC', 0xf0000000, 'p'))
