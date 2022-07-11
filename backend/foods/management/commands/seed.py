from django.core.management.base import BaseCommand


from foods.models import FoodCategory, Food


class Command(BaseCommand):
    help = 'Seeds the database.'

    def handle(self, *args, **options):

        #creating categories
        drinks = FoodCategory.objects.get_or_create(name_ru="Напитки",
                                    name_en=None, name_ch=None, order_id=10)[0]
        FoodCategory.objects.get_or_create(name_ru="Выпечка",
                                        name_en=None, name_ch=None, order_id=20)

        print('Created category - Напитки')
        print('Created category - Выпечка')
        #creating foods
        data = [
            ['Чай', 'Чай 100 гр'],
            ['Кола', 'Кола'],
            ['Спрайт', 'Спрайт'],
            ['Байкал', 'Байкал'],
            ['Дюшес', 'Дюшес'],
        ]
        is_publish = True
        iters = len(data)
        for i in range(iters):
            if i == iters:
                is_publish = False
            Food.objects.get_or_create(category=drinks, is_vegan=False,
                is_special=False, code=i+1, internal_code=(i+1)*100,
                name_ru=data[i][0], description_ru=data[i][1],
                description_en=None, description_ch=None, cost='123.00',
                is_publish=is_publish)

            print(f'Created food - {data[i][0]}')

        cola = Food.objects.get(name_ru=data[1][0])
        tea = Food.objects.get(name_ru=data[0][0])
        tea.additional.add(cola)
        tea.save()
        print(f'{data[1][0]} added to additional of {data[0][0]}')
