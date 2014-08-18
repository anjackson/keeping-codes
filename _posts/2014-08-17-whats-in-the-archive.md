---
title: What's in the archive?
layout: default
categories: ["Web Archives"]
tags: [complete]
publish: true
---

How much of the HTML is our archives is valid HTML? This question came up on the IIPC Members mailing list recently, and despite it's apparently simplicity, this turns to be a rather difficult question to answer. 

Firstly, what do you mean by valid? Certainly, the [W3C][3] works to create appropriate [web standards][4], and provides [tools to assist validation][5] according to those standards. But the web browser software that you are using has its own opinion as to what HTML can be. For example, during [the browser wars][6], competing software products invented individual features in order to gain market share, and ignoring any of the available standards. Even now, although the relationship between the browsers is much more amicable, they still maintain their own ['living standard'][7] that is similar to, but distinct from, the W3C HTML specification. Even aside from the issue of which format to validate against, there is the further complication that browsers have always attempted to resolve errors and problems with malformed documents (a.k.a. [tag soup][8]), and do their best to present the content anyway.

Consequently, anecdotally at least, we know that [much of the HTML on the web is perfectly acceptable despite being invalid][10], and so it is not quite clear what formal validation would achieve. Furthermore, the validation process itself is quite a computationally intensive procedure, and few web archives have the resources to carry our validation at scale. Based on this understanding of the costs and the benefits, we do not routinely run validation processes over our web archives.

However, we do process our archives in order to index the text from the resources.  Clearly, we have to perform different processes to extract the text from HTML versus, say, PDF or office documents. Therefore, have to identify the format of each one in order to determine how to get at the text. 

In fact, to help us understand our content, we run two different identification tools, [Apache Tika][1] and [DROID][2]. The former identifies for general format, and is a necessary part of the text extraction processes, whereas the latter attempts to perform a more fine-grained identification. For example, it is capable of distinguishing between the different versions of HTML.

Ideally, one would hope that each of these tools would agree on which documents are HTML, and DROID would provide a little additional information concerning the versions of the formats in use. However, it turns our that DROID takes a somewhat stricter view of what HTML should look like, whereas Tika is a little more forgiving of HTML content that strays further away from standard usage. Another way to look at this is to say that DROID attempts to partially validate the first part of a HTML page, and so those documents that Tika identifies as HMTL, but DROID does not, forms a reasonable estimate of the lower-bound of the percentage of invalid HTML in the collection.

Based on two thirds of our 1996-2010 collection (1.7 billion out of about 2.5 billion resources hosted from *.uk), I've determined the DROID 'misses' as a percentage of the Tika 'hits' for HTML, year by year, here:

[Insert image here]

From there one case see that pre-2000, around more than ten percent of the archived HTML *so* malformed that it's difficult to *even identify it as HTML*. For 1995, the percentage rises to 95%, with only 5% of the HTML being identified as such by DROID. Post-2000 the fraction has dropped significantly and as of 2010 appears to be around 1%.

Although the utility of validation is not yet certain, we will still consider adding HTML validation to future iterations of [our indexing toolkit][9]. We may only pass a smaller random-sample of the HTML through that costly process, as this would still allow us to understand how much content has the clarity of formal validation, and also tells a story about how important the W3C (and the standards it promotes) are to the UK web. Perhaps it will tell us something interesting about standard adoption and format dynamics over time.

[1]: http://tika.apache.org/
[2]: http://www.nationalarchives.gov.uk/information-management/manage-information/preserving-digital-records/droid/
[3]: http://www.w3.org/
[4]: http://www.w3.org/standards/
[5]: http://validator.w3.org/
[6]: http://en.wikipedia.org/wiki/Browser_wars#The_first_browser_war
[7]: http://whatwg.org/html
[8]: http://en.wikipedia.org/wiki/Tag_soup
[9]: https://github.com/ukwa/webarchive-discovery/issues/33
[10]: http://blog.codinghorror.com/its-a-malformed-world/
