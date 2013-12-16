---
title:  RISC OS Rescue
layout: default
categories: [experiments]
tags: [stub]
publish: false
---


http://www.forensicswiki.org/wiki/Ddrescue

TMP

opf:monitrix andy$ ddrescue --no-split /dev/disk4 sg.img log


GNU ddrescue 1.17
Press Ctrl-C to interrupt
rescued:     1281 MB,  errsize:       0 B,  current rate:     739 kB/s
   ipos:     1281 MB,   errors:       0,    average rate:    3578 kB/s
   opos:     1281 MB,    time since last successful read:       0 s
Finished                   



GNU ddrescue 1.17
Press Ctrl-C to interrupt
rescued:     1281 MB,  errsize:       0 B,  current rate:     739 kB/s
   ipos:     1281 MB,   errors:       0,    average rate:    3578 kB/s
   opos:     1281 MB,    time since last successful read:       0 s
Finished                   
opf:monitrix andy$ mv sg.img "1.2G8-Se-Media.img"
opf:monitrix andy$ ddrescue --no-split /dev/disk4 sg.img log2


GNU ddrescue 1.17
Press Ctrl-C to interrupt
rescued:    73474 kB,  errsize:  20401 MB,  current rate:     860 kB/s
   ipos:    73597 kB,   errors:       1,    average rate:    6679 kB/s
   opos:    73597 kB,    time since last successful read:       0 s
Finished                   
opf:monitrix andy$ ddrescue --no-split /dev/disk4 sg2.img log3


GNU ddrescue 1.17
Press Ctrl-C to interrupt
rescued:   140103 kB,  errsize:  20401 MB,  current rate:    1626 kB/s
   ipos:   140182 kB,   errors:       1,    average rate:    7005 kB/s
   opos:   140182 kB,    time since last successful read:       0 s
Finished                   
opf:monitrix andy$ ddrescue --direct --max-retries=3 /de
Developer/ dev/       
opf:monitrix andy$ ddrescue --direct --max-retries=3 /dev/di
disk0    disk0s1  disk0s2  disk0s3  disk1    disk1s1  disk1s2  disk2    disk2s1  disk2s2  disk3    disk3s1  disk3s2  disk4    
opf:monitrix andy$ ddrescue --direct --max-retries=3 /dev/disk4 sg.img lo
log   log2  log3  logs/ 
opf:monitrix andy$ ddrescue --direct --max-retries=3 /dev/disk4 sg.img log2
ddrescue: Direct disc access not available.
opf:monitrix andy$ rm sg.img 
.cache                         .settings/                     README.md                      log2                           public/                        temp.zip
.classpath                     .target/                       app/                           log3                           sg.img                         test/
.git/                          1.2G8-Se-Media.img             compression-test.py            logs/                          sg2.img                        test.txt
.gitignore                     LICENSE.txt                    conf/                          onclick-support-new-tabs.html  target/                        tools/
.project                       NotesIdeas.txt                 log                            project/                       temp.txt.Z                     
opf:monitrix andy$ rm sg.img 
opf:monitrix andy$ rm sg2.img 
opf:monitrix andy$ tm log2
-bash: tm: command not found
opf:monitrix andy$ rm log2 log3
opf:monitrix andy$ ddrescue --direct --max-retries=3 /dev/disk4 sg.img log2^C
opf:monitrix andy$ ddrescue --no-split /dev/disk4 sg.img log2


GNU ddrescue 1.17
Press Ctrl-C to interrupt
rescued:    15020 MB,  errsize:       0 B,  current rate:        0 B/s
   ipos:    15020 MB,   errors:       0,    average rate:    7819 kB/s
   opos:    15020 MB,    time since last successful read:       1 s
Finished                   


[16 bit IDE interface for Acorn Computers Resources][1], [Simtec 16-bit IDE interface for Acorn Archimedes][4]

[RPCEmu][8]
[error: use of undeclared identifier 'useDistantHdwrMem'][2]
[Installing RPCEmu and RISC OS 3.71 on Windows][9]

[hd4 not mounting][3]
[USB enclosure with IDE disc][5]

[FileCore boot blocks][6]

[RISC OS *Command Summaries][10]

[Re: [Rpcemu] Using RiscPC IDE diskimage as hd4.hdf - LBA issue][11]

[1]: http://www.simtec.co.uk/products/AUIDE16/resources.html
[2]: https://www.allegro.cc/forums/thread/608825
[3]: https://www.riscosopen.org/forum/forums/10/topics/1029
[4]: http://www.retro-kit.co.uk/page.cfm/content/Simtec-16bit-IDE-interface/
[5]: https://www.riscosopen.org/forum/forums/11/topics/1965
[6]: http://www.riscos.com/support/developers/prm/filecore.html#44373
[7]: http://www.armclub.org.uk/products/discknight/
[8]: http://www.marutan.net/rpcemuspoon/
[9]: http://www.4corn.co.uk/articles/rpcemu371win/
[10]: http://www.riscos.com/support/users/starcomms/index.htm
[11]: http://www.mail-archive.com/rpcemu@riscos.info/msg00735.html
[12]: http://www.mail-archive.com/rpcemu@riscos.info/msg00736.html

