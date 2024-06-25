from django.urls import path
from .views import EmployeeListCreateView, EmployeeDetailView, PositionListCreateView, PositionDetailView, BenefitLevelListCreateView, BenefitLevelDetailView, BenefitListCreateView, BenefitDetailView, EmployeeBenefitListCreateView, EmployeeBenefitDetailView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('positions/', PositionListCreateView.as_view(), name='position-list-create'),
    path('positions/<int:pk>/', PositionDetailView.as_view(), name='position-detail'),
    path('benefit-levels/', BenefitLevelListCreateView.as_view(), name='benefit-level-list-create'),
    path('benefit-levels/<int:pk>/', BenefitLevelDetailView.as_view(), name='benefit-level-detail'),
    path('benefits/', BenefitListCreateView.as_view(), name='benefit-list-create'),
    path('benefits/<int:pk>/', BenefitDetailView.as_view(), name='benefit-detail'),
    path('employee-benefits/', EmployeeBenefitListCreateView.as_view(), name='employee-benefit-list-create'),
    path('employee-benefits/<int:pk>/', EmployeeBenefitDetailView.as_view(), name='employee-benefit-detail'),
]
