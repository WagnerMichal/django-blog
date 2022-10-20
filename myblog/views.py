from django.shortcuts import redirect, render
from .models import Article, Tag
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.core.files import File


@login_required
def adminpage(request):
    return render(request, 'adminpage.html', {"tags": Tag.objects.all()})


@require_http_methods(["GET"])
def home(request):
    if request.GET.get("tag_id"):
        tag = Tag.objects.get(pk=request.GET.get("tag_id"))
        context = {
            "articles": tag.article_set.order_by('-published'),
            "tag": tag
        }
    else:

        context = {
            "articles": Article.objects.order_by('-published')[:3],
        }
    return render(request, 'home.html', context)


@require_http_methods(["GET"])
def article_details(request, id):
    tags = Tag.objects.all()
    article = Article.objects.get(pk=id)

    context = {
        "tag_choices": tags,
        "article": article
    }
    return render(request, 'article.html', context)


@require_http_methods(["POST"])
def create_article(request):
    title = request.POST.get("title")
    content = request.POST.get("content")

    if request.FILES.get('upload'):
        upload = File(request.FILES['upload'])
        Article.objects.create(
            title=title,
            content=content,
            image=upload
        )
    else:
        Article.objects.create(
            title=title,
            content=content,
            )
    return redirect('adminpage')


@require_http_methods(["POST"])
def update_article(request, id):
    title = request.POST.get("title")
    content = request.POST.get("content")

    Article.objects.filter(pk=id).update(
        title=title,
        content=content,
    )
    return redirect('article', id)


@require_http_methods(["GET"])
def edit_article(request, id):
    return render(request, "edit.html", {
        "article": Article.objects.get(pk=id)
        })
