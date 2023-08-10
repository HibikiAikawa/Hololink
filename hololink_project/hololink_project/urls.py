from django.contrib import admin
from django.urls import path, include
from hololink_app.views import frontpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage),
]