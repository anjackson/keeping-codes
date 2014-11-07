---
title: Bit Flipping
layout: default
category: On Tools
status: stub
publish: false
---

It should be possible to make a JavaScript page that downloads a JPG, like:

* http://stackoverflow.com/questions/20035615/using-raw-image-data-from-ajax-request-for-data-uri
* https://github.com/jseidelin/exif-js/blob/master/example/index.html

Then modify the bits, and pass them through this:

* https://github.com/notmasteryet/jpgjs/blob/master/jpg.js

And render to a Canvas. This would allow a simple UI where the consequences of bit-flipping a JPG can be explored:

* mouse-over an image that represents a JPG bitstream.
* Flip the bit and run it through jpg.js.
* Show the results
* Colour the pixel based on the outcome (black if no change, red if change etc.)
* Could also add JPG metadata extraction, and add another colour for that.
    * https://github.com/jseidelin/exif-js

