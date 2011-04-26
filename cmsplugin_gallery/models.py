from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.folder import FilerFolderField
import utils

TEMPLATE_CHOICES = utils.autodiscover_templates()


class GalleryPlugin(CMSPlugin):
    folder = FilerFolderField()
    template = models.CharField(max_length=255, 
                                choices=TEMPLATE_CHOICES, 
                                default='cmsplugin_gallery/gallery.html',
                                editable=len(TEMPLATE_CHOICES) > 1)
    width = models.PositiveSmallIntegerField(editable=False, null=True)
    height = models.PositiveSmallIntegerField(editable=False, null=True)
    
    def __unicode__(self):
        return _(u'%(count)d image(s) in gallery') % {'count': self.image_set.count()}

    def get_size(self):
        """ returns given or found width x height tuple"""
        size = (0, 0)
        if self.src_width:
            size = (self.src_width, self.src_height)
        else:
            if self.image_set.count() > 0:
                img = self.image_set.all()[0]
                size = (img.src.width, img.src.height) 
        return size 

    
    