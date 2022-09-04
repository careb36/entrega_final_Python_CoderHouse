
from django.urls import path
from users.views import login_request, register, View_profile, Update_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
path('login/',login_request,name='login'),
path('register/',register,name='register'),
path('logout/', LogoutView.as_view(template_name='users/logout.html'),name='logout'),
#path('new-profile/',create_profile,name='new-profile'),
path('profile/',View_profile.as_view(),name='view-profile'),
path('profile/<int:pk>/update',Update_profile.as_view(), name='update-profile')
]
