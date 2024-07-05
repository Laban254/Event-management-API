from rest_framework import serializers
from .models import Event, Item, Participant, Bid, Scenario, Award, Attachment, Template, EventRule, EventLog

class ItemSerializer(serializers.ModelSerializer):
    """Item Serializer"""
    
    class Meta:
        model = Item
        fields = ['id', 'event', 'name', 'description', 'quantity', 'currency']
        extra_kwargs = {
            'event': {'help_text': 'The event to which the item belongs'},
            'name': {'help_text': 'Name of the item'},
            'description': {'help_text': 'Description of the item'},
            'quantity': {'help_text': 'Quantity of the item'},
            'currency': {'help_text': 'Currency in which the item is priced'}
        }

class ParticipantSerializer(serializers.ModelSerializer):
    """Participant Serializer"""
    
    class Meta:
        model = Participant
        fields = ['id', 'event', 'name', 'contact_info', 'blocked']
        extra_kwargs = {
            'event': {'help_text': 'The event in which the participant is involved'},
            'name': {'help_text': 'Name of the participant'},
            'contact_info': {'help_text': 'Contact information of the participant'},
            'blocked': {'help_text': 'Indicates if the participant is blocked'}
        }

class BidSerializer(serializers.ModelSerializer):
    """Bid Serializer"""
    
    class Meta:
        model = Bid
        fields = ['id', 'event', 'participant', 'amount', 'timestamp', 'is_alternative']
        extra_kwargs = {
            'event': {'help_text': 'The event for which the bid is placed'},
            'participant': {'help_text': 'The participant who placed the bid'},
            'amount': {'help_text': 'The bid amount'},
            'timestamp': {'help_text': 'Time when the bid was placed'},
            'is_alternative': {'help_text': 'Indicates if this is an alternative bid'}
        }

class ScenarioSerializer(serializers.ModelSerializer):
    """Scenario Serializer"""
    
    class Meta:
        model = Scenario
        fields = ['id', 'event', 'name', 'description']
        extra_kwargs = {
            'event': {'help_text': 'The event to which the scenario applies'},
            'name': {'help_text': 'Name of the scenario'},
            'description': {'help_text': 'Description of the scenario'}
        }

class AwardSerializer(serializers.ModelSerializer):
    """Award Serializer"""
    
    class Meta:
        model = Award
        fields = ['id', 'scenario', 'participant', 'item', 'quantity', 'amount']
        extra_kwargs = {
            'scenario': {'help_text': 'The scenario for which the award is given'},
            'participant': {'help_text': 'The participant receiving the award'},
            'item': {'help_text': 'The item given as an award'},
            'quantity': {'help_text': 'Quantity of the award'},
            'amount': {'help_text': 'Monetary value of the award'}
        }

class AttachmentSerializer(serializers.ModelSerializer):
    """Attachment Serializer"""
    
    class Meta:
        model = Attachment
        fields = ['id', 'event', 'file', 'uploaded_at']
        extra_kwargs = {
            'event': {'help_text': 'The event to which the attachment belongs'},
            'file': {'help_text': 'The file attached to the event'},
            'uploaded_at': {'help_text': 'Time when the file was uploaded'}
        }

class TemplateSerializer(serializers.ModelSerializer):
    """Template Serializer"""
    
    class Meta:
        model = Template
        fields = ['id', 'name', 'rules']
        extra_kwargs = {
            'name': {'help_text': 'Name of the template'},
            'rules': {'help_text': 'JSON field containing the rules of the template'}
        }

class EventRuleSerializer(serializers.ModelSerializer):
    """Event Rule Serializer"""
    
    class Meta:
        model = EventRule
        fields = ['id', 'event', 'rule_name', 'rule_value']
        extra_kwargs = {
            'event': {'help_text': 'The event to which the rule applies'},
            'rule_name': {'help_text': 'Name of the rule'},
            'rule_value': {'help_text': 'Value of the rule'}
        }

class EventLogSerializer(serializers.ModelSerializer):
    """Event Log Serializer"""
    
    class Meta:
        model = EventLog
        fields = ['id', 'event', 'message', 'timestamp']
        extra_kwargs = {
            'event': {'help_text': 'The event to which the log belongs'},
            'message': {'help_text': 'Log message'},
            'timestamp': {'help_text': 'Time when the log was created'}
        }

class EventSerializer(serializers.ModelSerializer):
    """Event Serializer"""
    
    items = ItemSerializer(many=True, read_only=True)
    participants = ParticipantSerializer(many=True, read_only=True)
    bids = BidSerializer(many=True, read_only=True)
    scenarios = ScenarioSerializer(many=True, read_only=True)
    awards = AwardSerializer(many=True, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)
    rules = EventRuleSerializer(many=True, read_only=True)
    logs = EventLogSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'start_time', 'end_time', 'owner', 'status', 'approval_for_publish', 
                  'items', 'participants', 'bids', 'scenarios', 'awards', 'attachments', 'rules', 'logs']
        extra_kwargs = {
            'name': {'help_text': 'Name of the event'},
            'description': {'help_text': 'Description of the event'},
            'start_time': {'help_text': 'Event start time'},
            'end_time': {'help_text': 'Event end time'},
            'owner': {'help_text': 'Owner of the event'},
            'status': {'help_text': 'Current status of the event'},
            'approval_for_publish': {'help_text': 'Approval status for publishing the event'}
        }

    def validate(self, data):
        """
        Validates the Event data.
        Ensures the end time is after the start time and the event cannot be published without approval.
        """
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("End time must be after start time.")
        if data['status'] == Event.PUBLISHED and not data.get('approval_for_publish', False):
            raise serializers.ValidationError("Event cannot be published without approval.")
        return data
