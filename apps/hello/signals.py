from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import django

from models import Signal


def save_info(ob_type, ob_id, ob_action):
    sm = Signal(
        object_type=ob_type,
        object_id=ob_id,
        action=ob_action
    )
    sm.save()


def models_list():
    apps_dir = 'apps'
    models = []
    for model in django.db.models.get_models():
        if str(model.__module__).find(apps_dir) == 0:
            models.append(model)
    return models


@receiver(post_save)
def save_handler(sender, **kwargs):
    if sender == Signal or sender not in models_list():
        return

    action = 'create' if kwargs.get('created', False) else 'update'
    ob_id = kwargs.get('instance').id
    save_info(sender.__name__, ob_id, action)


@receiver(pre_delete)
def delete_handler(sender, **kwargs):
    if sender == Signal or sender not in models_list():
        return

    action = 'delete'
    ob_id = kwargs.get('instance').id
    save_info(sender.__name__, ob_id, action)
