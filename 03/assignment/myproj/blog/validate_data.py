from .models import Tag

def validate_tag():
    tags = Tag.objects.all()
    for tag in tags:
        if len(tag.content) >20:
            tag.content = tag.content.split()[0]
            tag.save()