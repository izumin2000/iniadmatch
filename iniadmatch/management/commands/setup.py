from django.core.management.base import BaseCommand
from social_django.models import UserSocialAuth

class Command(BaseCommand) :
    def handle(self, *args, **options) :
        UserSocialAuth.objects.all().delete()