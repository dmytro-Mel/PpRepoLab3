from django.urls import path
from . import views

urlpatterns = [
    path('user/create/', views.create_user, name='create_user'),
    path('user/<int:user_id>/wallet/create/', views.create_wallet, name='create_wallet'),
    path('user/<int:user_id>/', views.get_user, name='get_user'),
    path('user/<int:user_id>/update/', views.update_user, name='update_user'),
    path('user/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('aggregate_report/', views.aggregate_report, name='aggregate_report'),
]
