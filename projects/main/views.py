from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import reverse

from .models import Project


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
