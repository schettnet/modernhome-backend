from graphene_file_upload.scalars import Upload
import graphene
from bifrost.decorators import login_required
from esite.images.models import SNEKImage
from esite.documents.models import SNEKDocument
from .models import Property, Space


# > Property


class CreatePropertyAsset(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        propertyId = graphene.ID(required=True)
        featured_image = Upload(required=False)
        gallery_images = Upload(required=False)

    @login_required
    def mutate(
        self, info, propertyId, featured_image=None, gallery_images=None, **kwargs
    ):
        user = info.context.user

        p = Property.objects.get(id=propertyId, landlord__user=user)

        if featured_image:
            image = SNEKImage.objects.create(
                file=featured_image,
                title=f"Featured image of {p.__name__}",
                author=user,
            )

            p.featured_image = image

        if gallery_images:
            for image in gallery_images:
                image = SNEKImage.objects.create(
                    file=image, title=f"Gallery image of {p.__name__}", author=user
                )

                p.image_gallery.add(image)

        p.save()

        return CreatePropertyAsset(success=True)


# > Space


class CreateSpaceAsset(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        spaceId = graphene.ID(required=True)
        featured_image = Upload(required=False)
        gallery_images = Upload(required=False)
        contract_document = Upload(required=False)
        documents = Upload(required=False)

    @login_required
    def mutate(
        self,
        info,
        spaceId,
        featured_image=None,
        gallery_images=None,
        contract_document=None,
        documents=None,
        **kwargs,
    ):
        user = info.context.user

        s = Space.objects.get(id=spaceId, prop_landlord__user=user)

        if featured_image:
            image = SNEKImage.objects.create(
                file=featured_image,
                title=f"Featured image of {s.__name__}",
                author=user,
            )

            s.featured_image = image

        if gallery_images:
            for image in gallery_images:
                image = SNEKImage.objects.create(
                    file=image, title=f"Gallery image of {s.__name__}", author=user
                )

                s.image_gallery.add(image)

        if contract_document:
            document = SNEKDocument.objects.create(
                file=contract_document,
                title=f"Contract document of {s.__name__}",
            )

            s.contract = document

        if documents:
            for doc in documents:
                document = SNEKDocument.objects.create(
                    file=doc,
                    title=f"Document of {s.__name__}",
                )

                s.docs.add(document)

        s.save()

        return CreateSpaceAsset(success=True)


class DeleteAsset(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        imageId = graphene.ID(required=False)
        documentId = graphene.ID(required=False)

    @login_required
    def mutate(self, info, imageId=None, documentId=None, **kwargs):
        user = info.context.user

        if imageId:
            SNEKImage.objects.get(id=imageId, uploaded_by_user=user).delete()

        if documentId:
            SNEKDocument.objects.get(id=documentId, uploaded_by_user=user).delete()

        return DeleteAsset(success=True)


class Mutation(graphene.ObjectType):
    create_property_asset = CreatePropertyAsset.Field()
    create_space_asset = CreateSpaceAsset.Field()
    delete_asset = DeleteAsset.Field()
