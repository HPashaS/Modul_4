from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date','updated_date', 'auction'] # выводим данные таблицы в админке
    list_filter = ['auction', 'created_at'] # Задаем фильтрацию
    actions = ['make_action_at_false', 'make_action_at_true'] # Зададим действия с объектами таблицы и создадим данные фукнции, обернув в декоратор

    fieldsets = ( # При создании объявления, разделим данные на категории
        ('Общее', {
            'fields' : ('title','description')
            }),

        ('Финансы', {
            'fields' : ('price','auction'),
            'classes' : ['collapse'], # для создания выпадающего меню
            }),
    )

    @admin.action(description='Убрать возможность торга')
    def make_action_at_false(self, request, queryset):
        queryset.update(auction=False) # Если включили эту функцию, то будет ложь
        
    @admin.action(description='Добавить возможность торга')
    def make_action_at_true(self, request, queryset):
        queryset.update(auction=True) # Если включили эту функцию, то будет правда

admin.site.register(Advertisement, AdvertisementAdmin) # Позволяет зарегистрировать модель таблицы

    
