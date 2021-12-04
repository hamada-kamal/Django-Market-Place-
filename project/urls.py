
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('contact-us/', include('contact.urls', namespace='contactus')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
