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

We already had a special [BBC Master][1] that had been fitted [this with clever CompactFlash drive kit][1], which we had purchased for experimentation purposes earlier on. This device allows a relatively modern media type to be accessed on the BBC as if it were an IDE a hard disk. 

{% include figure.html src="images/bbc-master/15092009066-idekit.jpg" alt="The nifty 1MHz IDE kit, mounted inside the BBC Master." %}

Once data has been written to the flash drive, it can be can be physically transferred to a modern PC and accessed via a standard CompactFlash reader. This provided a complete chain of hardware, making the transfer possible, at least in principle. 

{% include figure.html src="images/bbc-l1.svg" alt="BBC Workflow - Level 1" %}

The software side turned our to be far more complex. 

Imaging
-------

Clearly, we wanted to minimise how hard we worked the disks, and so we aimed to clone the contents of the disk as a complete disk image as a one-off process, rather than access the data on the disks directly. 

We could load the floppy disks, and we even had some 'ground truth' in the form of offical Elite media we could use for testing. Even the, it wasn't clear how to actually get things working. The BBC Micro was one of the first machine I learned on, and I continued to use it's descendents (the Archimedies, the A3000 and the Risc PC) all the way into my early twenties (in the late 1990's). Many traces of the old DFS and AFDS operating systems can be found in the later machines, and so combining my aging memory with some judicious Googling I was able to start to start exploring the contents of the disks, and running some of the software.


Eventually, we discovered a BBC BASIC program called [BACKUP][4] has already been written for this purpose. In fact, a version was supplied on the CF disk supplied with the IDE kit, and this appeared to be an even more recent version (1.23) that the latest available version from the web site(1.20).

After more racking of brains and a lot of trail and error, we could finally run the backup process:

    *ADFS
    *DIR Datadir
    *LOAD "BACKUP"
    *RUN

{% include figure.html src="images/bbc-master/13102009111.jpg" alt="Screenshot: ADFS BACKUP 1.23" %}

This was indicative of the terse prompts that many pieces of software supplied, and working out the right answers required a lot of experimentation. Even then, we could not get this ADFS BACKUP program to work as we expected, and we ended up transferring over the 1.20 version of BACKUP we had found on the web. It's not clear what the problem was (perhaps ADFS BACKUP does not support DFS disks?), but we had more luck with version 1.20.

{% include figure.html src="images/bbc-master/12112009143.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Press any key..." %}

Unfortunately, it wasn't clear if the disk was a 40 or 80 track disk, so we had to guess. Nervously, I ran the program, and the drive chugged away, producing a noise that filled me with nostalgia...

{% include figure.html src="images/bbc-master/12112009138.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Mid-backup..." %}

{% include figure.html src="images/bbc-master/12112009142.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Mid-backup..." %}

A few moments later, success! The BACKUP program exited, and we could check how much free space we had, and see the new floppy disk image file we had created.

{% include figure.html src="images/bbc-master/12112009144.jpg" alt="Screenshot: BACKUP PROGRAM 1.20 - Post-backup..." %}

A few of the disks had errors (which [looks like this](images/bbc-master/12112009136.jpg)), but we were able to image almost all of the disks.

Migration
---------

[Floppy] -> [BACKUP] -> [Floppy Disk Images] -> [BBC Master] -> [CF] -> [PC] -> [Disk Images]

At this point, we had a disk image on the CF drive, and could take it our and transfer it to a PC. Unfortunately, Windows does not recognise the DFS disk format that the BBC needs, so the CF disk had to be directly imaged (an image with an image inside!), and then read using ADFSExplorer (which is a little buggy - disk image updates don't really work, full extraction needed). Finally, we had the disk image on the PC, and we could hook it up to [a suitable emulator|BeebEm?] and explore the contents.

[Floppy] -> [BACKUP] -> [Floppy Disk Images] -> [BBC Master] -> [CF] -> [PC] -> [Hard Disk Image] -> [ADFSExplorer] -> [Disk Images] -> [BeebEm]

Emulation
---------

But it didn't work. The file listing looked okay, but when booting the disk, the system kept failing mysteriously. Did something go wrong along this long chain of migration? Or was the condition of the disk itself the problem? To find out, we went back to the BBC and tried to read other disks, including one containing the Elite game, as this was believed to be in good condition and is one where we know what the performance should be like. We didn't want to fire up the disk we were given and explore the contents of it.

[Floppy] -> [BACKUP] -> [Floppy Disk Images] -> [BBC Master] -> [CF] -> [PC] -> [Hard Disk Image] -> [ADFSExplorer] -> [Disk Images] -> [BeebEm] -> [FAILURE]

Elite appeared to run perfectly on the BBC itself, but the cloned disk image failed consistently. We were stuck.

Guesswork
---------

Some months later, after once more searching and looking for possible alternatives for recovery, I found this hint that disk images are sometimes interlaced, on 20B boundaries. Guessing that this might be the issue, I wrote a small Java program that would re-interleave the data. The guess paid off, and Elite booted at last.

{% include figure.html src="images/bbc-lX.svg" alt="BBC Workflow - Level X" %}

Finally, I could open up the disk we had been given. It appeared to be a ViewStore data file, but we did not have any of that software, so we could not make full use of the data. However, we passed the disk image back to the contributor and they appeared to be happy with our efforts.

Summary
-------

Having learned more about this type of work, we would use Kryoflux or similar as a safer way of ripping the disk image (although once this is done, having the original hardware around is very helpful for determining what is supposed to happen!). While this change would make the migration chain shorter, it is still too much guess work involved.

Given that is has proven possible to access the data, some might argue that the floppy disks and the data on them are not obsolete. I would say that this long, brittle chains of migration and extensive guesswork are exactly what obsolescence looks like. Is is the slow death of a thousand ambiguities, rather than an sudden, jarring expiration. Obsolescence is approached, rather than attained, with the costs of access rising every step of the way.

Appendicies
-----------

### Notes from the owner ###
Discs from Judith Biddington, with this accompianing message:

> An interesting oral history project at the school, as part of a Disadvantaged Schools Programme, was developed in 1982 which received funding and gradually the children,  parents and teachers at Lee St combined with other schools and  organisations  in the area to develop a local history catalogue of historical material stored throughout the suburb and in peoples' heads and cupboards.  Over 3,500 items were catalogued.  These included newspaper articles, oral history interviews with residents, photographs, dance programmes, the Carlton Association's Building Register as well as school, church and community group records.During 1985-7 the catalogue was compiled by people who were out of work and employed in the Community Employment Program.
>
> Each of the 4 primary school involved had BBC microcomputers with modem and communiication software, the Melbourne City Council bought one for the Carlton Library and these were all linked into the BBC system of networked computers at Princes Hill Secondary College.  A hard disk was bought to allow sufficient storage.
>
> The data package used was called Viewstore, which was apparently user friendly, as it had instructions on screen: type in a letter and type in the subject  wanted and follow the instructions on the screen.  It was designed for school children and community members to use easily and to add material...Apparently there were 4 updatable indexes maintained, sort fields were unlimited and up to 40 megabytes of information could be stored. There were label and report utilities and links could be made to a word processor.  Subject headings were prepared according to the ASCIS cataloguing system and catalogue card could be printed for the card system in the library.
>
> The headings were author, title, publisher, place of publication, source, date of publication, illustrator, photographer, subject, time period, format, location, identity number, available for loan?,number of copies.

[1]: http://acorn.chriswhy.co.uk/Computers/Master128.html
[2]: http://www.retroclinic.com/acorn/kitide1mhz/kitide1mhz.htm
[3]: http://www.8bs.com/othrdnld/manuals/applications.shtml
[4]: http://mdfs.net/Apps/DiskTools/
[5]: http://www.8bs.com/filecon.htm#dit
[6]: http://mdfs.net/Docs/Books/HADFSMan/Chap5.htm
