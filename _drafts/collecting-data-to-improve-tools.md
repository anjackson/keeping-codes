---
title: Collecting Data To Improve Tools
category: Practice
tags: ["Web Archives"]
status: stub
---

Like many other institutions, we are heavily dependent on a number of open source tools. We couldn't function without them, and so we like to try to find ways to give back to those communities. We don't have a lot of spare time or development capacity to contribute, but we have found another way to provide useful feedback.

At the heart of our discovery stack lies [Apache Tika][1], the piece of software that attempts to parse the myriad of data formats in our collection and extract a textual representation and metadata that we can use to find them again. In this way, we have executed Apache Tika on many billions of distinct resources, dating from 1996 to the present day. This extreme usage often tests Tika to it's limits, as as well as failing to identify many formats, it sometimes simply fails, throwing out an unexpected error, or getting locked in a infinite loop.

Each of those failures represents a loss -- a resource that may never be discovered because we can't understand it. This may be because it's malformed, but it may also be an sign of obsolescence. So instead of ignoring these errors, we decided to remember them. Each is logged, along with the identity of the resource that caused the problem.

We've been collecting this data for a while, but it wasn't clear quite how it will help us tell a broken bitstream from a forgotten format. However, in a [recent discussion with the Apache Tika developers][2], they indicated that they would also find this data useful as a way of improving the coverage and robustness of their software.

This turns out to be a win-win situation. We store the data we were intending to store anyway, but also share it with the tool developers, who get to improve their software in ways we will be able to take direct advantage of as we run later versions of the tool over our archives in the future.
