"""Api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path

from apps.api import views


urlpatterns = []

for view in views.__all__:
    if callable(getattr(views, view)):
        urlpatterns.append(path(rf'{view}/', getattr(views, view), name=view))

urlpatterns.append(path('cities/', views.city_list))
urlpatterns.append(path('cities/<int:city_id>/', views.city_detail))
urlpatterns.append(path('users/', views.user_list))
urlpatterns.append(path('users/<int:user_id>/', views.user_detail))
