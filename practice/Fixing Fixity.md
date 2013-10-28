---
title: Fixing Fixity
layout: default
categories: [practice]
tags: [stub]
---

The [recent release][1] of a new checksumming tool, [Fixity][2], reminds me of some of the issues I faced a few years ago when trying to work out ways of pushing the checksumming process further up the ingest chain. 

Ideally, we would all prefers checksums to be generated at the point of creation, or at least prior to publication and/or submission to the repository. In many cases, this means we need reasonably simple tools that can generate reasonably simple checksums. Even [BagIt bags][3], while great for transfer, are a bit too complicated for content held in situ, as the structure around the payload gets in most users way.

So, we need some software that a general user can find acceptable to work with, and that stores its results somewhere useful. Some options (ACE-AM, Fixity?) store the results in a database, which makes repeated fixity checking easier, but is more difficult to deploy when using a lot of removable media. TBC.

A Simple Tool
-------------

So, what I wanted to find was a reasonably usable tool that could reliably create and validate checksum files in a [standard format][4]. Unfortunately, while there are many tools that very nearly satisfy this need, I discovered a number of edge cases that none of the tools I explored at the time were able to deal with.

Edge Cases
----------

=== Internationalisation ===
Or rather, non-ASCII filenames. An appropriate fixity tool MUST be able to cope with whatever characters are valid for filenames on a given operating system. For some, even spaces or dashes cause problems, but accented characters were the most common cause of failures. This is further complicated by the fact that different OSs have different character limitations, and therefore a fixity SHOULD really warn you if your filenames use characters that are not portable.

=== Standardised Output ===
The general checksum file format is well known, but there are a number of subtle requirements:

 * Output MUST be in UTF-8 and cope with any valid filename (see [[#Internationalisation]] above).
 * Output MUST use the asterisk to indicate that the binary data was checksummed.
 * Output SHOULD also have an option to standardise line-endings.

=== Scalability ===
To my surprise, many tools failed the most basic of scalability challenges, namely:

 * The tool MUST be able to cope with arbitrarily large files (certainly > 2GB).
 * The tool SHOULD be able to cope with arbitrarily large numbers of files.

The former should only be limited by the computation time available, and the latter should only be limited be the available disk space for storing checksums. For unclear reasons, some tools insisted on caching some or all of the files or checksums in memory, leading to failures on larger collections.

Resultant Practice
------------------
I never found ideal tools for the job. At the time, we ended up preferring [FastSum][] for general users and [ACE-AM][] for interim storage. The [ACE-AM Desktop Client][] was also quite promising. FastSum did have trouble with some of the cases outlined above, and came with default settings that did not meet our needs and so had to be modified per installation. ACE-AM worked quite well, but suffered some scalability issues - for very large collections it would become unstable, soaking up large amounts of RAM during fixity checks.

But this was a long time ago, and I hope the tools have all moved on since then. This kind of tool is not really a critical part of my work anymore, so I won't be looking into it, but I look forward to hearing what others find out about [Fixity][2].


[1]: http://www.avpreserve.com/blog/avpreserve-releases-fixity-and-mdqc-digital-preservation-tools/
[2]: https://github.com/avpreserve/fixity

[]: http://blogs.loc.gov/digitalpreservation/2012/03/file-fixity-and-digital-preservation-storage-more-results-from-the-ndsa-storage-survey/
