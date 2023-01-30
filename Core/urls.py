"""Core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


# from tasks.views import get_status, home, run_task


admin.site.site_header = 'Super Admin Panel'
admin.site.site_title = 'Super Admin Title'
admin.site.site_index = 'Super Admin Index'


urlpatterns = [
    # integrates admin routes

    path("admin/", admin.site.urls),
#    path("orders/", include("orders.urls")),
#    path('summernote/', include('django_summernote.urls')),

    # /UI/
    path(r'', include('UI.urls')),

    # Registration
    path('', include('Registration.urls')),

    # Celery
#    path("cel/", include("cel.urls")),
#    path("tasks/<task_id>/", get_status, name="get_status"),
#    path("tasks/", run_task, name="run_task"),
#    path("celery/", home, name="home"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)