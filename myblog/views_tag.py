from django.shortcuts import redirect, render, get_object_or_404
from .models import Article, Tag
from django.views.decorators.http import require_http_methods
from django.db.utils import IntegrityError


@require_http_methods(["POST"])
def add_tag(request, id):
    article = get_object_or_404(Article, pk=id)
    tag = get_object_or_404(Tag, pk=request.POST.get('tags'))
    article.tags.add(tag)
    return redirect('article', article.id)


@require_http_methods(["POST"])
def create_tag(request):
    tag = request.POST.get("tag")
    try:
        Tag.objects.create(
            name=tag,
        )
    except IntegrityError:
        raise Exception("Tag already exists")
    return redirect('adminpage')


@require_http_methods(["GET"])
def tags(request):
    return render(request, 'tags.html', {"tags": Tag.objects.all()})
