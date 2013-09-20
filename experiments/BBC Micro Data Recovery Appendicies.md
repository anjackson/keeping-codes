---
title:  BBC Micro Data Recovery - Appendicies
layout: default
---

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

Notes from the owner
--------------------

Discs from Judith Biddington, with this accompianing message:

> An interesting oral history project at the school, as part of a Disadvantaged Schools Programme, was developed in 1982 which received funding and gradually the children,  parents and teachers at Lee St combined with other schools and  organisations  in the area to develop a local history catalogue of historical material stored throughout the suburb and in peoples' heads and cupboards.  Over 3,500 items were catalogued.  These included newspaper articles, oral history interviews with residents, photographs, dance programmes, the Carlton Association's Building Register as well as school, church and community group records.During 1985-7 the catalogue was compiled by people who were out of work and employed in the Community Employment Program.
>
> Each of the 4 primary school involved had BBC microcomputers with modem and communiication software, the Melbourne City Council bought one for the Carlton Library and these were all linked into the BBC system of networked computers at Princes Hill Secondary College.  A hard disk was bought to allow sufficient storage.
>
> The data package used was called Viewstore, which was apparently user friendly, as it had instructions on screen: type in a letter and type in the subject  wanted and follow the instructions on the screen.  It was designed for school children and community members to use easily and to add material...Apparently there were 4 updatable indexes maintained, sort fields were unlimited and up to 40 megabytes of information could be stored. There were label and report utilities and links could be made to a word processor.  Subject headings were prepared according to the ASCIS cataloguing system and catalogue card could be printed for the card system in the library.
>
> The headings were author, title, publisher, place of publication, source, date of publication, illustrator, photographer, subject, time period, format, location, identity number, available for loan?,number of copies.
