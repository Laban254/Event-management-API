from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ItemViewSet, ParticipantViewSet, BidViewSet, ScenarioViewSet, AwardViewSet, AttachmentViewSet, TemplateViewSet, EventRuleViewSet, EventLogViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'items', ItemViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'bids', BidViewSet)
router.register(r'scenarios', ScenarioViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'templates', TemplateViewSet)
router.register(r'rules', EventRuleViewSet)
router.register(r'logs', EventLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
