#!/usr/bin/python
# -*- coding: utf8 -*-
from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'update_date']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Снять торг с объявлений')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить торг к объявлению')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
