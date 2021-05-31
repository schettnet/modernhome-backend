from django.db import models
from esite.utils.models import ContactMixin
from modelcluster.models import ClusterableModel, ParentalKey, ParentalManyToManyField
from bifrost.publisher.actions import register_publisher
from bifrost.publisher.options import PublisherOptions
from bifrost.decorators import login_required, operation_passes_test
from bifrost.api.models import (
    GraphQLString,
    GraphQLForeignKey,
    GraphQLCollection,
    GraphQLInt,
    GraphQLBoolean,
)
from graphql.error import GraphQLError
from django.db.models import Q


class PropertyType(models.TextChoices):
    EPH = "EPH", "EP house"
    MPH = "MPH", "MP house"
    DH = "DH", "D house"


alter_property_permission = operation_passes_test(
    lambda u, args: Property.objects.filter(
        id=args.get("id"), landlord__user=u
    ).exists()
)

alter_space_permission = operation_passes_test(
    lambda u, args: Space.objects.filter(
        id=args.get("id"), prop__landlord__user=u
    ).exists()
)


@register_publisher(
    read_singular=True,
    read_singular_permission=login_required,
    read_plural=True,
    read_plural_permission=login_required,
    create=True,
    create_permission=login_required,
    update=True,
    update_permission=alter_property_permission,
    delete=True,
    delete_permission=alter_property_permission,
)
class Property(ClusterableModel, ContactMixin):
    landlord = ParentalKey(
        "user.Landlord",
        null=True,
        blank=False,
        related_name="properties",
        on_delete=models.SET_NULL,
    )
    title = models.CharField(null=True, blank=False, max_length=250)
    status = models.CharField(
        max_length=3,
        choices=PropertyType.choices,
        default=PropertyType.EPH,
    )
    featured_image = models.ForeignKey(
        "images.SNEKImage",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    image_gallery = models.ManyToManyField(
        "images.SNEKImage",
        blank=True,
        related_name="+",
    )

    def tentants_total(self, info, **kwargs):
        return (
            Property.objects.annotate(total=models.Count("spaces__tenants"))
            .get(id=self.id)
            .total
        )

    def spaces_total(self, info, **kwargs):
        return self.spaces.count()

    def free_spaces_total(self, info, **kwargs):
        return (
            Property.objects.annotate(total=models.Count("spaces__tenants"))
            .filter(total__gt=0)
            .count()
        )

    def __str__(self):
        return f"{self.title}"

    graphql_fields = [
        GraphQLForeignKey(
            "landlord", "user.Landlord", publisher_options=PublisherOptions(read=True)
        ),
        GraphQLString(
            "title",
            publisher_options=PublisherOptions(
                read=True, readfilter=True, create=True, update=True
            ),
        ),
        GraphQLString(
            "status",
            publisher_options=PublisherOptions(read=True, create=True, update=True),
        ),
        GraphQLForeignKey(
            "featured_image",
            "images.SNEKImage",
            publisher_options=PublisherOptions(read=True),
        ),
        GraphQLCollection(
            GraphQLForeignKey,
            "image_gallery",
            "images.SNEKImage",
            publisher_options=PublisherOptions(read=True),
        ),
        GraphQLInt("tentants_total", publisher_options=PublisherOptions(read=True)),
        GraphQLInt("spaces_total", publisher_options=PublisherOptions(read=True)),
        GraphQLInt("free_spaces_total", publisher_options=PublisherOptions(read=True)),
        GraphQLString(
            "telephone",
            publisher_options=PublisherOptions(read=True, create=True, update=True),
        ),
        GraphQLString(
            "address",
            publisher_options=PublisherOptions(read=True, create=True, update=True),
        ),
        GraphQLString(
            "city",
            publisher_options=PublisherOptions(read=True, create=True, update=True),
        ),
        GraphQLString(
            "postal_code",
            publisher_options=PublisherOptions(read=True, create=True, update=True),
        ),
        GraphQLString(
            "country",
            publisher_options=PublisherOptions(read=True, create=True, update=True),
        ),
    ]

    def before_create(self, root, info, input):
        user = info.context.user

        # Throws error when user is not a landlord
        self.landlord = user.landlord

        return self, input

    @classmethod
    def before_read(cls, root, info, input):
        user = info.context.user

        qs = cls.objects.filter(landlord__user=user)

        return qs


@register_publisher(
    read_singular=True,
    read_singular_permission=login_required,
    read_plural=True,
    read_plural_permission=login_required,
    create=True,
    create_permission=login_required,
    update=True,
    update_permission=alter_space_permission,
    delete=True,
    delete_permission=alter_space_permission,
)
class Space(ClusterableModel):
    prop = ParentalKey(
        "Property",
        null=True,
        blank=False,
        related_name="spaces",
        on_delete=models.CASCADE,
    )
    tenants = models.ManyToManyField(
        "user.Tenant",
        blank=False,
        related_name="spaces",
    )
    title = models.CharField(null=True, blank=False, max_length=250)
    is_rental = models.BooleanField(default=True)
    featured_image = models.ForeignKey(
        "images.SNEKImage",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    image_gallery = models.ManyToManyField(
        "images.SNEKImage",
        blank=True,
        related_name="+",
    )
    contract = models.ForeignKey(
        "documents.SNEKDocument",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    docs = models.ManyToManyField(
        "documents.SNEKDocument",
        blank=True,
        related_name="+",
    )

    def tenants_total(self):
        return self.tenants.count()

    def __str__(self):
        return f"{self.title}"

    graphql_fields = [
        GraphQLForeignKey(
            "prop", "property.Property", publisher_options=PublisherOptions(read=True)
        ),
        GraphQLCollection(
            GraphQLForeignKey,
            "tenants",
            "user.Tenant",
            publisher_options=PublisherOptions(read=True),
        ),
        GraphQLString(
            "title",
            publisher_options=PublisherOptions(read=True, readfilter=True, update=True),
        ),
        GraphQLBoolean(
            "is_rental",
            publisher_options=PublisherOptions(read=True, create=True, update=True),
        ),
        # > Must be changed to GraphQLImage and GrapQLDocument in the future!
        GraphQLForeignKey(
            "featured_image",
            "images.SNEKImage",
            publisher_options=PublisherOptions(read=True),
        ),
        GraphQLCollection(
            GraphQLForeignKey,
            "image_gallery",
            "images.SNEKImage",
            publisher_options=PublisherOptions(read=True),
        ),
        GraphQLForeignKey(
            "contract",
            "documents.SNEKDocument",
            publisher_options=PublisherOptions(read=True),
        ),
        GraphQLCollection(
            GraphQLForeignKey,
            "docs",
            "documents.SNEKDocument",
            publisher_options=PublisherOptions(read=True),
        ),
        GraphQLInt("tenants_total", publisher_options=PublisherOptions(read=True)),
    ]

    @classmethod
    def before_read(cls, root, info, input):
        user = info.context.user

        qs = cls.objects.filter(Q(prop__landlord__user=user) | Q(tenants__user=user))

        return qs
