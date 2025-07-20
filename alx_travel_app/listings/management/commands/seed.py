from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        titles = ['Seaside Villa', 'Mountain Cabin', 'City Apartment', 'Cozy Studio']
        locations = ['Alexandria', 'Aswan', 'Cairo', 'Gouna']
        
        for _ in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description='A great place to stay!',
                location=random.choice(locations),
                price_per_night=random.randint(50, 300),
                is_available=True
            )
        self.stdout.write(self.style.SUCCESS('✅ Seeded database with sample listings.'))
