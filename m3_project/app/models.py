from django.db import models

# Create your models here.


class Person(models.Model):

    GENDERS = (
        (0, u''),
        (1, u'Мужской'),
        (2, u'Женский'),
    )

    name = models.CharField(max_length=150, verbose_name=u'Имя')
    surname = models.CharField(max_length=150, verbose_name=u'Фамилия')
    gender = models.PositiveSmallIntegerField(
        choices=GENDERS,
        default=GENDERS[0][0],
        verbose_name=u'Пол')
    birthday = models.DateField(
        null=True, blank=True,
        verbose_name=u'Дата рождения')

    def __unicode__(self):
        return u"%s %s" % (self.surname, self.name)

    class Meta:
        verbose_name = u'Физическое лицо'
        verbose_name_plural = u'Физические лица'