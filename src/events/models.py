from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    """
    Represents an event with attributes like name, description, start time, end time,
    status (draft, published, closed, paused, canceled), and approval status for publishing.
    
    Functionality:
    - Core entity for events, encapsulating details and lifecycle status.
    - Manages validation ensuring the start time is before the end time and that events cannot be published without approval.
    
    Example:
    - An event named "Annual Conference" with a start time on July 10, 2024, and end time on July 12, 2024.
    """
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
    owner = models.ForeignKey(User, related_name='event', on_delete=models.CASCADE)
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
    """
    An Item model represents specific items associated with an event, such as supplies or products.
    
    Functionality:
    - Manages items linked to events for resource management purposes.
    
    Example:
    - Items like "Microphones", "Projectors", etc., linked to the "Annual Conference" event to manage resources needed for the event.
    """
    event = models.ForeignKey(Event, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    currency = models.CharField(max_length=10, default='USD')

    def __str__(self):
        return self.name

class Participant(models.Model):
    """
    Participant model represents individuals attending or participating in the event.
    
    Functionality:
    - Manages attendee details and participation in the event.
    
    Example:
    - Participants registered for the "Annual Conference" event could include "John Doe", "Jane Smith", etc.
    """
    event = models.ForeignKey(Event, related_name='participants', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Bid(models.Model):
    """
    Bid model captures bids made by participants for event-related services or products.
    
    Functionality:
    - Facilitates procurement through competitive bidding.
    
    Example:
    - "John Doe" places a bid of $100 for catering services at the "Annual Conference".
    """
    event = models.ForeignKey(Event, related_name='bids', on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, related_name='bids', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_alternative = models.BooleanField(default=False)

    def __str__(self):
        return f"Bid by {self.participant.name} on {self.event.name}"

class Scenario(models.Model):
    """
    Scenario model represents predefined situations or scenarios within an event context.
    
    Functionality:
    - Helps event planners prepare contingencies and responses.
    - Provides a framework for managing unexpected or planned situations during an event.
    
    Example:
    - For an "Annual Tech Conference" event, a scenario could be "Keynote Speaker Delayed".
    - This scenario would include a detailed description of the actions to take, such as notifying attendees,
      adjusting the schedule, and preparing backup activities or speakers.
    """
    event = models.ForeignKey(Event, related_name='scenarios', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Award(models.Model):
    """
    Award model signifies awards given to participants based on predefined scenarios or criteria within an event.
    
    Functionality:
    - Recognizes outstanding contributions or achievements during the event.
    
    Example:
    - "Best Speaker Award" given to "Jane Smith" at the "Annual Conference".
    """
    scenario = models.ForeignKey(Scenario, related_name='awards', on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, related_name='awards', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='awards', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Award for {self.participant.name} on {self.item.name}"

class Attachment(models.Model):
    """
    Attachment model includes files or documents linked to an event.
    
    Functionality:
    - Provides essential information and resources for event stakeholders.
    
    Example:
    - Attachments like "Event Schedule PDF", "Speaker Bios", etc., for the "Annual Conference".
    """
    event = models.ForeignKey(Event, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.event.name}"

class Template(models.Model):
    """
    Template model represents reusable configurations or templates used in event management.
    
    Functionality:
    - Ensures consistency and efficiency in event planning.
    
    Example:
    - A "Conference Schedule Template" used to create structured schedules for events like the "Annual Conference".
    """
    name = models.CharField(max_length=255)
    rules = models.JSONField()

    def __str__(self):
        return self.name

class EventRule(models.Model):
    """
    EventRule model defines specific rules or conditions applicable to an event.
    
    Functionality:
    - Manages event capacity, restrictions, and compliance with venue limitations.
    
    Example:
    - A rule specifying "Maximum Attendance: 500" for the "Annual Conference".
    """
    event = models.ForeignKey(Event, related_name='rules', on_delete=models.CASCADE)
    rule_name = models.CharField(max_length=255)
    rule_value = models.CharField(max_length=255)

    def __str__(self):
        return f"Rule for {self.event.name}"

class EventLog(models.Model):
    """
    EventLog model records significant actions or events related to an event.
    
    Functionality:
    - Provides a chronological record of event activities.
    
    Example:
    - Logs documenting actions such as "Event Created", "Participant Registered", etc., for the "Annual Conference".
    """
    event = models.ForeignKey(Event, related_name='logs', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.event.name}"
