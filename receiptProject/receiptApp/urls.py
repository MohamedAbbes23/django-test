from django.urls import path
from .views import LoginView, LogoutView, SignUpView, logout_user, receipt_list, receipt_detail, receipt_create, receipt_edit, receipt_delete

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('list/', receipt_list, name='receipt_list'),
    path('<int:pk>/', receipt_detail, name='receipt_detail'),
    path('new/', receipt_create, name='receipt_create'),
    path('<int:pk>/edit/', receipt_edit, name='receipt_edit'),
    path('<int:pk>/delete/', receipt_delete, name='receipt_delete'),
]
