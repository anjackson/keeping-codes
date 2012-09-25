# Digital Preservation Notebook #

This notebook is a place to record useful tidbits of information about digital preservation. The [Wikipedia page on Digital Preservation][1]   provides quite a good overview of the field, but this notebook intends to dig a little deeper.
Roughly speaking, the technical side of digital preservation can be broken down into two parts:
 - Preserving the bytes. - Preserving access to the digital objects those bytes describe.
Most of this notebook deals with the latter issue, i.e. with how to preserve the meaning of digital objects so that they remain accessible over time. Of course, all of that work is based on the assumption that we can keep the actual binary data safe from bit-rot, and so the [first section][2]   will look at that issue.
# Bit Preservation #

The other sections of this notebook generally assume that there will be some digital objects storage system that can be relied upon to hold the bytes safely over time. Indeed, I believe it is sensible to deal with the bit-storage and access problems separately, in the sense that any access solutions should be designed to work independently of the chosen bit-store solution.
I used to think that the bit-storage problem was [essentially solved][3]  , but I have since realised that fighting bit-rot is not as easy as I originally thought.
...tbc...

## Keeping Bits Safe ##

 - Refreshing
 - Replication 
 - [MAID][4]   
 - etc... - [Long-term performance analysis of Intel Mainstream SSDs][5]

# Digital Object Formats #

See also this related effort: [Wikibook: Choosing The Right File Format][6] . [http://www.dptp.org/course/][7] 

## File Format Registries ##

 - Format registries to include:
 - A file extension registry?
 - [File Free File Command][8]
 - [JMimeMagic][9]   can help here.
 - [MIME Types][10]
 - [PRONOM][11]
 - [Global Digital Format Registry][12]
 - [Apple Uniform Type Identifiers][13]
 - [http://www.digitalpreservation.gov/formats/intro/format_eval_rel.shtml][14]

## Documents ##

 - Open Office v. Office Open XML 
 - [Compound Document Format][15]   
 - HTML

## Databases ##

Preservation-Format Approach.
 - [DANS M-XML][16]  
  - SIARD, [Providing Authentic Long-term Archival Access to Complex Relational Data][17]  

## Images ##

 - [JPEG][18]   
 - [JPEG 2000][19]  

# Digital Object Properties #

## Significant Properties ##

See [JISC: The Significant Properties of Digital Objects][20]  
Issues with this concept are legion.

# Property Extraction Methods #

Magic numbersMagic numbers is the name for the standard UNIX mechanism used to identify file types. This approach is not limited to UNIX, but is usually considered a UNIX related practice that has since spread to many other platforms. The mechanism is based on a database that maps byte strings and positions to file types. Common examples are GIF, JPEG and TIFF, that all contain reliable markers, at least for identifying the general file format. Minor version identification (i.e., format characterization rather than format identification) often requires a more sophisticated approach, e.g. parsing of header structures. On a UNIX system, the magic number mechanism can be accessed using the file command, e.g.:

`kb005264:~/Code/Graphics andersjohansen$ file logo.png`
`logo.png: PNG image data, 64 x 64, 8-bit/color RGBA, non-interlaced`

Advantages are fast performance and reliable identification for many file formats. Limitations include that often minor version variations can’t be determined (i.e., less than reliable characterization), that the method does not allow for formats that lack reliable identification strings (such as text files), and that it uncritically accepts the evidence (e.g., if a text file contains the magic number for a GIF file, the file command will identify it as a GIF file, regardless of other evidence).

# Property Extraction Tools #

[DROID][21]  DROID identifies files using the magic numbers approach.
 - Refers to [PRONOM][22]  , e.g. ''info:pronom/fmt/100'' is HTML 4.01. 
 - Required manual proxy configuration via text-file-hacking. 
 - Use ProxySelector and other magic? 
 - [DROID 5][23]  
 - [JHOVE][24]  JHOVE is an extensible, Java-based tool developed for the JSTOR/Harvard Object Validation Environment ([http://www.jstor.org/][25]  ) aimed at validating digital objects. It builds on a magic number approach and adds much richer parsing functionality in order to extract more information and more thoroughly assess validity.
 - Apparently tends to fail awkwardly when the network latency is high. - Also uses it's own system of type identifiers.- Adds attributes/metadata? - Validates?

InfernoInferno is a Java-based tool for rule inference and application of such sets of rules. It is currently heavily biased towards charcterization. It was developed at the Danish Royal Library as a proof-of-concept for using rule inference as an unifying approach to characterization, both directly to perform characterization tasks, and indirectly to integrate results from various existing characterization tools in an optimal way.

Inferno has been successfully applied to file and text string characterization by text file encoding (Latin 1, UTF-8, 
UTF-16LE and UTF-16BE), file type (text file encoding, JPEG and PNG) and language used in text file (Danish, Swedish, English and Norwegian).

 - Implementation not available yet. 
 - Is this done using one of the available [rule engines][26]  ?

## Other Tools ##

 - See [PRONOM links][27]   
 - [NLNZ Metadata Extraction Tool][28]  , [http://meta-extractor.sourceforge.net/][29]  . 
 - [FITS][30]   and links therein... 
 - Use pdffonts and other code from pdf-utils ([xpdf][31]   or [Poppler][32]  ) to extract information, like font dependencies.

# Preservation Strategies #

In many cases, a mixture.

## Migration ##

Authenticity issues.

## Emulation ##

Complexity, Russion dolls.

## Living Archive ##

e.g. The Web.
Limited coverage.

## Normalised Archive ##

Limited coverage and controlled input.
See [Quality Control Methods][33]  .

# Migration Tools & Pathways #

## Migrations ##

 - Migrations with Image Magick:    
 - Use [-list][34]   and -version etc to auto-build service info and pathways. 
 - Migrating wiki pages, via HTML, or HTML to Wiki.    
 - [http://diberri.dyndns.org/wikipedia/html2wiki/][35]     
 - [http://www.aaronsw.com/2002/html2text/][36]     
 - [http://deplate.sourceforge.net/][37]     
 - [http://wiki.docbook.org/topic/Html2DocBook][38]     
 - [http://wiki.docbook.org/topic/ConvertOtherFormatsToDocBook][39]   
 - Convert fonts between formats:    
 - [http://www.ics.uci.edu/~chenli/pdf-font-types/index.html][40]     
 - [http://fondu.sourceforge.net/][41]     
 - Fun With Encodings Awaits. 
 - Migrating wiki pages, via HTML, or HTML to Wiki.    
 - [http://diberri.dyndns.org/wikipedia/html2wiki/][42]     
 - [http://www.aaronsw.com/2002/html2text/][43]   
 - Migrating to XML, [MIXED][44]      
 - Mostly databases, like SIARD.   
 - See also [this news article][45]  
 - Could also merge in the [CRiB service][46]  .

# Quality Control Methods #

 - Create a .NET service to [strip macros from OpenXML][47]  . 
- Use a [HTML Tidy profile][48]   and implements as a [JTidy][49]   service.

# Quality Assurance #

This is the hard part.
e.g the comparator that compares two sets of measured properties and evaluates the difference.

# Digital Object Storage #

Here, we will not worry about the system that [keeps the bits safe][50]  , but start with the assumption that we have some reliable digital object repository that supports one or more protocols, allowing items to be read and written.
 - [BuildingScalableInfrastructures]

# Repository Systems #

Ideally, we want repositories of digital objects, with features like:
 - Versioning. 
 - Change-logs/audit trails. 
 - Metadata attachments 
 - Relationships. 
 - Trusted Repository ([TRAC][51]  ) conformance.

## Digital Object Storage Systems ##

 - The file system.    
 - Actually, many different implementations and not enough standards. 
 - Content Management Systems    
 - [Fedora][52]     
 - [DSpace][53]     
 - [Alfresco][54]   (embedded by Adobe)   
 - Anything with an OAI-PMH interface (see next section). 
 - Similar to [Open Service Interface Definitions][55]  ?
Standards for Document Repositories 
 - [The JISC Digital Repository Programme as part of its work is exploring the interaction between repositories and other systems.][56]  
 - [DSpace API Outline][57]   
 - Multiple, so need a repository definition layer that defines:    
 - Read method (HTTP hopefully).   
 - Write method (HTTP too, on WebDAV etc, but we may need property definitions for different services).   
 - Authentication system. Write, and probably reads need authentication with the repo. 
 - WebDAV plus standard metadata partner file ('''name'''.metadata.xml) would be fine for uploads. 
 - IDEA: Local wrapper allowing WebDAV access to selected local files/directories would be a nice way of allowing Planets access to arbitrary file resources. Even if just read-only access.

# Content Access Protocols #

## Content Access Prototols ##

The pipes that make the sources work.
[OAI-PMH][58]  See [this overview][59]  .
 - [Attaching DC, RFC 1807 or MARC metadata][60]   
 - [A Java Harvester][61]  . 
 - [A big list of repositories][62]  . 
 - [http://arxiv.org/help/oa/index][63]   
 - [Summary of ResearchArchive at Victoria University of Wellington][64]   
 - [XML Schemas and Support for Multiple Record Formats in OAI-PMH][65]  
AtomPub 
 - [AtomServer][66]  , [AtomServer article][67]  , APL 
 - [Apache Abdera][68]   APL 
 - [Atomojo server & client][69]   NBSD 
 - [atom-multipart][70]   
 - [Offical Atom link relationships][71]  .
 - [Fedora][72]   
 - Supports a range of APIs, some Fedora-specific, and OAI-PMH too. - Stores and moves in [FOXML][73]  

## Others ##

 - DB access, Amazon S3, DSpace, WebDav, CalDav, JCR, Atom, etc. - [Content Management Interoperability Services][74]   - [Google Data APIs (like Atom)][75]   - [Windows Live Data API][76]  
List, from [http://discerning.com/topics/standards/resource_management.txt][77]  
 - list(resource_path, query_expr, accept_mime_type) these kinds of formats 
 - HXDLG http://hdlg.sourceforge.net/ xmlns=http://www.hdlg.info/XML/filesystem 
 - manifest.xml xmlns=http://openoffice.org/2001/manifest 
 - atom:feed "application/rss+xml revision=http://purl.org/rss/1.0/" 
 - RMP (builtin) - Web Collections http://www.w3.org/TR/NOTE-XMLsubmit 
 - OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/static-repository" 
 - TODO: RDDL http://www.rddl.org/rddl2 (explain what namespaces mean) and http://www.w3.org/2001/tag/doc/nsDocuments/ 
 - simply lists all metadata objects for all immediate children, in a XML response wrapper
    
      <collection xmlns="http://gupe.org/rmp" path="some/resource_path">
        <collection name="fred" ...>
          <atom:entry>...</atom:entry>
        </collection>
        <data name="fred/xml">
        </data>
      </collection>
    

# Metadata Standards #

 - [Dublin Core][78]      
 - Note finding that [dc.identifier is not an unambiguous identifier for that which should be preserved, as it may point to a derived representation][79]  . 
 - [MARC][80]   
 - Bibliographic, authority and related metadata. 
 - [METS][81]   
 - a container/wrapper?    
 - [METS - Structural][82]   
 - [MODS][83]   
 - Metadata Object Description Schema (relations?)    
 - [MODS - Descriptive][84]  
 - [RFC 1807][85]  
 - Bibliographic metadata.
 - [ONIX][86]  
 - ONline Information eXchange
 - [MIT Selected Metadata Standards][87]   and notes therein contain lots of information. There are clearly metadata standards for different classes of data and metadata.
 - [Z39.87 Data dictionary - Technical Metadata for Digital Still Images (MIX)][88]  
 - [EXIF - Images][89]  
 - [IPTC/XMP - Images][90]  
 - [MIX - Images][91]  
 - [Open Archives Initiative][92]  
 - [PBCore - Video/Audio][93]  
 - [SMPTE - Video/Audio][94]  
PREMISE
 - [PREMIS][95]  
 - [Using PREMIS with METS][96]  
 - [PREMIS Tools][97]  
CrosswalkingMigrations that convert between metadata formats, mapping elements of one into the other.
 - [bibtex2rdf][98]  .

## References ##

 - This book is quite good: [Metadata for Digital Resources: Implementation, Systems Design and Interoperability][99]  
 - [A Standards Primer - Understanding Technology Standardization Efforts][100]  .

# Digital Preservation Projects #

## Digital Preservation ##

 - [Planets][101]  
 - [PADI - Preserving Access to Digital Information][102]   lots of useful, deep information.
 - [PADI - Digital preservation strategies][103]  
 - [PANIC - Preservation webservices Architecture for Newmedia and Interactive Collections][104]  
 - [Data Portability][105]  , [Data Portability, for Developers][106]  
## Software Archives ##

 - Web Browsers   
 - [Netscape 4.7 - 9.0][107]    
 - [Netscape 3.0 - 3.04][108]  

# The Digital Preservation Community #

 - Organisations   
 - [DPC][109]  , etc etc...  
 - Steering Factors, EU, Digital Britain,
 - Conferences   
 - [Joint Conference on Digital Libraries][110]    
 - [International Conference on Digital Preservation][111]       
 - [iPres 2009][112]    
 - [European Conference on Digital Libraries][113]  
 - Journals   
 - [International Journal of Digital Curation][114]    
 - [Code4Lib][115]    
 - [International Journal on Digital Libraries][116]  
 - People:   
 - [Herbert Van de Sompel - Papers][117]  

# Physical Media #

Notes on different physical media for storing digital data.
# Disk Image Tools #

All disks are block devices... blah... Volumes, partitions, file systems, ???
# Imaging Tools #

Software for pulling the bits off a disk. Note that [forensicswiki.org][118]   has some useful info on this.

 - [Disk Imaging@forensicswiki.org][119]  
 - [AIR - Automated Image and Restore][120]   
 - [dskdump][121]   
 - [ddrescue@forensicswiki.org][122]   
 - [dcfldd@forensicswiki.org][123]   
 - [rdd][124]  , 'robust with respect to read errors'. 
 - [AcetoneISO][125]   
 - [Snorkel][126], which is Java, and interesting, but closed-source and by-arrangement. 
 - [PyFlag][127] includes disk forensics

## Drive Emulation ##

 - [CDemu, a CD/DVD drive emulator for Linux][128]   
 - [Mount raw CD-ROM image][129]   
 - this has some good info. 
 - [DAEMON Tools for Windows][130]  

## Converting between image formats ##

 - [A list of tools for linux][131]  
 - [CloneCD image to ISO image file converter][132]  

# File System Support #

How to interpret the bits of a disk image and turn it into a set of files. e.g. NTFS, FAT, ADFS, ISO, etc.

 - [Comparison of file systems][133]   
 - [File Systems@forensicswiki.org][134]   
 - [LIBDSK][135]   is a library for accessing discs and disc image files. 
 - [ADFS][136]      
 - [Reading DFS and ADFS floppy disks under Linux][137]     
 - [FUSE ADFS][138]   
 - [Linux kernel file system support][139]  

  [1]: http://en.wikipedia.org/wiki/Digital_preservation
  [2]: http://anjackson.net/digital_preservation_notebook/bit_preservation
  [3]: http://anjackson.net/2008/06/27/science_digital_preservation
  [4]: http://en.wikipedia.org/wiki/Massive_array_of_idle_disks
  [5]: http://www.pcper.com/article.php?aid=669
  [6]: http://en.wikibooks.org/wiki/Choosing_The_Right_File_Format
  [7]: http://www.dptp.org/course/
  [8]: http://www.darwinsys.com/file/
  [9]: http://sourceforge.net/projects/jmimemagic/
  [10]: http://www.iana.org/assignments/media-types/
  [11]: http://www.nationalarchives.gov.uk/pronom/
  [12]: http://hul.harvard.edu/gdfr/
  [13]: http://developer.apple.com/documentation/Carbon/Conceptual/understanding_utis/utilist/chapter_4_section_1.html#//apple_ref/doc/uid/TP40001319-CH205-CHDIJFGJ
  [14]: http://www.digitalpreservation.gov/formats/intro/format_eval_rel.shtml
  [15]: http://www.w3.org/TR/WICD/
  [16]: http://mixed.dans.knaw.nl/node/114
  [17]: http://arxiv.org/abs/cs/0408054
  [18]: http://delicious.com/beardedstoat/jpeg
  [19]: http://delicious.com/beardedstoat/jpeg2000
  [20]: http://www.jisc.ac.uk/whatwedo/programmes/preservation/2008sigprops
  [21]: http://droid.sourceforge.net/
  [22]: http://www.nationalarchives.gov.uk/pronom/
  [23]: http://droid5.yourwiki.net/wiki/DROID_5.0
  [24]: http://hul.harvard.edu/jhove/
  [25]: http://www.jstor.org/
  [26]: http://java-source.net/open-source/rule-engines
  [27]: http://www.nationalarchives.gov.uk/aboutapps/PRONOM/tools.htm
  [28]: http://www.natlib.govt.nz/about-us/current-initiatives/past-initiatives/metadata-extraction-tool
  [29]: http://meta-extractor.sourceforge.net/
  [30]: http://code.google.com/p/fits/
  [31]: http://www.foolabs.com/xpdf/
  [32]: http://poppler.freedesktop.org/
  [33]: http://anjackson.net/digital_preservation_notebook/preservation_strategies/quality_control_methods
  [34]: http://www.imagemagick.org/script/command-line-options.php#list
  [35]: http://diberri.dyndns.org/wikipedia/html2wiki/
  [36]: http://www.aaronsw.com/2002/html2text/
  [37]: http://deplate.sourceforge.net/
  [38]: http://wiki.docbook.org/topic/Html2DocBook
  [39]: http://wiki.docbook.org/topic/ConvertOtherFormatsToDocBook
  [40]: http://www.ics.uci.edu/%7Echenli/pdf-font-types/index.html
  [41]: http://fondu.sourceforge.net/
  [42]: http://diberri.dyndns.org/wikipedia/html2wiki/
  [43]: http://www.aaronsw.com/2002/html2text/
  [44]: http://mixed.dans.knaw.nl/
  [45]: http://lonewolflibrarian.wordpress.com/2009/06/17/digital-preservation-by-immediate-conversion-to-xml-06-17-09/
  [46]: http://crib.dsi.uminho.pt/
  [47]: http://openxmldeveloper.org/articles/1868.aspx
  [48]: http://tidy.sourceforge.net/docs/quickref.html
  [49]: http://jtidy.sourceforge.net/
  [50]: http://anjackson.net/digital_preservation_notebook/bit_preservation
  [51]: http://www.crl.edu/content.asp?l1=13
  [52]: http://www.fedora-commons.org/documentation/3.0b1/userdocs/digitalobjects/objectModel.html
  [53]: http://www.dspace.org/
  [54]: http://www.alfresco.com/
  [55]: http://en.wikipedia.org/wiki/Open_Service_Interface_Definitions
  [56]: http://www.ukoln.ac.uk/repositories/digirep/index/Deposit_API
  [57]: http://www.dlib.org/dlib/january03/smith/01smith.html
  [58]: http://www.openarchives.org/OAI/openarchivesprotocol.html
  [59]: http://xml.coverpages.org/oams.html
  [60]: http://www.openarchives.org/OAI/1.0/openarchivesprotocol.htm#appendix%201
  [61]: http://www.oclc.org/research/software/oai/harvester2.htm
  [62]: http://gita.grainger.uiuc.edu/registry/
  [63]: http://arxiv.org/help/oa/index
  [64]: http://gita.grainger.uiuc.edu/registry/details.asp?id=2208
  [65]: http://www.oaforum.org/tutorial/english/page5.htm
  [66]: http://atomserver.codehaus.org/index.html
  [67]: http://www.infoq.com/articles/atomserver
  [68]: http://incubator.apache.org/abdera/
  [69]: http://code.google.com/p/atomojo/
  [70]: http://www.tbray.org/ongoing/When/200x/2008/07/07/Atom
  [71]: http://www.iana.org/assignments/link-relations.html
  [72]: http://www.fedora.info/documentation/
  [73]: http://www.fedora.info/download/2.2.1/userdocs/digitalobjects/introFOXML.html
  [74]: http://en.wikipedia.org/wiki/Content_Management_Interoperability_Services
  [75]: http://code.google.com/apis/gdata/
  [76]: https://dev.live.com/livedata/sdk/Default.aspx
  [77]: http://discerning.com/topics/standards/resource_management.txt
  [78]: http://dublincore.org/
  [79]: http://libtechissues.blogspot.com/2006/12/digital-preservation-using-oai-pmh-as.html
  [80]: http://www.loc.gov/marc/
  [81]: http://www.loc.gov/standards/mets/
  [82]: http://www.loc.gov/standards/mets/METSOverview.v2.html
  [83]: http://www.loc.gov/standards/mods/
  [84]: http://www.loc.gov/standards/mods/
  [85]: http://rfc.net/rfc1807.html
  [86]: http://libraries.mit.edu/guides/subjects/metadata/standards/onix.html
  [87]: http://libraries.mit.edu/guides/subjects/metadata/standards.html
  [88]: http://www.loc.gov/standards/mix/
  [89]: http://www.jeita.or.jp/
  [90]: http://www.iptc.org/IPTC4XMP/
  [91]: http://www.niso.org/standards/resources/Z39_87_trial_use.pdf
  [92]: http://www.openarchives.org/
  [93]: http://www.utah.edu/cpbmetadata/
  [94]: http://www.smpte-ra.org/mdd
  [95]: http://www.loc.gov/standards/premis/
  [96]: http://www.loc.gov/standards/premis/premis-mets.html
  [97]: http://www.loc.gov/standards/premis/tools.html
  [98]: http://www.l3s.de/%7Esiberski/bibtex2rdf/
  [99]: http://www.amazon.co.uk/gp/product/1843343010?ie=UTF8
  [100]: http://stephesblog.blogs.com/my_weblog/2008/04/a-standards-pri.html
  [101]: http://www.planets-project.eu/
  [102]: http://www.nla.gov.au/padi/
  [103]: http://www.nla.gov.au/padi/topics/18.html
  [104]: http://metadata.net/panic/
  [105]: http://dataportability.org/
  [106]: http://wiki.dataportability.org/display/dpmain/For+Developers
  [107]: http://browser.netscape.com/releases
  [108]: http://sillydog.org/narchive/full123.php
  [109]: http://www.dpconline.org/
  [110]: http://www.jcdl.org/
  [111]: http://rdd.sub.uni-goettingen.de/conferences/ipres/ipres-en.html
  [112]: http://www.cdlib.org/iPres/
  [113]: http://www.ecdlconference.eu/
  [114]: http://www.ijdc.net/
  [115]: http://journal.code4lib.org/
  [116]: http://www.dljournal.org/
  [117]: http://public.lanl.gov/herbertv/papers/
  [118]: http://www.forensicswiki.org/
  [119]: http://www.forensicswiki.org/wiki/Category:Disk_Imaging
  [120]: http://air-imager.sourceforge.net/
  [121]: http://linux.die.net/man/1/dskdump
  [122]: http://www.forensicswiki.org/wiki/Ddrescue
  [123]: http://www.forensicswiki.org/wiki/Dcfldd
  [124]: http://sourceforge.net/projects/rdd/
  [125]: http://sourceforge.net/projects/acetoneiso2/
  [126]: http://www.holmes.nl/NFIlabs/Snorkel/
  [127]: http://www.pyflag.net/
  [128]: http://cdemu.sourceforge.net/
  [129]: http://superuser.com/questions/27895/mount-raw-cd-rom-image
  [130]: http://www.daemon-tools.cc/
  [131]: http://qgqlochekone.blogspot.com/2008/04/iso-linux-debian-venenux-tools.html
  [132]: http://sourceforge.net/projects/ccd2iso
  [133]: http://en.wikipedia.org/wiki/Comparison_of_file_systems
  [134]: http://www.forensicswiki.org/wiki/File_Systems
  [135]: http://www.seasip.demon.co.uk/Unix/LibDsk/
  [136]: http://mdfs.net/Docs/Comp/Disk/Format/ADFS
  [137]: http://www.adsb.co.uk/bbc/linux/
  [138]: http://www.boddie.org.uk/david/Projects/Python/FUSE
  [139]: http://howto.wikia.com/wiki/Howto_configure_the_Linux_kernel/fs
