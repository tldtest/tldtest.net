# Generated by Django 5.0.2 on 2024-03-01 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RootZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rectype', models.CharField(max_length=10)),
                ('value', models.CharField(max_length=4096)),
                ('lastEdition', models.DateTimeField(auto_now=True)),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='tldtester_r_name_40033d_idx'), models.Index(fields=['rectype'], name='tldtester_r_rectype_1bc68d_idx')],
            },
        ),
        migrations.CreateModel(
            name='TLD',
            fields=[
                ('tld', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('unicodetld', models.CharField(max_length=30)),
                ('nsamount', models.IntegerField(default=0)),
                ('v4nsamount', models.IntegerField(default=0)),
                ('v6nsamount', models.IntegerField(default=0)),
                ('dnssec', models.IntegerField(choices=[(0, 'Delete DS'), (1, 'RSA/MD5'), (2, 'Diffie-Hellman'), (3, 'DSA/SHA1'), (5, 'RSA/SHA-1'), (6, 'DSA-NSEC3-SHA1'), (7, 'RSASHA1-NSEC3-SHA1'), (8, 'RSA/SHA-256'), (10, 'RSA/SHA-512'), (12, 'GOST R 34.10-2001'), (13, 'ECDSA Curve P-256 with SHA-256'), (14, 'ECDSA Curve P-384 with SHA-384'), (15, 'Ed25519'), (16, 'Ed448'), (17, 'SM2 signing algorithm with SM3 hashing algorithm'), (23, 'GOST R 34.10-2012'), (252, 'Reserved for Indirect Keys'), (253, 'private algorithm'), (254, 'private algorithm OID'), (300, 'Unknown'), (400, 'None')], default=300)),
                ('amountofkeys', models.IntegerField(default=0)),
                ('lastEdition', models.DateTimeField(auto_now=True)),
                ('organisation', models.CharField(max_length=30)),
            ],
            options={
                'indexes': [models.Index(fields=['tld'], name='tldtester_t_tld_b4cdc5_idx'), models.Index(fields=['dnssec'], name='tldtester_t_dnssec_694343_idx'), models.Index(fields=['nsamount'], name='tldtester_t_nsamoun_8ca22f_idx')],
            },
        ),
    ]
