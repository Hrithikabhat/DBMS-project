from django.contrib import admin
from django.urls import include, path

import store

urlpatterns = [
    path('', include('store.urls')),
    path('admin/',admin.site.urls),
]