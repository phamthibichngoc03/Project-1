from django.db import models

class BenefitLevel(models.Model):
    level = models.CharField(max_length=20, unique=True)
    benefit_description = models.TextField()

    def __str__(self):
        return self.level

class Position(models.Model):
    name = models.CharField(max_length=20, unique=True)
    benefit_level = models.ForeignKey(BenefitLevel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Benefit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Thêm cột cost

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def total_benefit_cost(self):
        total_cost = EmployeeBenefit.objects.filter(employee=self).aggregate(
            total=models.Sum('benefit__cost')
        )['total']
        return total_cost if total_cost is not None else 0


class EmployeeBenefit(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE)
    granted_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.benefit}"
