from django.urls import path
from .views import index_view, photo_detail, category_view

urlpatterns = [
    path('', index_view, name='index'),
    path('photo/<int:photo_id>', photo_detail, name="detail"),
    path('category/<int:category_id>', category_view, name='category')
]