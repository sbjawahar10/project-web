"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ind, name="home"),
    path('shop',views.sh, name="shop"),
    path('about',views.ab),
    path('services',views.se, name="services"),
    path('blog',views.bl, name="blog"),
    path('contact',views.co, name="contact"),
    path('login',views.log, name="login"),
    path('reg',views.reg, name="register"),
    path('logout',views.logout),
    path('index',views.adminhome),
    path('user',views.userhome),
    path('display',views.display),
    path('addproduct',views.addpro),
    path('viewproduct',views.displaypro),
    path('deleteproduct/<r>',views.deleteproduct),
    path('updatepro/<int:id>',views.proupdate),
    path('forgot',views.forgot_password,name="forgot"),
    path('reset/<token>',views.reset_password,name='reset_password'),
    path('product',views.user_product),
    path('buy/<int:d>',views.booking),
    path('cart/<int:d>',views.addtocart),
    path('display_cart',views.display_cart,name='display_cart'),
    path('remove_cart/<int:d>', views.remove_cart),
    path('display_cart/increment/<int:d>/', views.increment_quantity, name='increment_quantity'),
    path('display_cart/decrement/<int:d>/', views.decrement_quantity, name='decrement_quantity'),
    path('checkout_cart/<int:total>/<int:qty>',views.checkoutcart),
    path('checkout/<int:d>',views.checkout),
    path('payment_cart/<int:l>',views.payment_cart),
    path('payment_success_cart',views.payment_success_cart),
    path('payment/<int:l>/<int:d>', views.payment),
    path('payment_success', views.paymentsuccess),
    path('user_recent_orders', views.userrecentorders, name='user_recent_orders'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('add_to_wishlist/<int:d>',views.addtowishlist),
    path('delete_wishlist/<int:d>',views.deletewishlist),
    path('admin_user', views.adminuser),
    path('admin_order_update/<int:d>',views.adminorderupdate),


]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)