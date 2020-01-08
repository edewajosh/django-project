from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    path('list_two/', views.product_list_two, name='product_list_two'),
    path('performance', views.test_comparison, name='test_comparison'),
    path('cheap/<price>/', views.cheap_products, name='cheap_products'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
