from django.db import models
from django.utils import timezone

class Event(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    CLOSED = 'closed'
    PAUSED = 'paused'
    CANCELED = 'canceled'
    
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (CLOSED, 'Closed'),
        (PAUSED, 'Paused'),
        (CANCELED, 'Canceled'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=DRAFT)
    approval_for_publish = models.BooleanField(default=False)

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be after start time.")
        if self.status == self.PUBLISHED and not self.approval_for_publish:
            raise ValidationError("Event cannot be published without approval.")

    def __str__(self):
        return self.name

class Item(models.Model):
    event = models.ForeignKey(Event, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    currency = models.CharField(max_length=10, default='USD')

    def __str__(self):
        return self.name

class Participant(models.Model):
    event = models.ForeignKey(Event, related_name='participants', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Bid(models.Model):
    event = models.ForeignKey(Event, related_name='bids', on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, related_name='bids', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_alternative = models.BooleanField(default=False)

    def __str__(self):
        return f"Bid by {self.participant.name} on {self.event.name}"

class Scenario(models.Model):
    event = models.ForeignKey(Event, related_name='scenarios', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Award(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='awards', on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, related_name='awards', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='awards', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Award for {self.participant.name} on {self.item.name}"

class Attachment(models.Model):
    event = models.ForeignKey(Event, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.event.name}"

class Template(models.Model):
    name = models.CharField(max_length=255)
    rules = models.JSONField()

    def __str__(self):
        return self.name

class EventRule(models.Model):
    event = models.ForeignKey(Event, related_name='rules', on_delete=models.CASCADE)
    rule_name = models.CharField(max_length=255)
    rule_value = models.CharField(max_length=255)

    def __str__(self):
        return f"Rule for {self.event.name}"

class EventLog(models.Model):
    event = models.ForeignKey(Event, related_name='logs', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.event.name}"
