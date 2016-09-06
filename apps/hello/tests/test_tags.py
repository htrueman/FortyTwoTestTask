
from django.template import Template, Context, TemplateSyntaxError
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

from apps.hello.models import MyData


class TagEditLink(TestCase):
    def test_tag_with_existing_obj(self):
        """ test tag with existing object """
        person = MyData.objects.first()
        out = Template(
            "{% load admin_link %}"
            "{% edit_link information %}"
        ).render(Context({'information': person}))
        self.assertIn('/admin/hello/mydata/1/', out)

    def test_tag_with_not_valid_obj(self):
        """ test tag with not valid object """
        with self.assertRaises(TemplateSyntaxError):
            Template("{% load admin_link %}"
                     "{% edit_link information %}").render(
                Context({'information': 1})
            )

    def test_link_on_template(self):
        """ test what link contains on the main page """
        self.client = Client()
        response = self.client.get(reverse('contacts'))
        self.assertIn('Admin', response.content)
