pyelf
=====

An ELF file reader written in Python

```sh
$ pyelf -h
usage: pyelf [-h] [-d] [-H] [-r] [-S] [-s] file

Display information about the contents of ELF format files

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  -d, --dynamic         Display the dynamic section (if present)
  -H, --header          Display the ELF file header
  -r, --relocations     Display the relocations (if present)
  -S, --section-headers
                        Display the section headers
  -s, --symbols         Display the symbol table

$ pyelf -H fibonacci.o
ELF Header:
  Magic:                             7f 45 4c 46
  Class:                             ELF64
  Data:                              2s complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              REL (Relocatable file)
  Machine:                           AMD x86-64
  Version:                           1
  Entry point address:               0x0
  Start of program headers:          0 (bytes into file)
  Start of section headers:          400 (bytes into file)
  Flags:                             0
  Size of this header:               64 (bytes)
  Size of program headers:           0 (bytes)
  Number of program headers:         0
  Size of section headers:           64 (bytes)
  Number of section headers:         14
  Section header string table index: 11

  $ pyelf -S fibonacci.o
  Section headers:
  No.  Name             Type        Address    Offset    Size    Entry size  Flags      Link    Info    Align
    0                   NULL              0         0       0             0                0       0        0
    1  .text            PROGBITS          0        64     109             0  XA            0       0        1
    2  .rela.text       RELA              0      1648      48            24               12       1        8
    3  .data            PROGBITS          0       176      16             0  AW            0       0        8
    4  .rela.data       RELA              0      1696      24            24               12       3        8
    5  .bss             NOBITS            0       192       4             0  AW            0       0        4
    6  .rodata          PROGBITS          0       192       7             0  A             0       0        1
    7  .comment         PROGBITS          0       199      37             1  SM            0       0        1
    8  .note.GNU-stack  PROGBITS          0       236       0             0                0       0        1
    9  .eh_frame        PROGBITS          0       240      56             0  A             0       0        8
   10  .rela.eh_frame   RELA              0      1720      24            24               12       9        8
   11  .shstrtab        STRTAB            0       296     102             0                0       0        1
   12  .symtab          SYMTAB            0      1296     312            24               13       9        8
   13  .strtab          STRTAB            0      1608      38             0                0       0        1

Key to flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), l (large)
  I (info), L (link order), G (group), T (TLS), E (exclude), x (unknown)
  O (extra OS processing required) o (OS specific), p (processor specific)
```

and so on...
