from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
from rest_framework import generics
from myapp.models import Employee
from myapp.serializers import EmployeeSerializer
# Create your views here.
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee
    serializer_class = EmployeeSerializer   









def Home(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        form=EmployeeForm()
    
    data=Employee.objects.all()

    


    context={
        'form':form,
        'data':data,
    }
    return render(request,'myapp/index.html',context)



# Delete View
def Delete_record(request,id):
    a=Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')
    

# Update View
def Update_Record(request,id):
    if request.method=='POST':
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'myapp/update.html',context)