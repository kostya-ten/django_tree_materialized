from functools import partial

from django.contrib import admin
from . import models


class MPAdmin(admin.ModelAdmin):
    readonly_fields = ('level', 'path')
    list_display = ('id', 'parent', 'level', 'path')
    #autocomplete_fields = ('parent',)
    #search_fields = ('parent',)

    def get_form(self, request, obj=None, change=False, **kwargs):
        return super().get_form(request, obj, change, **kwargs)

    #     obj_id = request.resolver_match.kwargs['object_id']
    #     obj = self.get_object(request, obj_id)
    #     print(obj_id)
    #
    #     self.get_queryset(request).model.objects.filter(id=obj_id)
    #     #.filter(path__startswith=self.path)
    #
    #
    #     # print(db, db_field, request, self.get_inline_instances(request=request))
    #

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        obj_id = kwargs.get('request').resolver_match.kwargs.get('object_id')
        if obj_id:
            res = self.get_queryset(kwargs.get('request')).model.objects.get(id=obj_id)
            # print(res.get_children())

        #if db_field.name == 'parent':
            #obj_id = kwargs.get('request').resolver_match.kwargs.get('object_id')
            #res = self.get_queryset(kwargs.get('request')).model.objects.get(id=obj_id)

            #print(res.get_children())

            # print(formfield)
            #return formfield

        return formfield

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     print('formfield_for_dbfield')
    #     return super().formfield_for_dbfield(db_field, **kwargs)

    # def formfield_for_dbfield(self, db_field, request, **kwargs):
    #     if db_field.name == 'parent':
    #         print(db_field, request, kwargs)
    #
    #     return super().formfield_for_dbfield(db_field, request, **kwargs)

    # def formfield_for_dbfield(self, db_field, request, **kwargs):
    #     if db_field.name == 'parent':
    #         print('ddddddddd', self.parent_instance)
    #
    #     return super().formfield_for_dbfield(db_field, request, **kwargs)

    # def get_field_queryset(self, db, db_field, request):
    #     if db_field.column == 'parent_id':
    #         print('eeeeeeeeeee', db, db_field)
    #         # result = super().get_field_queryset(db, db_field, request)
    #         # print(result)
    #         return
    #     return super().get_field_queryset(db, db_field, request)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        obj.level = 1
        # print(obj.get_children())

        #for item in self.get_children():
        #    if obj.id == item.id:
        #        raise exceptions.InvalidMove("Unable to transfer object")

        if obj.parent:
            obj.level = obj.parent.level + 1
            obj.path = obj.parent.path + models.MPTree.number_to_str(obj.id)
        else:
            obj.path = models.MPTree.number_to_str(obj.id)

        obj.save()
