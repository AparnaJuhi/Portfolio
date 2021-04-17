from django.contrib import admin
from django.urls import path,include
admin.site.site_header = "Aparna Portfolio Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to Aparna Portfolio Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
