# import re
# from functools import reduce
from django.template import Template, Context
from django_grapesjs.settings import NAME_RENDER_TAG
from lxml import html
# NAME_RENDER_TAG = "render"
__all__ = ('ApplyRenderTag', )


REGEX_RENDER_TAG = '<%s>(.*?)</%s>' % (NAME_RENDER_TAG, NAME_RENDER_TAG)
print(REGEX_RENDER_TAG)

class ApplyRenderTag(object):
    def apply_tag_init(self, string):
        document = html.fromstring(string)
        # print(NAME_RENDER_TAG)
        for tag in document.xpath(f"//{NAME_RENDER_TAG}"):
            # tag.replace(tag, html.fromstring(Template(html.tostring(tag, encoding="unicode")).render(Context({}))))

            tag.getparent().append(html.fromstring(Template(html.tostring(tag, encoding="unicode")).render(Context({}))))
            # tag.tail = "<render><h1>Hello</h1></render>"

            # print(tag.tail)
        # etree.strip_elements(document, NAME_RENDER_TAG, with_tail=False)
        # print(html.tostring(document, pretty_print=True).decode("utf-8"))

        return html.tostring(document, pretty_print=True, encoding="unicode", method="html")


    def apply_tag_save(self, string):
        return string

# data = """<document>
# <h1>
# Heading
# </h1>
# <render>
# <p>p1</p>
# <p>p2</p>
# </render>
# </document>
# """
