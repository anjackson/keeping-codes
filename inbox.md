---
title:  Inbox
layout: default
---

## Practice
{% include collectionList.html filter="/practice/" unpublished=true %}

## Experiments
{% include collectionList.html filter="/experiments/" unpublished=true %}

## War Stories
{% include collectionList.html filter="/war-stories/" unpublished=true %}

## Fundamentals
{% include collectionList.html filter="/fundamentals/" unpublished=true %}



## Blog Posts
<ul>
{% for post in site.posts %}
<li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>: <small><strong>{{ post.date | date: "%B %e, %Y" }}</strong> . {{ post.category }} </small><span class="badge badge-{{ post.status }}">{{ post.status }}</span></li>
{% endfor %} 
</ul>


## Ideas

* Space-time plots for digital preservation as communications. 

* [IDCC15 Call For Papers](http://www.dcc.ac.uk/events/idcc15/call-papers)
    * Due 13th October 2014.
    * 10 pages (Research or Practice Papers) or one-page abstract (5 min presentation) Data Papers.
    * Themes:
        * A decade of data curation -- Papers should reflect on the developments that have taken place in the area of digital curation over the past ten years, and the implications these have for the future; reflections and synthesis of what has happened are welcome but all should aim to draw on this to identify future and current perspectives and action:
            * Whatever happened to...?
            * What were the lasting trends and passing phases?
            * What lessons have we learned?
            * What are the major advances that have been made?
            * What are the next big challenges we need to tackle?
        * Curation Infrastructure -- Papers should describe institutional, consortia, national or international infrastructure supporting digital curation and research data management:
            * Tools, systems and services that are in development
            * Evaluations of existing tools
            * Proposals for new approaches to large-scale service delivery
            * Cutting edge research and exploration into new curation methods
        * Working with challenging data -- Papers should discuss work with particularly challenging or specialist forms of data
            * Data on a large scale big data or large collections of long tail data
            * Complex data, models and formats
            * Disciplinary data
    * Ideas:
        * Lessons Learned From Ten Years Of Digital Preservation
            * Essentially the DP Myths papers, but reframing as lessons learned as an attempt to gain more traction. Also includes "Whatever happend to Significant Properties". Challenges around representing minorities (mobile phone economics etc.), mid-value niches (Pages), not obsolescence itself...
        * Format Identification In The Long Tail
            * Comparing DROID and Tika, but moreover, using various correlates to explore understand the likely formats in the long-tail of application/octet-stream.
            * Involves coding up the extractions.
        * Obsolescence in the Web Archive
            * Studying examples of obsolescence,leading to User-Driven Digital Preservation.
            * Also include element trend analysis and script things?
            * Involves researching formats and developing actions.
        * Mining Meaning
            * (as below)

* [Web Archives as scholarly Sources: Issues, Practices and Perspectives -- Call For Papers](http://resaw.eu/events/international-conference-aarhus-june-2015/)
    * Due 8th December 2014.
    * 1,500 words (short) or 2,500 words (long).
    * Themes:
        * research methods for studying the archived web
        * the evolution of language on the web
        * the history(ies) of the web
        * the changing structure of the web
    * Ideas:
        * Mining Meaning 
            * Making sense of 2 billion fragments of UK web history. Issues of interpretation and context etc.


### Longwrites

* Practice
    * Ref from Bitwiser: Good practice and Quirks Mode
    * OAIS is clumsy, arbitrary boundary, not user centered.
* Experiments
    * Bitwiser II: ignored v redundant via MC.
* Fundamentals
    * Simplification pressure? e.g. Markdown or even Wikipedia? REST over SOAP. HTML over PDF? Others?

### Sources

* Sources: W3ACT, Monitrix, The crawl, OpenWayback?
* Pull in requirements and issues, AIT stuff.
* Pull in Monitrix, BDT, IMAQA, WAT Mining.
* [anjackson.net book](http://anjackson.net/book/export/html/1836)
* [xcltools HEAD](http://sourceforge.net/p/xcltools/code/HEAD/tree/)
* [Capturing Properties](http://wiki.opf-labs.org/display/SP/Capturing+Properties)
* [INTRANET: Capturing Properties](https://intranet.bl.uk:8443/confluence/display/DT/Representation+Information+Capture+Project)





