import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)  # Пропускаем заголовок
            for line in phone_reader:
                Phone.objects.create(
                    name=line[1],
                    image=line[2],
                    price=int(line[3]),
                    release_date=line[4],
                    lte_exists=bool(line[5])
                )
