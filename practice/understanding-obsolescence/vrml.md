---
title: VRML
subtitle: .wrl
layout: default
category: Formats
status: stub
publish: true
---

Found in NLA, enquote?
VRML (logical superset option, identification gap, version issues)

 * [x-world/x-vrml](mimeExamples/nistlogo.wrl), Virtual reality modeling, e.g. Alteros 3D

TODO Also implement VRML support, combining migration (vrml to x3d, meshlabserver or XSLT based) and emulation (or rather x3d to html+JavaScript)
http://cic.nist.gov/vrml/nistlogo_x3dom.html
Also 
http://www.webarchive.org.uk/aadda-discovery/formats?sort_by=solr_document&sort_order=DESC&f%5B0%5D=content_type_ext%3A%22.wrl%22 > 8000 WRL VRML 1 or 2/97

Cleaner to just use the FFB:
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_ffb%3A%222356524d%22

ID tools need to cover 1.0 versus 2.0. And then Interject needs to cope with 1.0 and all I can find is a Windows binary.

A list here, mostly dead:
http://www.web3d.org/pipermail/x3d-public_web3d.org/2012-February/001923.html

This dodgy thing seems to be the only option: http://www.interocitors.com/polyhedra/vr1tovr2/index.html

Other resources:

http://www.subdude-site.com/WebPages_Local/RefInfo/Computer/Linux/LinuxGuidesByBlaze/apps3Dtools/3D_viewers-converters/3D_vrml1_and_vrml2_notes.htm

This seems to be a good converter (Windows only AFAICT)
http://merlin.fit.vutbr.cz/wiki/index.php?title=Open_Inventor_Tools

VRML Plugin and Browser Detector
http://cic.nist.gov/vrml/vbdetect.html

http://www.cortona3d.com/cortona3dviewer

EXCELLENT:
http://castle-engine.sourceforge.net/view3dscene.php#section_converting


http://www.xj3d.org/tutorials/basic_applet.html


http://www.web3d.org/wiki/index.php/Player_support_for_X3D_components

http://www.subdude-site.com/WebPages_Local/RefInfo/Computer/Linux/LinuxGuidesByBlaze/apps3Dtools/3D_viewers-converters/3D_vrml1_and_vrml2_notes.htm

DROID distinguishes 1/97 (fmt/93 and fmt/94), but does not identify x3d.
Tika only knows VRML extension (not even that?!), but can be taught all.

VRML via JavaScript:
http://threejs.org/examples/webgl_loader_vrml.html
https://github.com/mrdoob/three.js/blob/2d59713328c421c3edfc3feda1b116af13140b94/examples/js/loaders/VRMLLoader.js#L61


VRML1 to VRML97

* http://www.cs.princeton.edu/~min/meshconv/

VRML97 to X3D

* http://www.x3dom.org/?page_id=532 etc. /Applications/Instant\ Player.app/Contents/MacOS/aopt --help
    * /Applications/Instant\ Player.app/Contents/MacOS/aopt -i penguin4.wrl -x penguin5-aopt.x3d
    * Works but proprietary and no commercial use allowed.
* meshlabserver.exe -i <wrl file> -o <x3d file> (no colour, just the mesh, it seems)
* Blender, c.f. http://auxmem.com/2012/01/24/convert-3ds-files-to-obj-with-blender/ script created and works.
* http://ovrt.nist.gov/v2_x3d.html seems to work and is simpler to integrate.

X3D to HTML

* X3DOM looks like a fairly simple wrap. http://www.x3dom.org/
* See http://x3dom.org/x3dom/example/blenderExport/horse-inline.html for an example of pulling in the X3D via URL

X3D to PNG

* http://castle-engine.sourceforge.net/view3dscene.php#section_screenshot
    * view3dscene my_model.wrl --screenshot 0 output.png
* http://www.niallmoody.com/heilan/
* http://libx3d.sourceforge.net/ 

Blender can't load VRML1, view3dscence can't convert, apparently (at least from CLI?)

Uh-oh, VRML can haz hyperlinks, of course, so https://twitter.com/archivetype/status/429004845102944256

So, maybe tweak so they are subtypes of text/plain and allow the text to be indexed?
Nah, it's only c. 10,000 so pull them out and look for links via WWWAnchor/Anchor.

- http://www.sv.vt.edu/classes/vrml/NCSA_VRML_Tutorial/examples/ThreeSpheresURL.wrl.txt
- http://graphcomp.com/info/specs/sgi/vrml/spec/part1/nodesRef.html#Anchor

