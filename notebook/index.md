Digital Preservation Notebook
=============================

This notebook is a place to record useful tidbits of information about
digital preservation. The [Wikipedia page on Digital
Preservation](http://en.wikipedia.org/wiki/Digital_preservation)  
provides quite a good overview of the field, but this notebook intends
to dig a little deeper. Roughly speaking, the technical side of digital
preservation can be broken down into two parts: - Preserving the bytes.
- Preserving access to the digital objects those bytes describe. Most of
this notebook deals with the latter issue, i.e. with how to preserve the
meaning of digital objects so that they remain accessible over time. Of
course, all of that work is based on the assumption that we can keep the
actual binary data safe from bit-rot, and so the [first
section](http://anjackson.net/digital_preservation_notebook/bit_preservation)
  will look at that issue. \# Bit Preservation \#

The other sections of this notebook generally assume that there will be
some digital objects storage system that can be relied upon to hold the
bytes safely over time. Indeed, I believe it is sensible to deal with
the bit-storage and access problems separately, in the sense that any
access solutions should be designed to work independently of the chosen
bit-store solution. I used to think that the bit-storage problem was
[essentially
solved](http://anjackson.net/2008/06/27/science_digital_preservation)  ,
but I have since realised that fighting bit-rot is not as easy as I
originally thought. ...tbc...

Keeping Bits Safe
-----------------

-   Refreshing
-   Replication
-   [MAID](http://en.wikipedia.org/wiki/Massive_array_of_idle_disks)  
-   etc... - [Long-term performance analysis of Intel Mainstream
    SSDs](http://www.pcper.com/article.php?aid=669)

Digital Object Formats
======================

See also this related effort: [Wikibook: Choosing The Right File
Format](http://en.wikibooks.org/wiki/Choosing_The_Right_File_Format)
. [http://www.dptp.org/course/](http://www.dptp.org/course/)

File Format Registries
----------------------

-   Format registries to include:
-   A file extension registry?
-   [File Free File Command](http://www.darwinsys.com/file/)
-   [JMimeMagic](http://sourceforge.net/projects/jmimemagic/)   can help
    here.
-   [MIME Types](http://www.iana.org/assignments/media-types/)
-   [PRONOM](http://www.nationalarchives.gov.uk/pronom/)
-   [Global Digital Format Registry](http://hul.harvard.edu/gdfr/)
-   [Apple Uniform Type
    Identifiers](http://developer.apple.com/documentation/Carbon/Conceptual/understanding_utis/utilist/chapter_4_section_1.html#//apple_ref/doc/uid/TP40001319-CH205-CHDIJFGJ)
-   [http://www.digitalpreservation.gov/formats/intro/format\_eval\_rel.shtml](http://www.digitalpreservation.gov/formats/intro/format_eval_rel.shtml)

Documents
---------

-   Open Office v. Office Open XML
-   [Compound Document Format](http://www.w3.org/TR/WICD/)  
-   HTML

Databases
---------

Preservation-Format Approach. - [DANS
M-XML](http://mixed.dans.knaw.nl/node/114)   - SIARD, [Providing
Authentic Long-term Archival Access to Complex Relational
Data](http://arxiv.org/abs/cs/0408054)  

Images
------

-   [JPEG](http://delicious.com/beardedstoat/jpeg)  
-   [JPEG 2000](http://delicious.com/beardedstoat/jpeg2000)  

Digital Object Properties
=========================

Significant Properties
----------------------

See [JISC: The Significant Properties of Digital
Objects](http://www.jisc.ac.uk/whatwedo/programmes/preservation/2008sigprops)
  Issues with this concept are legion.

Property Extraction Methods
===========================

Magic numbersMagic numbers is the name for the standard UNIX mechanism
used to identify file types. This approach is not limited to UNIX, but
is usually considered a UNIX related practice that has since spread to
many other platforms. The mechanism is based on a database that maps
byte strings and positions to file types. Common examples are GIF, JPEG
and TIFF, that all contain reliable markers, at least for identifying
the general file format. Minor version identification (i.e., format
characterization rather than format identification) often requires a
more sophisticated approach, e.g. parsing of header structures. On a
UNIX system, the magic number mechanism can be accessed using the file
command, e.g.:

`kb005264:~/Code/Graphics andersjohansen$ file logo.png`
`logo.png: PNG image data, 64 x 64, 8-bit/color RGBA, non-interlaced`

Advantages are fast performance and reliable identification for many
file formats. Limitations include that often minor version variations
can’t be determined (i.e., less than reliable characterization), that
the method does not allow for formats that lack reliable identification
strings (such as text files), and that it uncritically accepts the
evidence (e.g., if a text file contains the magic number for a GIF file,
the file command will identify it as a GIF file, regardless of other
evidence).

Property Extraction Tools
=========================

[DROID](http://droid.sourceforge.net/)  DROID identifies files using the
magic numbers approach. - Refers to
[PRONOM](http://www.nationalarchives.gov.uk/pronom/)  , e.g.
''info:pronom/fmt/100'' is HTML 4.01. - Required manual proxy
configuration via text-file-hacking. - Use ProxySelector and other
magic? - [DROID 5](http://droid5.yourwiki.net/wiki/DROID_5.0)   -
[JHOVE](http://hul.harvard.edu/jhove/)  JHOVE is an extensible,
Java-based tool developed for the JSTOR/Harvard Object Validation
Environment ([http://www.jstor.org/](http://www.jstor.org/)  ) aimed at
validating digital objects. It builds on a magic number approach and
adds much richer parsing functionality in order to extract more
information and more thoroughly assess validity. - Apparently tends to
fail awkwardly when the network latency is high. - Also uses it's own
system of type identifiers.- Adds attributes/metadata? - Validates?

InfernoInferno is a Java-based tool for rule inference and application
of such sets of rules. It is currently heavily biased towards
charcterization. It was developed at the Danish Royal Library as a
proof-of-concept for using rule inference as an unifying approach to
characterization, both directly to perform characterization tasks, and
indirectly to integrate results from various existing characterization
tools in an optimal way.

Inferno has been successfully applied to file and text string
characterization by text file encoding (Latin 1, UTF-8, UTF-16LE and
UTF-16BE), file type (text file encoding, JPEG and PNG) and language
used in text file (Danish, Swedish, English and Norwegian).

-   Implementation not available yet.
-   Is this done using one of the available [rule
    engines](http://java-source.net/open-source/rule-engines)  ?

Other Tools
-----------

-   See [PRONOM
    links](http://www.nationalarchives.gov.uk/aboutapps/PRONOM/tools.htm)
     
-   [NLNZ Metadata Extraction
    Tool](http://www.natlib.govt.nz/about-us/current-initiatives/past-initiatives/metadata-extraction-tool)
     ,
    [http://meta-extractor.sourceforge.net/](http://meta-extractor.sourceforge.net/)
     .
-   [FITS](http://code.google.com/p/fits/)   and links therein...
-   Use pdffonts and other code from pdf-utils
    ([xpdf](http://www.foolabs.com/xpdf/)   or
    [Poppler](http://poppler.freedesktop.org/)  ) to extract
    information, like font dependencies.

Preservation Strategies
=======================

In many cases, a mixture.

Migration
---------

Authenticity issues.

Emulation
---------

Complexity, Russion dolls.

Living Archive
--------------

e.g. The Web. Limited coverage.

Normalised Archive
------------------

Limited coverage and controlled input. See [Quality Control
Methods](http://anjackson.net/digital_preservation_notebook/preservation_strategies/quality_control_methods)
 .

Migration Tools & Pathways
==========================

Migrations
----------

-   Migrations with Image Magick:\
-   Use
    [-list](http://www.imagemagick.org/script/command-line-options.php#list)
      and -version etc to auto-build service info and pathways.
-   Migrating wiki pages, via HTML, or HTML to Wiki.\
-   [http://diberri.dyndns.org/wikipedia/html2wiki/](http://diberri.dyndns.org/wikipedia/html2wiki/)
     \
-   [http://www.aaronsw.com/2002/html2text/](http://www.aaronsw.com/2002/html2text/)
     \
-   [http://deplate.sourceforge.net/](http://deplate.sourceforge.net/)
     \
-   [http://wiki.docbook.org/topic/Html2DocBook](http://wiki.docbook.org/topic/Html2DocBook)
     \
-   [http://wiki.docbook.org/topic/ConvertOtherFormatsToDocBook](http://wiki.docbook.org/topic/ConvertOtherFormatsToDocBook)
     
-   Convert fonts between formats:\
-   [http://www.ics.uci.edu/\~chenli/pdf-font-types/index.html](http://www.ics.uci.edu/%7Echenli/pdf-font-types/index.html)
     \
-   [http://fondu.sourceforge.net/](http://fondu.sourceforge.net/)  \
-   Fun With Encodings Awaits.
-   Migrating wiki pages, via HTML, or HTML to Wiki.\
-   [http://diberri.dyndns.org/wikipedia/html2wiki/](http://diberri.dyndns.org/wikipedia/html2wiki/)
     \
-   [http://www.aaronsw.com/2002/html2text/](http://www.aaronsw.com/2002/html2text/)
     
-   Migrating to XML, [MIXED](http://mixed.dans.knaw.nl/)  \
-   Mostly databases, like SIARD.\
-   See also [this news
    article](http://lonewolflibrarian.wordpress.com/2009/06/17/digital-preservation-by-immediate-conversion-to-xml-06-17-09/)
     
-   Could also merge in the [CRiB service](http://crib.dsi.uminho.pt/)
     .

Quality Control Methods
=======================

-   Create a .NET service to [strip macros from
    OpenXML](http://openxmldeveloper.org/articles/1868.aspx)  .
-   Use a [HTML Tidy
    profile](http://tidy.sourceforge.net/docs/quickref.html)   and
    implements as a [JTidy](http://jtidy.sourceforge.net/)   service.

Quality Assurance
=================

This is the hard part. e.g the comparator that compares two sets of
measured properties and evaluates the difference.

Digital Object Storage
======================

Here, we will not worry about the system that [keeps the bits
safe](http://anjackson.net/digital_preservation_notebook/bit_preservation)
 , but start with the assumption that we have some reliable digital
object repository that supports one or more protocols, allowing items to
be read and written. - [BuildingScalableInfrastructures]

Repository Systems
==================

Ideally, we want repositories of digital objects, with features like: -
Versioning. - Change-logs/audit trails. - Metadata attachments -
Relationships. - Trusted Repository
([TRAC](http://www.crl.edu/content.asp?l1=13)  ) conformance.

Digital Object Storage Systems
------------------------------

-   The file system.\
-   Actually, many different implementations and not enough standards.
-   Content Management Systems\
-   [Fedora](http://www.fedora-commons.org/documentation/3.0b1/userdocs/digitalobjects/objectModel.html)
     \
-   [DSpace](http://www.dspace.org/)  \
-   [Alfresco](http://www.alfresco.com/)   (embedded by Adobe)\
-   Anything with an OAI-PMH interface (see next section).
-   Similar to [Open Service Interface
    Definitions](http://en.wikipedia.org/wiki/Open_Service_Interface_Definitions)
     ? Standards for Document Repositories
-   [The JISC Digital Repository Programme as part of its work is
    exploring the interaction between repositories and other
    systems.](http://www.ukoln.ac.uk/repositories/digirep/index/Deposit_API)
     
-   [DSpace API
    Outline](http://www.dlib.org/dlib/january03/smith/01smith.html)  
-   Multiple, so need a repository definition layer that defines:\
-   Read method (HTTP hopefully).\
-   Write method (HTTP too, on WebDAV etc, but we may need property
    definitions for different services).\
-   Authentication system. Write, and probably reads need authentication
    with the repo.
-   WebDAV plus standard metadata partner file ('''name'''.metadata.xml)
    would be fine for uploads.
-   IDEA: Local wrapper allowing WebDAV access to selected local
    files/directories would be a nice way of allowing Planets access to
    arbitrary file resources. Even if just read-only access.

Content Access Protocols
========================

Content Access Prototols
------------------------

The pipes that make the sources work.
[OAI-PMH](http://www.openarchives.org/OAI/openarchivesprotocol.html)
 See [this overview](http://xml.coverpages.org/oams.html)  . -
[Attaching DC, RFC 1807 or MARC
metadata](http://www.openarchives.org/OAI/1.0/openarchivesprotocol.htm#appendix%201)
  - [A Java
Harvester](http://www.oclc.org/research/software/oai/harvester2.htm)  .
- [A big list of repositories](http://gita.grainger.uiuc.edu/registry/)
 . - [http://arxiv.org/help/oa/index](http://arxiv.org/help/oa/index)  
- [Summary of ResearchArchive at Victoria University of
Wellington](http://gita.grainger.uiuc.edu/registry/details.asp?id=2208)
  - [XML Schemas and Support for Multiple Record Formats in
OAI-PMH](http://www.oaforum.org/tutorial/english/page5.htm)   AtomPub -
[AtomServer](http://atomserver.codehaus.org/index.html)  , [AtomServer
article](http://www.infoq.com/articles/atomserver)  , APL - [Apache
Abdera](http://incubator.apache.org/abdera/)   APL - [Atomojo server &
client](http://code.google.com/p/atomojo/)   NBSD -
[atom-multipart](http://www.tbray.org/ongoing/When/200x/2008/07/07/Atom)
  - [Offical Atom link
relationships](http://www.iana.org/assignments/link-relations.html)  . -
[Fedora](http://www.fedora.info/documentation/)   - Supports a range of
APIs, some Fedora-specific, and OAI-PMH too. - Stores and moves in
[FOXML](http://www.fedora.info/download/2.2.1/userdocs/digitalobjects/introFOXML.html)
 

Others
------

-   DB access, Amazon S3, DSpace, WebDav, CalDav, JCR, Atom, etc. -
    [Content Management Interoperability
    Services](http://en.wikipedia.org/wiki/Content_Management_Interoperability_Services)
      - [Google Data APIs (like
    Atom)](http://code.google.com/apis/gdata/)   - [Windows Live Data
    API](https://dev.live.com/livedata/sdk/Default.aspx)   List, from
    [http://discerning.com/topics/standards/resource\_management.txt](http://discerning.com/topics/standards/resource_management.txt)
     
-   list(resource\_path, query\_expr, accept\_mime\_type) these kinds of
    formats
-   HXDLG http://hdlg.sourceforge.net/
    xmlns=http://www.hdlg.info/XML/filesystem
-   manifest.xml xmlns=http://openoffice.org/2001/manifest
-   atom:feed "application/rss+xml revision=http://purl.org/rss/1.0/"
-   RMP (builtin) - Web Collections http://www.w3.org/TR/NOTE-XMLsubmit
-   OAI-PMH
    xmlns="http://www.openarchives.org/OAI/2.0/static-repository"
-   TODO: RDDL http://www.rddl.org/rddl2 (explain what namespaces mean)
    and http://www.w3.org/2001/tag/doc/nsDocuments/
-   simply lists all metadata objects for all immediate children, in a
    XML response wrapper

      <collection xmlns="http://gupe.org/rmp" path="some/resource_path">
        <collection name="fred" ...>       <atom:entry>...</atom:entry>
        </collection>     <data name="fred/xml">     </data>  
    </collection>

Metadata Standards
==================

-   [Dublin Core](http://dublincore.org/)  \
-   Note finding that [dc.identifier is not an unambiguous identifier
    for that which should be preserved, as it may point to a derived
    representation](http://libtechissues.blogspot.com/2006/12/digital-preservation-using-oai-pmh-as.html)
     .
-   [MARC](http://www.loc.gov/marc/)  
-   Bibliographic, authority and related metadata.
-   [METS](http://www.loc.gov/standards/mets/)  
-   a container/wrapper?\
-   [METS -
    Structural](http://www.loc.gov/standards/mets/METSOverview.v2.html)
     
-   [MODS](http://www.loc.gov/standards/mods/)  
-   Metadata Object Description Schema (relations?)\
-   [MODS - Descriptive](http://www.loc.gov/standards/mods/)  
-   [RFC 1807](http://rfc.net/rfc1807.html)  
-   Bibliographic metadata.
-   [ONIX](http://libraries.mit.edu/guides/subjects/metadata/standards/onix.html)
     
-   ONline Information eXchange
-   [MIT Selected Metadata
    Standards](http://libraries.mit.edu/guides/subjects/metadata/standards.html)
      and notes therein contain lots of information. There are clearly
    metadata standards for different classes of data and metadata.
-   [Z39.87 Data dictionary - Technical Metadata for Digital Still
    Images (MIX)](http://www.loc.gov/standards/mix/)  
-   [EXIF - Images](http://www.jeita.or.jp/)  
-   [IPTC/XMP - Images](http://www.iptc.org/IPTC4XMP/)  
-   [MIX -
    Images](http://www.niso.org/standards/resources/Z39_87_trial_use.pdf)
     
-   [Open Archives Initiative](http://www.openarchives.org/)  
-   [PBCore - Video/Audio](http://www.utah.edu/cpbmetadata/)  
-   [SMPTE - Video/Audio](http://www.smpte-ra.org/mdd)  

PREMIS - [PREMIS](http://www.loc.gov/standards/premis/)   - [Using
PREMIS with METS](http://www.loc.gov/standards/premis/premis-mets.html)
  - [PREMIS Tools](http://www.loc.gov/standards/premis/tools.html)  
CrosswalkingMigrations that convert between metadata formats, mapping
elements of one into the other. -
[bibtex2rdf](http://www.l3s.de/%7Esiberski/bibtex2rdf/)  .

References
----------

-   This book is quite good: [Metadata for Digital Resources:
    Implementation, Systems Design and
    Interoperability](http://www.amazon.co.uk/gp/product/1843343010?ie=UTF8)
     
-   [A Standards Primer - Understanding Technology Standardization
    Efforts](http://stephesblog.blogs.com/my_weblog/2008/04/a-standards-pri.html)
     .

Digital Preservation Projects
=============================

Digital Preservation
--------------------

-   [Planets](http://www.planets-project.eu/)  
-   [PADI - Preserving Access to Digital
    Information](http://www.nla.gov.au/padi/)   lots of useful, deep
    information.
-   [PADI - Digital preservation
    strategies](http://www.nla.gov.au/padi/topics/18.html)  
-   [PANIC - Preservation webservices Architecture for Newmedia and
    Interactive Collections](http://metadata.net/panic/)  
-   [Data Portability](http://dataportability.org/)  , [Data
    Portability, for
    Developers](http://wiki.dataportability.org/display/dpmain/For+Developers)
      \#\# Software Archives \#\#

-   Web Browsers\
-   [Netscape 4.7 - 9.0](http://browser.netscape.com/releases)  \
-   [Netscape 3.0 - 3.04](http://sillydog.org/narchive/full123.php)  

The Digital Preservation Community
==================================

-   Organisations\
-   [DPC](http://www.dpconline.org/)  , etc etc...\
-   Steering Factors, EU, Digital Britain,
-   Conferences\
-   [Joint Conference on Digital Libraries](http://www.jcdl.org/)  \
-   [International Conference on Digital
    Preservation](http://rdd.sub.uni-goettingen.de/conferences/ipres/ipres-en.html)
     \
-   [iPres 2009](http://www.cdlib.org/iPres/)  \
-   [European Conference on Digital
    Libraries](http://www.ecdlconference.eu/)  
-   Journals\
-   [International Journal of Digital Curation](http://www.ijdc.net/)  \
-   [Code4Lib](http://journal.code4lib.org/)  \
-   [International Journal on Digital
    Libraries](http://www.dljournal.org/)  
-   People:\
-   [Herbert Van de Sompel -
    Papers](http://public.lanl.gov/herbertv/papers/)  

Physical Media
==============

Notes on different physical media for storing digital data. \# Disk
Image Tools \#

All disks are block devices... blah... Volumes, partitions, file
systems, ??? \# Imaging Tools \#

Software for pulling the bits off a disk. Note that
[forensicswiki.org](http://www.forensicswiki.org/) has some useful info
on this.

-   [Disk
    Imaging@forensicswiki.org](http://www.forensicswiki.org/wiki/Category:Disk_Imaging)
     
-   [AIR - Automated Image and
    Restore](http://air-imager.sourceforge.net/)  
-   [dskdump](http://linux.die.net/man/1/dskdump)  
-   [ddrescue@forensicswiki.org](http://www.forensicswiki.org/wiki/Ddrescue)
     
-   [dcfldd@forensicswiki.org](http://www.forensicswiki.org/wiki/Dcfldd)
     
-   [rdd](http://sourceforge.net/projects/rdd/), 'robust with respect to
    read errors'.
-   [AcetoneISO](http://sourceforge.net/projects/acetoneiso2/)  
-   [Snorkel](http://www.holmes.nl/NFIlabs/Snorkel/), which is Java, and
    interesting, but closed-source and by-arrangement.
-   [PyFlag](http://www.pyflag.net/) includes disk forensics

Drive Emulation
---------------

-   [CDemu, a CD/DVD drive emulator for
    Linux](http://cdemu.sourceforge.net/)
-   [Mount raw CD-ROM
    image](http://superuser.com/questions/27895/mount-raw-cd-rom-image)
-   this has some good info.
-   [DAEMON Tools for Windows](http://www.daemon-tools.cc/)

Converting between image formats
--------------------------------

-   [A list of tools for
    linux](http://qgqlochekone.blogspot.com/2008/04/iso-linux-debian-venenux-tools.html)
-   [CloneCD image to ISO image file
    converter](http://sourceforge.net/projects/ccd2iso)

File System Support
===================

How to interpret the bits of a disk image and turn it into a set of
files. e.g. NTFS, FAT, ADFS, ISO, etc.

-   [Comparison of file
    systems](http://en.wikipedia.org/wiki/Comparison_of_file_systems)
-   [File
    Systems@forensicswiki.org](http://www.forensicswiki.org/wiki/File_Systems)
-   [LIBDSK](http://www.seasip.demon.co.uk/Unix/LibDsk/) is a library
    for accessing discs and disc image files.
-   [ADFS](http://mdfs.net/Docs/Comp/Disk/Format/ADFS)
-   [Reading DFS and ADFS floppy disks under
    Linux](http://www.adsb.co.uk/bbc/linux/)
-   [FUSE ADFS](http://www.boddie.org.uk/david/Projects/Python/FUSE)
-   [Linux kernel file system
    support](http://howto.wikia.com/wiki/Howto_configure_the_Linux_kernel/fs)

