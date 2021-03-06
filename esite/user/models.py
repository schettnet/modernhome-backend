import django.contrib.auth.validators
from bifrost.api.models import GraphQLBoolean, GraphqlDatetime, GraphQLString
from django.contrib.auth.models import AbstractUser
from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from esite.utils.models import ContactMixin


# Extend AbstractUser Model from django.contrib.auth.models
class SNEKUser(AbstractUser, ClusterableModel, ContactMixin):
    username = models.CharField(
        "username",
        null=True,
        blank=False,
        error_messages={"unique": "A user with that username already exists."},
        help_text="Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.",
        max_length=36,
        unique=True,
        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
    )
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=False
    )
    company_name = models.CharField(null=True, blank=True, max_length=250)
    company_vat = models.CharField(null=True, blank=True, max_length=250)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("username"),
                FieldPanel("first_name"),
                FieldPanel("last_name"),
                FieldPanel("email"),
            ],
            "Main",
        ),
        MultiFieldPanel(
            [
                FieldPanel("birthdate"),
                FieldPanel("telephone"),
                FieldPanel("address"),
                FieldPanel("city"),
                FieldPanel("postal_code"),
                FieldPanel("country"),
                FieldPanel("company_name"),
                FieldPanel("company_vat"),
            ],
            "Details",
        ),
        MultiFieldPanel(
            [
                FieldPanel("is_active"),
            ],
            "Settings",
        ),
    ]

    graphql_fields = [
        GraphQLString("username"),
        GraphQLString("first_name"),
        GraphQLString("last_name"),
        GraphQLString("email"),
        GraphQLString("birthdate"),
        GraphQLString("telephone"),
        GraphQLString("address"),
        GraphQLString("city"),
        GraphQLString("postal_code"),
        GraphQLString("country"),
        GraphQLString("company_name"),
        GraphQLString("company_vat"),
    ]

    def __str__(self):
        return f"{self.username}"


class Landlord(ClusterableModel):
    user = models.OneToOneField("SNEKUser", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.user.username}"


class Tenant(ClusterableModel):
    user = models.OneToOneField("SNEKUser", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.user.username}"


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright ?? 2021 Nico Schett
