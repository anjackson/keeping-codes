---
title:  War stories
layout: default
---

{% include collectionList.html filter="/war-stories/" %}


War Stories - Inbox
-------------------


### Identification Problems and Text Formats

Note that re-building WARCs from files is tricky as we have to infer the right MIME types, and this is not always trivial. We had a migration fail because the tool we used to infer the type relied on the file extension and when this was wrong, HTML got marked octet-stream. Unfortunately, NO files reliably guess scripts/css so unless the extension is there, you can't know what it is without looking through it yourself.


### Virus Scanning Deployment

As a matter of process we virus-scan every bitstream prior to storage. We very seldom get any hits but one that does keep cropping up is “phishing scams” (i.e. fraudulent emails trying to get your bank details). However, in every instance I’ve seen to date the actual object is usually a page of the form “I just got this email which is a phishing scam…”. That is, it’s a warning followed by an example.


### Kakadu DPI loss.

### JHOVE restating the obvious
MSBooks JHOVE property dump. >> documents in many cases.

### Stories of loss 
My first data loss, grandfather disks etc.
http://sethclifford.me/2013/12/11/data-loss-and-noble-truths/

###  Missing Manifests 
Over Summer 2011 the we were asked to help QA the ingest of some digitised newspaper material. The ingest process had finished but the material for both streams was still been held on approximately 80TB of intermediate storage. One of the aims was to be able to delete the material on the intermediate storage, freeing it for other purposes, but only safe in the knowledge that it was all ingested. 

There was also a proposal to supply third-parties with complete sets of both collections. The first problem was that there was no manifest of the digitised material, just a set of files on intermediate storage. Some of these files did provide checksummed manifests of individual batches of material, but it was not easy to ascertain: 

* How many newspaper titles/issues made up each collection? 
* What issues had been digitised for a particular title? 
* Had a particular issued been completely ingested? 

The solution was not entirely satisfactory. We Team produced some scripts that trawled the intermediate storage to produce a manifest. This was produced by listing the files on the disk and parsing the names to give title, issue, and page inventories. The same information was also parsed from the XML manifest files on the intermediate storage. The data was then sorted and consolidated to produce a manifest of every title and issue either found on the intermediate storage, or in the manifest files. The result didn't provide a definitive manifest of the material as any items not on the intermediate storage, or in a manifest file on that storage, will have been missed. This underlines the need for content suppliers to provide full, checksummed manifests up front. 

Even after the manifests of Collection Two material were generated from the intermediate storage (see above), checking that the items on the store had been preserved in full was not easy, and is still not complete. We obtained a manifest of items by: 

* Obtaining the full set of items that had been flagged in the repository system as part of the collection. 
* Parsing these files to pull out the title and issue details from the descriptive metadata, and the page manifest from the METS fileGroup record for the master image container. 

The problems with this approach are 

* The database records are not 100% accurate, meaning that there may be other material that we cannot identify as such. 
* The content items themselves have not been checked so we only know of the issues and pages listed in the METS files. 

### Zipped CDs 
One content stream took digital material from third-parties and ingested them into a commercial repository system to manage the content in pre-ingest. The programme received a significant quantity of material submitted on CD, and DVD. Rather than ingest the files directly, the contents of the CD were first consolidated into a zip file first so only a single item had to be processed. 

There are multiple concerns over this practise: 

* Was compression used when creating the zip files? If so was the compressed data verified to ensure that the decompressed file read from the zip was identical to the original? 
* Were the zip files verified ensuring that all files were present and could be successfully read from the archive? 
* Placing the visible files from a CD into a zip archive does not guarantee that the material will be able to be viewed/used in the future as originally intended. The zip will not contain the boot sector information required to use the contents. 

The last point could be illustrated by taking any Windows installation or audio CD, zipping the contents together and then trying to install Windows, or play the audio tracks from the zip file. 

### Zip Containers 
The zip file format is used for data compression and archiving. Within the repo there are many zip archives, some supplied to us, others created by us. *N.B.* this does not include the zip archives created from optical media which have their own section above. 

### Zip Containers Provided for Ingest 

### Zip Containers Created for Ingest


## Others

* Migration of TIFFs to JP2K 
    * Lack of QA means JP2Ks can't be guaranteed to be valid, or identical to original TIFF (truncated code stream issue). 
    * No manifest, and migrated material means that it's not possible to use the checksum to ascertain whether a particular TIFF is held within DLS. 
    * Some image metadata is missing from the migrated JP2Ks (dpi, colour space) 
* Creation and Storage of PDF versions 
    * PDFs are made up of the TIFF or JPEG2000 master images in a linearized PDF file. This is too big for access. 
    * Dramatically increase storage costs at no benefit. 
    * Creation of PDFs not QA'd but still written to a "write once, never erase" store. 
    * Access PDFs could be created on the fly from JP2Ks (-> JPEG -> PDF) on demand and stored on an access cache. 
* Multi Image TIFF files 
    * What's the story here? I know we have had some multi page TIFF images, just not the context. 
* PDFs that rely on external resources 
    * PDFs containing links to external URLs that may not exist in perpetuity. 
    * Non embedded fonts may mean a document cannot be properly rendered. 
    * There are VDEP PDFs that exhibit both of these problems. 
* Dark archive risk 
* Carrier Degradation
    * Masters on CD-ROM for 10 years 
    * JPEG derivatives on spinning disk for web site 
    * Are the masters still the same? 
