Title: Festering Hate
Date: 2026-08-20
Category: PRODOS8
Tags: file, prodos8
Preview: gallery/viruses/appleii/festeringscr1.png
summary: This article is about the Festering Hate virus...

## Details

 - **Replication**: Accidentally when opening an infected SYS file.
 - **Virus size**: 3840 bytes.
 - **Attached**: SYS files, counter in the last byte of the second block.
 - **PRODOS**: all versions

### Description

Festering Hate (Authors: Lord Digital & Dead Lord)
It attached itself to SYS files on all available volumes.
It only affected SYS files in the root directory.
It could attack locked files, 
but still was unable to act on a disk that was write-protected.
It would not attack the file PRODOS unless its name was changed to something else.
The 4th through 6th bytes on a file with the virus were bytes that added up to 39 which serves as an identifier for the virus itself.
For some strange reason, the latest version of RX.GS cannot find Festering Hate in the file.
The virus put a one-byte counter in block 2 of a disk that had infected files.
if the counter is equal to FF somehow then when the file is infected the virus will reset it to 00 and will not activate.
When the counter reaches 23 (17 in hexadecimal), the virus is triggered.
At the bottom of the screen, the inscription Festering Hate appears, which is all on fire, and below it, there is a picture of a needle being inserted into a disk, 
and on the sides of the skull, and there is also the Electronic Arts logo.
If you press CTRL+RESET at the moment this text appears, this picture will appear at the bottom of the screen and will start to emerge from there again.
When this happens the disk is already destroyed.
Erases the entire bitmap of the disk.
It also erases the boot block of the disk.
searches all folders and not just in the root directory.
Can infect an empty SYS file, but this file will not be able to infect others.
Does not infect a file infected with CyberAIDS.
Does not touch file with names: PRODOS.

<img src="{attach}festeringhate.png" width="60%"/>
