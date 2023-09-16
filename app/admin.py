from django.contrib import admin

from app.models import News, Contact,TarifProduct,Tarif


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass



@admin.register(Tarif)
class TarifAdmin(admin.ModelAdmin):
    pass

@admin.register(TarifProduct)
class TarifProduct(admin.ModelAdmin):
    pass






@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


