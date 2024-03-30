from django.contrib import admin
from .models import Expense
from .models import employee
from .models import Budget
from .models import Sales
from .models import slides, register
# Register your models here.

admin.site.register(Expense)
admin.site.register(employee)
admin.site.register(Budget)
admin.site.register(slides)
admin.site.register(register)
admin.site.register(Sales)
