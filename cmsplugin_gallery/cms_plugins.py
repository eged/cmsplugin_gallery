from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
import models 


class CMSGalleryPlugin(CMSPluginBase):
    
    model = models.GalleryPlugin
    name = _('Image gallery')
    render_template = 'cmsplugin_gallery/gallery.html'
    admin_preview = False
    
    
    def render(self, context, instance, placeholder):
        images = instance.folder.files.filter(image__isnull=False)
        context.update({'images': images, 'gallery': instance})
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CMSGalleryPlugin)