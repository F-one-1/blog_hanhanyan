from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    #  path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    # path('archives/<int:pk>/', views.archiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]