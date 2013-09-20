---
title:  Keeping Codes
layout: default
---

Introduction
------------

This is a collection of notes on digital preservation.

Inclusive definition of digital preservation: Ensuring reuse


{% for cat in site.category-list %}
{{ cat | capitalize }}
---------
<ul>
{% for page in site.pages %}
{% if page.publish == true %}
{% for pc in page.categories %}
{% if pc == cat %}
<li><a href="{{ site.baseurl }}{{ page.url }}">{{ page.title }}</a></li>
{% endif %}   <!-- cat-match-p -->
{% endfor %}  <!-- page-category -->
{% endif %}   <!-- publish-p -->
{% endfor %} <!-- page -->
</ul>
{% endfor %}  <!-- cat -->


License
-------
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_GB"><img alt="Creative Commons Licence" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/80x15.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Keeping Codes</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://anjackson.github.io/dp-notes/" property="cc:attributionName" rel="cc:attributionURL">Andrew N. Jackson</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_GB">Creative Commons Attribution 3.0 Unported License</a>.
