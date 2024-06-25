from django.contrib import admin
from .models import Employee, Position, BenefitLevel, Benefit, EmployeeBenefit

class EmployeeBenefitInline(admin.TabularInline):
    model = EmployeeBenefit
    extra = 0  # Số lượng dòng trống để thêm mới phúc lợi
    readonly_fields = ('cost',)  # Trường cost là chỉ đọc

    def cost(self, instance):
        return instance.benefit.cost

    cost.short_description = 'Cost'  # Tên hiển thị của trường

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'position', 'total_benefit_cost')
    search_fields = ('first_name', 'last_name', 'email', 'department')
    inlines = [EmployeeBenefitInline]
    # readonly_fields = ('cost',)

    def total_benefit_cost(self, obj):
        return obj.total_benefit_cost
    total_benefit_cost.short_description = 'Total Benefit Cost'

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
admin.site.register(BenefitLevel)
admin.site.register(Benefit)
admin.site.register(EmployeeBenefit)
