from django.contrib import admin
from django.urls import path
from blogapp.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name="home"),
    path('post/create/', create_blog, name="blog_create"),
    path('post/<int:id>/', post_detail, name="post_detail"),
    path('update_post/<int:id>/', update_post, name="update_post"),
    path('delete_post/<int:id>/', delete_post, name="delete_post"),
    
    # AUTH
    
    path('signup', signUp, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout', user_logout, name='logout'),
    
    # path('comment/<int:id>/', CommentView, name='comment')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)