# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('precios.api_precios.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
