from django.contrib import admin
from django.urls import path
from cruisechronicle import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('brand/', views.brand, name='brand'),
    path('contact/', views.contact, name='contact'),
    path('brandkoenigsigg/', views.brandkoenigsig, name='brandkoenigsigg')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

