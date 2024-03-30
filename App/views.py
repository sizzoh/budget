from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import  login_required
from django.db.models import Q, Sum
from django.contrib import messages
import json
from .models import Expense
from .models import employee
from .models import Budget
from .models import Sales
from .models import slides
from .forms import customForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def home2(request):
    return render(request, 'home1.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already registered')
            return redirect('register')
        elif  User.objects.filter(email=email).exists():
                messages.info(request, ' email already taken')
                return redirect('register')
        elif  password != password_confirmation:
                    messages.info(request, ' password do not match')
                    return redirect('register')
        elif len(password) < 8:
            messages.info(request, 'password must contain at least 8 characters')  
            return redirect('register')      
        else:
            user = User.objects.create(username=username, email=email, password=password)
            user.save() 
            return redirect('login')       
    return render(request, 'register.html')


def login(request):
    login_user = User.objects.all()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username== "" or password==" ":
            messages.info(request, 'Please enter a username and password to login')
            return redirect('login')
            
        else:
            if len(password) < 8:
                messages.info(request, 'password must contain at least 8 characters')
                return redirect('login') 
            else:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('home')
                else:
                    messages.info(request, 'invalid credentials')
                       
        '''       
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
        '''        
    return render(request, 'login.html', {'user': login_user})

def logout(request):
    auth.logout(request)
    return redirect('login')


def recover(request):
    if request.method=='POST':
        username_new = request.POST.get('username')
        password_new = request.POST.get('password')
        user = User.objects.filter(username=username_new)
        for i in user:
         if i.username==username_new:
            i.username = username_new
            i.password= password_new
            i.save()
            messages.info(request, "User password changed successfully")
            break
        else:
            messages.info(request, 'username not found')    
                
    return render(request, 'recover.html')

def  expenses(request):
    if request.method == 'POST':
        day= request.POST.get('day')
        date = request.POST['date']
        category = request.POST['category']
        quantity = request.POST['quantity']
        amount = request.POST['ex_amount']
        description = request.POST['description']
        image=request.POST['image']
        '''
        status = ['completed', 'failed','pending', 'success','aborted', 'no expenses yet']
        budget = Budget.objects.all()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'Friday', 'Saturday','sunday']
        #execute amount calculation based on days
        monday_amount = budget.filter(day__iexact=days[0]).aggregate(Sum('amount'))['amount__sum']
        tuesday_amount = budget.filter(day__iexact=days[1]).aggregate(Sum('amount'))['amount__sum']
        wednesday_amount = budget.filter(day__iexact=days[2]).aggregate(Sum('amount'))['amount__sum']
        thursday_amount = budget.filter(day__iexact=days[3]).aggregate(Sum('amount'))['amount__sum']
        friday_amount = budget.filter(day__iexact=days[4]).aggregate(Sum('amount'))['amount__sum']
        saturday_amount = budget.filter(day__iexact=days[5]).aggregate(Sum('amount'))['amount__sum']
        sunday_amount = budget.filter(day__iexact=days[6]).aggregate(Sum('amount'))['amount__sum'] 
        
        if monday_amount < float(amount) and day == days[0] and budget[0]==date:
            messages.info(request, 'Expense amount exceeded the available budget  for %s' % day)
            return redirect('expenses')
        elif tuesday_amount < amount and day == days[1]:
            messages.info(request, 'Expense amount exceeded the available budget  for %s' % day)
            return redirect('expenses')
        elif wednesday_amount < amount and day==days[2]:
            messages.info(request, 'Expense amount exceeded the available budget  for %s' % day)
            return redirect('expenses')
        elif thursday_amount < amount and day==days[3]:
            messages.info(request, 'Expense amount exceeded the available budget  for %s' % day)
            return redirect('expenses')   
        elif friday_amount < amount and day==days[4]:
            messages.info(request, 'Expense amount exceeded the available budget  for %s' % day)
            return redirect('expenses')
        elif saturday_amount < amount and day==days[5]:
            messages.info(request, 'Expense amount exceeded the available budget  for %s' % day)
            return redirect('expenses')  
        elif sunday_amount < amount and day == days[6]:
            messages.info(request, 'Expense amount exceeded the available budget  for %s' % day)
            return redirect('expenses') 
        else:
            '''
        ex= Expense(day=day, date=date, category=category, quantity=quantity, amount=amount, description=description, image=image)
        ex.save()
    return render(request, 'expenses.html')


def budget(request):
    if request.method == 'POST':
        date = request.POST['date']
        day= request.POST['day']
        category = request.POST['category']
        quantity = request.POST['quantity']
        amount = request.POST['amount']
        description = request.POST['description']
        
        save = Budget(date=date,day=day, category=category, quantity=quantity, amount=amount, description=description)
        save.save()
                    
    return render(request, 'budget.html')


def sales(request):
    if request.method == 'POST':
        sale_name = request.POST['name']
        sale_day = request.POST['day']
        sale_date = request.POST['date']
        sale_quantity = request.POST['quantity']
        sale_category = request.POST['category']
        sale_amount = request.POST['amount']
        pay_method = request.POST['pay_method']
        sale_description = request.POST['description']
        image = request.POST['image']
        
        sale = Sales(name= sale_name, day=sale_day,date = sale_date, amount= sale_amount, pay_method=pay_method, description=sale_description, image=image, quantity=sale_quantity,category=sale_category)
        sale.save()
    return render(request, 'sales.html')
    
def employees(request):
    context = []
    if request.method == 'GET':
         data = employee.objects.all()
         
         return render(request, 'employees.html', {'data': data})
     


def budgetList(request):
    if 'day_category' in request.GET:
        DAY_CATEGORY = request.GET['day_category']
        items = Budget.objects.filter(Q(day__icontains=DAY_CATEGORY)|Q(category__icontains=DAY_CATEGORY))
    else:
        items = Budget.objects.all()
    context = {'item': items}
        
    return render(request, 'home.html', context)


def expenseList(request):
    if 'day_category' in request.GET:
        DAY_CATEGORY = request.GET['day_category']
        items = Expense.objects.filter(Q(day__icontains=DAY_CATEGORY)|Q(category__icontains=DAY_CATEGORY))
    else:
        items = Expense.objects.all()
    context = {'items': items}
        
    return render(request, 'home1.html', context)

def salesList(request):
    if 'day_category' in request.GET:
        DAY_CATEGORY = request.GET['day_category']
        items = Sales.objects.filter(Q(day__icontains=DAY_CATEGORY)|Q(category__icontains=DAY_CATEGORY))
    else:
        items = Sales.objects.all()
    context = {'sales': items}
        
    return render(request, 'sales_Views.html', context)


class budgetAction:
    def delete(request, pk):
        Budget.objects.get(id=pk).delete()
        return redirect('budgetList')
        
    def update(request, pk):
        new_budget = Budget.objects.get(id=pk)
        if request.method == 'POST': 
             new_day= request.POST.get('day')
             new_date = request.POST['date']
             new_category = request.POST['category']
             new_quantity = request.POST['quantity']
             new_amount = request.POST['ex_amount']
             new_description = request.POST['description']
             new_image=request.POST['image']
             
             new_budget.day = new_day
             new_budget.date = new_date
             new_budget.category = new_category
             new_budget.quantity = new_quantity
             new_budget.amount = new_amount
             new_budget.description = new_description
            
             new_budget.save()
             if new_budget.date != new_date:
                 messages.info(request, 'budget updated successfully')
                 return redirect('budgetList')
             else:
                 messages.info(request, 'some thing went wrong')
                 return redirect('update')
        
        return render(request, 'budget_update.html', {'budget': new_budget})     
        
class expenseAction:
    def delete_expense(request, pk):
        Expense.objects.get(id=pk).delete()
        return redirect('expenseList')
        
    def update_expense(request, pk):
        new_expense = Expense.objects.get(id=pk)
        if request.method == 'POST':
             new_day= request.POST.get('day')
             new_date = request.POST['date']
             new_category = request.POST['category']
             new_quantity = request.POST['quantity']
             new_amount = request.POST['ex_amount']
             new_description = request.POST['description']
             new_image=request.POST['image']
             
             new_expense.day = new_day
             new_expense.date = new_date
             new_expense.category = new_category
             new_expense.quantity = new_quantity
             new_expense.amount = new_amount
             new_expense.description = new_description
             new_expense.image = new_image
             new_expense.save()
        return render(request, 'expense_update.html', {'expense': new_expense} ) 

class salesAction:
    def delete_sales(request, pk):
        Sales.objects.get(id=pk).delete()
        return redirect('salesList')
    
    def update_sales(request, pk):
        sale_selected = Sales.objects.get(id=pk)
        if request.method== 'GET':
            sale_name = request.POST.get('name')
            sale_day = request.POST.get('day')
            sale_date = request.POST.get('date')
            sale_quantity = request.POST.get('quantity')
            sale_category = request.POST.get('category')
            sale_amount = request.POST.get('amount')
            sale_description = request.POST.get('description')
            image = request.POST.get('image')
            
            sale_selected.name = sale_name
            sale_selected.day = sale_day
            sale_selected.date = sale_date
            sale_selected.quantity = sale_quantity
            sale_selected.category = sale_category
            sale_selected.amount = sale_amount
            sale_selected.description = sale_description
            sale_selected.image = image
            
            if sale_selected.name == sale_name:
                sale_selected.save()
                messages.info(request, "Sale updated successfully")
            else:
                messages.info(request, "something went wrong try again")    
               
        return render(request, 'sales_update.html', {'sales': sale_selected})    
                    
            

class count:
    def budgetAccounts(request):
        context1=[]
        budget = Budget.objects.all()
        budget_all= budget.count()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'Friday', 'Saturday','sunday'] 
        if request.method=='GET':
            monday_budget_count= budget.filter(day__iexact=days[0]).count()
            tuesday_budget_count= budget.filter(day__iexact=days[1]).count()
            wednesday_budget_count= budget.filter(day__iexact=days[2]).count()
            thursday_budget_count= budget.filter(day__iexact=days[3]).count()
            friday_budget_count= budget.filter(day__iexact=days[4]).count()
            saturday_budget_count= budget.filter(day__iexact=days[5]).count()
            sunday_budget_count= budget.filter(day__iexact=days[6]).count()
            
            list1 =[
               monday_budget_count,
               tuesday_budget_count,
               wednesday_budget_count,
               thursday_budget_count,
               friday_budget_count,
               saturday_budget_count,
               sunday_budget_count
                
            ]
            #execute amount calculation based on days
            monday_amount = budget.filter(day__iexact=days[0]).aggregate(Sum('amount'))['amount__sum']
            tuesday_amount = budget.filter(day__iexact=days[1]).aggregate(Sum('amount'))['amount__sum']
            wednesday_amount = budget.filter(day__iexact=days[2]).aggregate(Sum('amount'))['amount__sum']
            thursday_amount = budget.filter(day__iexact=days[3]).aggregate(Sum('amount'))['amount__sum']
            friday_amount = budget.filter(day__iexact=days[4]).aggregate(Sum('amount'))['amount__sum']
            saturday_amount = budget.filter(day__iexact=days[5]).aggregate(Sum('amount'))['amount__sum']
            sunday_amount = budget.filter(day__iexact=days[6]).aggregate(Sum('amount'))['amount__sum'] 
            
            list2= [
               monday_amount,
               tuesday_amount,
               wednesday_amount,
               thursday_amount,
               friday_amount,
               saturday_amount,
               sunday_amount 
            ] 
            
            context1.extend(list1)
            context1.extend(list2)
            
        context ={
            "data1": context1,
            "data2":budget_all
        } 
        json.dumps(context)
        return JsonResponse(context)
    
    #----------------------------------------------------------------
    #expense function
    
    def expenseAccounts(request):
        context1=[]
        expense = Expense.objects.all()
        budget = Budget.objects.all()
        expense_all= expense.count()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'Friday', 'Saturday','sunday']
        #you may use or_conditions a Q object
        
        day_match_budget=  Budget.objects.filter(Q(day__icontains=days[0])|Q(day__icontains=days[1])|Q(day__icontains=days[2])|Q(day__icontains=days[3])|Q(day__icontains=days[4])|Q(day__icontains=days[5])|Q(day__icontains=days[6]))
        day_match_expense= Expense.objects.filter(Q(day__icontains=days[0])|Q(day__icontains=days[1])|Q(day__icontains=days[2])|Q(day__icontains=days[3])|Q(day__icontains=days[4])|Q(day__icontains=days[5])|Q(day__icontains=days[6]))
        if request.method=='GET':
            monday_expense_count= expense.filter(day__iexact=days[0]).count()
            tuesday_expense_count= expense.filter(day__iexact=days[1]).count()
            wednesday_expense_count= expense.filter(day__iexact=days[2]).count()
            thursday_expense_count= expense.filter(day__iexact=days[3]).count()
            friday_expense_count= expense.filter(day__iexact=days[4]).count()
            saturday_expense_count= expense.filter(day__iexact=days[5]).count()
            sunday_expense_count= expense.filter(day__iexact=days[6]).count()
            
            list1 =[
               monday_expense_count,
               tuesday_expense_count,
               wednesday_expense_count,
               thursday_expense_count,
               friday_expense_count,
               saturday_expense_count,
               sunday_expense_count
                
            ]
            #execute amount calculation based on days
            monday_amount = expense.filter(day__iexact=days[0]).aggregate(Sum('amount'))['amount__sum']
            tuesday_amount = expense.filter(day__iexact=days[1]).aggregate(Sum('amount'))['amount__sum']
            wednesday_amount = expense.filter(day__iexact=days[2]).aggregate(Sum('amount'))['amount__sum']
            thursday_amount = expense.filter(day__iexact=days[3]).aggregate(Sum('amount'))['amount__sum']
            friday_amount = expense.filter(day__iexact=days[4]).aggregate(Sum('amount'))['amount__sum']
            saturday_amount = expense.filter(day__iexact=days[5]).aggregate(Sum('amount'))['amount__sum']
            sunday_amount = expense.filter(day__iexact=days[6]).aggregate(Sum('amount'))['amount__sum'] 
            
            list2= [
               monday_amount,
               tuesday_amount,
               wednesday_amount,
               thursday_amount,
               friday_amount,
               saturday_amount,
               sunday_amount 
            ] 
            
            #get days for setting budget and expense  status
            day_budget = budget.values()
            day_expense=expense.values()
                
            
            context1.extend(list1)
            context1.extend(list2)
            budget_day=day_match_budget
            expense_day=day_match_expense
        contextDay=[{
            "budget_day": budget_day,
            "expense_day":expense_day
        } for day_budget in budget_day for day_expense in expense_day]  
        #print(contextDay) 
        #import query values into  list
        Days_for_budget = []
        Days_for_expense=[]
        Days_for_budget.extend(budget_day)
        Days_for_expense.extend(day_expense)      
        
        #create queryset value context
        Days_context={
            "Days_for_budget":Days_for_budget,
            "Days_for_expense":Days_for_expense
        }
        context ={
            "ex_data": context1,
            "ex_data3": expense_all,
            
        }
        
        json.dumps(context)
        #json.dumps(Days_for_expense)
        #json.dumps(Days_for_budget)
        return JsonResponse(context)
    
#sales_details
    def salesAccounts(request):
        context1=[]
        sales = Sales.objects.all()
        sales_all= sales.count()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'Friday', 'Saturday','sunday'] 
        if request.method=='GET':
            monday_sales_count= sales.filter(day__iexact=days[0]).count()
            tuesday_sales_count= sales.filter(day__iexact=days[1]).count()
            wednesday_sales_count= sales.filter(day__iexact=days[2]).count()
            thursday_sales_count= sales.filter(day__iexact=days[3]).count()
            friday_sales_count= sales.filter(day__iexact=days[4]).count()
            saturday_sales_count= sales.filter(day__iexact=days[5]).count()
            sunday_sales_count= sales.filter(day__iexact=days[6]).count()
            
            list1 =[
               monday_sales_count,
               tuesday_sales_count,
               wednesday_sales_count,
               thursday_sales_count,
               friday_sales_count,
               saturday_sales_count,
               sunday_sales_count
                
            ]
            #execute amount calculation based on days
            monday_amount = sales.filter(day__iexact=days[0]).aggregate(Sum('amount'))['amount__sum']
            tuesday_amount = sales.filter(day__iexact=days[1]).aggregate(Sum('amount'))['amount__sum']
            wednesday_amount = sales.filter(day__iexact=days[2]).aggregate(Sum('amount'))['amount__sum']
            thursday_amount = sales.filter(day__iexact=days[3]).aggregate(Sum('amount'))['amount__sum']
            friday_amount = sales.filter(day__iexact=days[4]).aggregate(Sum('amount'))['amount__sum']
            saturday_amount = sales.filter(day__iexact=days[5]).aggregate(Sum('amount'))['amount__sum']
            sunday_amount = sales.filter(day__iexact=days[6]).aggregate(Sum('amount'))['amount__sum'] 
            
            list2= [
               monday_amount,
               tuesday_amount,
               wednesday_amount,
               thursday_amount,
               friday_amount,
               saturday_amount,
               sunday_amount 
            ] 
            
            context1.extend(list1)
            context1.extend(list2)
            
        context ={
            "sales": context1,
            "sale":sales_all
        } 
        json.dumps(context)
        return JsonResponse(context)    
       
def salesPage(request):
    return render(request, 'sales_Views.html')


             
class counts:
    def budgetCount(request):
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'Friday', 'Saturday','sunday'] 
        if request:
            monday_budgets= Budget.objects.filter(day__iexact=days[0])
            amount_sum= monday_budgets.aggregate(sum('amount'))['amount__sum'] or 0
            print(amount_sum)
            
            


                           
                           
class sort:
    def sortBudget(request):
        context = []
        if request.method == 'GET':
            sort_by = request.GET.get('sort-by','alphabetically')
            order = request.GET.get('order','ascending')
            
            if sort_by == 'alphabetically':
                if order == 'ascending':
                    ascending = Budget.objects.all().order_by('day')
                    context.append(ascending)
                    
                else:
                    descending = Budget.objects.all().order_by('day')
                    context.append(descending)
        return render(request, 'home1.html', {'item': context})
    
    def sortExpense(request):
        context=[]
        if request.method == 'GET':
            sort_by = request.GET.get('sort-by','alphabetically')
            order = request.GET.get('order','ascending')
            
            if sort_by == 'alphabetically':
                if order == 'ascending':
                    ascending = Expense.objects.all().order_by('name')
                    context.append(ascending)
                    
                else:
                    descending = Expense.objects.all().order_by('name')
                    context.append(descending)
                   
        return render(request, 'home1.html', {'item': context})


class countHover:
    def budget(request):
        if request.method == 'GET':
            data = Budget.objects.all()
            
        return HttpResponse({'count': data})   
    
    
def CarouselSlides(request):
    slide = slides.objects.all()  
    return render(request, 'index.html', {'slides': slide})  


class more:
    def Budget_moreInfo(request, pk):
        day_budget = Budget.objects.filter(day=pk)
        
        return render(request, 'day_budget.html', {'day': day_budget})
    
    def Expense_moreInfo(request, pk):
        day_expense = Expense.objects.filter(day=pk)
        
        return render(request, 'day_expense.html', {'day': day_expense})
    
    def sales_moreInfo(request, pk):
        day_sales= Sales.objects.filter(day=pk)
        return render(request, 'day_sales.html', {'day': day_sales})
        
        
    
class report:  
    def getSalesReport(request): 
        sales_list=[]
        sales = Sales.objects.all()
        sales_all = sales.count()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'Friday', 'Saturday','sunday']
        if request.method == 'GET': 
            monday_sales_count= sales.filter(day__iexact=days[0]).count()
            tuesday_sales_count= sales.filter(day__iexact=days[1]).count()
            wednesday_sales_count= sales.filter(day__iexact=days[2]).count()
            thursday_sales_count= sales.filter(day__iexact=days[3]).count()
            friday_sales_count= sales.filter(day__iexact=days[4]).count()
            saturday_sales_count= sales.filter(day__iexact=days[5]).count()
            sunday_sales_count= sales.filter(day__iexact=days[6]).count()
            
            #get amount for each day
            monday_amount = sales.filter(day__iexact=days[0]).aggregate(Sum('amount'))['amount__sum']
            tuesday_amount = sales.filter(day__iexact=days[1]).aggregate(Sum('amount'))['amount__sum']
            wednesday_amount = sales.filter(day__iexact=days[2]).aggregate(Sum('amount'))['amount__sum']
            thursday_amount = sales.filter(day__iexact=days[3]).aggregate(Sum('amount'))['amount__sum']
            friday_amount = sales.filter(day__iexact=days[4]).aggregate(Sum('amount'))['amount__sum']
            saturday_amount = sales.filter(day__iexact=days[5]).aggregate(Sum('amount'))['amount__sum']
            sunday_amount = sales.filter(day__iexact=days[6]).aggregate(Sum('amount'))['amount__sum'] 
            
            total = monday_amount+ tuesday_amount+wednesday_amount+thursday_amount+friday_amount+saturday_amount+sunday_amount
            sales_count = [
            monday_sales_count,
            tuesday_sales_count,
            wednesday_sales_count,
            thursday_sales_count,
            friday_sales_count,
            saturday_sales_count,
            sunday_sales_count
            ]        
            
            sales_amount=[
            monday_amount,
            tuesday_amount,
            wednesday_amount,
            thursday_amount,
            friday_amount,
            saturday_amount,
            sunday_amount
            ]
            
            sales_list.extend(sales_count)
            sales_list.extend(sales_amount)
            sales_list.append(total)
        sales_context ={
          'sales_report':sales_list  
        }
        json.dumps(sales_context)    
        return JsonResponse(sales_context)
    
    def getBudgetReport(request):
        budget_list=[]
        budget = Budget.objects.all()
        budget_all= budget.count()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'Friday', 'Saturday','sunday']
        if request.method=='GET':
            monday_budget_count= budget.filter(day__iexact=days[0]).count()
            tuesday_budget_count= budget.filter(day__iexact=days[1]).count()
            wednesday_budget_count= budget.filter(day__iexact=days[2]).count()
            thursday_budget_count= budget.filter(day__iexact=days[3]).count()
            friday_budget_count= budget.filter(day__iexact=days[4]).count()
            saturday_budget_count= budget.filter(day__iexact=days[5]).count()
            sunday_budget_count= budget.filter(day__iexact=days[6]).count()
            
            list1 =[
               monday_budget_count,
               tuesday_budget_count,
               wednesday_budget_count,
               thursday_budget_count,
               friday_budget_count,
               saturday_budget_count,
               sunday_budget_count
                
            ]
            #execute amount calculation based on days
            monday_amount = budget.filter(day__iexact=days[0]).aggregate(Sum('amount'))['amount__sum']
            tuesday_amount = budget.filter(day__iexact=days[1]).aggregate(Sum('amount'))['amount__sum']
            wednesday_amount = budget.filter(day__iexact=days[2]).aggregate(Sum('amount'))['amount__sum']
            thursday_amount = budget.filter(day__iexact=days[3]).aggregate(Sum('amount'))['amount__sum']
            friday_amount = budget.filter(day__iexact=days[4]).aggregate(Sum('amount'))['amount__sum']
            saturday_amount = budget.filter(day__iexact=days[5]).aggregate(Sum('amount'))['amount__sum']
            sunday_amount = budget.filter(day__iexact=days[6]).aggregate(Sum('amount'))['amount__sum'] 
            
            list2= [
               monday_amount,
               tuesday_amount,
               wednesday_amount,
               thursday_amount,
               friday_amount,
               saturday_amount,
               sunday_amount 
            ] 
            total = monday_amount+ tuesday_amount+wednesday_amount+thursday_amount+friday_amount+saturday_amount+sunday_amount
            budget_list.extend(list1)
            budget_list.extend(list2)
            budget_list.append(total)
            
        context ={
            "data1": budget_list,
            "data2": budget_all,
            
        } 
        json.dumps(context)
        print('hello world in budget report')
        return JsonResponse(context)
    
    def getExpenseReport(request):
        expense_list=[]
        expense = Expense.objects.all()
        expense_all= expense.count()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'Friday', 'Saturday','sunday']
        if request.method=='GET':
            monday_expense_count= expense.filter(day__iexact=days[0]).count()
            tuesday_expense_count= expense.filter(day__iexact=days[1]).count()
            wednesday_expense_count= expense.filter(day__iexact=days[2]).count()
            thursday_expense_count= expense.filter(day__iexact=days[3]).count()
            friday_expense_count= expense.filter(day__iexact=days[4]).count()
            saturday_expense_count= expense.filter(day__iexact=days[5]).count()
            sunday_expense_count= expense.filter(day__iexact=days[6]).count()
            
            list1 =[
               monday_expense_count,
               tuesday_expense_count,
               wednesday_expense_count,
               thursday_expense_count,
               friday_expense_count,
               saturday_expense_count,
               sunday_expense_count
                
            ]
            #execute amount calculation based on days
            monday_amount = expense.filter(day__iexact=days[0]).aggregate(Sum('amount'))['amount__sum']
            tuesday_amount = expense.filter(day__iexact=days[1]).aggregate(Sum('amount'))['amount__sum']
            wednesday_amount = expense.filter(day__iexact=days[2]).aggregate(Sum('amount'))['amount__sum']
            thursday_amount = expense.filter(day__iexact=days[3]).aggregate(Sum('amount'))['amount__sum']
            friday_amount = expense.filter(day__iexact=days[4]).aggregate(Sum('amount'))['amount__sum']
            saturday_amount = expense.filter(day__iexact=days[5]).aggregate(Sum('amount'))['amount__sum']
            sunday_amount = expense.filter(day__iexact=days[6]).aggregate(Sum('amount'))['amount__sum'] 
            
            list2= [
               monday_amount,
               tuesday_amount,
               wednesday_amount,
               thursday_amount,
               friday_amount,
               saturday_amount,
               sunday_amount 
            ] 
            
            #get days for setting budget and expense  status
            total = monday_amount+ tuesday_amount+wednesday_amount+thursday_amount+friday_amount+saturday_amount+sunday_amount
            expense_list.extend(list1)
            expense_list.extend(list2)
            expense_list.append(total)

        context ={
            "ex_data": expense_list,
            "ex_data3": expense_all,
        
        }
        
        json.dumps(context)
        print('hello world in expense report')
        
        return JsonResponse(context)
    
    def ReportPage(request):
        sales = Sales.objects.all()
        budget = Budget.objects.all()
        expense = Expense.objects.all()

        all_class_context={
            "sales_report": sales,
            "budgets_report": budget,
            "expenses_report": expense
        }
        return render(request, 'Report.html', all_class_context)        
    

class   QueryToSetStatus:
    def saleStatus(request):
        my_list = []
        new_list=[]
        status = Sales.objects.all().values()
        
        my_list.extend(status)
        
        context ={
            "lists": my_list
        }    
        #print(context)
        return JsonResponse(context)   
    
def images(request):
    return render(request, 'index3.html')

def customerEdit(request, pk):
    item = Customer.objects.get(id=pk)
    form = customForm(instance=item)
    if request.method == "POST":
        form = customForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
    
    context = {
        'form': form
    }
    return render(request, 'employee.html', context)         