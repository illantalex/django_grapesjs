from django.template import Template, Context
from django_grapesjs.settings import NAME_RENDER_TAG
from lxml import html
__all__ = ('ApplyRenderTag', )



class ApplyRenderTag(object):
    def apply_tag_init(self, string):
        document = html.fromstring(string)
        for tag in document.xpath(f"//{NAME_RENDER_TAG}"):
            tag.getparent().replace(tag, html.fromstring(Template(html.tostring(tag, encoding="unicode")).render(Context({}))))

        return html.tostring(document, pretty_print=True, encoding="unicode", method="html")


    def apply_tag_save(self, string):
        return string
