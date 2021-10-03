from django.apps import AppConfig

#class onde é possível adicionar e tratar campos
class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
    verbose_name = 'Catálogo' #muda o nome do objeto dentro da area admin para Catálogo ao invés de Catalog
