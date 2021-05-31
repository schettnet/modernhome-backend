from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from .models import Property, Space
from esite.user.models import Landlord, Tenant


class PropertyAdmin(ModelAdmin):
    model = Property
    menu_label = "Property"
    menu_icon = "fa-building"


class SpaceAdmin(ModelAdmin):
    model = Space
    menu_label = "Space"
    menu_icon = "fa-home"


class LandlordAdmin(ModelAdmin):
    model = Landlord
    menu_label = "Landlord"
    menu_icon = "fa-user"


class TenantAdmin(ModelAdmin):
    model = Tenant
    menu_label = "Tenant"
    menu_icon = "fa-user"


class PropertyManagementAdmin(ModelAdminGroup):
    menu_label = "Proptery Management"
    menu_icon = "fa-globe"
    menu_order = 110
    add_to_settings_menu = False
    exclude_from_explorer = False
    items = (PropertyAdmin, SpaceAdmin, LandlordAdmin, TenantAdmin)


modeladmin_register(PropertyManagementAdmin)
