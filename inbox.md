---
title:  Inbox
layout: default
---

All Pages
---------
{% for cat in site.all-category-list %}
### {{ cat | capitalize }}
{% include pageList.html cat=cat unpublished=true %}
{% endfor %}  <!-- cat -->

Outlines
--------

* [Communicating With The Future](fundamentals/Communicating With The Future.html)
* [The Zeroth Law of Digital Preservation](The Zeroth Law of Digital Preservation.html)
* [What's so special about digital preservation?](What is Special About Digital Preservation.html)
* von Neumann Machines
* Code as Communication
* [The First Preservation Action](The First Preservation Action - Save As.html)
* [Codes](codes.html)
* [What to Preserve](What to Preserve.html)
* [A perfect digital preservation experiment](A Perfect Digital Preservation Experiment.html)
* [Credible Threats](Credible Threats.html)
* [Making Plans](Making Plans.html)
* [How to preserve](How to Preserve.html)

Inbox
-----

* Practice
    * Using web archvies to preserve your project.
    * Ref from Bitwiser: Good practice and Quirks Mode
    * Lessons Learned from the Planets Testbed
    * OAIS is clumsy, arbitrary boundary, not user centered.
* Experiments
    * Bitwiser II: ignored v redundant via MC.
* Fundamentals
    * The Perfect Digital Preservation Experiment
    * Simplification pressure? e.g. Markdown or even Wikipedia? REST over SOAP. HTML over PDF? Others?

- Format Herd Immunity
    - Format obsolescence as disease 
    - We are the immune system 
- Data And Metadata, interpretation difference.
- eBook wars, like early years of DRM music etc.
- files versus filesystems. Latter obsolete first, former at risk due to persistent ram plus walled gardens.
-  Is ISO Enough? Open standards etc.
- http://www.endangeredlanguages.com/lang/3049
* Characterising Codes
* Significant properties - content properties not the priority.
   * Dependency analysis and critical characterisation role
   * For content, in future, eye of stakeholder means users should be able to express format preference.


### Sources

* Pull in requirements and issues, AIT stuff.
* Pull in Monitrix, BDT, IMAQA, WAT Mining.
* http://anjackson.net/book/export/html/1836
* http://sourceforge.net/p/xcltools/code/HEAD/tree/
* http://wiki.opf-labs.org/display/SP/Capturing+Properties
* https://intranet.bl.uk:8443/confluence/display/DT/Representation+Information+Capture+Project


Data Mining Methodology
-----------------------
The emphasis on big data and statistical analysis in cultural and social contexts makes me uneasy. There is no 'noise' in humanities data sets. There are only silenced voices.
The direct adoption of big data/statistical methods makes me uneasy. There is no 'noise' in humanities data. There are only silenced voices.

Other: false positive scaling problem http://mobile.theverge.com/2012/10/28/3567048/carnegie-mellon-video-surveillance-action-recognition


Coding at Scale
---------------

Scaling Issues: File numbers

* DROID file handles
* Results, all in memory, JHOVE v Tika.
* Also, Tika at scale issue, where keeping the same class was building up RAM? Need to reinstanciate to make things stop going OOM and/or running OOFileHandles. (???)

Scaling issues: File size, 
Aggressive random-access-file opening:
https://github.com/openplanets/droid/commit/2c9f9b1a86e3fd219ecc8b8ed4cde0b81cfe2057


War Stories - Inbox
-------------------

### Identification Problems and Text Formats

Note that re-building WARCs from files is tricky as we have to infer the right MIME types, and this is not always trivial. We had a migration fail because the tool we used to infer the type relied on the file extension and when this was wrong, HTML got marked octet-stream. Unfortunately, NO files reliably guess scripts/css so unless the extension is there, you can't know what it is without looking through it yourself.


### Virus Scanning Deployment

As a matter of process we virus-scan every object going into DLS. We very seldom get any hits but one that does keep cropping up is “phishing scams” (i.e. fraudulent emails trying to get your bank details). However, in every instance I’ve seen to date the actual object is usually a page of the form “I just got this email which is a phishing scam…”. That is, it’s a warning followed by an example.


### Kakadu DPI loss.

### JHOVE restating the obvious
MSBooks JHOVE property dump. >> documents in many cases.


DP Myths
--------

- The AIP Is Finished (OAIS interpretation issue)
- Significant Property Schemes Will Save Us (Sig Prop interp issue)
- The Bytes Are The Digital Object (process versus state)
- The Format Specification Is Enough (Formal languages thing)
- Formats Are Defined By Specification (The code always comes first)
http://www.library.cornell.edu/iris/tutorial/dpm/oldmedia/obsolescence1.html
- You can fix it with a document (people change each other, the document produced is an artefact not a cause)
- Obsolescence is the main problem
    - Various...
- It's the digital bit of Digital Preservation that makes it difficult (technology, book to audio to flip books to digital to etc growing media complexity and technology dependence.
- Obsolescence means emulation or migration. (porting as a third way)
- Emulation and migration (i think you mean transformation or translocation)
    - PA: Encourage data sharing.
    - PA: Encourage use of sustainable formats.
- Multiple PA mean loss is inevitable, just like analogue. (Countable!)
    - Find that link to that blog.
- Planning mixing choice and implementation in one?
- The solution to every DP problem is a new project from scratch. This time we'll get it right! (from-scratch solutions)
- The basic problem is solved.
- RI needs and processes they support ... 


What is this Page? 
------------------
This is the entry page for a collection of descriptions of the preservation problems encountered with digital material at The British Library. 

The Stories
-----------

### JISC Newspapers & Missing Manifests 
Over Summer 2011 the Digital Preservation Team were asked to help QA the DLS ingest of the JISC newspaper material. The DLS ingest process had finished but the material for both JISC streams was still been held on approximately 80TB of intermediate storage in London. One of the aims was to be able to delete the material on the intermediate storage, freeing it for other purposes, but only safe in the knowledge that it was all ingested into DLS. 

There was also a proposal to supply Bright Solid with a complete set of JISC One, and JISC Two images. The first problem was that there was no manifest of the digitised material, just a set of files on intermediate storage. Some of these files did provide checksummed manifests of individual batches of material, but it was not easy to ascertain: 

* How many newspaper titles/issues made up each collection? 
* What issues had been digitised for a particular title? 
* Had a particular issued been completely ingested into DLS? 

The solution was not entirely satisfactory. The Digital Preservation Team produced some scripts that trawled the intermediate storage to produce a manifest. This was produced by listing the files on the disk and parsing the names to give title, issue, and page inventories. The same information was also parsed from the XML manifest files on the intermediate storage. The data was then sorted and consolidated to produce a manifest of every title and issue either found on the intermediate storage, or in the manifest files. The result didn't provide a definitive manifest of the JISC material as any items not on the intermediate storage, or in a manifest file on that storage, will have been missed. This underlines the need for content suppliers to provide full, checksummed manifests up front. 

Even after the manifests of JISC 2 material were generated from the intermediate storage (see above), checking that the items on the store had been preserved in full within DLS was not easy, and is still not complete. We obtained a manifest of items believed to be JISC 2 newspapers within DLS by: 

* Obtaining the full set of DLS items that had been flagged in the DLS database as JISC 2 METS files. 
* Parsing these files to pull out the title and issue details from the descriptive metadata, and the page manifest from the METS fileGroup record for the master image container. 

The problems with this approach are 

* The DLS database records are not 100% accurate, meaning that there may be other JISC 2 material in DLS that we cannot identify as such. 
* The content items themselves have not been checked so we only know of the issues and pages listed in the METS files. 

### Zipped VDEP CDs 
The Voluntary Deposit content stream took digital material deposited with The British Library, ingested them into a third party repository system called DigiTool, and then exported the DigiTool material for ingest into DLS. The programme received a significant quantity of material submitted on CD, and DVD. Rather than ingest multiple files into DigiTool and DLS, the contents of the CD were first consolidated into a zip file first so only a single item had to be processed. 

There are multiple concerns over this practise: 

* Was compression used when creating the zip files? If so was the compressed data verified to ensure that the decompressed file read from the zip was identical to the original? 
* Were the zip files verified ensuring that all files were present and could be successfully read from the archive? 
* Placing the visible files from a CD into a zip archive does not guarantee that the material will be able to be viewed/used in the future as originally intended. The zip will not contain the boot sector information required to use the contents. 

The last point could be illustrated by taking any Windows installation or audio CD, zipping the contents together and then trying to install Windows, or play the audio tracks from the zip file. 

### DLS Zip Containers 
The zip file format is used for data compression and archiving. Within DLS there are many zip archives, some supplied to the BL, others created by the BL to group like material for ingest into DLS. *N.B.* this does not include the zip archives created from VDEP optical media which have their own section above. 

### Zip Containers Supplied to The British Library 

### Zip Containers Created by The British Library for Ingest into DLS 

* Migration of JISC 1 TIFFs to JP2K 
    * Lack of QA means JP2Ks can't be guaranteed to be valid, or identical to original TIFF (truncated code stream issue). 
    * No manifest, and migrated material means that it's not possible to use the checksum to ascertain whether a particular TIFF is held within DLS. 
    * Some image metadata is missing from the migrated JP2Ks (dpi, colour space) 
* Creation and Storage of PDF Access Versions within DLS 
    * PDFs are made up of the TIFF or JPEG2000 master images in a linearized PDF file. This is too big for access. 
    * Dramatically increase storage costs at no benefit. 
    * Creation of PDFs not QA'd but still written to a "write once, never erase" store. 
    * Access PDFs could be created on the fly from JP2Ks (-> JPEG -> PDF) on demand and stored on an access cache. 
* Multi Image TIFF files 
    * What's the story here? I know we have had some multi page TIFF images, just not the context. 
* PDFs that rely on external resources 
    * VDEP PDFs containing links to external URLs that may not exist in perpetuity. 
    * Non embedded fonts may mean a document cannot be properly rendered. 
    * There are VDEP PDFs that exhibit both of these problems. 
* Lack of Resource Discovery for DLS material 
* Carrier Degradation for IDP material 
    * Masters on CD-ROM for 10 years 
    * JPEG derivatives on spinning disk for web site 
    * Are the masters still the same? 