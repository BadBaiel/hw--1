from django.db import models

# Create your models here.
class TVshow(models.Model):
        GENRE = (
             ('HORROR', ('HORROR'),
              ('COMEDY', 'COMEDY'),
              ('FANTASY', 'FANTASY'),
              )
        )
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='')
        quantity = models.PositiveBigIntegerField('Колличество фильмов')
        qenre = models.CharField(max_length=100, choices=GENRE)
        video = models.URLField()
        price = models.PositiveIntegerField('Цена билета', null=True)

        def __str__(self):
            return self.title