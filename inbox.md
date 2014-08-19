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


## TODO

* Space-time plots for digital preservation as communications. 

### Ideas for Longwrites

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
* <http://anjackson.net/book/export/html/1836>
* <http://sourceforge.net/p/xcltools/code/HEAD/tree/>
* <http://wiki.opf-labs.org/display/SP/Capturing+Properties>
* <https://intranet.bl.uk:8443/confluence/display/DT/Representation+Information+Capture+Project>





