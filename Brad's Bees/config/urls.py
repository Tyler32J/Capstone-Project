"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),

#|=================|#
#|--- USER SIDE ---|#
#|=================|#

    path('', app.views.index, name="index"),
    path('home/', app.views.home, name="home"),
    path('removal/', app.views.bee_removal, name="removal"),
    path('shop/', app.views.shop, name="shop"),
    path('education/', app.views.education, name="education"),
    path('gallery/', app.views.gallery, name="gallery"),

#|==================|#
#|--- ADMIN SIDE ---|#
#|==================|#

    path('admin_home/', app.views.admin, name="admin")

]
