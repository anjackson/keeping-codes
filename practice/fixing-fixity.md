---
title: Fixing Fixity
layout: default
categories: What We Need
status: complete
publish: true
tags: ["Requirements for Tools"]
---

The [recent release][1] of a new checksumming tool, [Fixity][2], reminds me of some of the issues I faced a few years ago when trying to work out ways of pushing the checksumming process further up the ingest chain. 

Ideally, we would prefer that checksums were generated at the point of creation, or at least prior to publication and/or submission to a repository (see [this survey for more context][6]). In many cases, this means we need reasonably simple tools that can generate reasonably simple, verifiable checksum manifests.

One option would be to use [BagIt bags][3]. However, while great for transfer, are a bit too complicated for content held in situ, as the structure around the payload gets in most users way.

Some tools (e.g. [ACE-AM][2] and, I think, [Fixity][2]) deal with this by storing the results in a database, either locally or remotely, which makes repeated fixity checking much easier. However, this more difficult to deploy, as it requires more complexity on the originating system. Furthermore, for potential content transfers, or when dealing with removable media, it is preferable to keep the checksums next to the content.

In essense, what we want is an 'open bag' - a [BagIt-compliant manifest][4] that sits at the top-level of the root folder of the content. If transfer is necessary at some later point, this structure can be turned into a 'bag' simply by making some folders and moving the data and manifest into their proper locations. 

A Simple Tool
-------------

So, what I wanted to find was a reasonably usable tool that could reliably create and validate checksum files in a [standard format][4]. From the command-line, under Linux, Cygwin or OS X, this is pretty easy (e.g. for [md5sum][5]):

    find . -type f -exec md5sum -b {} \; > manifest-md5.txt

...and to verify:

    md5sum --check manifest-md5.txt

So all I needed was a simple GUI application that would replicate this functionality.

Unfortunately, while there are many tools that _very nearly_ satisfy this need, I discovered a number of edge cases that none of the tools I explored at the time were able to deal with.


Manifest Edge Cases
-------------------

While testing the various tools, the 'difficult' cases I came across were as follows.

### Internationalisation ###
Or more simply, non-ASCII filenames. An appropriate fixity tool MUST be able to cope with whatever characters are valid for filenames on a given operating system. For some tools, even spaces caused problems, but accented characters were the most common cause of failures. This is further complicated by the fact that different OSs have different character limitations, although the [BagIt specification][4] already tells you how to deal with that.

### Standardised Output ###
The [general checksum file format][10] is well known, but there are a number of subtle requirements in this context (again, refer the the [BagIT specification][4] for details):

 * Output MUST be in UTF-8 and cope with any valid filename (see [above](#toc2)).
 * Output MUST use the asterisk to indicate that the data was checksummed in binary mode.
 * Output MUST use cross-platform path notation (forward-slashes, not back-slashes).
 * Output MUST standardise line-endings.

### Scalability ###
To my surprise, many tools failed the most basic of scalability challenges, namely:

 * The tool MUST be able to cope with arbitrarily large files (certainly > 2GB).
 * The tool SHOULD be able to cope with arbitrarily large numbers of files.

The former should only be limited by the computation time available, and the latter should only be limited be the available disk space for storing checksums. For unclear reasons, some tools insisted on caching some or all of the files or checksums in memory, leading to failures on larger collections. The simple command-line tools like md5sum do not suffer from these issues.

Practice Imperfect
------------------
I never found an ideal tool for this job. Every tool I looked at failed to deal with one or more of the these edge cases and, frankly, the user interfaces were not very good. Surprisingly few offered true Windows integration (e.g. right-click in file explorer to generate or validate this folder). Surprisingly many offered strange and confusing interfaces and weird and obscure options.

At the time, we ended up preferring [FastSum][7] for general users and [ACE-AM][8] for interim storage (i.e. monitoring network drives with checksums in a database). FastSum did have trouble with some of the cases outlined above, and came with default settings that did not meet our needs (and so had to be modified per installation), but it was workable. ACE-AM worked quite well, but suffered some scalability issues - for very large collections it would become unstable, soaking up large amounts of RAM during fixity checks.  The [ACE-AM Desktop Client][9] was also quite promising, although it wasn't clear where source code was, which left me reticent to get too deeply committed to it.

In many cases, for reasonably technical individuals, it actually made more sense to train them in how to use Cygwin and how to invoke the command line tools. There are a lot of overheads in maintaining a GUI framework, and by training people to use lower-level tools, you also enable and empower them to perform more sophisticated manipulations of the content they are responsible for.

Time Lapse
----------
This was a long time ago, and I hope the tools have all moved on since then. This kind of tool is not really a critical part of my work anymore, so I won't be looking into it further. However, I look forward to hearing what others find out about [Fixity][2].



[1]: http://www.avpreserve.com/blog/avpreserve-releases-fixity-and-mdqc-digital-preservation-tools/
[2]: https://github.com/avpreserve/fixity
[3]:https://wiki.ucop.edu/display/Curation/BagIt
[4]: http://tools.ietf.org/html/draft-kunze-bagit-06#section-2.1.3
[5]: http://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html
[6]: http://blogs.loc.gov/digitalpreservation/2012/03/file-fixity-and-digital-preservation-storage-more-results-from-the-ndsa-storage-survey/
[7]: http://www.fastsum.com/
[8]: https://wiki.umiacs.umd.edu/adapt/index.php/Ace:Main
[9]: https://wiki.umiacs.umd.edu/adapt/index.php/Ace:Webstart_Client
[10]: https://en.wikipedia.org/wiki/Md5sum

