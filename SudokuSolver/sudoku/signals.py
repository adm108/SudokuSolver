from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from sudoku.models import Sudoku


def unique_slug_generator(instance):
    author_slug = slugify(instance.author.username)
    random_slug = generate_random_string()
    slug = author_slug + "-" + random_slug
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return slug


@receiver(pre_save, sender=Sudoku)
def add_sulg_to_sudoku(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        my_slug = unique_slug_generator(instance)
        instance.slug = my_slug
