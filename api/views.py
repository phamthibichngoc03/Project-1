from rest_framework import generics
from .models import Employee, Position, BenefitLevel, Benefit, EmployeeBenefit
from .serializers import EmployeeSerializer, PositionSerializer, BenefitLevelSerializer, BenefitSerializer, EmployeeBenefitSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PositionListCreateView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class BenefitLevelListCreateView(generics.ListCreateAPIView):
    queryset = BenefitLevel.objects.all()
    serializer_class = BenefitLevelSerializer

class BenefitLevelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BenefitLevel.objects.all()
    serializer_class = BenefitLevelSerializer

class BenefitListCreateView(generics.ListCreateAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

class BenefitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

class EmployeeBenefitListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeBenefit.objects.all()
    serializer_class = EmployeeBenefitSerializer

class EmployeeBenefitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeBenefit.objects.all()
    serializer_class = EmployeeBenefitSerializer
