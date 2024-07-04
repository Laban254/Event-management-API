from rest_framework import serializers
from .models import Event, Item, Participant, Bid, Scenario, Award, Attachment, Template, EventRule, EventLog

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class EventRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRule
        fields = '__all__'

class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
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
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("End time must be after start time.")
        if data['status'] == Event.PUBLISHED and not data.get('approval_for_publish', False):
            raise serializers.ValidationError("Event cannot be published without approval.")
        return data
