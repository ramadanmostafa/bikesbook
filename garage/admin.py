from django.contrib import admin
from .models import BicycleMake, BicyceStyle, NewMotorcycle, NewBicycle, MotorEngine, MotorMake, MotorStyle, MotorModel


class BicycleStyleAdmin(admin.ModelAdmin):
    search_fields = ['style','active']
    list_display = ['style','active']
    list_filter = ['active']

    class Meta:
        model = BicyceStyle


class BicycleMakeAdmin(admin.ModelAdmin):

    search_fields = ['brand', 'active']
    list_display = ['brand', 'active']
    list_filter = [ 'active']

    class Meta:
        model = BicycleMake



def accept_request_bicycle(admin_class, request, new_items):
    for new_bike in new_items:
        BicycleMake.objects.create(brand=new_bike.make)
        BicyceStyle.objects.create(style=new_bike.style)
        NewBicycle.objects.filter(id=new_bike.id).delete()

def accept_request_motorcycle(admin_class, request, new_items):

    for new_motor in new_items:
        MotorEngine.objects.create(cc=new_motor.engine_size)
        new_make = MotorMake.objects.create(brand=new_motor.make)
        MotorStyle.objects.create(style=new_motor.style)
        MotorModel.objects.create(model=new_motor.model, make=new_make)
        NewMotorcycle.objects.filter(id=new_motor.id).delete()



class NewMotorcycleAdmin(admin.ModelAdmin):
    readonly_fields = ["make", "style", "engine_size", "model"]
    list_display = ["make", "style", "engine_size", "model"]
    actions = [accept_request_motorcycle]

    class Meta:
        module = NewMotorcycle

class NewBicycleAdmin(admin.ModelAdmin):
    readonly_fields = ["make", "style"]
    list_display = ["make", "style"]
    actions = [accept_request_bicycle]

    class Meta:
        module = NewBicycle



admin.site.register(BicycleMake, BicycleMakeAdmin)
admin.site.register(BicyceStyle, BicycleStyleAdmin)
admin.site.register(NewBicycle, NewBicycleAdmin)
admin.site.register(NewMotorcycle, NewMotorcycleAdmin)


