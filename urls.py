from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pizza'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('features', views.features, name='features'),
    path('order', views.order, name='order'),
    path('order/<int:pk>', views.edit_order, name='edit_order'),
    path('contact', views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()
