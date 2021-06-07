# Website for OPTIMADE ontology workshops

A single page for the OMDI2021 workshop.

## Development

To work on this website locally do the following:

```console
$ git clone https://github.com/Materials-Consortia/omdi2021
$ cd omdi2021
$ pip install -r requirements.txt
$ ./make_pages.py
```

Open `build/index.html` to see the page.

## Information

The webpage is built around the CSS and template for the www.optimade.org website.

In the future, this page should be ported over to use Gem and Jekyll instead of rendering the website directly through Jinja2 and the python [`markdown`](https://python-markdown.github.io/) package.
