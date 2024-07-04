from rest_framework import serializers
from .models import Event, Item, Participant, Bid, Scenario, Award, Attachment, Template, EventRule, EventLog

class ItemSerializer(serializers.ModelSerializer):
    """
    This serializer handles the conversion of Item instances to JSON format and vice versa.
    """
    class Meta:
        model = Item
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    """
    This serializer manages the serialization and deserialization of Participant instances.
    """
    class Meta:
        model = Participant
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    """
    This serializer converts Bid instances to JSON format and handles incoming JSON data.
    """
    class Meta:
        model = Bid
        fields = '__all__'

class ScenarioSerializer(serializers.ModelSerializer):
    """
    This serializer handles the serialization of Scenario instances and deserialization of JSON data.
    """
    class Meta:
        model = Scenario
        fields = '__all__'

class AwardSerializer(serializers.ModelSerializer):
    """
    This serializer manages the conversion of Award instances to JSON format and vice versa.
    """
    class Meta:
        model = Award
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    """
    This serializer handles the serialization and deserialization of Attachment instances.
    """
    class Meta:
        model = Attachment
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    """
    This serializer manages the conversion of Template instances to JSON format and vice versa.
    """
    class Meta:
        model = Template
        fields = '__all__'

class EventRuleSerializer(serializers.ModelSerializer):
    """ 
    This serializer handles the serialization and deserialization of EventRule instances.
    """
    class Meta:
        model = EventRule
        fields = '__all__'

class EventLogSerializer(serializers.ModelSerializer):
    """
    This serializer manages the conversion of EventLog instances to JSON format and vice versa.
    """
    class Meta:
        model = EventLog
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    """
    This serializer includes nested serializers for related models, converting Event instances
    and their related data to JSON format.
    """
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
        fields = '__all__'

    def validate(self, data):
        """
        Validates the Event data ensuring:
        - The end time is after the start time.
        - The event cannot be published without approval.
        
        Raises:
        - ValidationError: If the end time is not after the start time or if an unapproved event is being published.
        """
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("End time must be after start time.")
        if data['status'] == Event.PUBLISHED and not data.get('approval_for_publish', False):
            raise serializers.ValidationError("Event cannot be published without approval.")
        return data
