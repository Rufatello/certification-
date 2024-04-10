from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            is_active=True,
            is_staff=True,
            is_superuser=True,
            email='1@mail.ru',
            country='Россия',
            city='Череповец',
            street='Победы',
            house_number='10'
        )
        user.set_password('12345')
        user.save()