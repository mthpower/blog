Title: Making this blog
Date: 2015-01-26 09:00
Tags: pelican, jinja, skeleton
Category: Web Dev
Slug: making-this-blog
Authors: Matthew Power
Summary: How I built this blog.

There are loads of really good tools for generating static sites, but I went with [Pelican](http://docs.getpelican.com/). It's written in Python, uses Jinja for templating, and allows composing articles in both reStructuredText and Markdown.

The quickstart guide is great, and had me with a working site in short order. I didn't much like the default theme that Pelican ships with, but that wasn't a problem, as there is lots of [inspiration](http://pelicanthemes.com/)  available. I wanted something simple and readable, that I could easily add my own customisations on top of, so I forked Jody Frankowski's [blue-penguin](https://github.com/jody-frankowski/blue-penguin). It also comes with the popular Solarized colour scheme for Pygments, which lends some nicely styled code highlighting that matches the colour scheme of the site.

I wanted to change the fonts in the theme, so looked on [Google Fonts](https://www.google.com/fonts) for some fonts with free and open licences. I found Crimson and Raleway. For the font nerds, Crimson is very similar to Minion, and Raleway I chose for being a sans font that stands out a little more than most.
