from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Здесь создаются модели новых таблиц, затем нужно будет мигрировоть с помощью "python manage.py migrate" их в БД, но сначала их создать с помощью "python manage.py makemigrations" в миграциях
class Advertisement(models.Model):
    def __str__(self):
        return f'Advertisement (id= {(self.id)}, title= {self.title}, price = {self.price})'    
    
    class Meta:
        db_table = "advertisement"
    title = models.CharField('заголовок', max_length=128) # Символьное поле. max_length - количество символов в названии
    description = models.TextField('описание') # Текстовое поле
    price = models.DecimalField('цена', max_digits=10, decimal_places=2) # Числовой поле. max_digits - максимальное количество цифр, decimal_places - количество цифр после запятой
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен') # Булевое поле. значение help_text - текст-подсказка
    created_at = models.DateTimeField(auto_now_add=True) # Поле для даты создания, auto_now_add - при создании объявления
    updated_at = models.DateTimeField(auto_now=True) # Поле для даты обновления, auto_now - при обновлении
    
    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date(): # если дата создания-сегодня
            created_time = self.created_at.time().strftime("%H:%M:%S") # добавим время
            return format_html(
                '<span style="color: red; font-weight: bold;">Сегодня в {}</span>', created_time # вернем в нужном формате + время
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S") # иначе другой формат
    
    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date(): # если дата создания-сегодня
            updated_time = self.updated_at.time().strftime("%H:%M:%S") # добавим время
            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', updated_time # вернем в нужном формате + время
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S") # иначе другой формат