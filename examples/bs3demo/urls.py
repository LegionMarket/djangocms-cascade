# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/select2/', include('django_select2.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
]
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
