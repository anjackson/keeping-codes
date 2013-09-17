---
title:  Fundamentals
layout: default
---

<ul>
{% for page in site.pages %}
{% if page.publish == true %}
{% for pc in page.categories %}
{% if pc == 'case-studies' %}
<li><a href="{{ site.baseurl }}{{ page.url }}">{{ page.title }}</a></li>
{% endif %}   <!-- cat-match-p -->
{% endfor %}  <!-- page-category -->
{% endif %}   <!-- publish-p -->
{% endfor %} <!-- page -->
</ul>
