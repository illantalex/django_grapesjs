from django_grapesjs.settings import GRAPESJS_DEFAULT_HTML
from django.db import models
from django_grapesjs.models import GrapesJsHtmlField


class ExampleModel(models.Model):
    html = GrapesJsHtmlField(apply_django_tag=False, default_html="test.html")
