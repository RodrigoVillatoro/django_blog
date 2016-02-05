from django.conf.urls import url

from .views import PostList, post_detail


urlpatterns = [
    url(r'^$', PostList.as_view(), {'parent_template': 'base.html'},
        name='blog_post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$',
        post_detail, name='blog_post_detail')
]
