from django import template
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from django.db.models.base import Model

register = template.Library()


@register.simple_tag
def edit_link(person):
    if not isinstance(person, Model):
        raise template.TemplateSyntaxError(
            "{} isn't correct object".format(person)
        )
    content_type = ContentType.objects.get_for_model(person.__class__)
    return urlresolvers.reverse_lazy(
        "admin:%s_%s_change" % (
            content_type.app_label, content_type.model
        ),
        args=(
            person.id,)
    )
