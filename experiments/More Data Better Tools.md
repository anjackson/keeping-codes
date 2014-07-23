---
title: Using Web Archives To Improve Preservation Tools
layout: default
categories: [experiments]
tags: [stub]
publish: true
---

We use Web Archive data to drive tool development.

So, according to our experiments, there are at least two thousand distinct formats in our historical web archive, and at least three thousand if you distinguish between all formats (e.g. HTML) and their specific versions and character sets (e.g. UTF-8). It’s worth pointing out that we don’t really know exactly how precise our identification tools are, and also that a small proportion remains unidentified. Therefore, we don’t yet know exactly how many formats there are. However, the contents of the archives are dominated by HTML, web image formats, PDF, Office documents and so on, and in the ‘tail’ of the distribution, thousands of formats accounts for a very small fraction of the content (not sure exactly, certainly less than 1%). Nevertheless, just because a format is rare, we cannot necessarily assume it is of little value, and I wonder if that is where the real preservation challenge for web archives lies. The ‘big’ formats look after themselves, and require little effort to preserve over moderate timescales. But in the tail of the format distribution, formats are less likely to survive without our intervention, and so we need to be able to work out where to invest our efforts.

I ended up passing my snowballAnalyzer and standardAnalyzers as parameters to ShingleFilterWrappers and processing the outputs via a TermVectorMapper.
http://searchhub.org/2009/05/26/accessing-words-around-a-positional-match-in-lucene/


n.b. the 'long tail' of file extensions in the JISC data set is a foul and hideous mess.
http://192.168.1.151:8984/solr/#/jisc/schema-browser?field=content_type_ext
Need to strip %xx from extensions, e.g. .php%3ffrom=1170
Seems #fragments are not being caught/stripped?
Also '@', '=', '$' among the 'unlikely to be valid extension characters' posse

In the 'null' set:
http://192.168.1.151:8984/solr/#/jisc/query?q=content_type_ext:%22.wps%22

As of 15:11 on 24 Sept 2013: 295,991,273
16:16 295991273

Also c.f. [Testing Software Tools of Potential Interest for Digital Preservation Activities at the National Library of Australia](http://www.openplanetsfoundation.org/system/files/Digital%20Preservation%20Project%20Report%20-%20Testing%20Software%20Tools.pdf)


http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.ico%22

http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.sib%22
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_ffb%3A%220f534942%22
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.mus%22&f[1]=content_ffb%3A%2252454d20%22


Language:
http://www.webarchive.org.uk/aadda-discovery/browse?f[0]=links_public_suffixes%3A%22fr%22&f[1]=content_language%3A%22fr%22

Mining for Signatures
---------------------
Starting with unidentified formats: http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22, we can script a series of queries for different extensions that attempt to build plausible signatures for each, based on the FFB. 

http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22
application/octet-stream: 146,541
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22null%22
null: 351,779 almost all OLE2 with a few ZIP.

11109 .s5, with P%000010 or L%000010 as FFB
5302 .ipx, with very similar FFB, sb%xx01/2/6
4394 .nwc, all with '[Not' with a few '[NWZ' FFB (http://www.noteworthysoftware.com/player/)
3822 .dbf, with mostly 'OPLD' FFB and some other similar binary ones.
2482 .adx, with largely no FFB?

### Psion 5 ###
Starting at 'application/octet-stream' the most common unknown extension was .s5 - this had consistent magic (two FFB variants).
* [psiconv](http://software.frodo.looijaard.name/psiconv/) may be able to extract info/text.
* [s5 Header Format](http://software.frodo.looijaard.name/psiconv/formats/Header_Section.html#Header Section)


Firefox uses application/x-extension-EXT



An old 3D format.
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.mus%22&f[1]=content_ffb%3A%2252454d20%22



Psion s5
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22&f[1]=content_type_ext%3A%22.s5%22

Psion MC/HC/Series 3 data files.
ftp://ftp.cs.tu-berlin.de/pub/palmtops/psion/src.doc.ic-mirror/Unsorted/mcfile.txt
http://www.sat.dundee.ac.uk/~arb/psion/

DBF
www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22&f[1]=content_type_ext%3A%22.dbf%22

dBASE
http://www.dbase.com/Knowledgebase/INT/db7_file_fmt.htm
earlier versions
http://www.clicketyclick.dk/databases/xbase/format/dbf.html#DBF_STRUCT
http://www.clicketyclick.dk/databases/xbase/format/dbf.html#DBF_STRUCT

IPIX
http://en.wikipedia.org/wiki/IPIX
http://www.ipix.com/support/downloads.cfm
www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22&f[1]=content_type_ext%3A%22.ipx%22

AXD
www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22&f[1]=content_type_ext%3A%22.axd%22

NWC
www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22&f[1]=content_type_ext%3A%22.nwc%22


http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_full%3A%22application/zip%22

ArcFS, Spark, etc.

    vim /usr/share/file/magic/archive
> # Acorn archive formats (Disaster prone simpleton, m91dps@ecs.ox.ac.uk)
> # I can't create either SPARK or ArcFS archives so I have not tested this stuff
> # [GRR:  the original entries collide with ARC, above; replaced with combined
> #  version (not tested)]
> #0  byte    0x1a    RISC OS archive (spark format)
> 0 string    \032archive RISC OS archive (ArcFS format)
> 0       string          Archive\000     RISC OS archive (ArcFS format)

Spark, most match 0x1a(82|88|FF).

Followed by:
> # All these were taken from idarc, many could not be verified. Unfortunately,
> # there were many low-quality sigs, i.e. easy to trigger false positives.

http://www.bttr-software.de/freesoft/arc2.htm#idarc


SPSS
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22&f[1]=content_type_served%3A%22application/spss%22

MatLab
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22&f[1]=content_type_served%3A%22application/matlab%22


### Binary NGram Shingling

Along the same lines, experimenting with shingling the hex-encoded first few (32) bytes. We space separate and hex-encode the first 32 bytes of every resource. We pass that to Solr, which treats each hex-encoded byte as a single token. Solr then 'shingles' the tokens, from four to eight overlapping character sequences corresponding to all combinations of byte sequence between four and eight bytes long within the 32 bytes.

The total header size of 32 bytes, and the minimum and maximum shingle lengths of four and eight bytes, have been chosen in an attempt to reduce weak potential signatures (e.g. short byte sequences that might match too often by chance) with the significant storate requirement that arises due to indexing all possible shingles. For smaller collections, it would be possible to extend this technique to much longer shingles throughout whole length of the file.

Initial results from small corpus.
- Long sequences of asterisks notable indicative of .js!
- HTML/PDF signatures bear strong relation to manual ones, but generally spot more possible 'signals'.
- Not terribly useful as a Facet, due to presenting all shorter matching facets even when longer facets (that encapsulate the smaller ones) exist. May be possible to do some fancy facet filtering to make this more powerful.
- Certainly, the field results could be mined and if the offset is know, shingles concatenated into longer ones as appropriate.

See also:
* http://www.forensicswiki.org/wiki/File_Format_Identification
* [](http://web.archive.org/web/20051124132220/http://www.itoc.usma.edu/workshop/2005/Papers/Follow%20ups/FilePrintPresentation-final.pdf)
* [A New Approach to Content-based File Type Detection (2008)](http://arxiv.org/ftp/arxiv/papers/1002/1002.3174.pdf)
* [Predicting the types of file fragments (2008)](http://www.dfrws.org/2008/proceedings/p14-calhoun.pdf)
* [Fast File-type Identification (2010)](http://www.alphaminers.net/thesis/International%20Conference/IAKLHSMH_2010.pdf)
* [Fast Content-Based File Type Identification (2011)](http://link.springer.com/chapter/10.1007/978-3-642-24212-0_5)

### Indexing/Similarity Note:

We are interested in identifying the work, not making a substitutable work available. Crypto hashes are one way of doing this, but less precise hashing methods and signals can be combined to be just as specific, while also telling us something about the content, but while never giving the content away. Encrypted in plain sight.


### Keyword spotting

Pull keywords out of source code formats? Just using the full-text index PLUS extensions.
FUTURE consider token frequencies including punctuation.

Parse Error Analysis
====================

http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22null%22

http://192.168.1.206:8990/solr/#/jisc/schema-browser?field=parse_error


Encryption:

PDF:
- http://192.168.1.182:8989/solr/jisc3/select?q=parse_error%3A%22org.apache.pdfbox.exceptions.CryptographyException%3A+Error%3A+The+supplied+password+does+not+match+either+the+owner+or+user+password+in+the+document.%22&wt=json&indent=true

Office:
- http://192.168.1.182:8989/solr/jisc3/select?q=parse_error%3A%22org.apache.poi.EncryptedDocumentException%3A+Cannot+process+encrypted+word+file%22&wt=json&indent=true
- http://192.168.1.182:8989/solr/jisc3/select?q=parse_error%3A%22org.apache.poi.EncryptedDocumentException%3A+Default+password+is+invalid+for+docId%2FsaltData%2FsaltHash%22&wt=json&indent=true
- http://192.168.1.182:8989/solr/jisc3/select?q=parse_error%3A%22org.apache.poi.hslf.exceptions.EncryptedPowerPointFileException%3A+The+CurrentUserAtom+specifies+that+the+document+is+encrypted%22&wt=json&indent=true
- http://192.168.1.182:8989/solr/jisc3/select?q=parse_error%3A%22org.apache.poi.hslf.exceptions.EncryptedPowerPointFileException%3A+Encrypted+PowerPoint+files+are+not+supported%22&wt=json&indent=true

Fuzzy Hash Analysis
===================

Need to show
* different content making the same hash?
* degree of change of a site over time, e.g. homepages.
* finding similar content across domains?

http://commons.apache.org/proper/commons-lang/javadocs/api-3.1/org/apache/commons/lang3/StringUtils.html#getLevenshteinDistance%28java.lang.CharSequence,%20java.lang.CharSequence,%20int%29

Data in warc-discovery/analysis-tools

www.york.ac.uk
http://192.168.1.206:8990/solr/jisc/select?q=url%3A%22http%3A%2F%2Fwww.york.ac.uk%3A80%2F%22&sort=crawl_date+asc&rows=50&fl=ssdeep_hash_bs_*%2Ccrawl_date&wt=xml&indent=true

www.amazon.co.uk
http://192.168.1.206:8990/solr/jisc/select?q=url%3A%22http%3A%2F%2Fwww.amazon.co.uk%3A80%2F%22&sort=crawl_date+asc&rows=50&fl=ssdeep_hash_bs_*%2Ccrawl_date&wt=xml&indent=true

www.bbc.co.uk
http://192.168.1.206:8990/solr/jisc/select?q=url%3A%22http%3A%2F%2Fwww.bbc.co.uk%3A80%2F%22&sort=crawl_date+asc&rows=50&fl=ssdeep_hash_bs_*%2Ccrawl_date&wt=xml&indent=true

www.wales.gov.uk
http://192.168.1.206:8990/solr/jisc/select?q=url%3A%22http%3A%2F%2Fwww.wales.gov.uk%3A80%2F%22&sort=crawl_date+asc&rows=50&fl=ssdeep_hash_bs_*%2Ccrawl_date&wt=xml&indent=true


Works well for catching small changes in wales and york.  However, need to compare it with raw crypto hash of payload to see if the fuzzy has an advantage.

Case for the others is less clear, partially due to gaps in the record. Really need diffs/overlaps next to change graph.

Could also experiment with profiling location of edits to determine if changes are at top or bottom of the page.

Future work
-----------

Do this with NIST

http://www.nsrl.nist.gov/nsrl-faqs.html#faq19
