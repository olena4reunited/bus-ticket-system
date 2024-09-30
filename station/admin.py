from django.contrib import admin

from station.models import Bus, Ticket, Trip, Order, Facility


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [TicketInline]


admin.site.register(Bus)
admin.site.register(Ticket)
admin.site.register(Trip)
admin.site.register(Facility)
