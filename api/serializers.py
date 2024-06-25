from rest_framework import serializers
from .models import Employee, Position, BenefitLevel, Benefit, EmployeeBenefit

class BenefitLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitLevel
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    benefit_level = BenefitLevelSerializer()

    class Meta:
        model = Position
        fields = '__all__'

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeBenefitSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    benefit = BenefitSerializer()

    class Meta:
        model = EmployeeBenefit
        fields = '__all__'
