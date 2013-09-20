---
title: BBC Master Images
layout: default
img-hardware:
  - 12112009139-disks.jpg
  - 15092009064-master.jpg
  - 15092009065-open.jpg
  - 15092009067-kbd.jpg
  - 15092009069-kitdisk.jpg
  - 15092009070-kitdisk.jpg
  - 15092009066-idekit.jpg
img-screens:
  - 07102009091.jpg
  - 07102009092.jpg
  - 07102009093.jpg
  - 07102009095.jpg
  - 07102009096.jpg
  - 12112009136.jpg
  - 12112009137.jpg
  - 12112009138.jpg
  - 12112009142.jpg
  - 12112009143.jpg
  - 12112009144.jpg
  - 12112009145.jpg
  - 12112009146.jpg
  - 12112009147.jpg
  - 12112009148.jpg
  - 13102009106.jpg
  - 13102009107.jpg
  - 13102009108.jpg
  - 13102009109.jpg
  - 13102009110.jpg
  - 13102009111.jpg
  - 15092009068.jpg
---

Hardware
--------
{% for image in page.img-hardware %}
<a href="{{ site.baseurl }}/case-studies/images/bbc-master/{{ image }}" style="float: left;">
  <img src="{{ site.baseurl }}/case-studies/images/bbc-master/{{ image }}" style="width:200px;"/>
</a>
{% endfor %}

<div style="clear: both;">&nbsp;</div>

Screenshots
-----------
{% for image in page.img-screens %}
<a href="{{ site.baseurl }}/case-studies/images/bbc-master/{{ image }}" style="float: left;">
  <img src="{{ site.baseurl }}/case-studies/images/bbc-master/{{ image }}" style="width:200px;"/>
</a>
{% endfor %}


