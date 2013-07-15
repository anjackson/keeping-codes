---
title:  BBC Micro Data Recovery via CF Card
layout: default
---

Accessing BBC Floppy Disks Via Migration, Emulation & Guesswork

About two years ago, we were given a small set of 5¼' floppy disks from a BBC Master, and asked if we could recover the data and make it usable. This is how we did it.

We already had a special BBC Master that had been fitted [this with clever CompactFlash drive kit], which we had purchased for XXX. This device allows a modern media to be accessed on the BBC as a hard disk, but can be transferred to a modern PC via CompactFlash reader. This provided a complete chain of hardware, making the transfer possible in principle, but the software side was far more complex.

Clearly, we wanted to minimise how hard we worked the disks, and so we aimed to clone the contents of the disk as a complete disk image as a one-off process, rather than access the data on the disks directly. Fortunately a [BBC BASIC program exists that is able to do this], and came included on the CF drive. VERSION? Unfortunately, it wasn't clear if the disk was a 40 or 80 track disk, so we had to try both. Nervously, I ran the program, and the drive chugged away, producing a noise that filled me with nostalgia.

At this point, we had a disk image on the CF drive, and could take it our and transfer it to a PC. Unfortunately, Windows does not recognise the DFS disk format that the BBC needs, so the CF disk had to be directly imaged (an image with an image inside!), and then read using ADFSExplorer (which is a little buggy - disk image updates don't really work, full extraction needed). Finally, we had the disk image on the PC, and we could hook it up to [a suitable emulator|BeebEm?] and explore the contents.

But it didn't work. The file listing looked okay, but when booting the disk, the system kept failing mysteriously. Did something go wrong along this long chain of migration? Or was the condition of the disk itself the problem? To find out, we went back to the BBC and tried to read other disks, including one containing the Elite game, as this was believed to be in good condition and is one where we know what the performance should be like. We didn't want to fire up the disk we were given and explore the contents of it.

Elite appeared to run perfectly on the BBC itself, but the cloned disk image failed consistently. We were stuck.

Some months later, after once more searching and looking for possible alternatives for recovery, I found this hint that disk images are sometimes interlaced, on 20B boundaries. Guessing that this might be the issue, I wrote a small Java program that would de-interlace the data. The guess paid off, and Elite booted at last.

Finally, I could open up the disk we had been given. It appeared to be a ViewStore data file, but we did not have any of that software, so we could not make full use of the data. However, we passed the disk image back to the contributor and they appeared to be happy with our efforts.

Having learned more about this type of work, we would use Kryoflux or similar as a safer way of ripping the disk image (although once this is done, having the original hardware around is very helpful for determining what is supposed to happen!). While this change would make the migration chain shorter, it is still too much guess work involved.

Given that is has proven possible to access the data, some might argue that the floppy disks and the data on them are not obsolete. I would say that this long, brittle chains of migration and extensive guesswork are exactly what obsolescence looks like. Is is the slow death of a thousand ambiguities, rather than an sudden, jarring expiration. Obsolescence is a approached, rather than attained, with the costs of access rising every step of the way.

