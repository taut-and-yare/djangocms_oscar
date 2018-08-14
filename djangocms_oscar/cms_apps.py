# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from oscar.app import application


class OscarApp(CMSApp):
    """
    Allows "mounting" the oscar shop and all of its urls to a specific CMS page.
    e.g at "/shop/"
    """
    name = _("Oscar")
    urls = [
        application.urls[0]
    ]
    exclude_permissions = ['dashboard']


apphook_pool.register(OscarApp)
