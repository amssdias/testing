# Generated by Django 3.2.12 on 2022-05-27 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220302_2320'),
        ('foods', '0009_auto_20220421_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyUserFoodStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_fat', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('carbs', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fiber', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('salt', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('date', models.DateField()),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_status', to='accounts.profile')),
            ],
            options={
                'verbose_name': 'Daily User Food Status',
                'verbose_name_plural': 'Daily User Food Status',
                'ordering': ['-date'],
            },
        ),
        migrations.AddConstraint(
            model_name='dailyuserfoodstatus',
            constraint=models.UniqueConstraint(fields=('user_profile', 'date'), name='unique_daily_user_stats'),
        ),
    ]
