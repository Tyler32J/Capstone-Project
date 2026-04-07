from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_home_page, name='home'),
    path('services/', views.render_services_page, name="services"),
    path('education/', views.render_educational_page, name="education"),
    path('gallery/', views.render_gallery, name="gallery"),
    path('removal/', views.bee_removal, name="removal"),
]