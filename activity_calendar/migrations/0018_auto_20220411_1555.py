# Generated by Django 2.2.15 on 2022-04-11 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership_file', '0016_auto_20211231_1334'),
        ('activity_calendar', '0017_core_activity_groupings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(help_text='The local url string', unique=True, verbose_name='url string')),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='full_day',
            field=models.BooleanField(default=False, help_text='Whether this event marks the entire day'),
        ),
        migrations.AddField(
            model_name='activity',
            name='is_public',
            field=models.BooleanField(default=True, help_text='If activity should be on public calendar'),
        ),
        migrations.AddField(
            model_name='activitymoment',
            name='local_full_day',
            field=models.BooleanField(blank=True, default=None, help_text='Whether this event marks the entire day', null=True),
        ),
        migrations.CreateModel(
            name='MemberCalendarSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('use_birthday', models.BooleanField(default=False, verbose_name='Display my birthday in Knights birthday calendar')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='membership_file.Member')),
            ],
        ),
        migrations.CreateModel(
            name='CalendarActivityLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_calendar.Activity')),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_calendar.Calendar')),
            ],
        ),
        migrations.AddField(
            model_name='calendar',
            name='activities',
            field=models.ManyToManyField(through='activity_calendar.CalendarActivityLink', to='activity_calendar.Activity'),
        ),
    ]
