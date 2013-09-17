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
