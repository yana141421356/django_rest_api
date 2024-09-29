from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ItemViewSet, AddressViewSet, item_description_detail
from django.http import JsonResponse

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'address', AddressViewSet)


#404を返すjsonのエンドポイントを追加
def custom_404_view(request, exception=None):
    response = JsonResponse(data={
        'message': "Not found",
        'status': 404
    })
    response.status_code = 404
    return response

urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include(router.urls)),
    path('items_description/<int:pk>', item_description_detail),  
]

handler404=custom_404_view