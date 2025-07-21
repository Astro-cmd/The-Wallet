
from django.contrib import admin
from django.urls import path, include

def homepage(request):
    from django.http import HttpResponse
    return HttpResponse("Welcome  The Wallet API!")

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/budget/', include('budgets.urls')),
    
]
