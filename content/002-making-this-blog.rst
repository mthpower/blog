================
Making this blog
================

:date: 2015-01-26 09:00
:tags: pelican, jinja
:category: Web Dev
:slug: making-this-blog
:authors: Matthew Power
:summary: How I built this blog.

There are loads of really good tools for generating static sites, but I went with `Pelican <http://docs.getpelican.com/>`_. It's written in Python, uses Jinja for templating, and allows writting articles in both reStructuredText and Markdown.

The quickstart guide is great, and had me with a working site in short order. I didn't much like the default theme Pelican ships with, but that isn't a problem, as there is lots of `inspiration <http://pelicanthemes.com/>`_  available. I wanted something simple and readable, that I could easily add my own customisations on top of, so I forked Jody Frankowski's `blue-penguin <https://github.com/jody-frankowski/blue-penguin>`_.

I wanted to change the fonts in the theme, so looked on `Google Fonts<https://www.google.com/fonts>`_ for some fonts with free and open licences. I found Crimson and Raleway. For the font nerds, Crimson is very similar to Minion, and Raleway I chose for being a sans font that stands out a little more than most.

Skeleton is a barebones responsive CSS framework that I built into the markup to make it display better on mobile devices. I didn't need all the features of something more fully featured such as either Bootstrap or Foundation.

In doing this I've realised for the n-th time how just tricky to maintain CSS is. Sometimes it can be so hard to figure out the original coder's intention, and it's not always obvious why some lines
