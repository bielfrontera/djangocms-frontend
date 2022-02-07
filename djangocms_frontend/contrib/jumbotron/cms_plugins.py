from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from ... import settings
from ...cms_plugins import CMSUIPlugin
from .. import jumbotron
from . import forms, models

mixin_factory = settings.get_renderer(jumbotron)


@plugin_pool.register_plugin
class JumbotronPlugin(mixin_factory("Jumbotron"), CMSUIPlugin):
    """
    Components > "Jumbotron" Plugin
    https://getbootstrap.com/docs/5.1/examples/jumbotron/
    """

    name = _("Jumbotron")
    module = _("Frontend")
    model = models.Jumbotron
    form = forms.JumbotronForm
    change_form_template = "djangocms_frontend/admin/jumbotron.html"
    allow_children = True

    fieldsets = [
        (None, {"fields": ("jumbotron_fluid",)}),
        (
            _("Advanced settings"),
            {
                "classes": ("collapse",),
                "fields": (
                    "tag_type",
                    "attributes",
                ),
            },
        ),
    ]
