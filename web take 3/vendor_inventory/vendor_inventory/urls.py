# vendor_inventory/urls.py
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from vendors import views as vendor_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vendor_views.index, name='index'),
    path('vendors/', vendor_views.vendor_list, name='vendor_list'),
    path('vendors/<int:vendor_id>/', vendor_views.vendor_detail, name='vendor_detail'),
    path('register/', vendor_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='vendors/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_vendor/', vendor_views.add_vendor, name='add_vendor'),
    path('add_product/', vendor_views.add_product, name='add_product'),
    path('view_products/', vendor_views.view_products, name='view_products'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
