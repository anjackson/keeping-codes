---
title: What Have We Saved?
category: Practice
tags: ["Web Archives"]
status: stub
publish: false
---

The UK Web Archive started archiving web content towards the end of 2004 ([e.g. The Hutton Enquiry](http://www.webarchive.org.uk/wayback/archive/*/http://www.the-hutton-inquiry.org.uk/index.html)). In the (almost) ten years that have passed since then, can we find a way to look back, and see what we've achieved? Are the URLs we've archived still available on the live web? Or are they long since gone? If those URLs _are_ still working, is the content the same as it was? How as our [archival sliver](http://inkdroid.org/journal/2013/11/26/the-web-as-a-preservation-medium/) of the web changed?

Looking Back
------------

One option would be to go through our archives and exhaustively examine every single URL, and work out what has happened to it.  However, the Open UK Web Archive contains many millions of archived resource, and even just checking their basic status would be very time-consuming, never mind performing any kind of comparison of the content of those pages.

Fortunately, to get a good idea of what has happened, we don't need to visit every single item. Our full-text index categorizes our holdings by, among other things, the year in which the item was crawled. We can therefore use this facet of the search index to randomly sample a number of URLs from each year the archive has been in operation, and use those to build up a picture that compares those holdings to the current web.

URLs by the Thousand
--------------------

Our search system has built in support for randomizing the order of the results, so a simple script that performs a faceted search was all that was needed to build up a list of one thousand URLs for each year. A second script was used to attempt to re-download each of those URLs, and record the outcome of that process. Those results were then aggregated into an overall table showing how many URLs fell into each different class of outcome, over time, as shown below:

![Overall Status Trends]({{ site.baseurl }}/images/halflife/halflife-1000-overall-status.png)

Here, 'GONE' means that not only is the URL missing, but the host that originally served that URL has disappeared from the web. 'ERROR', on the other hand, means that a server still responded to our request, but that our once-valid URL now causes the server to throw an error.

The next class, 'MISSING', ably illustrates the fate of the majority of our archived content - the server is there, and responds, but no longer recognizes that URL. Those early URLs have become [404 Not Found](https://en.wikipedia.org/wiki/HTTP_404) (either directly, or via [redirects](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#3xx_Redirection)). The remaining two classes show URLs that end with a valid [HTTP 200 OK](https://en.wikipedia.org/wiki/HTTP_200) response, either via redirects ('MOVED') or directly ('OK'). 

The horizontal axis shows the results over time, since late 2004, broken down by each quarter (i.e. 2004-4 is the fourth quarter of 2004). The overall trend clearly shows how the items we have archived have disappeared from the web, with individual URLs being forgotten as time passes. This is in contrast to the fairly stable baseline of 'GONE' web hosts.

Is OK okay?
-----------

However, so far, this only tells us what URLs are still active - the content could be completely different! To explore this issue, we have to dig a little deeper by downloading the content and trying to compare what's inside.

This is very hard to do in a way that is both automated and highly accurate, so we have to settle for something simpler. If the content is exactly the same, we can record that the resources are binary identical. If not, we extract whatever text we can from the archived and live URLs, and compute the 'fuzzy hash' of each one. TBA?

https://en.wikipedia.org/wiki/Fingerprint_%28computing%29

[Fuzzy hashing helps researchers spot morphing malware](http://www.techrepublic.com/blog/it-security/fuzzy-hashing-helps-researchers-spot-morphing-malware/)

http://www.forensicswiki.org/wiki/Ssdeep

The hashes can then be compared, and if ssdeep is able to identify any significant overlap in the textual content of the items, we record the result as 'SIMILAR'. Otherwise, we record that the items are 'DISSIMILAR'.

Processing all of the 'MOVED' or 'OR' results in this way leads to this graph:

![Detailed Similarity Trends]({{ site.baseurl }}/images/halflife/halflife-1000-not-really-ok.png)

So, for all those 'OK' or 'MOVED' URLs, the vast majority appear to have changed. Very few are binary identical ('SAME'), and while the rest remain 'SIMILAR' at first, this rapidly drops off over time.

Summarizing Similarity
----------------------

Combining the similarity data with the original graph, we can replace the 'OK' and 'MOVED' parts of the graph with the similarity results in order to see those trends in context.

![Overall Similarity Trends]({{ site.baseurl }}/images/halflife/halflife-1000-detailed-status.png)

Shown in this way, it is clear that very few archived resources are still available, unchanged, on the current web. Or, in other words, very few of our archived URLs are [cool](http://www.w3.org/Provider/Style/URI.html.en).

Local Versus Global Trends
--------------------------

While this analysis helps us understand the trends and value of our open archive, it's not yet clear how much it tells us about other collections, or more global trends. Historically, the UK Web Archive has focused on both high-visibility site and sites known to be at risk, and these selection criteria are likely to affect the overall trends we see. We can partially address this by running the same kind of analysis over our broader, domain-scale collections. However, that would still bias things towards the UK, and it would be interesting to understand how these trends might differ across countries, and globally.




