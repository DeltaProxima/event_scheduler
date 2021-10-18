# Generated by Django 3.1.2 on 2021-10-18 20:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0070_auto_20211019_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='resources_upload',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 308750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 308750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 308750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 308750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 308750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 308750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 324753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 324753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 324753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 324753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 324753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 324753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 318752, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 318752, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 318752, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 318752, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 318752, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 318752, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 309750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 309750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 310750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 310750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 309750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 309750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 292750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 292750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 293750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 293750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 292750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 293750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 310750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 311750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 311750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 311750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 311750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 311750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ccdclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 325753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ccdclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 325753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ccdclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 325753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ccdclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 325753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ccdclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 325753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ccdclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 325753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 296749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 296749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 296749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 296749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 296749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 296749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 294749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 294749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 294749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 294749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 294749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 294749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 295749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 295749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 295749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 295749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 295749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 295749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 307750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 307750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 307750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 307750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 307750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 307750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 297750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 297750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 298751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 298751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 297750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 298751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 299750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 299750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 299750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 299750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 299750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 299750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 300750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 300750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 300750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 300750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 300750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 300750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 316751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 316751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 316751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 316751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 316751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 316751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 312750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 312750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 312750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 312750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 312750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 312750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 301750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 301750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 301750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 301750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 301750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 301750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 314750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 314750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 314750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 314750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 314750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 314750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 302750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 302750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 302750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 302750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 302750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 302750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 304750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 304750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 304750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 304750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 304750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 304750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 320751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 320751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 321751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 321751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 321751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 321751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 305750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 305750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 305750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 305750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 305750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 305750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 313751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 313751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 313751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 313751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 313751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 313751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 315751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 315751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 315751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 315751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 315751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 315751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 321751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 321751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 322751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 322751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 322751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 322751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 306750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 306750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 306750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 306750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 306750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 306750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='announcements',
            field=models.TextField(blank=True, default='', help_text='announcements should be seperated by comma, so that we can list them as points', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 109207, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 291750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 291750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 291750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 291750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 291750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 319751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 319751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 320751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 320751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 319751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 319751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 317751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 317751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 317751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 317751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 317751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 20, 21, 4, 317751, tzinfo=utc)),
        ),
    ]
