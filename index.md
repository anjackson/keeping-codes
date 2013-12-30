---
title:  Keeping Codes
layout: default
---

> "Digital Preservation is access... in the future."
>
> <small>David Brunton (via [Ed Summers](https://twitter.com/edsu)' [The Web as a Preservation Medium](http://inkdroid.org/journal/2013/11/26/the-web-as-a-preservation-medium/))</small>

Introduction
------------

This is a collection of notes on digital preservation, defined the broadest sense: anything that enables or ensures re-use of digital resources. The aim is to collect my unpublished notes and 'war stories' from various digital preservation projects and get them online, even though they may be rough drafts, and then develop them in the open. The hope is that anyone who is interested in this kind of work can find it earlier and more easily.

However, this also means the site will be something of a mish-mash of content at varying stages of completion. Hopefully, any confusion can be minimized by tagging the content appropriately (e.g. <span class="badge badge-stub">stub</span>, <span class="badge badge-outline">outline</span>, <span class="badge badge-draft">draft</span>, <span class="badge badge-complete">complete</span>). If all goes well, later on, it should be possible to start tying individual entries into longer, more coherent threads. Having said that, I doubt anything here will ever be tagged as <span class="badge badge-final">final</span>.

If you have any questions or comments, you are more than welcome to contact me via [this form][1], or use [the appropriate GitHub issue tracker][2].

{% for cat in site.category-list %}
{{ cat | capitalize }}
---------
{% include pageList.html cat=cat %}
{% endfor %}  <!-- cat -->


License
-------

<span style="float:right; padding: 0.1em 0.5em;">
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB"><img alt="Creative Commons Licence" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a>
</span>
<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Keeping Codes</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://anjackson.github.io/keeping-codes/" property="cc:attributionName" rel="cc:attributionURL">Andrew N. Jackson</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.

[1]: http://anjackson.net/contact
[2]: https://github.com/anjackson/keeping-codes/issues

