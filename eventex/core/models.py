from django.db import models
from django.shortcuts import resolve_url as r
from eventex.core.managers import KindQuerySet, PeriodManager


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('Descricao', blank=True)

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural = 'Palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone')
    )

    # model as string, django will find the correct model to import
    speaker = models.ForeignKey('Speaker', verbose_name='Palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    # Query Set that works as a model manager
    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value


# abstract model
class Talk(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo')
    start = models.TimeField(verbose_name='inicio', blank=True, null=True)
    description = models.TextField(verbose_name='descricao', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

    objects = PeriodManager()

    class Meta:
        ordering = ['start']
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title


class Course(Talk):
    '''
    Course would inherit from Talk. Then, any Course is a Talk, but a Talk is not a Course.

    * This change would make Django drop the old Course table (losing all data already entered in the DB),
    * so we need to apply specific migrations to keep the data that is already in the DB and use the new
    * relationship between Talk and Course.

    * With this class commented, we need to make a new migration, so Django will detect a name change from Course to
    * CourseOld.
    '''

    slots = models.IntegerField()

    objects = PeriodManager()

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

