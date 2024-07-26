from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event, Item, Participant, Bid, Scenario, Award, Attachment, Template, EventRule, EventLog
from .serializers import (
    EventSerializer, ItemSerializer, ParticipantSerializer, BidSerializer, 
    ScenarioSerializer, AwardSerializer, AttachmentSerializer, 
    TemplateSerializer, EventRuleSerializer, EventLogSerializer
)
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsEventOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser
from .schema_extensions import (
    event_viewset_schema, item_viewset_schema, participant_viewset_schema, 
    bid_viewset_schema, scenario_viewset_schema, award_viewset_schema, 
    attachment_viewset_schema, template_viewset_schema, 
    event_rule_viewset_schema, event_log_viewset_schema
)

@event_viewset_schema
class EventViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['Event'])
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsEventOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'owner']

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        event = self.get_object()
        event.status = 'published'
        event.save()
        return Response({'status': 'Event published'})

    @action(detail=True, methods=['post'])
    def republish(self, request, pk=None):
        event = self.get_object()
        event.status = 'republished'
        event.save()
        return Response({'status': 'Event republished'})

    @action(detail=True, methods=['post'])
    def lock(self, request, pk=None):
        event = self.get_object()
        event.status = 'locked'
        event.save()
        return Response({'status': 'Event locked'})

    @action(detail=True, methods=['post'])
    def unlock(self, request, pk=None):
        event = self.get_object()
        event.status = 'unlocked'
        event.save()
        return Response({'status': 'Event unlocked'})

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        event = self.get_object()
        event.status = 'cancelled'
        event.save()
        return Response({'status': 'Event cancelled'})

    @action(detail=True, methods=['post'])
    def pause(self, request, pk=None):
        event = self.get_object()
        event.status = 'paused'
        event.save()
        return Response({'status': 'Event paused'})

    @action(detail=True, methods=['post'])
    def resume(self, request, pk=None):
        event = self.get_object()
        event.status = 'active'
        event.save()
        return Response({'status': 'Event resumed'})

    @action(detail=True, methods=['post'])
    def stop(self, request, pk=None):
        event = self.get_object()
        event.status = 'stopped'
        event.save()
        return Response({'status': 'Event stopped'})

    @action(detail=True, methods=['post'])
    def reopen(self, request, pk=None):
        event = self.get_object()
        event.status = 'reopened'
        event.save()
        return Response({'status': 'Event reopened'})

@item_viewset_schema
class ItemViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['Item'])
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@participant_viewset_schema
class ParticipantViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['Participant'])
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

@bid_viewset_schema
class BidViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['Bid'])
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

@scenario_viewset_schema
class ScenarioViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['Scenario'])
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

@award_viewset_schema
class AwardViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['Award'])
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

@attachment_viewset_schema
class AttachmentViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['Attachment'])
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    parser_classes = [MultiPartParser]

@template_viewset_schema
class TemplateViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['Template'])
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

@event_rule_viewset_schema
class EventRuleViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['EventRule'])
    queryset = EventRule.objects.all()
    serializer_class = EventRuleSerializer

@event_log_viewset_schema
class EventLogViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(tags=['EventLog'])
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer
