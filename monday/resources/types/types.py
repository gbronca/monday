from typing import Literal

BoardAttributes = Literal["communication", "description", "name"]
BoardKind = Literal["private", "public", "share"]
BoardSubscriberKind = Literal["owner", "subscriber"]
DuplicateBoardType = Literal[
    "duplicate_board_with_structure",
    "duplicate_board_with_pulses",
    "duplicate_board_with_pulses_and_updates",
]
NotificationTargetType = Literal["Project", "Post"]
OrderBy = Literal["created_at", "used_at"]
State = Literal["active", "all", "archived", "deleted"]
SubscriberKind = Literal["owner", "subscriber"]
UserKind = Literal["all", "non_guests", "guests", "non_pending"]
WorkspaceKind = Literal["open", "closed"]
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
FolderColor = Literal[
    "AQUAMARINE",
    "BRIGHT_BLUE",
    "BRIGHT_GREEN",
    "CHILI_BLUE",
    "DARK_ORANGE",
    "DARK_PURPLE",
    "DARK_RED",
    "DONE_GREEN",
    "INDIGO",
    "LIPSTICK",
    "PURPLE",
    "SOFIA_PINK",
    "STUCK_RED",
    "SUNSET",
    "WORKING_ORANGE",
]
GroupColor = Literal[
    "#ff5ac4",
    "#ff158a",
    "#bb3354",
    "#e2445c",
    "#ff642e",
    "#fdab3d",
    "#ffcb00",
    "#cab641",
    "#9cd326",
    "#00c875",
    "#037f4c",
    "#0086c0",
    "#579bfc",
    "#66ccff",
    "#a25ddc",
    "#784dl",
    "#7f5347",
    "#c4c4c4",
    "#808080",
]
