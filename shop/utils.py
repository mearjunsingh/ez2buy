import uuid

from django.template.defaultfilters import slugify


def upload_image_path(instance, filename):
    ext = filename.split(".")[-1]
    name = uuid.uuid4()
    return f"{name}.{ext}"


def generate_unique_slug(klass, word):
    original = slugify(word)
    unique = original
    num = 1
    while klass.objects.filter(slug=unique).exists():
        unique = "%s-%d" % (original, num)
        num += 1
    return unique
