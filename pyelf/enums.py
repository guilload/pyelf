from .enum import Enum


class _D_TAG(Enum):
    members = (('DT_NULL', 0, 'NULL'),
               ('DT_NEEDED', 1, 'NEEDED'),
               ('DT_PLTRELSZ', 2, 'PLTRELSZ'),
               ('DT_PLTGOT', 3, 'PLTGOT'),
               ('DT_HASH', 4, 'HASH'),
               ('DT_STRTAB', 5, 'STRTAB'),
               ('DT_SYMTAB', 6, 'SYMTAB'),
               ('DT_RELA', 7, 'RELA'),
               ('DT_RELASZ', 8, 'RELASZ'),
               ('DT_RELAENT', 9, 'RELAENT'),
               ('DT_STRSZ', 10, 'STRSZ'),
               ('DT_SYMENT', 11, 'SYMENT'),
               ('DT_INIT', 12, 'INIT'),
               ('DT_FINI', 13, 'FINI'),
               ('DT_SONAME', 14, 'SONAME'),
               ('DT_RPATH', 15, 'RPATH'),
               ('DT_SYMBOLIC', 16, 'SYMBOLIC'),
               ('DT_REL', 17, 'REL'),
               ('DT_RELSZ', 18, 'RELSZ'),
               ('DT_RELENT', 19, 'RELENT'),
               ('DT_PLTREL', 20, 'PLTREL'),
               ('DT_DEBUG', 21, 'DEBUG'),
               ('DT_TEXTREL', 22, 'TEXTREL'),
               ('DT_JMPREL', 23, 'JMPREL'),
               ('DT_BIND_NOW', 24, 'BIND_NOW'),
               ('DT_INIT_ARRAY', 25, 'INIT_ARRAY'),
               ('DT_FINI_ARRAY', 26, 'FINI_ARRAY'),
               ('DT_INIT_ARRAYSZ', 27, 'INIT_ARRAYSZ'),
               ('DT_FINI_ARRAYSZ', 28, 'FINI_ARRAYSZ'),
               ('DT_RUNPATH', 29, 'RUNPATH'),
               ('DT_FLAGS', 30, 'FLAGS'),
               ('DT_ENCODING', 32, 'ENCODING'),
               ('DT_PREINIT_ARRAY', 32, 'PREINIT_ARRAY'),
               ('DT_PREINIT_ARRAYSZ', 33, 'PREINIT_ARRAYSZ'),
               ('DT_NUM', 34, 'NUM'),
               ('DT_LOOS', 0x6000000d, 'LOOS'),
               ('DT_SUNW_AUXILIARY', 0x6000000d, 'SUNW_AUXILIARY'),
               ('DT_SUNW_RTLDINF', 0x6000000e, 'SUNW_RTLDINF'),
               ('DT_SUNW_FILTER', 0x6000000f, 'SUNW_FILTER'),
               ('DT_SUNW_CAP', 0x60000010, 'SUNW_CAP'),
               ('DT_SUNW_SYMTAB', 0x60000011, 'SUNW_SYMTAB'),
               ('DT_SUNW_SYMSZ', 0x60000012, 'SUNW_SYMSZ'),
               ('DT_SUNW_ENCODING', 0x60000013, 'SUNW_ENCODING'),
               ('DT_SUNW_SORTENT', 0x60000013, 'SUNW_SORTENT'),
               ('DT_SUNW_SYMSORT', 0x60000014, 'SUNW_SYMSORT'),
               ('DT_SUNW_SYMSORTSZ', 0x60000015, 'SUNW_SYMSORTSZ'),
               ('DT_SUNW_TLSSORT', 0x60000016, 'SUNW_TLSSORT'),
               ('DT_SUNW_TLSSORTSZ', 0x60000017, 'SUNW_TLSSORTSZ'),
               ('DT_SUNW_CAPINFO', 0x60000018, 'SUNW_CAPINFO'),
               ('DT_SUNW_STRPAD', 0x60000019, 'SUNW_STRPAD'),
               ('DT_SUNW_CAPCHAIN', 0x6000001a, 'SUNW_CAPCHAIN'),
               ('DT_SUNW_LDMACH', 0x6000001b, 'SUNW_LDMACH'),
               ('DT_SUNW_CAPCHAINENT', 0x6000001d, 'SUNW_CAPCHAINENT'),
               ('DT_SUNW_CAPCHAINSZ', 0x6000001f, 'SUNW_CAPCHAINSZ'),
               ('DT_HIOS', 0x6ffff000, 'HIOS'),
               ('DT_LOPROC', 0x70000000, 'LOPROC'),
               ('DT_HIPROC', 0x7fffffff, 'HIPROC'),
               ('DT_PROCNUM', 0x35, 'PROCNUM'),
               ('DT_VALRNGLO', 0x6ffffd00, 'VALRNGLO'),
               ('DT_GNU_PRELINKED', 0x6ffffdf5, 'GNU_PRELINKED'),
               ('DT_GNU_CONFLICTSZ', 0x6ffffdf6, 'GNU_CONFLICTSZ'),
               ('DT_GNU_LIBLISTSZ', 0x6ffffdf7, 'GNU_LIBLISTSZ'),
               ('DT_CHECKSUM', 0x6ffffdf8, 'CHECKSUM'),
               ('DT_PLTPADSZ', 0x6ffffdf9, 'PLTPADSZ'),
               ('DT_MOVEENT', 0x6ffffdfa, 'MOVEENT'),
               ('DT_MOVESZ', 0x6ffffdfb, 'MOVESZ'),
               ('DT_SYMINSZ', 0x6ffffdfe, 'SYMINSZ'),
               ('DT_SYMINENT', 0x6ffffdff, 'SYMINENT'),
               ('DT_GNU_HASH', 0x6ffffef5, 'GNU_HASH'),
               ('DT_TLSDESC_PLT', 0x6ffffef6, 'TLSDESC_PLT'),
               ('DT_TLSDESC_GOT', 0x6ffffef7, 'TLSDESC_GOT'),
               ('DT_GNU_CONFLICT', 0x6ffffef8, 'GNU_CONFLICT'),
               ('DT_GNU_LIBLIST', 0x6ffffef9, 'GNU_LIBLIST'),
               ('DT_CONFIG', 0x6ffffefa, 'CONFIG'),
               ('DT_DEPAUDIT', 0x6ffffefb, 'DEPAUDIT'),
               ('DT_AUDIT', 0x6ffffefc, 'AUDIT'),
               ('DT_PLTPAD', 0x6ffffefd, 'PLTPAD'),
               ('DT_MOVETAB', 0x6ffffefe, 'MOVETAB'),
               ('DT_SYMINFO', 0x6ffffeff, 'SYMINFO'),
               ('DT_VERSYM', 0x6ffffff0, 'VERSYM'),
               ('DT_RELACOUNT', 0x6ffffff9, 'RELACOUNT'),
               ('DT_RELCOUNT', 0x6ffffffa, 'RELCOUNT'),
               ('DT_FLAGS_1', 0x6ffffffb, 'FLAGS_1'),
               ('DT_VERDEF', 0x6ffffffc, 'VERDEF'),
               ('DT_VERDEFNUM', 0x6ffffffd, 'VERDEFNUM'),
               ('DT_VERNEED', 0x6ffffffe, 'VERNEED'),
               ('DT_VERNEEDNUM', 0x6fffffff, 'VERNEEDNUM'),
               ('DT_AUXILIARY', 0x7ffffffd, 'AUXILIARY'),
               ('DT_FILTER', 0x7fffffff, 'FILTER'))


class _EI_CLASS(Enum):
    members = (('EI_CLASS_32', 1, 'ELF32'),
               ('EI_CLASS_64', 2, 'ELF64'),)


class _EI_DATA(Enum):
    members = (('EI_DATA_LSB', 1, "2's complement, little endian"),
               ('EI_DATA_MSB', 2, "2's complement, big endian"))


class _EI_VERSION(Enum):
    members = (('EI_VERSION', 1, '1 (current)'),)


class _EI_OSABI(Enum):
    members = (('EI_OSABI_SYSV', 0, 'UNIX - System V'),)


class _EI_ABIVERSION(Enum):
    members = (('EI_ABIVERSION_0', 0, '0'),)


class _E_TYPE(Enum):
    members = (('E_TYPE_REL', 1, 'REL (Relocatable file)'),
               ('E_TYPE_EXEC', 2, 'EXEC (Executable file)'))


class _E_MACHINE(Enum):
    members = (('EM_X86_64', 62, 'AMD x86-64'),)


class _R_RELOCATION(Enum):
    members = (('R_X86_64_NONE', 0, 'X86_64_NONE'),
               ('R_X86_64_64', 1, 'X86_64_64'),
               ('R_X86_64_PC32', 2, 'X86_64_PC32'),
               ('R_X86_64_GOT32', 3, 'X86_64_GOT32'),
               ('R_X86_64_PLT32', 4, 'X86_64_PLT32'),
               ('R_X86_64_COPY', 5, 'X86_64_COPY'),
               ('R_X86_64_GLOB_DAT', 6, 'X86_64_GLOB_DAT'),
               ('R_X86_64_JUMP_SLOT', 7, 'X86_64_JUMP_SLOT'),
               ('R_X86_64_RELATIVE', 8, 'X86_64_RELATIVE'),
               ('R_X86_64_GOTPCREL', 9, 'X86_64_GOTPCREL'),
               ('R_X86_64_32', 10, 'X86_64_32'),
               ('R_X86_64_32S', 11, 'X86_64_32S'),
               ('R_X86_64_16', 12, 'X86_64_16'),
               ('R_X86_64_PC16', 13, 'X86_64_PC16'),
               ('R_X86_64_8', 14, 'X86_64_8'),
               ('R_X86_64_PC8', 15, 'X86_64_PC8'),
               ('R_X86_64_NUM', 16, 'X86_64_NUM'))


class _SH_Nindex(Enum):
    members = (('SHN_UNDEF', 0, 'UND'),
               ('SHN_LORESERVE', 0xff00, 'LORESERVE'),
               ('SHN_LOPROC', 0xff00, 'LOPROC'),
               ('SHN_HIPROC', 0xff1f, 'HIPROC'),
               ('SHN_ABS', 0xfff1, 'ABS'),
               ('SHN_COMMON', 0xfff2, 'COMMON'),
               ('SHN_HIRESERVE', 0xffff, 'HIRESERVE'))


class _SH_TYPE(Enum):
    members = (('SHT_NULL', 0, 'NULL'),
               ('SHT_PROGBITS', 1, 'PROGBITS'),
               ('SHT_SYMTAB', 2, 'SYMTAB'),
               ('SHT_STRTAB', 3, 'STRTAB'),
               ('SHT_RELA', 4, 'RELA'),
               ('SHT_HASH', 5, 'HASH'),
               ('SHT_DYNAMIC', 6, 'DYNAMIC'),
               ('SHT_NOTE', 7, 'NOTE'),
               ('SHT_NOBITS', 8, 'NOBITS'),
               ('SHT_REL', 9, 'REL'),
               ('SHT_SHLIB', 10, 'SHLIB'),
               ('SHT_DYNSYM', 11, 'DYNSYM'),
               ('SHT_NUM', 12, 'NUM'),
               ('SHT_INIT_ARRAY', 14, 'INIT_ARRAY'),
               ('SHT_FINI_ARRAY', 15, 'FINI_ARRAY'),
               ('SHT_GNU_HASH', 0x6ffffff6, 'GNU_HASH'),
               ('SHT_GNU_VERDEF', 0x6ffffffd, 'VERDEF'),
               ('SHT_GNU_VERNEED', 0x6ffffffe, 'VERNEED'),
               ('SHT_GNU_VERSYM', 0x6fffffff, 'VERSYM'),
               ('SHT_LOPROC', 0x70000000, 'LOPROC'),
               ('SHT_HIPROC', 0x7fffffff, 'HIPROC'),
               ('SHT_LOUSER', 0x80000000, 'LOUSER'),
               ('SHT_HIUSER', 0xffffffff, 'HIUSER'))


class _ST_BIND(Enum):
    members = (('STB_LOCAL', 0, 'LOCAL'),
               ('STB_GLOBAL', 1, 'GLOBAL'),
               ('STB_WEAK', 2, 'WEAK'),
               ('STB_LOOS', 10, 'LOOS'),
               ('STB_HIOS', 12, 'HIOS'),
               ('STB_LOPROC', 13, 'LOPROC'),
               ('STB_HIPROC', 15, 'HIPROC'))


class _ST_TYPE(Enum):
    members = (('STT_NOTYPE', 0, 'NOTYPE'),
               ('STT_OBJECT', 1, 'OBJECT'),
               ('STT_FUNC', 2, 'FUNC'),
               ('STT_SECTION', 3, 'SECTION'),
               ('STT_FILE', 4, 'FILE'),
               ('STT_LOPROC', 13, 'LOPROC'),
               ('STT_HIPROC', 15, 'HIPROC'))


class _ST_VISIBILITY(Enum):
    members = (('STV_DEFAULT', 0, 'DEFAULT'),
               ('STV_INTERNAL', 1, 'INTERNAL'),
               ('STV_HIDDEN', 2, 'HIDDEN'),
               ('STV_PROTECTED', 3, 'PROTECTED'),
               ('STV_EXPORTED', 4, 'EXPORTED'),
               ('STV_SINGLETON', 5, 'SINGLETON'),
               ('STV_ELIMINATE', 6, 'ELIMINATE'))


ENUMS = (_D_TAG,
         _EI_CLASS,
         _EI_DATA,
         _E_MACHINE,
         _E_TYPE,
         _EI_ABIVERSION,
         _EI_OSABI,
         _EI_VERSION,
         _R_RELOCATION,
         _SH_Nindex,
         _SH_TYPE,
         _ST_BIND,
         _ST_TYPE,
         _ST_VISIBILITY)


def populate_namespace(namespace=globals()):
    for enum in ENUMS:
        name = enum.__name__.lstrip('_')
        namespace[name] = enum(namespace)  # hackish... but quite effective

populate_namespace()
