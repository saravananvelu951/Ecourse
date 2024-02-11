from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings 

from rest_framework import routers, serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', views.registrationViewSet)
router.register(r'order', views.orderViewSet)


urlpatterns = [
    path('',views.home,name="homepage"),
    path('help',views.help,name="help"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('order',views.order,name="order"),
    path('video',views.video,name="video"),
    path('restapi/', include(router.urls)),

    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
