from django.contrib import admin
from django.urls import include, path, reverse
from django.shortcuts import redirect



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect(reverse('polls:index'))),
    path('polls/', include('surveys.polls.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
