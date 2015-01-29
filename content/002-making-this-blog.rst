================
Making this blog
================

:date: 2015-01-26 09:00
:tags: pelican, jinja, skeleton
:category: Web Dev
:slug: making-this-blog
:authors: Matthew Power
:summary: How I built this blog.

There are loads of really good tools for generating static sites, but I went with `Pelican <http://docs.getpelican.com/>`_. It's written in Python, uses Jinja for templating, and allows composing articles in both reStructuredText and Markdown.

The quickstart guide is great, and had me with a working site in short order. I didn't much like the default theme Pelican ships with, but that isn't a problem, as there is lots of `inspiration <http://pelicanthemes.com/>`_  available. I wanted something simple and readable, that I could easily add my own customisations on top of, so I forked Jody Frankowski's `blue-penguin <https://github.com/jody-frankowski/blue-penguin>`_. It also comes with the popular Solarized colour scheme for Pygments, which lends some nicely styled code highlighting that matches the colour scheme of the site.

I wanted to change the fonts in the theme, so looked on `Google Fonts <https://www.google.com/fonts>`_ for some fonts with free and open licences. I found Crimson and Raleway. For the font nerds, Crimson is very similar to Minion, and Raleway I chose for being a sans font that stands out a little more than most, and also being the default in Skeleton.

`Skeleton <http://getskeleton.com/>`_ is a barebones responsive CSS framework that I wanted to integrate into the theme to make it display better on mobile devices. I picked Skeleton because I wanted to try it and I felt I didn't need all the features of something more fully featured such as either Bootstrap or Foundation.
