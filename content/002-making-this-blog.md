Title: Making this blog
Date: 2015-01-26 09:00
Tags: pelican, jinja, skeleton
Category: Web Dev
Slug: making-this-blog
Authors: Matthew Power
Summary: How I built this blog.

There are loads of really good tools for generating static sites, but I went with [Pelican](http://docs.getpelican.com/). It's written in Python, uses Jinja for templating, and allows composing articles in both reStructuredText and Markdown.

The quickstart guide is great, and had me with a working site in short order. I didn't much like the default theme that Pelican ships with, but that wasn't a problem, as there is lots of [inspiration](http://pelicanthemes.com/)  available. I wanted something simple and readable, that I could easily add my own customisations on top of, so I forked Jody Frankowski's [blue-penguin](https://github.com/jody-frankowski/blue-penguin). It also comes with the popular Solarized colour scheme for Pygments, which lends some nicely styled code highlighting that matches the colour scheme of the site.

I wanted to change the fonts in the theme, so looked on [Google Fonts](https://www.google.com/fonts) for some fonts with free and open licences. I found Crimson and Raleway. For the font nerds, Crimson is very similar to Minion, and Raleway is the base font in [Skeleton](). I wanted to make the blog look better on smaller devices, and so decided to pull a CSS Grid into the framework. Skeleton is ~400 lines long, which means it's dead easy to see what it's doing, and makes a great base to work off for a small site with very few elements like this, where any of the more popular grids would have been overengineering for the problem.

I think grids can be a double-edged sword. Inless you are very diligent in how you structure your markup, it's easy to add unneccesary `<divs>` and classes. They add a lot of utility but can work against you if you are trying to make the markup semantic. Ideally, I should me able to swap out the CSS, and the markup would not need touching.

Pelican requires some work after you generate the blog to make pretty URLS. To avoid all my URLs looking like ending with `.html`, I needed to change all the `_URL` and _`SAVE_AS` settings in my `pelicanconf.py`:

```python
# Pretty URLs
ARTICLE_URL = 'article/{slug}'
ARTICLE_SAVE_AS = 'article/{slug}.html'
PAGE_URL = 'page/{slug}'
PAGE_SAVE_AS = 'page/{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'
```
You can look at the source for both the blog and the theme on my Github.
