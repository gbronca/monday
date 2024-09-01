from typing import Literal

ColumnType = Literal[
    "auto_number",
    "board_relation",
    "button",
    "checkbox",
    "color_picker",
    "country",
    "creation_log",
    "date",
    "dependency",
    "doc",
    "dropdown",
    "email",
    "file",
    "formula",
    "hour",
    "item_assignees",
    "item_id",
    "last_updated",
    "link",
    "location",
    "long_text",
    "mirror",
    "name",
    "numbers",
    "people",
    "phone",
    "progress",
    "rating",
    "status",
    "subtasks",
    "tags",
    "team",
    "text",
    "timeline",
    "time_tracking",
    "vote",
    "week",
    "world_clock",
    "unsupported",
]

ORDER_BY = Literal["created_at", "used_at"]

State = Literal["active", "all", "archived", "deleted"]
SubscriberKind = Literal["owner", "subscriber"]
WorkspaceKind = Literal["open", "closed"]
UserKind = Literal["all", "non_guests", "guests", "non_pending"]
