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
        identifiers = [
            '10.1038/nrn3241',
            'arXiv:1705.10311',
            'MAG:112218234',
            'ACL:W12-3903',
            'PMID:19872477',
            'CorpusID:37220927',
            '',
        ]

        projects = []
        for _ in range(20_000):
            projects.append(Project(
                title=' '.join(fake.words(3)),
                responsible_researcher=fake.name(),
                department=random.choice(departments),
                paper_identifier=random.choice(identifiers),
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
