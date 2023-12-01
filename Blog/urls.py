
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),
    path('maqolalar/', maqolalar),
    path('sign/', sign),
    path('logout/', log_out),
    path('malumot/<int:id>', malumot)
]
