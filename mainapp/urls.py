from rest_framework.routers import DefaultRouter as DR

from mainapp.views import (
    IphoneView,
)
from mainapp.views import (
    MacbookView,
)
from mainapp.views import (
    AirpodsView,
)
router = DR()

router.register('iphone', IphoneView)

router.register('macbook', MacbookView)

router.register('airpods', AirpodsView)

urlpatterns = []

urlpatterns += router.urls