from django.db import models


# Здесь создаются модели новых таблиц, затем нужно будет мигрировоть с помощью "python manage.py migrate" их в БД, но сначала их создать с помощью "python manage.py makemigrations" в миграциях
class Advertisement(models.Model):
    class Meta:
        db_table = "advertisement"
    title = models.CharField('заголовок', max_length=128) # Символьное поле. max_length - количество символов в названии
    description = models.TextField('описание') # Текстовое поле
    price = models.DecimalField('цена', max_digits=10, decimal_places=2) # Числовой поле. max_digits - максимальное количество цифр, decimal_places - количество цифр после запятой
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен') # Булевое поле. значение help_text - текст-подсказка
    created_at = models.DateTimeField(auto_now_add=True) # Поле для даты создания, auto_now_add - при создании объявления
    updated_at = models.DateTimeField(auto_now=True) # Поле для даты обновления, auto_now - при обновлении
    
