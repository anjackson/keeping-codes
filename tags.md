---
title: Tag Index
---

{% capture site_tags %}{% for page in site.pages %}{% if include.unpublished == true or page.publish == true %}{% for pc in page.tags %}{{ pc }}~{% endfor %}{% endif %}{% endfor %}{% endcapture %}
{% assign tags_list_dups = site_tags | split:'~' | sort %}

{% capture site_tags_sorted %}{% for tag in tags_list_dups %}{%if tag != prev %}{{ tag }}{% unless forloop.last %}~{% endunless %}{%assign prev = tag %}{% endif %}{% endfor %}{% endcapture %}
{% assign tags_list = site_tags_sorted | split:'~' | sort %}


<ul class="tag-box inline">
  {% for item in (0..site.tags.size) %}{% unless forloop.last %}
    {% capture this_word %}{{ tags_list[item] | strip_newlines }}{% endcapture %}
    <li><a href="#{{ this_word }}">{{ this_word }} <span>{{ site.tags[this_word].size }}</span></a></li>
  {% endunless %}{% endfor %}
</ul>

<hr/>

{% for item in (0..site.tags.size) %}{% unless forloop.last %}
  {% capture this_word %}{{ tags_list[item] | strip_newlines }}{% endcapture %}
  <h3 id="{{ this_word }}">{{ this_word }}</h3>
  <ul class="post-list">
  {% for page in site.pages %}{% if page.tags contains tags_list[item] %}
    <li><a href="{{ site.url }}{{ page.url }}">{{ page.title }}</a></li>
  {% endif %}{% endfor %}
  </ul>
{% endunless %}{% endfor %}