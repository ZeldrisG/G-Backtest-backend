# Generated by Django 3.2 on 2022-03-15 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ticker', '0003_rename_date_timeseries_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Capital')),
                ('date_start', models.DateTimeField(verbose_name='Fecha de inicio')),
                ('date_end', models.DateTimeField(verbose_name='Fecha final')),
                ('interval', models.CharField(max_length=10, verbose_name='Intervalo de tiempo')),
                ('indicators_data', models.JSONField(verbose_name='Indicadores')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticker.ticker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
