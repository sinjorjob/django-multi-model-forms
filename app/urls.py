from django.urls import path
from .views import EmployeeListView, EmployeeDetailView, EmployeeDetailUpdateView, EmployeeDetailUpdateView2


urlpatterns = [
    path('list/', EmployeeListView.as_view(), name='list'),
    path('detail/<int:pk>/', EmployeeDetailView.as_view(), name="detail"),
    path('employee/edit/<int:pk>/', EmployeeDetailUpdateView.as_view(), name='update'),
    path('employee/multi_edit/<int:pk>/', EmployeeDetailUpdateView2.as_view(), name='multi_update'),
]
