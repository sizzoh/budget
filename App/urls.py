from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('home2', views.home2, name='home2'),
    path('register', views.register, name='register'),
    path('recover', views.recover, name='recover'),
    path('expenses', views.expenses, name='expenses'),
    path('employees', views.employees, name='employees'),
    path('budget', views.budget, name='budget'),
    path('sales', views.sales, name='sales'),
    path('salesPage', views.salesPage, name='salesPage'),
    path('budgetList', views.budgetList, name='budgetList'),
    path('expenseList', views.expenseList, name='expenseList'),
    path('salesList', views.salesList, name='salesList'),
    path('delete<int:pk>', views.budgetAction.delete, name='delete'),
    path('update<int:pk>', views.budgetAction.update, name='update'),
    path('delete_expense<int:pk>', views.expenseAction.delete_expense, name='delete_expense'),
    path('update_expense<int:pk>', views.expenseAction.update_expense, name='update_expense'),
    path('delete_sales<int:pk>', views.salesAction.delete_sales, name= 'delete_sales'),
    path('update_sales<int:pk>', views.salesAction.update_sales, name= 'update_sales'),
    path('sortBudget', views.sort.sortBudget, name='sortBudget'),
    path('sortExpense', views.sort.sortExpense, name='sortExpense'),
    path('budgetCount', views.counts.budgetCount, name='budgetCount'),
    path('budgetAccounts', views.count.budgetAccounts, name='budgetAccounts'),
    path('expenseAccounts', views.count.expenseAccounts, name='expenseAccounts'),
    path('salesAccounts', views.count.salesAccounts, name='salesAccounts'),
    path('CarouselSlides',views.CarouselSlides, name='CarouselSlides'),
    path('Budget_moreInfo<str:pk>', views.more.Budget_moreInfo, name='Budget_moreInfo'),
    path('Expense_moreInfo<str:pk>', views.more.Expense_moreInfo, name='Expense_moreInfo'),
    path('sales_moreInfo<str:pk>', views.more.sales_moreInfo, name='sales_moreInfo'),
    path('getSalesReport', views.report.getSalesReport, name='getSalesReport'),
    path('getBudgetReport', views.report.getBudgetReport, name='getBudgetReport'),
    path('getExpenseReport', views.report.getExpenseReport, name='getExpenseReport'),
    path('ReportPage', views.report.ReportPage, name='ReportPage'),
    path('saleStatus', views.QueryToSetStatus.saleStatus, name= 'saleStatus'),
    path('images', views.images, name='images'),
]
