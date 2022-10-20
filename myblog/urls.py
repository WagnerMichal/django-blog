from django.urls import path
from . import views
from . import views_tag
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_article, name='create_article'),
    path('create_tag', views_tag.create_tag, name='create_tag'),
    path('articles/<id>', views.article_details, name='article'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('articles/<id>/add_tag', views_tag.add_tag, name='tag_article'),
    path('edit/<id>', views.edit_article, name='edit'),
    path('tags', views_tag.tags, name='tag'),
    path('articles/<id>/update', views.update_article, name='update_article')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
