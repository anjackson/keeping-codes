---
title:  Site Map
layout: default
---

<ul>
  {% for page in site.pages %}
    <li>
      <a href="{{ page.url }}">{{ page.title }}</a>
    </li>
  {% endfor %}
</ul>

{% for cat in site.category-list %}
{{ cat | capitalize }}
---------
<ul>
{% for page in site.pages %}
{% for pc in page.categories %}
{% if pc == cat %}
<li><a href="{{ page.url }}">{{ page.title }}</a></li>
{% endif %}   <!-- cat-match-p -->
{% endfor %}  <!-- page-category -->
{% endfor %} <!-- page -->
</ul>
{% endfor %}  <!-- cat -->
