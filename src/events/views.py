from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event, Item, Participant, Bid, Scenario, Award, Attachment, Template, EventRule, EventLog
from .serializers import EventSerializer, ItemSerializer, ParticipantSerializer, BidSerializer, ScenarioSerializer, AwardSerializer, AttachmentSerializer, TemplateSerializer, EventRuleSerializer, EventLogSerializer
from .permissions import IsEventOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser

class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Event instances.

    This ViewSet allows for CRUD operations on Event instances and includes additional actions for specific event statuses.
    
    Methods:
    - list: Get a list of all events.
    - retrieve: Get details of a specific event.
    - create: Create a new event.
    - update: Update an existing event.
    - partial_update: Partially update an existing event.
    - destroy: Delete an event.
    
    Custom Actions:
    - publish: Change the event status to 'published'.
    - republish: Re-publish an event.
    - lock: Lock the event for publication approval.
    - unlock: Unlock the event from publication approval.
    - cancel: Cancel the event.
    - pause: Pause the event.
    - resume: Resume the paused event.
    - stop: Stop the event.
    - reopen: Reopen a closed event.
    
    Example Usage:
    - To publish an event: POST /api/events/{id}/publish/
    - To cancel an event: POST /api/events/{id}/cancel/
    """
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
    """
    ViewSet for managing Item instances.

    This ViewSet allows for CRUD operations on Item instances.
    
    Methods:
    - list: Get a list of all items.
    - retrieve: Get details of a specific item.
    - create: Create a new item.
    - update: Update an existing item.
    - partial_update: Partially update an existing item.
    - destroy: Delete an item.
    
    Example Usage:
    - To create a new item: POST /api/items/
    - To get a list of items: GET /api/items/
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Participant instances.

    This ViewSet allows for CRUD operations on Participant instances.
    
    Methods:
    - list: Get a list of all participants.
    - retrieve: Get details of a specific participant.
    - create: Create a new participant.
    - update: Update an existing participant.
    - partial_update: Partially update an existing participant.
    - destroy: Delete a participant.
    
    Example Usage:
    - To create a new participant: POST /api/participants/
    - To get a list of participants: GET /api/participants/
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class BidViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Bid instances.

    This ViewSet allows for CRUD operations on Bid instances.
    
    Methods:
    - list: Get a list of all bids.
    - retrieve: Get details of a specific bid.
    - create: Create a new bid.
    - update: Update an existing bid.
    - partial_update: Partially update an existing bid.
    - destroy: Delete a bid.
    
    Example Usage:
    - To create a new bid: POST /api/bids/
    - To get a list of bids: GET /api/bids/
    """
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

class ScenarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Scenario instances.

    This ViewSet allows for CRUD operations on Scenario instances.
    
    Methods:
    - list: Get a list of all scenarios.
    - retrieve: Get details of a specific scenario.
    - create: Create a new scenario.
    - update: Update an existing scenario.
    - partial_update: Partially update an existing scenario.
    - destroy: Delete a scenario.
    
    Example Usage:
    - To create a new scenario: POST /api/scenarios/
    - To get a list of scenarios: GET /api/scenarios/
    """
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

class AwardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Award instances.

    This ViewSet allows for CRUD operations on Award instances.
    
    Methods:
    - list: Get a list of all awards.
    - retrieve: Get details of a specific award.
    - create: Create a new award.
    - update: Update an existing award.
    - partial_update: Partially update an existing award.
    - destroy: Delete an award.
    
    Example Usage:
    - To create a new award: POST /api/awards/
    - To get a list of awards: GET /api/awards/
    """
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Attachment instances.

    This ViewSet allows for CRUD operations on Attachment instances.
    
    Methods:
    - list: Get a list of all attachments.
    - retrieve: Get details of a specific attachment.
    - create: Create a new attachment.
    - update: Update an existing attachment.
    - partial_update: Partially update an existing attachment.
    - destroy: Delete an attachment.
    
    Example Usage:
    - To create a new attachment: POST /api/attachments/
    - To get a list of attachments: GET /api/attachments/
    """
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    parser_classes = [MultiPartParser]

class TemplateViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Template instances.

    This ViewSet allows for CRUD operations on Template instances.
    
    Methods:
    - list: Get a list of all templates.
    - retrieve: Get details of a specific template.
    - create: Create a new template.
    - update: Update an existing template.
    - partial_update: Partially update an existing template.
    - destroy: Delete a template.
    
    Example Usage:
    - To create a new template: POST /api/templates/
    - To get a list of templates: GET /api/templates/
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class EventRuleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing EventRule instances.

    This ViewSet allows for CRUD operations on EventRule instances.
    
    Methods:
    - list: Get a list of all event rules.
    - retrieve: Get details of a specific event rule.
    - create: Create a new event rule.
    - update: Update an existing event rule.
    - partial_update: Partially update an existing event rule.
    - destroy: Delete an event rule.
    
    Example Usage:
    - To create a new event rule: POST /api/eventrules/
    - To get a list of event rules: GET /api/eventrules/
    """
    queryset = EventRule.objects.all()
    serializer_class = EventRuleSerializer

class EventLogViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing EventLog instances.

    This ViewSet allows for CRUD operations on EventLog instances.
    
    Methods:
    - list: Get a list of all event logs.
    - retrieve: Get details of a specific event log.
    - create: Create a new event log.
    - update: Update an existing event log.
    - partial_update: Partially update an existing event log.
    - destroy: Delete an event log.
    
    Example Usage:
    - To create a new event log: POST /api/eventlogs/
    - To get a list of event logs: GET /api/eventlogs/
    """
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer
