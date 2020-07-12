

# -*- coding: utf-8 -*-
from django.contrib import admin
# Register your models here.

from .models import *

# class AuthorAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Author, AuthorAdmin)

# admin.site.register(Plans)
# admin.site.register(Projects)
# admin.site.register(Proctor)


# class ProjectsInline(admin.StackedInline):
#     #   admin.TabularInline OR admin.StackedInline
#     model = Projects
#     extra = 2
#
#
# class ProctorInline(admin.TabularInline):
#     model = Proctor
#     extra = 1
#
#
@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'organization', 'beneficiary')
    # list_filter = ('name', 'proctor', 'entry_datetime')
    #
    # search_fields = ('proctor__name', 'name', 'entry_datetime')

    # inlines = [ProjectsInline]

    # fields = ('plan_name', ('plan_organization', 'plan_beneficiary'), ('plan_number', 'beneficiary_code'),
    #      ('plan_start_date', 'plan_end_date', 'plan_entry_datetime'), ('proctor', 'plan_type', 'project_quantity'))

    # fieldsets = (
    #     ('اطلاعات پایه طرح', {
    #         'fields': (('name', 'type', 'project_quantity'), ('organization', 'beneficiary'),
    #                    ('number', 'beneficiary_code'))
    #     }),
    #     ('تاریخهای شروع و پایان و اعتبار طرح', {
    #         'fields': ('start_date', 'end_date', 'credit')
    #     }),
    #     ('مجری طرح و ردیف شغلی در شرکت', {
    #         'fields': ('proctor',)
    #     }),
    # )


#
#


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')


@admin.register(Proctor)
class ProctorAdmin(admin.ModelAdmin):
    pass


@admin.register(InfoCard)
class InfoCardAdmin(admin.ModelAdmin):
    pass
# @admin.register(OfficeGroup)
# class OfficeGroupAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(OfficeProgram)
# class OfficeProgramAdmin(admin.ModelAdmin):
#     pass


@admin.register(AttachmentFiles)
class AttachmentFilesAdmin(admin.ModelAdmin):
    pass






# @admin.register(PlanDescription)
# class PlanDescriptionAdmin(admin.ModelAdmin):
#     pass


# @admin.register(ProjectDescription)
# class ProjectDescriptionAdmin(admin.ModelAdmin):
#     pass


# @admin.register(ProctorDescription)
# class ProctorDescriptionAdmin(admin.ModelAdmin):
#     pass

