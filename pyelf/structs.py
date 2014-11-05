from .enums import *
from .structs32 import *
from .structs64 import *
from .structure import Structure


STRUCTS = {64: {'Elf_Dyn': Elf64_Dyn,
                'Elf_Ehdr': Elf64_Ehdr,
                'Elf_Phdr': Elf64_Phdr,
                'Elf_Rel': Elf64_Rel,
                'Elf_Rela': Elf64_Rela,
                'Elf_Shdr': Elf64_Shdr,
                'Elf_Sym': Elf64_Sym,
                },

           32: {'Elf_Dyn': Elf32_Dyn,
                'Elf_Ehdr': Elf32_Ehdr,
                'Elf_Phdr': Elf32_Phdr,
                'Elf_Rel': Elf32_Rel,
                'Elf_Rela': Elf32_Rela,
                'Elf_Shdr': Elf32_Shdr,
                'Elf_Sym': Elf32_Sym,
                },
           }


class Elf_Eident(Structure):

    members = ({'name': 'ei_mag', 'type': '4s'},
               {'name': 'ei_class', 'type': 'B', 'enum': EI_CLASS},
               {'name': 'ei_data', 'type': 'B', 'enum': EI_DATA},
               {'name': 'ei_version', 'type': 'B', 'enum': EI_VERSION},
               {'name': 'ei_osabi', 'type': 'B', 'enum': EI_OSABI},
               {'name': 'ei_abiversion', 'type': 'B', 'enum': EI_ABIVERSION},
               {'name': 'ei_pad', 'type': '7s'})
