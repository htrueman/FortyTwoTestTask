
from django.template import Template, Context, TemplateSyntaxError
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

from apps.hello.models import MyData


class TagEditLink(TestCase):
    def test_tag_with_existing_obj(self):
        """ Test tag with existing object """
        person = MyData.objects.first()
        out = Template(
            "{% load link_to_admin %}"
            "{% edit_link information %}"
        ).render(Context({'information': person}))
        self.assertIn('/admin/hello/aboutme/1/', out)

    def test_tag_with_not_valid_obj(self):
        """ Test tag with not valid object """
        with self.assertRaises(TemplateSyntaxError):
            Template("{% load link_to_admin %}"
                     "{% edit_link information %}").render(
                Context({'information': 1})
            )