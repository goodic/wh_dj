from django.contrib import admin
from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data.keys():
                if form.cleaned_data['is_main']:
                    counter += 1
            if counter > 1:
                raise ValidationError('Может быть только один основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = RelationshipInlineFormset


@admin.register(Tag)
class ScopeAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
