---
title:  BBC Micro Data Recovery
layout: default
categories: [experiments]
tags: [complete]
publish: true
---

In 2007, we were given a set of fifteen 5¼' floppy disks from a BBC Master, and asked if we could recover the data and make it usable. We were told that the disks were expected to contain a catalogue of local historical material, collected as part of an oral history project involving schools in and around Melbourne (Australia). That project started in 1982, building up to the creation of a larger, combined database compiled in 1985-87, and built using Acornsoft ViewStore (you can find a scan of the manuals for ViewStore [in this list][3])

Eventually, in 2009, we had the time and the opportunity to spend time working how to access this data, and this document covers what we learned as we did so.

Hardware
--------

{% include figure.html src="images/bbc-master/15092009064-master.jpg" alt="BBC Master, with floppy drive and screen." %}

We already had a special [BBC Master][1] that had been fitted [this with clever CompactFlash drive kit][1], which we had already purchased for experimentation purposes. This [device][13] allows a relatively modern media type to be accessed on the BBC as if it were an 1MHz IDE a hard disk. 

{% include figure.html src="images/bbc-master/15092009066-idekit.jpg" alt="The nifty 1MHz IDE kit, mounted inside the BBC Master." %}

Once data has been written to the flash drive, it can be can be physically transferred to a modern PC and accessed via a standard CompactFlash reader. This provided a complete chain of hardware, making the transfer possible, at least in principle. 

{% include figure.html src="images/bbc-l1.svg" alt="BBC Workflow - Level 1" %}

The whole story turned out to be far more complex. 

Imaging
-------

Clearly, we wanted to minimise how hard we worked the disks we'd been given, and so we aimed to clone the contents of the disk as a complete disk image as a one-off process, rather than access the data on the disks directly. Unfortunately, we had no idea how to make the BBC image a floppy disk.

Eventually, after a lot of internet searches and reading around, we discovered a BBC BASIC program called [BACKUP][4] has already been written for this purpose. In fact, a appeared that version was supplied on the CF disk supplied with the IDE kit, and it was an even more recent version (1.23) that the latest version available on the web (1.20).

Even them, it wasn't clear how to actually get things working. The BBC Micro was one of the first machine I learned on, and I continued to use it's descendants (the Archimedes, the A3000 and the Risc PC) all the way into my early twenties (in the late 1990's). Many traces of the old DFS and AFDS operating systems can be found in the later machines, and so combining my ageing memory with some more judicious Googling I was able to start to start exploring the contents of the disks, and running some of the software. 

While working out how basic file system commands worked, it also became clear that our BBC Master came equipped with at least to operating system ROMs, i.e. that both DFS and ADFS were present in this machine. After more racking of brains and a lot of trail and error, we could finally run the backup process:

    *ADFS
    *DIR Datadir
    *LOAD "BACKUP"
    *RUN

{% include figure.html src="images/bbc-master/13102009111.jpg" alt="Screenshot: ADFS BACKUP 1.23" %}

This was indicative of the terse prompts that many pieces of software supplied, and working out the right answers required [a lot of experimentation][14]. Even then, we could not get this ADFS BACKUP program to work as we expected, and we ended up transferring over the 1.20 version of BACKUP we had found on the web. It's not clear what the problem was, but it seems reasonable to assume ADFS BACKUP cannot read DFS disks, which BACKUP appears to be able to read both.

{% include figure.html src="images/bbc-master/12112009143.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Press any key..." %}

Unfortunately, it wasn't clear if the disk was a 40 or 80 track disk, so we had to guess. Nervously, I guessed '80', ran the program, and the drive chugged away, producing a noise that filled me with nostalgia...

{% include figure.html src="images/bbc-master/12112009138.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Mid-backup..." %}

{% include figure.html src="images/bbc-master/12112009142.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Mid-backup..." %}

A few moments later, success! The BACKUP program exited, and we could check how much free space we had, and see the new floppy disk image file we had created.

{% include figure.html src="images/bbc-master/12112009144.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Post-backup..." %}

A few of the disks had errors (which [looks like this](images/bbc-master/12112009136.jpg)), but we were able to image almost all of the disks.

Migration
---------

At this point, we had a disk image on the CF drive, and could take it our and transfer it to a PC. Of course, it wasn't as easy as that makes it sound.

Unfortunately, Windows does not recognise the ADFS disk format and so every time we inserted the CF card into the USB card reader, we were invited to reformat the disk and overwrite out data. Therefore to access the data, the CF disk itself had to be imaged, i.e. in order to copy over the floppy image, we had to image the CompactFlash card - using a disk image inside a disk image to complete the transfer. The IDE kit came with a software package designed to help with this, called CDUTILS_V100, containing the CFBACKUP and CFRESTORE tools. A carefully typed:

    C:\> CFBACKUP h C:\CF.DAT

...and a binary image of the CompactFlash disk in drive H: has been cloned into the file C:\CF.DAT, and we've managed not to overwrite the contents of any other devices (which can happen if you get the syntax wrong, although more so for CFRESTORE which we needed to use when transferring files to the BBC).

That raw disk image is still little use on it's own, and must be read using [ADFSExplorer][7] (which as of version 2.0.0 was rather buggy - disk image updates don't really work, full extraction and image rebuild was needed to add files to the images - but 2.2.0 is now available so hopefully these issues are resolved). This last layer allowed us to pull the floppy disk image files out of the ADFS file system and onto the native Windows NTFS.

Finally, we had the disk image on the PC, and we could hook it up to a suitable emulator (like [BeebEm][8] or [B-EM][9]) and explore the contents.


Emulation
---------

But it didn't work. Basic disk operations seemed to work, and the file listings looked okay, but when booting the disks, the system kept failing mysteriously. Did something go wrong along the long chain of migration? Or was the condition of the disk itself the problem? 

Fortunately, we had [a few other disks][18] we were willing to use for experimentation, including an official [Elite][19] floppy disk (which, as it's so well known, can act as 'ground truth' against which our experiences could be benchmarked). Elite appeared to run perfectly on the BBC itself, but the cloned disk image failed consistently. Our 'ground truth' image had ruled out floppy disk failure, but we had no idea which of the other parts of the long chain to access had failed.

{% include figure.html src="images/bbc-master/beebem3-elite-fail.png" alt="Screenshot: Elite failure." %}

We were stuck.


One More Lucky Guess
--------------------

Some months later, after more searching and reading, I found [these][5] [hints][6] that disk images are sometimes interleaved, on 20 bytes boundaries. i.e. when accessed from an emulator, disk images will not work as expected if the data from one side of the disk is not sliced up and interspersed between the data from the other side. Perhaps BACKUP copied the right data, but arranged it the wrong way.

Guessing that this might be the issue, I wrote [a small Java program that would re-interleave the data (mistakenly calling it 'interlace' rather than 'interleave')][10]. The guess paid off, and Elite booted at last.

{% include figure.html src="images/bbc-master/beebem3-elite-win.png" alt="Screenshot: Elite success!" %}

Finally, we could open up the disk we had been given in the emulator. It appeared to be a ViewStore data file, although as we did not have a copy of ViewStore to hand, we could not verify the data ourselves. However, we passed the floppy disk images back to the contributor and they appeared to be happy with our efforts and able to access the data themselves.


Summary
-------

Although successful, our final workflow leaves a lot to be desired:

{% include figure.html src="images/bbc-lX.svg" alt="BBC Workflow - Level X" %}

Indeed, since this project was carried out, much superior approaches have become well known. PC-based disk imaging solutions (e.g. [Kryoflux][11], [among others][12]) provide much safer and simpler ways of creating the floppy disk image.

{% include figure.html src="images/kryoflux.svg" alt="Kryoflux Workflow" %}

Of course, having the original hardware around can be very helpful, especially when it's not clear that and emulation is behaving correctly, but PC-based disk imaging means that it's no longer an absolutely necessity. We've not experimented with Kryoflux, but presumably the accompanying software also knowns to interleave the disk images (and if not, let's hope Google leads people here).

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
[18]: images/bbc-master/12112009139-disks.jpg
[19]: http://en.wikipedia.org/wiki/Elite_(video_game)

