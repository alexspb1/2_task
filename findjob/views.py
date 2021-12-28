from django.db.models import Count, Avg
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from django.views.generic import ListView

from findjob.models import Vacancy, Company, Specialty


def main_view(request):
    companies_list = Company.objects.annotate(count=Count('vacancies'))
    specialties_list = Specialty.objects.annotate(count=Count('vacancies'))
    context = {
        'companies_list' : companies_list,
        'specialties_list' : specialties_list,
    }
    return render(request, 'findjob/index.html', context=context)

# class Main_view(ListView):
#     model = Vacancy
#     template_name = 'findjob/index.html'
#     context_object_name = 'list_of_vacancy'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
#
#     def get_queryset(self):
#         return Tours.objects.filter(departure__exact='Novgorod')




def all_vacancies(request):
    vacancies_list = Vacancy.objects.values('id','title','skills','description','salary_min','salary_max','specialty','company')
    vacancy_title = 'Все вакансии'
    context = {
        'vacancies_list' : vacancies_list,
        'vacancy_title' : vacancy_title,
    }
    return render(request, 'findjob/vacancies.html', context=context)

def all_vacancies_special(request, specialty_input:str):
    specialties_list = Specialty.objects.get(code=specialty_input)
    vacancies_list = specialties_list.vacancies.values('id','title','skills','description','salary_min','salary_max','specialty','company')
    vacancy_title = specialties_list.title
    context = {
        'vacancies_list': vacancies_list,
        'vacancy_title': vacancy_title,
        'specialties_list' : specialties_list,
    }
    return render(request, 'findjob/vacancies.html', context=context)

def company_cart(request, company_id: int):
    companies_list = Company.objects.get(id=company_id)
    vacancies_list = companies_list.vacancies.values('id','title', 'skills', 'description', 'salary_min', 'salary_max',
                                                       'specialty', 'company')
    context = {
        'companies_list' : companies_list,
        'vacancies_list' : vacancies_list,
    }
    return render(request, 'findjob/company.html', context=context)

def vacancy_cart(request, vacancy_id: int):
    vacancies_list = Vacancy.objects.values('id','title', 'skills', 'description', 'salary_min', 'salary_max', 'specialty', 'company').get(id=vacancy_id)
    companies_list = Company.objects.get(vacancies__id=vacancy_id)
    context = {
        'vacancies_list' : vacancies_list,
        'companies_list' : companies_list,
    }
    return render(request, 'findjob/vacancy.html', context=context)
