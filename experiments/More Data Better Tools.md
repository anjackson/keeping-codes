---
title: Using Web Archives To Improve Preservation Tools
layout: default
categories: [experiments]
tags: [stub]
publish: true
---

We use Web Archive data to drive tool development.

So, according to our experiments, there are at least two thousand distinct formats in our historical web archive, and at least three thousand if you distinguish between all formats (e.g. HTML) and their specific versions and character sets (e.g. UTF-8). It’s worth pointing out that we don’t really know exactly how precise our identification tools are, and also that a small proportion remains unidentified. Therefore, we don’t yet know exactly how many formats there are. However, the contents of the archives are dominated by HTML, web image formats, PDF, Office documents and so on, and in the ‘tail’ of the distribution, thousands of formats accounts for a very small fraction of the content (not sure exactly, certainly less than 1%). Nevertheless, just because a format is rare, we cannot necessarily assume it is of little value, and I wonder if that is where the real preservation challenge for web archives lies. The ‘big’ formats look after themselves, and require little effort to preserve over moderate timescales. But in the tail of the format distribution, formats are less likely to survive without our intervention, and so we need to be able to work out where to invest our efforts.

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


Mining for Signatures
---------------------
Starting with unidentified formats: http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22, we can script a series of queries for different extensions that attempt to build plausible signatures for each, based on the FFB. 

application/octet-stream: 146,541
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


Parse Error Analysis
====================

http://192.168.1.206:8990/solr/#/jisc/schema-browser?field=parse_error


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

 
