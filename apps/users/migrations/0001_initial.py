# Generated by Django 4.2.7 on 2023-11-08 10:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=25,
                        validators=[
                            django.core.validators.RegexValidator(
                                "[A-Z][a-z]{2,24}", ""
                            )
                        ],
                    ),
                ),
                (
                    "surname",
                    models.CharField(
                        max_length=25,
                        validators=[
                            django.core.validators.RegexValidator(
                                "[A-Z][a-z]{2,24}", ""
                            )
                        ],
                    ),
                ),
                ("bio", models.TextField()),
                (
                    "age",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(18),
                            django.core.validators.MaxValueValidator(90),
                        ]
                    ),
                ),
                ("avatar", models.ImageField(blank=True, upload_to="image/")),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "profile_users",
            },
        ),
        migrations.CreateModel(
            name="TypeAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_seller", models.BooleanField(default=False)),
                ("is_premium", models.BooleanField(default=False)),
                ("expire_premium", models.DateTimeField(blank=True)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "type_acount_user",
            },
        ),
        migrations.CreateModel(
            name="UserModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_block", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "account",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user",
                        to="users.typeaccount",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user",
                        to="users.profilemodel",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        max_length=128,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[A-Za-z0-9@!#$_\\-+]{4,128}$",
                                "The password must be from 4 to 128 characters including Latin characters of any case, numbers and special characters, !@#$_-+",
                            )
                        ],
                    ),
                ),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "auth_users",
            },
        ),
    ]
