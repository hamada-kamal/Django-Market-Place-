from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this

app_name = 'accounts'

urlpatterns = [
    
    path('signup',views.signup , name='signup' ),
    path('profile',views.profile , name='profile' ),
    path('account-settings',views.AccountSettings , name='settings' ),
    path('edit',views.editProfile , name='profile_edit' ),
    path('reset_password',auth_views.PasswordResetView.as_view() , name='reset_password' ),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view() , name='reset_password_done' ),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view() , name='reset_password_confirm' ),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view() , name='reset_password_complete' ),



] 