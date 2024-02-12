from django.urls import path
from blog import views



app_name = 'blog'


urlpatterns = [
    path("", views.post_list, name='post_list'),
    path("<int:year>/<int:moth>/<int:day>/<slug:post><int:post_id>/", views.post_detail, name='post_detail'),
    path("<int:post_id>/comment/", views.post_comment, name='post_comment')
]
