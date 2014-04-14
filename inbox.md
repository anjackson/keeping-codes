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

If you want to really optimise this thing, it should be possible to do all this (including checksum calculation) while only streaming over the whole input stream once. I've been trying to do that in our web archive indexer (which also incorporates the Nanite tool) with some success, but gracefully handling large files is not proving easy when some tools (e.g. DROID, PDFBox Preflight) tend to assume that you have a random access file and can flip to the end of the bitstream and back easily.



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
This is the entry page for a collection of descriptions of the preservation problems encountered with digital material. 

The Stories
-----------

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



## Blog Ideas ##
- Compression Is Not A Significant Property
- Defining Format
- Preservation Planning - Baysian versus frequentist... First principles/ab initio or Empirical modelling.
- eBook wars, like early years of DRM music etc.
- files versus filesystems. Latter obsolete first, former at risk due to persistent ram plus walled gardens.
- Simplification pressure? e.g. Markdown or even Wikipedia? REST over SOAP. HTML over PDF? Others?
* Is ISO Enough? Open standards etc.
* Stack Overflow for Digital Curation
* Trust http://en.wikipedia.org/wiki/Source_criticism
* The Performance Spectrum, just the one.
** http://notepad.benfinoradin.info/2012/08/28/take-a-picture/

http://www.endangeredlanguages.com/lang/3049

Writing:
programming versus car mechanic
http://www.codinghorror.com/blog/2012/05/please-dont-learn-to-code.html
http://www.codinghorror.com/blog/2012/05/so-you-want-to-be-a-programmer.html
programming versus writing, not all of us need to be novelists.


TODO BLOG: Paying for Open Source ('pro', license, support, pooled)
TODO BLOG: Preserving processes, software and test suites.

Time travel
- Passive history is needed too.

Knowing first is impossible
"Need to be very *very* clear about what is to be preserved before developing tools"
https://twitter.com/mopennock/status/375271606085378048

QA costs and variation
"QA for emulation can be at an environment rather than object level so potentially cheaper"
https://twitter.com/euanc/status/375272042511491072

Letters to my son
- Plans for digital preservation
- Scaleability from the low side, to contrast with BL scale later.
- A business opportunity?
- Costs manageable via scale?

My fathers story
- Learning to geek

Career planning computer
- And jobs that didn't exist.

Vendors, communities and trust
-The enthusilasts will be the ones who save us, who are right no biolding the towers flog tepees gain information that thefuure will need to reconstruct t IRS past.
- Also, many institutions hands are tied by the law or he fear of it. The enthusiatst carry on, generally safe from prosecution while non commercial. 
- So how do we trust them? How do we build this expertise into our systems
- Earlier
- A comment by a sceneor manager made me realise that, as things are now, vendor onsolcsnce is a real risk. The only route to establishing a access system relies on extren vendrs. 
- I took it for granted that an institution like the bl would maintain the people it needs to undrstans it's own content. Surely no memory institution could expect to function without the people and code that embody the undrstansibg? We could not function without staff that understand paper, why should digital be different?
- Economics, skills, etc
- But also, contractual approach 
- or at least the wider comm

Sig props and format
- Ce nest par un object numerique
- Our designated communities are already choosing which properties are significant, and expressing that through their choice of format. Our first task, therefore, is to listen.
- Then encourage, protect, refine, converge, champion, etc

Fundamentals of DP
- The Zeroth Preservation Action: Save As...
- Significant Property Schemes 
- Data And Metadata
- The Stack
- Migrations And Emulations
- Choosing the performances: wikipedia black out case study
- Halting problem and the space of all future models equals the no superset problem

Neither Significance Nor Properties
- Significant Properties and the DOPWG
- See http://www.planets-project.eu/private/pages/wiki/index.php/User:Andrewj/To_Do/Properties

Beating Bit-Rot
- Bit Bucket Options: Evaluate existing platforms
- Alignment of non arcival and archival content: What stored where? Who accesses it?
- Problems with Petabyte-for-a-century and the half-life model.
- https://code.facebook.com/posts/229861827208629/scaling-the-facebook-data-warehouse-to-300-pb/
- http://www.openplanetsfoundation.org/blogs/2011-01-12-format-obsolescence-and-sustainable-access
- Pick apart http://queue.acm.org/detail.cfm?id=1866298
"No feasible experiment could validate them. They are projections based on models of how components of the system such as disks and software behave. "

Atlas of Digital Damages
- Big migration matrix plot w no of tools
- Gap Analysis v services spine chart
- Identity tool fails
Start with format corpus
- Parse sig files too.
- Build a map.
- Create an analysis/map-maker application folder?
- Import foreg into it, setting up sync with PRONOM.
- Aim to make the Atlas instead of sync to Drupal.

Registry Game?
- Social pressures plus...
- reward, competitions, achievements, progress tracking, challenges...
- Look at stack overflow and steal...
- Badges:
- {Format [Master} Minter]
- Tweaker (lots of small changes)
- Perfectionist (retweaking)
- Grammartron
- Regex Ninja or Magic Ninja
- Reviewer? Mentor? Teacher?
- Shotgun! Whoever is always there first, reviewing.
- Uploader, Test Data Provider
- Firestarter, first of an edit flurry
- Schema Schemer
- Addict. Most visits.
- Public timeline of achievement 
- Ranking etc

The Rosetta Corpus/Time Capsule
The Bootstraps
-Enough to parse other docs, rather than every possible format.
-Includes multiple codes as well as specifications.
-ASCII, then more...
-Documents and images, types, multiple formats.

Use error-correction codes to patch up bit-level errors?
- http://en.wikipedia.org/wiki/Forward_error_correction
Parity Alternatives
-Format+Size+hash+ECC+brute-force is sufficient?
-Shannon Entropy helps?


----


Wikipedia's echo chamber
Deletionists
Self reinforcing etc.

http://gty.im/149366163

https://intranet.bl.uk:8443/confluence/pages/viewpage.action?pageId=139630062

PMRs:
What worked well?
What hasn't worked well?

2012, the year DP jumped the shark
Rothenberg arguing dp should outline its society by design - long now
Rosenthal's straw man
HTML as rothenbergs types
Still apparently arguing Migration v Emulation, more straw men
Unproven strategies taught?
Hopelessly overambitious levels of preservation, most folks need reasons to get off the bottom rung.

Designing a RCT for DP
- imagine what a auitable RCT would look like
- reverse engineer closest approximation
- argue that TB (and actually pt) are cargo cult science post hoc rationalisation of the first bit only. e.g. modelled on paper, not true process, maps one experiment to one decision,which is unrealistic, as a theory is usually supported by multiple experiments.
- Pt non random sampling as danger
- Strategy, action and then implementation to be chosen separately?
- Current framework evaluates whether the action was implemented well, rather than whether it succeeds in it's aim of preserving digital material. The critical issues, of whether the significant properties you chose are truly significant, are poorly addressed.
- The most important decisions - what strategies shall we consider and why? what significant properties will we use and why? - are not actually documented explicitly.
- This is not a case of theory, but of values, as the basic 'theory' is known (not speculation to be tested). Which PA should be lead by rich understanding of the choices and evaluation should focus on distinguishing those choices rather than their implementation.
- http://en.wikipedia.org/wiki/Design_of_experiments, http://en.wikipedia.org/wiki/Multivariate_testing, RCTs, A/B testing, 
Go back and check Delos paper
See also trial registries http://blogs.worldbank.org/impactevaluations/what-can-we-learn-from-medicine-three-mistakes-to-avoid-when-designing-a-trial-registry-guest-post-b


Every data point is a thought, a mind, etc
Those future users who will, with tears in there eyes, click Save As...
Publishers memory to truly a national memory. Our people's memory
Archives of emotion
Preserve the Mona Lisa by duplication? Delete the original?

Paper on ldwa
- oais as rep model not digital preservation
- Js  stuff
- Storage scaling 
- Characterisation as core problem
- Silly restrictions
- User feedback to judge SIG prop
- Reindexing as bau, hence cluster but any performing chechsumming store could piggyback 
- Linear implied discovery model of oais as painfully wrong
- Catalogue data as derivative data plus annotations
Loop of evaluation at dip stage to PACT preservation actions
Actually linked to stakeholders rather than lone decision maker
Cost rise over time plateau's at 'complete reverse engineering'? Or infinite because of what you are forced to guess
Instead of guessing what they'll need, collect evidence to validate the approach.
Web archive to keep thumbnails, screenshots, Dom trees? Render traces?

### On Format Languages ###
http://www.nationalarchives.gov.uk/PRONOM/Format/proFormatSearch.aspx?status=detailReport&id=1160&strPageToDisplay=summary
I understand the desire to focus PRONOM development on creating signatures, and I realise that keeping the references up to date would be a lot of work. However, I worry that signatures alone are not enough, because without the references, I don't think it's clear what is actually being identified. Without reference to any version of the ISO spec., or indeed MS Office, what does it mean to identify a file as 'Open Office XML' fmt/412? That kind of fine-grained identification is critically important if you wish to really understand the preservation issues around OOXML, because on the strict form has transparent semantics and can be considered preservation friendly. The transitional form is full of opaque semantics like 'render this paragraph like Word95 does'.

Except, actually, right now, it doesn't matter, because as far as I know there is no generally available software that implements OOXML Strict (I think only the latest Office betas do so). So right now, the ambiguity in the PRONOM definition is harmless, and getting into the details is pretty much a waste of time. If you just need to ID files right now, it works just fine.

http://www.zdnet.com/office-to-finally-fully-support-odf-open-xml-and-pdf-formats-7000002696/

Except, except, when the new versions arrive, and the various formats start to get supported to varying degrees, and the standard keep moving and 

Also, it's worth noting that the Open Digital Formats Registry idea is quite close to the Registry Ecosystem idea outline here (http://www.openplanetsfoundation.org/blogs/2011-02-15-file-format-registry-report-released). I used to be quite skeptical about this idea, but I've come around to it (http://www.openplanetsfoundation.org/blogs/2012-07-06-biodiversity-and-registry-ecosystem).

----

BLOG: Vendor Obsolescence, IE6, SilverLight, Flash?
http://blog.colbyrabideau.com/post/8317497197/i-dont-know-how-to-ie6
http://arstechnica.com/microsoft/news/2010/11/silverlight-html5-and-microsofts-opaque-development-strategy.ars
http://www.guardian.co.uk/technology/2011/jun/14/microsoft-windows-8-developers
http://www.zdnet.com/blog/microsoft/microsoft-needs-to-tell-windows-8-developers-now-about-jupiter-and-silverlight/9608
http://www.theregister.co.uk/2011/06/06/windows_tablets_without_silverlight_dot_net/


--- 

BLOG: Re-inventing the wheel (to be changed)
Issue about CITE paper, W3C Fragment effort, and issue about whether the fragment can reference the entity rather than the resource.

http://www.ariadne.ac.uk/issue67/blackwell-hackneyBlackwell/
http://www.w3.org/2008/WebVideo/Fragments/

In particular, if we wish the fragment identifiers to be insulated from some details., i.e. fractions used be CITE rather than pixels, we need to get that in the standard? It does % for spatial dimensions, so is that okay? is that precise enough? What if we want to point at something really small? How many SigFig.


---
Cargo Cult Standards

p.s. and if I anyone starts writing yet another standalone identifier, provenance or metadata standard from scratch, I will come around to your house, take away your computer, and replace it with a Chrome tablet so you always have to GOOGLE IT FIRST. :-)

Every time you start writing a new standalone metadata standard from scratch, God kills a kitten. Please make it stop.

---
BLOG: IT's not that cheap or easy - BBC Archive/Shutdown issue
http://www.wired.co.uk/news/archive/2011-02/11/bbc-torrent-archive-websites
http://www.webcitation.org/60lBTX2oN

---
BLOG: Cargo Cult Standards
BLOG: SCAPE and OPF
BLOG: Deconstructing the Planets Testbed
BLOG: Building Trust
BLOG: Format data model - what is permanent? Why opaque IDs.
BLOG: The long-tail of formats
BLOG: Identifying Microsoft formats. Why DROID and File fail. JHOVE2 it. Use those os and office installers or images to make test corpus?
BLOG/PAPER: Compression & Entropy

Full decomposition of Identification and RI?

RI - IDs - (identify) - TestFiles - (create) - Software - (implements) - RI
RI - (validate) - Testfiles

So, Fido etc manage identifiers, and link to RI about formats.
Identifiers also come with test documents, which describe the SW that created them.
RI has unique IDs and links to information about SW.
RI includes specifications that Validators validate objects against.

---

I'm not sure it's reasonable to expect what is appropriate for the Internet Archive's web archive to be appropriate elsewhere. For example, when accessing the content, the archive's visitors are expected to come to the Wayback Machine armed with the URL of the site they want. They look up the URL, choose the date, and download the items they want, and the interpretation of the content is left entirely to them. Very little metadata is required for discovery, and the IA only need to support access at the protocol level (HTTP has been pretty stable so far).

I think the web archive is quite exceptional in this regard and that, in order to be enable their users to discover and use their collections effectively, most other institutions will have to understand how to interpret their content. For example, to support full-text search, some sort of transformation to plain text is required. One must choose therefore choose whether to make this text version an archival artefact (which assumes it could never be improved), or whether to support the software required to re-parse the original items in order to be able to generate new indexes in the future. Similarly, 

---

Misc. Blog Ideas
 - Format features for standards. Eg mime type embed. 
 - Why open? Other issues than code.
 - Comms not content.
 - OPF: How to join in... (also collect stuff from SF TRAC wiki)
 -    - [https://sourceforge.net/apps/trac/planets-suite/][1]  
 - OPF: Reponse to Planets Testbed Review
 -    - In reponse to [http://e-records.chrisprom.com/?p=1183][2]  
 - OPF:  The need for a roadmap.
 -    - [http://gamearchitect.net/Articles/SoftwareIsHard.html][3] 
   - [http://www.codinghorror.com/blog/2006/04/best-practices-and-puffer-fish.html][4] 
   - [http://www.jisc.ac.uk/events/2010/07/jif10/virtualgoodybag/understandingsustainability.aspx][5] 
 - OPF: Blog on other systems and similarities:[][6] 
 -    - [http://www.naa.gov.au/records-management/secure-and-store/e-preservation/at-naa/software.aspx][7] 
   - Each has a plug-in architecture, each has a new GUI, need to share....
   - [http://inkdroid.org/journal/2010/08/24/notes-on-retooling-libraries/][8] 

 - Blog idea: THE ROBOT[][9] 
 -    - [http://www.youtube.com/my_videos][10] 
   - [http://www.youtube.com/watch?v=3L44R9FJ-9U][11] 
 - On The Naming Of Things
 - On Preserving Conversations
 -    - Blog on HTTP v. HTML
   - Connect to DSHR blog. [http://blog.dshr.org/2010/06/jcdl-2010-keynote.html][12]  

  - Software Engineering versus Computer Sciece. CS4SC? Comp-to-Data arc.
http://www.delicious.com/beardedstoat/cs4sc

OPF Ideas

Idea: Double-check and publicise:
 - Write on iPres BOF etc session. Merrit, JHOVE, etc.
 - The Open Planets Foundation at iPres: Exploring Planets and Beyond
 - http://www.openplanetsfoundation.org/node/31


OPF Education Links
 - Move our training resources page to OPF
 - http://blogs.ecs.soton.ac.uk/keepit/2010/08/23/keepit-course-3-game-playing-characterisation-transmission-metadata-and-provenance/
 - http://blogs.ecs.soton.ac.uk/keepit/2010/08/23/keepit-course-3-introducing-preservation-workflow-and-format-risks/
 - http://blogs.ecs.soton.ac.uk/keepit/2010/08/23/keepit-course-3-significant-characteristics/
 - [http://blogs.ecs.soton.ac.uk/keepit/2010/08/23/keepit-course-3-describing-significant-characteristics-and-recording-provenance/][13] 
 - [http://digital-scholarship.org/dcpb/dcpb.htm][14]  Digital Curation and Preservation Bibliography
 - Collect the blog preservation link conversation: [http://lists.ala.org/wws/arc/digipres/2010-08/msg00007.html][15]  


OPF Potential Special Interest Groups
 - Web archiving
 - Removable media
 - Personal archiving
 - Designed to last - Thinking long term when writing software.

OPF: Working with other groups
 - Work with National Digital Stewardship Alliance [http://www.digitalpreservation.gov/ndsa/][16] 
 - [][17] sustaining software effort. [http://www.software.ac.uk/SustainingSoftware.html][18]  
 - Join w3c (7,800 EUR per year!) and make it better. See also http://lists.w3.org/Archives/Public/public-html/



Idea: Communications etc
http://www.guardian.co.uk/commentisfree/2010/aug/09/tony-judt-words-all-we-have-tribute/print
Problem mistaking lack of understanding to lack of clarity/content. Pairwise effects critical.

http://blog.martinh.net/2010/08/intrinsic-motivation-from-magic.html

http://paper.li/digipresnews

http://www.w3.org/2002/09/wbs/1/rdf-2010/results

http://www.digitalpreservation.gov/news/2010/20100809news_article_partners_meeting10.html

http://www.digitalpreservation.gov/news/2010/20100809news_article_GW_presentation.html

http://www.newswiretoday.com/news/75238/

http://stereosubversion.com/commentary/bin-the-black-circle-08-09-2010/

http://www.digitalpreservation.gov/news/2010/20100726news_article_archive-it.html

[http://www.culturegrid.org.uk/][19] 

Planets Techies Mailing List
[https://sourceforge.net/mail/admin/list_subscribers.php?group_id=265364&group_list_id=68391&func=display][20] 





  [1]: https://sourceforge.net/apps/trac/planets-suite/
  [2]: http://e-records.chrisprom.com/?p=1183
  [3]: http://gamearchitect.net/Articles/SoftwareIsHard.html
  [4]: http://www.codinghorror.com/blog/2006/04/best-practices-and-puffer-fish.html
  [5]: http://www.jisc.ac.uk/events/2010/07/jif10/virtualgoodybag/understandingsustainability.aspx
  [6]: http://www.codinghorror.com/blog/2006/04/best-practices-and-puffer-fish.html
  [7]: http://www.naa.gov.au/records-management/secure-and-store/e-preservation/at-naa/software.aspx
  [8]: http://inkdroid.org/journal/2010/08/24/notes-on-retooling-libraries/
  [9]: http://www.naa.gov.au/records-management/secure-and-store/e-preservation/at-naa/software.aspx
  [10]: http://www.youtube.com/my_videos
  [11]: http://www.youtube.com/watch?v=3L44R9FJ-9U
  [12]: http://blog.dshr.org/2010/06/jcdl-2010-keynote.html
  [13]: http://blogs.ecs.soton.ac.uk/keepit/2010/08/23/keepit-course-3-describing-significant-characteristics-and-recording-provenance/
  [14]: http://digital-scholarship.org/dcpb/dcpb.htm
  [15]: http://lists.ala.org/wws/arc/digipres/2010-08/msg00007.html
  [16]: http://www.digitalpreservation.gov/ndsa/
  [17]: http://www.digitalpreservation.gov/ndsa/
  [18]: http://www.software.ac.uk/SustainingSoftware.html
  [19]: http://www.culturegrid.org.uk/
  [20]: https://sourceforge.net/mail/admin/list_subscribers.php?group_id=265364&amp;group_list_id=68391&amp;func=display


