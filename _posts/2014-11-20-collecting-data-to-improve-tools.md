---
title: Collecting Data To Improve Tools
category: Practice
tags: ["Web Archives"]
status: stub
---

Like many other institutions, we are heavily dependent on a number of open source tools. We couldn't function without them, and so we like to find ways to give back to those communities. We don't have a lot of spare time or development capacity to contribute, but recently we have found another way to provide useful feedback.

### Large-scale extraction ###

At the heart of our [discovery stack][1] lies [Apache Tika][2], the piece of software we use to try to parse the myriad of data formats in our collection in order to extract the textual representation (along with any useful metadata) that goes into our search indexes. Consequently, we have now executed Apache Tika on many billions of distinct resources, dating from 1995 to the present day. Due to the age and variablity of the content, this often tests Tika to it's limits. As well as failing to identify many formats, it sometimes simply fails, throwing out an unexpected error, or by getting locked in a infinite loop.

### Logging losses ###

Each of those failures represents a loss -- a resource that may never be discovered because we can't understand it. This may be because it's malformed, perhaps even damaged during download. It may also be an sign of obsolescence, in that it may indicate the presence of data formats that are poorly understood, and are therefore likely to present a challenge to our discovery and access systems. So, instead of ignoring these errors, we decided to remember them. Specifically, each is logged as a facet of our full-text index, alongside the identity of the resource that caused the problem.

### Sharing the results ###

We've been collecting this data for a while, in order to help us tell a broken bitstream from a forgotten format. However, in a [recent discussion with the Apache Tika developers][3], they have indicated that they would also find this data useful as a way of improving the coverage and robustness of their software.

This turns out to be a win-win situation. We store the data we were intending to store anyway, but also share it with the tool developers, who get to improve their software in ways we will be able to take direct advantage of as we run later versions of the tool over our archives in the future. 

And it feels good to give a little something back.

[1]: https://github.com/ukwa/webarchive-discovery
[2]: http://tika.apache.org/
[3]: https://issues.apache.org/jira/browse/TIKA-1302
