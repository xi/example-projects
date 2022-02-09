import random

from django.core.management.base import BaseCommand
from faker import Faker
from model_bakery import baker

from projects.main.models import Department
from projects.main.models import DataType
from projects.main.models import Project

fake = Faker('de_DE')


class Command(BaseCommand):
    help = 'Populate database with demo data.'

    def handle(self, *args, **options):
        departments = list(Department.objects.all())
        data_types = list(DataType.objects.all())
        projects = []

        for _ in range(20_000):
            projects.append(Project(
                title=' '.join(fake.words(3)),
                responsible_researcher=fake.name(),
                department=random.choice(departments),
            ))
        Project.objects.bulk_create(projects)

        Rel = Project.data_type.through
        rels = []
        for project in Project.objects.filter(data_type=None):
            k = random.randint(1, 3)
            for data_type in random.sample(data_types, k=k):
                rels.append(
                    Rel(project_id=project.id, datatype_id=data_type.id)
                )
        Rel.objects.bulk_create(rels)
