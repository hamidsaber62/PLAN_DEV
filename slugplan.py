# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'plan_site.settings')
import django
django.setup()
"""
Ìò «”ò—ÌÅ  »—«Ì Å—ò—œ‰ « Ê„« Ìò ›Ì·œ «”·«ê œ— „œ·Â«ÌÌ òÂ «?‰ ›?·œ —« œ«—‰œ  « œ— ¬œ—” œÂ? Ê Ê?Ê «“ «?‰ ›?·œ «” ›«œÂ ‘Êœ
 «·» Â «“ «?‰ «”ò—?Å  «” ›«œÂ ‰ò—œ Ê»Â Ã«? ¬‰ «“  «»Â SAVE œ— „œ·Â« «” ›«œÂ ò—œ„
"""
from sa_plan_app.models import *
print('@@@@@@@@@@@  START PROCESS  @@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@  START PLAN SLUG   @@@@@@@@@@@@')
for pl in Plan.objects.all():
    pl.slug = pl.name.replace(' ', '-')
    pl.save()
print('@@@@@@@@@@@  END PLAN SLUG   @@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@  START Project SLUG   @@@@@@@@@@@@')

for prj in Project.objects.all():
    prj.slug = prj.name.replace(' ', '-')
    prj.save()
print('@@@@@@@@@@@  END Project SLUG   @@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@  START Proctor SLUG   @@@@@@@@@@@@')
for proc in Proctor.objects.all():
    proc.slug = proc.name.replace(' ', '-')
    proc.save()
print('@@@@@@@@@@@  END Proctor SLUG   @@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@  START InfoCard SLUG   @@@@@@@@@@@@')
for info in InfoCard.objects.all():
    info.slug = info.name.replace(' ', '-')
    info.save()
print('@@@@@@@@@@@  END InfoCard SLUG   @@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@  START ImageGallery SLUG   @@@@@@@@@@@@')
for gallery in ImageGallery.objects.all():
    gallery.slug = gallery.name.replace(' ', '-')
    gallery.save()
print('@@@@@@@@@@@  END ImageGallery SLUG   @@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@  END PROCESS  @@@@@@@@@@@@')
