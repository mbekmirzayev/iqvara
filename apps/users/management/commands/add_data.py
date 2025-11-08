# apps/management/commands/generate_fake_data.py
import random

from django.core.management.base import BaseCommand
from faker import Faker

from apps.users.models import AboutUs, Blog, Category, Course, Instructor, User


class Command(BaseCommand):
    help = "Faker orqali test ma'lumotlar yaratadi (masalan: --users 10 --courses 5) o‘zbek tilida"

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, help='Foydalanuvchi soni')
        parser.add_argument('--courses', type=int, help='Kurslar soni')
        parser.add_argument('--instructors', type=int, help='O‘qituvchilar soni')
        parser.add_argument('--categories', type=int, help='Kategoriya soni')
        parser.add_argument('--blogs', type=int, help='Blog postlar soni')
        parser.add_argument('--about', type=int, help='AboutUs yozuvlar soni')
        parser.add_argument('--all', action='store_true', help='Barcha modellarga ma’lumot yaratadi')

    def handle(self, *args, **kwargs):
        faker = Faker('uz_UZ')  # O‘zbek tilida

        generators = {
            'users': lambda n: self._generate_users(faker, n),
            'courses': lambda n: self._generate_courses(faker, n),
            'instructors': lambda n: self._generate_instructors(faker, n),
            'categories': lambda n: self._generate_categories(faker, n),
            'blogs': lambda n: self._generate_blogs(faker, n),
            'about': lambda n: self._generate_aboutus(faker, n),
        }

        if kwargs.get('all'):
            for name, func in generators.items():
                func(5)
            self.stdout.write(self.style.SUCCESS("✅ Barcha modellarga ma’lumot qo‘shildi!"))
            return

        for key, func in generators.items():
            count = kwargs.get(key)
            if count:
                func(count)

    # --------------------------
    # Har bir model uchun alohida generatorlar
    # --------------------------

    def _generate_users(self, faker, n):
        for _ in range(n):
            User.objects.create(
                username=faker.user_name(),
                email=faker.email(),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                is_active=True,
            )
        self.stdout.write(self.style.SUCCESS(f"✅ {n} ta foydalanuvchi yaratildi"))

    def _generate_categories(self, faker, n):
        for _ in range(n):
            Category.objects.create(name=faker.word())
        self.stdout.write(self.style.SUCCESS(f"✅ {n} ta kategoriya yaratildi"))

    def _generate_instructors(self, faker, n):
        for _ in range(n):
            Instructor.objects.create(
                username=faker.user_name(),
                email=faker.email(),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                biography=faker.text(max_nb_chars=200),
                balance=random.uniform(100, 10000),
                image=faker.image_url(),
            )
        self.stdout.write(self.style.SUCCESS(f"✅ {n} ta o‘qituvchi (Instructor) yaratildi"))

    def _generate_courses(self, faker, n):
        instructors = list(Instructor.objects.all())
        categories = list(Category.objects.all())
        if not instructors or not categories:
            self.stdout.write(self.style.ERROR("❌ Avval instructor va kategoriya yaratish kerak!"))
            return
        for _ in range(n):
            Course.objects.create(
                title=faker.sentence(nb_words=4),          # o‘zbekcha kurs nomi
                description=faker.text(max_nb_chars=200),  # o‘zbekcha tavsif
                price=random.randint(100, 1000) * 1000,
                duration=random.randint(5, 50),
                instructor=random.choice(instructors),
                category=random.choice(categories),
            )
        self.stdout.write(self.style.SUCCESS(f"✅ {n} ta kurs yaratildi"))

    def _generate_blogs(self, faker, n):
        for _ in range(n):
            Blog.objects.create(
                title=faker.sentence(),                 # o‘zbekcha sarlavha
                content=faker.text(max_nb_chars=400),  # o‘zbekcha matn
                image=faker.image_url(),
                author_name=faker.name(),
            )
        self.stdout.write(self.style.SUCCESS(f"✅ {n} ta blog yozuvi yaratildi"))

    def _generate_aboutus(self, faker, n):
        for _ in range(n):
            AboutUs.objects.create(
                name=faker.text(max_nb_chars=200)       # o‘zbekcha matn
            )
        self.stdout.write(self.style.SUCCESS(f"✅ {n} ta AboutUs yozuvi yaratildi"))
