# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from collections import OrderedDict
import warnings
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cmsplugin_cascade.widgets import MultipleCascadingSizeWidget, ColorPickerWidget, SelectOverflowWidget


CASCADE_PLUGINS = getattr(settings, 'CMSPLUGIN_CASCADE_PLUGINS', ('cmsplugin_cascade.generic', 'cmsplugin_cascade.link',))

# all other configuration settings are replaced by a dictionary
if hasattr(settings, 'CMSPLUGIN_CASCADE_ALIEN_PLUGINS'):
    warnings.warn("CMSPLUGIN_CASCADE_ALIEN_PLUGINS is deprecated. "
                  "Use CMSPLUGIN_CASCADE['alien_plugins'] instead.")

if hasattr(settings, 'CMSPLUGIN_CASCADE_DEPENDENCIES'):
    warnings.warn("CMSPLUGIN_CASCADE_DEPENDENCIES is deprecated. "
                  "Use CMSPLUGIN_CASCADE['dependencies'] instead.")

if hasattr(settings, 'CMSPLUGIN_CASCADE_WITH_EXTRAFIELDS'):
    warnings.warn("CMSPLUGIN_CASCADE_WITH_EXTRAFIELDS is deprecated. "
                  "Use CMSPLUGIN_CASCADE['plugins_with_extra_fields'] instead.")

if hasattr(settings, 'CMSPLUGIN_CASCADE_WITH_SHARABLES'):
    warnings.warn("CMSPLUGIN_CASCADE_WITH_SHARABLES is deprecated. "
                  "Use CMSPLUGIN_CASCADE['plugins_with_sharables'] instead.")

if hasattr(settings, 'CMSPLUGIN_CASCADE_LINKPLUGIN_CLASSES'):
    warnings.warn("CMSPLUGIN_CASCADE_LINKPLUGIN_CLASSES is deprecated. "
                  "Use CMSPLUGIN_CASCADE['link_plugin_classes'] instead.")

if hasattr(settings, 'CMSPLUGIN_CASCADE_EXTRA_INLINE_STYLES'):
    warnings.warn("CMSPLUGIN_CASCADE_EXTRA_INLINE_STYLES is deprecated. "
                  "Use CMSPLUGIN_CASCADE['extra_inline_styles'] instead.")

if hasattr(settings, 'CMSPLUGIN_CASCADE_SEGMENTATION_MIXINS'):
    warnings.warn("CMSPLUGIN_CASCADE_SEGMENTATION_MIXINS is deprecated. "
                  "Use CMSPLUGIN_CASCADE['segmentation_mixins'] instead.")

if hasattr(settings, 'CMSPLUGIN_CASCADE_PLUGINS_WITH_EXTRA_RENDER_TEMPLATES'):
    warnings.warn("CMSPLUGIN_CASCADE_PLUGINS_WITH_EXTRA_RENDER_TEMPLATES is deprecated. "
                  "Use CMSPLUGIN_CASCADE['plugins_with_extra_render_templates'] instead.")

CMSPLUGIN_CASCADE = getattr(settings, 'CMSPLUGIN_CASCADE', {})
orig_config = dict(CMSPLUGIN_CASCADE)

# Specify location of CSS file used to load fonts from http://fontawesome.io/
CMSPLUGIN_CASCADE.setdefault('fontawesome_css_url', 'https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css')

CMSPLUGIN_CASCADE.setdefault('alien_plugins', ['TextPlugin'])

# Use a prefix to symbolize a Cascade plugin in case there are ambiguous names.
CMSPLUGIN_CASCADE.setdefault('plugin_prefix', None)

CMSPLUGIN_CASCADE['dependencies'] = {
    'cascade/js/ring.js': 'cascade/js/underscore.js',
    'cascade/js/admin/sharableglossary.js': 'cascade/js/ring.js',
    'cascade/js/admin/segmentplugin.js': 'cascade/js/ring.js',
    'cascade/js/admin/jumbotronplugin.js': 'cascade/js/ring.js',
    'cascade/js/admin/fonticonplugin.js': 'cascade/js/ring.js',
    'cascade/js/admin/linkpluginbase.js': ('cascade/js/admin/sharableglossary.js',),
    'cascade/js/admin/defaultlinkplugin.js': ('cascade/js/admin/linkpluginbase.js',),
    'cascade/js/admin/imageplugin.js': ('cascade/js/admin/linkpluginbase.js',),
    'cascade/js/admin/pictureplugin.js': ('cascade/js/admin/linkpluginbase.js',),
}
CMSPLUGIN_CASCADE['dependencies'].update(orig_config.get('dependencies', {}))

if 'cmsplugin_cascade.extra_fields' in settings.INSTALLED_APPS:
    CMSPLUGIN_CASCADE['plugins_with_extra_fields'] = [
        'BootstrapButtonPlugin', 'BootstrapContainerPlugin', 'BootstrapRowPlugin',
        'BootstrapJumbotronPlugin', 'SimpleWrapperPlugin', 'HeadingPlugin', 'HorizontalRulePlugin',
    ]
    CMSPLUGIN_CASCADE['plugins_with_extra_fields'].extend(orig_config.get('plugins_with_extra_fields', []))
else:
    CMSPLUGIN_CASCADE['plugins_with_extra_fields'] = []

if 'cmsplugin_cascade.sharable' in settings.INSTALLED_APPS:
    CMSPLUGIN_CASCADE.setdefault('plugins_with_sharables', {})
else:
    CMSPLUGIN_CASCADE['plugins_with_sharables'] = {}

CMSPLUGIN_CASCADE.setdefault('link_plugin_classes', (
    'cmsplugin_cascade.link.plugin_base.DefaultLinkPluginBase',
    'cmsplugin_cascade.link.plugin_base.LinkElementMixin',
    'cmsplugin_cascade.link.forms.LinkForm',
))
"""
3-Tuple containing shared base classes for classes wishing to link onto something:
1. Base class for a CMSPlugin, 2. A Model Mixin, 3. The base class used to build the form.
"""

CMSPLUGIN_CASCADE.setdefault('plugins_with_bookmark', [
    'SimpleWrapperPlugin', 'HeadingPlugin'])

CMSPLUGIN_CASCADE.setdefault('bookmark_prefix', '')

CMSPLUGIN_CASCADE['extra_inline_styles'] = OrderedDict((
    ('Margins', (('margin-top', 'margin-right', 'margin-bottom', 'margin-left',), MultipleCascadingSizeWidget)),
    ('Paddings', (('padding-top', 'padding-right', 'padding-bottom', 'padding-left',), MultipleCascadingSizeWidget)),
    ('Widths', (('min-width', 'width', 'max-width',), MultipleCascadingSizeWidget)),
    ('Heights', (('min-height', 'height', 'max-height',), MultipleCascadingSizeWidget)),
    ('Font Size', (('font-size',), MultipleCascadingSizeWidget)),
    ('Colors', (('color', 'background-color',), ColorPickerWidget)),
    ('Overflow', (('overflow', 'overflow-x', 'overflow-y',), SelectOverflowWidget)),
))
CMSPLUGIN_CASCADE['extra_inline_styles'].update(orig_config.get('extra_inline_styles', {}))

CMSPLUGIN_CASCADE.setdefault('segmentation_mixins', [
    ('cmsplugin_cascade.segmentation.mixins.EmulateUserModelMixin', 'cmsplugin_cascade.segmentation.mixins.EmulateUserAdminMixin')
])

CMSPLUGIN_CASCADE.setdefault('plugins_with_extra_render_templates', {
    'TextLinkPlugin': (
        ('cascade/link/text-link.html', _("default")),
        ('cascade/link/text-link-linebreak.html', _("with line break")),
    )
})

# Folder where extracted icon fonts are stored.
CMSPLUGIN_CASCADE.setdefault('icon_font_root',
                             os.path.abspath(os.path.join(settings.MEDIA_ROOT, 'icon_fonts')))
try:
    os.makedirs(CMSPLUGIN_CASCADE['icon_font_root'])
except os.error:
    pass
