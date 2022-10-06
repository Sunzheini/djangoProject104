from django.shortcuts import render

from djangoProject104.web.models import Employees


def index(request):
    employees = Employees.objects.all()
    employees2 = Employees.objects.filter(age=23).\
        order_by('last_name', 'first_name')

    context = {
        'employees': employees,
        'employees2': employees2,
    }

    return render(request, 'index.html', context)


