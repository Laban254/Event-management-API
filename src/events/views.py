from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event, Item, Participant, Bid, Scenario, Award, Attachment, Template, EventRule, EventLog
from .serializers import EventSerializer, ItemSerializer, ParticipantSerializer, BidSerializer, ScenarioSerializer, AwardSerializer, AttachmentSerializer, TemplateSerializer, EventRuleSerializer, EventLogSerializer
from .permissions import IsEventOwnerOrReadOnly

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsEventOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'start_time', 'end_time']

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        event = self.get_object()
        event.status = Event.PUBLISHED
        event.save()
        EventLog.objects.create(event=event, message='Event published')
        return Response({'status': 'Event published'})

    @action(detail=True, methods=['post'])
    def republish(self, request, pk=None):
        event = self.get_object()
        event.status = Event.PUBLISHED
        event.save()
        EventLog.objects.create(event=event, message='Event republished')
        return Response({'status': 'Event republished'})

    @action(detail=True, methods=['post'])
    def lock(self, request, pk=None):
        event = self.get_object()
        event.approval_for_publish = True
        event.save()
        EventLog.objects.create(event=event, message='Event locked')
        return Response({'status': 'Event locked'})

    @action(detail=True, methods=['post'])
    def unlock(self, request, pk=None):
        event = self.get_object()
        event.approval_for_publish = False
        event.save()
        EventLog.objects.create(event=event, message='Event unlocked')
        return Response({'status': 'Event unlocked'})

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        event = self.get_object()
        event.status = Event.CANCELED
        event.save()
        EventLog.objects.create(event=event, message='Event canceled')
        return Response({'status': 'Event canceled'})

    @action(detail=True, methods=['post'])
    def pause(self, request, pk=None):
        event = self.get_object()
        event.status = Event.PAUSED
        event.save()
        EventLog.objects.create(event=event, message='Event paused')
        return Response({'status': 'Event paused'})

    @action(detail=True, methods=['post'])
    def resume(self, request, pk=None):
        event = self.get_object()
        event.status = Event.PUBLISHED
        event.save()
        EventLog.objects.create(event=event, message='Event resumed')
        return Response({'status': 'Event resumed'})

    @action(detail=True, methods=['post'])
    def stop(self, request, pk=None):
        event = self.get_object()
        event.status = Event.CLOSED
        event.save()
        EventLog.objects.create(event=event, message='Event stopped')
        return Response({'status': 'Event stopped'})

    @action(detail=True, methods=['post'])
    def reopen(self, request, pk=None):
        event = self.get_object()
        event.status = Event.PUBLISHED
        event.save()
        EventLog.objects.create(event=event, message='Event reopened')
        return Response({'status': 'Event reopened'})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class EventRuleViewSet(viewsets.ModelViewSet):
    queryset = EventRule.objects.all()
    serializer_class = EventRuleSerializer

class EventLogViewSet(viewsets.ModelViewSet):
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer
