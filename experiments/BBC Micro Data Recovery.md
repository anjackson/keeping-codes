---
title:  BBC Micro Data Recovery
layout: default
categories: [case-studies]
publish: true
---

In 2007, we were given a set of fifteen 5¼' floppy disks from a BBC Master, and asked if we could recover the data and make it usable. We were told that the disks were expected to contain a catalogue of local historical materia, collected as part of an oral history project involving schools in and around Melbourne (Australia). The project started in 1982, leading up to a larger combined database compiled in 1985-87, built using Acornsoft ViewStore (you can find a scan of the manuals for ViewStore [in this list][3])

Eventually, in 2009, we had the time and the opportunity to spend time working how to access this data, and this document covers what we learned as we did so.

Hardware
--------

{% include figure.html src="images/bbc-master/15092009064-master.jpg" alt="BBC Master, with floppy drive and screen." %}

We already had a special [BBC Master][1] that had been fitted [this with clever CompactFlash drive kit][1], which we had purchased for experimentation purposes earlier on. This [device][13] allows a relatively modern media type to be accessed on the BBC as if it were an IDE a hard disk. 

{% include figure.html src="images/bbc-master/15092009066-idekit.jpg" alt="The nifty 1MHz IDE kit, mounted inside the BBC Master." %}

Once data has been written to the flash drive, it can be can be physically transferred to a modern PC and accessed via a standard CompactFlash reader. This provided a complete chain of hardware, making the transfer possible, at least in principle. 

{% include figure.html src="images/bbc-l1.svg" alt="BBC Workflow - Level 1" %}

The software side turned our to be far more complex. 

Imaging
-------

Clearly, we wanted to minimise how hard we worked the disks, and so we aimed to clone the contents of the disk as a complete disk image as a one-off process, rather than access the data on the disks directly. 

We could load the floppy disks, and we even had some 'ground truth' in the form of offical Elite media we could use for testing. Even the, it wasn't clear how to actually get things working. The BBC Micro was one of the first machine I learned on, and I continued to use it's descendents (the Archimedies, the A3000 and the Risc PC) all the way into my early twenties (in the late 1990's). Many traces of the old DFS and AFDS operating systems can be found in the later machines, and so combining my aging memory with some judicious Googling I was able to start to start exploring the contents of the disks, and running some of the software.

----

In common with most computers of this period, the computer starts up at the BASIC interpreter command line. Unlike most computers of the age, it also has another set of commands that allow lower level access and direct file manipulation (as opposed to the application-oriented BASIC). These are called star commands, as the are all invoked from BASIC by using the asterix '*' prefix. Very, very rougly speaking, BASIC is to Star commands as Windows is to the DOS prompt. Also, unlike other systems, the OS and other built-in software is held on ROM chips, so cannot be damaged or modified by the user.

Two operating systems are included on the ROMS of our main BBC Master, the older DFS and the newer ADFS. You can switch between them, and this is necessary as DFS discs can only be accessed directly from DFS, and the same for ADFS. If you try to access a disc from the wrong OS, then you'll get at least a disc error, and the machine may even hang and require rebooting.

Note also that the physical drives have different identities in the different operating systems. In DFS, the floppy drive is drive 0, and the CF drive is drive 4 but cannot be accessed

    *DISC
    *DRIVE 0
    *.

Will list the contents of the DFS floppy  in the drive.
Under ADFS, the CF drive is the 0 drive, and the floppy drive is drive 4.

    *ADFS
    *DIR 0:
    *.

----

Eventually, we discovered a BBC BASIC program called [BACKUP][4] has already been written for this purpose. In fact, a version was supplied on the CF disk supplied with the IDE kit, and this appeared to be an even more recent version (1.23) that the latest available version from the web site(1.20).

After more racking of brains and a lot of trail and error, we could finally run the backup process:

    *ADFS
    *DIR Datadir
    *LOAD "BACKUP"
    *RUN

{% include figure.html src="images/bbc-master/13102009111.jpg" alt="Screenshot: ADFS BACKUP 1.23" %}

This was indicative of the terse prompts that many pieces of software supplied, and working out the right answers required [a lot of experimentation][14]. Even then, we could not get this ADFS BACKUP program to work as we expected, and we ended up transferring over the 1.20 version of BACKUP we had found on the web. It's not clear what the problem was (perhaps ADFS BACKUP does not support DFS disks?), but we had more luck with version 1.20.

{% include figure.html src="images/bbc-master/12112009143.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Press any key..." %}

Unfortunately, it wasn't clear if the disk was a 40 or 80 track disk, so we had to guess. Nervously, I ran the program, and the drive chugged away, producing a noise that filled me with nostalgia...

{% include figure.html src="images/bbc-master/12112009138.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Mid-backup..." %}

{% include figure.html src="images/bbc-master/12112009142.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Mid-backup..." %}

A few moments later, success! The BACKUP program exited, and we could check how much free space we had, and see the new floppy disk image file we had created.

{% include figure.html src="images/bbc-master/12112009144.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Post-backup..." %}

A few of the disks had errors (which [looks like this](images/bbc-master/12112009136.jpg)), but we were able to image almost all of the disks.

Migration
---------

At this point, we had a disk image on the CF drive, and could take it our and transfer it to a PC. Of course, it wasn't as easy as that makes it sound.

Unfortunately, Windows does not recognise the ADFS disk format that the BBC needs, so the CF disk had to be directly imaged (i.e. a disk image with an image inside!). The IDE kit came with a software package designed to help with this, called CDUTILS_V100, containing the CFBACKUP and CFRESTORE tools. A carefully typed:

    C:\> CFBACKUP h C:\CF.DAT

...and a binary image of the CompactFlash disk in drive H: has been cloned into the file C:\CF.DAT, and we've managed not to overwrite the contents of any other devices (which can happen if you get the syntax wrong, although moreso for CFRESTORE).

That raw disk image is still little use on it's own, and much be read using [ADFSExplorer][7] (which as of version 2.0.0 was rather buggy - disk image updates don't really work, full extraction and rebuild was needed to add files to the images - but 2.2.0 is now available so hopefully these issues are resolbed). This last layer allowed us to pull the floppy disk image files out of the ADFS file system and onto the native Windows NTFS.

Finally, we had the disk image on the PC, and we could hook it up to a suitable emulator (like [BeebEm][8] or [B-EM][9]) and explore the contents.

Emulation
---------

But it didn't work. Basic disk operations seemed to work, and the file listings looked okay, but when booting the disks, the system kept failing mysteriously. 

Did something go wrong along this long chain of migration? Or was the condition of the disk itself the problem? To find out, we went back to the BBC and tried to read other disks, including one containing the Elite game, as this was believed to be in good condition and is one where we know what the performance should be like.

Elite appeared to run perfectly on the BBC itself, but the cloned disk image failed consistently. Our 'ground truth' image had failed. We were stuck.

{% include figure.html src="images/bbc-master/beebem3-elite-fail.png" alt="Screenshot: Elite failure." %}


Guesswork
---------

Some months later, after once more searching and looking for possible alternatives for recovery, I found [these][5] [hints][6] that disk images are sometimes interleaved, on 20 bytes boundaries. i.e. when accessed from an emulator, disk images will not work as expected if the data from one side of the disk is not sliced up and interspersed between the data from the other side.

Guessing that this might be the issue, I wrote [a small Java program that would re-interleave the data (mistakenly calling it 'interlace' rather than 'interleave')][10]. The guess paid off, and Elite booted at last.

{% include figure.html src="images/bbc-master/beebem3-elite-win.png" alt="Screenshot: Elite success!" %}

Finally, we could open up the disk we had been given in the emulator. It appeared to be a ViewStore data file, but we did not have any of that software, so we could not make full use of the data. However, we passed the disk image back to the contributor and they appeared to be happy with our efforts.


Summary
-------

Although successful, our final workflow leaves a lot to be desired:

{% include figure.html src="images/bbc-lX.svg" alt="BBC Workflow - Level X" %}

Indeed, since this project was carried out, much superior approaches have become well known. PC-based disk imaging solutions (e.g. [Kryoflux][11], [among others][12]) provide much safer and simpler ways of creating the floppy disk image.

{% include figure.html src="images/kryoflux.svg" alt="Kryoflux Workflow" %}

Of course, having the original hardware around is very helpful, e.g. if it's not clear that the emulation is behaving correctly, but it's no longer an absolute necessity. 

Given that is has proven possible to access the data, some might argue that the floppy disks and the data on them are not obsolete. I would say that this long, brittle chains of migration and extensive guesswork are exactly what obsolescence looks like. 

Even though a more efficient way to access the disks themselves is now available, the problem shifts understanding how to use the disks and the software, and how to access the data within.

It is the slow death of a thousand ambiguities, rather than an sudden, jarring expiration. Obsolescence is approached, rather than attained, with the costs of access rising every step of the way.

[1]: http://acorn.chriswhy.co.uk/Computers/Master128.html
[2]: http://www.retroclinic.com/acorn/kitide1mhz/kitide1mhz.htm
[3]: http://www.8bs.com/othrdnld/manuals/applications.shtml
[4]: http://mdfs.net/Apps/DiskTools/
[5]: http://www.8bs.com/filecon.htm#dit
[6]: http://mdfs.net/Docs/Books/HADFSMan/Chap5.htm
[7]: http://www.g7jjf.com/adfs_explorer.htm
[8]: http://www.mkw.me.uk/beebem/
[9]: http://b-em.bbcmicro.com/
[10]: BBCUtils/src/uk/bl/dpt/bbc/DiskImageInterlacer.java.html
[11]: http://www.kryoflux.com/
[12]: http://www.archiveteam.org/index.php?title=Rescuing_Floppy_Disks
[13]: images/bbc-master/
[14]: images/bbc-master/#toc1
[15]: http://acorn.chriswhy.co.uk/docs/Acorn/Manuals/Acorn_DiscSystemUGI2.pdf
[16]: http://acorn.chriswhy.co.uk/docs/Acorn/Manuals/Acorn_ADFSUG.pdf
[17]: https://www.youtube.com/watch?feature=player_detailpage&v=TYetKjaVl6k#t=322

