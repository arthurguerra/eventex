# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 00:42
from __future__ import unicode_literals

from django.db import migrations


def copy_src_to_dst(Source, Destination):
    for src in Source.objects.all():
        dst = Destination(
            title=src.title,
            start=src.start,
            description=src.description,
            slots=src.slots
        )

        dst.save()
        dst.speakers.set(src.speakers.all())
        src.delete()


def forward_course_abc_to_mti(apps, schema_editor):
    '''
    para cada abc instanciar um mti com todos os attributos
    salvar o mti
    associar os speakers do course abc no mti
    deletar o abc
    '''

    # loading history model, if you import from eventex instead, you would get the latest model that may not have
    # all fields you wanted for the migration
    copy_src_to_dst(
        apps.get_model('core', 'CourseOld'),
        apps.get_model('core', 'Course')
    )


def backward_course_abc_to_mti(apps, schema_editor):
    copy_src_to_dst(
        apps.get_model('core', 'CourseOld'),
        apps.get_model('core', 'Course')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_course'),
    ]

    operations = [
        migrations.RunPython(forward_course_abc_to_mti,
                             backward_course_abc_to_mti)
    ]
