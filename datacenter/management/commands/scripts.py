from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import *
from django.core.management.base import BaseCommand

def find_schoolkid(full_name: str):
    """Поиск ученика в базе данных по ФИО.

    Args:
        full_name (str): ФИО ученика

    Returns:
        Schoolkid: Найденная запись ученика
    """
    try:
        return Schoolkid.objects.get(full_name__contains=full_name)
    except ObjectDoesNotExist:
        print('Ученик не найден.')
    except MultipleObjectsReturned:
        print('Найдено слишком много учеников.')


def fix_marks(schoolkid):
    for mark in Mark.objects.filter(schoolkid=schoolkid, points__lte=3):
        mark.points = 5
        mark.save()


def del_chastisements(schoolkid):
    for chastisement in Chastisement.objects.filter(schoolkid=schoolkid):
        chastisement.delete()


def create_commendation(full_name, subject_title):
    schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    # schoolkid = Schoolkid.objects.filter(full_name__contains='Фролов Иван')
    # lesson = Lesson.objects.filter(subject__title=subject_title, year_of_study=6, group_letter='А').order_by('-date').first()

    print('schoolkid123')


class Command(BaseCommand):
    """Start the bot."""

    help = 'Hack DB'

    def handle(self, *args, **options):
        # create_commendation('Фролов Иван', 'Музыка')
        print(find_schoolkid('Фролов Иван'))
