from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpRequest

from .models import Vacancy

@permission_required('employmentapp.view_vacancy')
def vacancy_list(request: HttpRequest):
    # if not request.user.has_perm('employmentapp.view_vacancy'): # <app>.<action>_<object_name>
    #     raise PermissionDenied()
    vacancies = Vacancy.objects.all()
    context = {
        'vacancy_list': vacancies
    }
    return render(request, 'employmentapp/vacancy-list.html', context=context)



