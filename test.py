from monday import MondayClient

client = MondayClient(
    api_key="eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE1NjY2MzQzNywiYWFpIjoxMSwidWlkIjoyMzUxMjk2MywiaWFkIjoiMjAyMi0wNC0yMFQxMzo0MDozNC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTA5NTE3MCwicmduIjoidXNlMSJ9._mZrxMGl_Xo7e075V_IfmhbenxO4HEeNvDBA8_cnMT4",
    # api_version="2024-01",
)

# response = client.users.fetch_users(limit=5, kind="all")
# response = client.versions.fetch_versions()
# response = client.workspaces.fetch_workspaces(
#     state="active",
#     order_by="created_at",
# )
# response = client.workspaces.create_workspace(
#     "test", "open", "test workspace description"
# )
# response = client.workspaces.delete_workspace("123")
# response = client.boards.fetch_boards(
#     # ids=["6313230780"],
#     order_by="created_at",
#     limit=5,
#     board_kind="public",
#     state="deleted",
# )
# response = client.boards.duplicate_board(
#     board_id="6313230780",
#     board_name="123",
#     duplicate_type="duplicate_board_with_pulses_and_updates",
#     workspace_id="345",
#     folder_id="1235667",
# )
# response = client.boards.update_board(
#     board_id="45734",
#     board_attribute="name",
#     new_value="123",
# )
# response = client.boards.create_board(
#     board_name="123",
#     board_kind="public",
# )
# response = client.boards.duplicate_board(
#     board_id="6313230780",
#     board_name="123",
#     workspace_id="345",
#     folder_id="1235667",
#     keep_subscribers=True,
# )
# response = client.boards.archive_board("123")
# response = client.notifications.create_notification(
#     user_id="123",
#     target_id="123",
#     text="123",
#     target_type="project",
# )
# response = client.workspaces.update_workspace(
#     workspace_id="123",
#     attributes='{name:"Marketing team", description: "This workspace is for the marketing team." }',
# )
print(response)
