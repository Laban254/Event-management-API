from drf_spectacular.utils import extend_schema_view, extend_schema

event_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all events",
        description="Return a list of all events in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve an event",
        description="Get details of a specific event by ID.",
    ),
    create=extend_schema(
        summary="Create a new event",
        description="Create a new event instance.",
    ),
    update=extend_schema(
        summary="Update an event",
        description="Update an existing event instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update an event",
        description="Partially update an existing event instance.",
    ),
    destroy=extend_schema(
        summary="Delete an event",
        description="Delete an existing event instance.",
    ),
    publish=extend_schema(
        summary="Publish an event",
        description="Change the event status to 'published'.",
    ),
    republish=extend_schema(
        summary="Re-publish an event",
        description="Re-publish an event.",
    ),
    lock=extend_schema(
        summary="Lock the event",
        description="Lock the event for publication approval.",
    ),
    unlock=extend_schema(
        summary="Unlock the event",
        description="Unlock the event from publication approval.",
    ),
    cancel=extend_schema(
        summary="Cancel an event",
        description="Cancel the event.",
    ),
    pause=extend_schema(
        summary="Pause an event",
        description="Pause the event.",
    ),
    resume=extend_schema(
        summary="Resume an event",
        description="Resume the paused event.",
    ),
    stop=extend_schema(
        summary="Stop an event",
        description="Stop the event.",
    ),
    reopen=extend_schema(
        summary="Reopen an event",
        description="Reopen a closed event.",
    ),
)

item_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all items",
        description="Return a list of all items in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve an item",
        description="Get details of a specific item by ID.",
    ),
    create=extend_schema(
        summary="Create a new item",
        description="Create a new item instance.",
    ),
    update=extend_schema(
        summary="Update an item",
        description="Update an existing item instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update an item",
        description="Partially update an existing item instance.",
    ),
    destroy=extend_schema(
        summary="Delete an item",
        description="Delete an existing item instance.",
    ),
)

participant_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all participants",
        description="Return a list of all participants in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a participant",
        description="Get details of a specific participant by ID.",
    ),
    create=extend_schema(
        summary="Create a new participant",
        description="Create a new participant instance.",
    ),
    update=extend_schema(
        summary="Update a participant",
        description="Update an existing participant instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update a participant",
        description="Partially update an existing participant instance.",
    ),
    destroy=extend_schema(
        summary="Delete a participant",
        description="Delete an existing participant instance.",
    ),
)

bid_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all bids",
        description="Return a list of all bids in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a bid",
        description="Get details of a specific bid by ID.",
    ),
    create=extend_schema(
        summary="Create a new bid",
        description="Create a new bid instance.",
    ),
    update=extend_schema(
        summary="Update a bid",
        description="Update an existing bid instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update a bid",
        description="Partially update an existing bid instance.",
    ),
    destroy=extend_schema(
        summary="Delete a bid",
        description="Delete an existing bid instance.",
    ),
)

scenario_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all scenarios",
        description="Return a list of all scenarios in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a scenario",
        description="Get details of a specific scenario by ID.",
    ),
    create=extend_schema(
        summary="Create a new scenario",
        description="Create a new scenario instance.",
    ),
    update=extend_schema(
        summary="Update a scenario",
        description="Update an existing scenario instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update a scenario",
        description="Partially update an existing scenario instance.",
    ),
    destroy=extend_schema(
        summary="Delete a scenario",
        description="Delete an existing scenario instance.",
    ),
)

award_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all awards",
        description="Return a list of all awards in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve an award",
        description="Get details of a specific award by ID.",
    ),
    create=extend_schema(
        summary="Create a new award",
        description="Create a new award instance.",
    ),
    update=extend_schema(
        summary="Update an award",
        description="Update an existing award instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update an award",
        description="Partially update an existing award instance.",
    ),
    destroy=extend_schema(
        summary="Delete an award",
        description="Delete an existing award instance.",
    ),
)

attachment_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all attachments",
        description="Return a list of all attachments in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve an attachment",
        description="Get details of a specific attachment by ID.",
    ),
    create=extend_schema(
        summary="Create a new attachment",
        description="Create a new attachment instance.",
    ),
    update=extend_schema(
        summary="Update an attachment",
        description="Update an existing attachment instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update an attachment",
        description="Partially update an existing attachment instance.",
    ),
    destroy=extend_schema(
        summary="Delete an attachment",
        description="Delete an existing attachment instance.",
    ),
)

template_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all templates",
        description="Return a list of all templates in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a template",
        description="Get details of a specific template by ID.",
    ),
    create=extend_schema(
        summary="Create a new template",
        description="Create a new template instance.",
    ),
    update=extend_schema(
        summary="Update a template",
        description="Update an existing template instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update a template",
        description="Partially update an existing template instance.",
    ),
    destroy=extend_schema(
        summary="Delete a template",
        description="Delete an existing template instance.",
    ),
)

event_rule_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all event rules",
        description="Return a list of all event rules in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve an event rule",
        description="Get details of a specific event rule by ID.",
    ),
    create=extend_schema(
        summary="Create a new event rule",
        description="Create a new event rule instance.",
    ),
    update=extend_schema(
        summary="Update an event rule",
        description="Update an existing event rule instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update an event rule",
        description="Partially update an existing event rule instance.",
    ),
    destroy=extend_schema(
        summary="Delete an event rule",
        description="Delete an existing event rule instance.",
    ),
)

event_log_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all event logs",
        description="Return a list of all event logs in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve an event log",
        description="Get details of a specific event log by ID.",
    ),
    create=extend_schema(
        summary="Create a new event log",
        description="Create a new event log instance.",
    ),
    update=extend_schema(
        summary="Update an event log",
        description="Update an existing event log instance.",
    ),
    partial_update=extend_schema(
        summary="Partially update an event log",
        description="Partially update an existing event log instance.",
    ),
    destroy=extend_schema(
        summary="Delete an event log",
        description="Delete an existing event log instance.",
    ),
)
