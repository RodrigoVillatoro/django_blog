from django.conf.urls import url

from .views import PostCreate, PostDelete, PostList, PostUpdate, post_detail


urlpatterns = [
    url(r'^$', PostList.as_view(), {'parent_template': 'base.html'},
        name='blog_post_list'),
    url(r'^create/$', PostCreate.as_view(),
        name='blog_post_create'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/delete/$',
        PostDelete.as_view(), name='blog_post_delete'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/update/$',
        PostUpdate.as_view(), name='blog_post_update'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$',
        post_detail, name='blog_post_detail'),
]
