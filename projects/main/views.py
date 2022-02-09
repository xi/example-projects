from django import forms
from django.core.exceptions import SuspiciousOperation
from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import reverse

from .models import Department
from .models import DataType
from .models import Project


class FilterForm(forms.Form):
    department = forms.ModelChoiceField(
        Department.objects.all(), required=False
    )
    data_type = forms.ModelChoiceField(
        DataType.objects.all(), required=False
    )


class ProjectCreateView(CreateView):
    model = Project
    fields = [
        'title',
        'responsible_researcher',
        'department',
        'data_type',
        'identifier',
    ]

    def get_success_url(self):
        return reverse('list')


class ProjectListView(ListView):
    model = Project
    paginate_by = 20

    def get_filter_form(self):
        form = FilterForm(self.request.GET)
        if not form.is_valid():
            raise SuspiciousOperation
        return form

    def get_queryset(self):
        qs = super().get_queryset()
        form = self.get_filter_form()
        if department := form.cleaned_data.get('department'):
            qs = qs.filter(department=department)
        if data_type := form.cleaned_data.get('data_type'):
            qs = qs.filter(data_type=data_type)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.get_filter_form()
        return context
