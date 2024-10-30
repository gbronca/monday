import os

from dotenv import load_dotenv

from src.monday import MondayClient

load_dotenv()

API_KEY: str = os.getenv("MONDAY_API_KEY", "key")
client = MondayClient(api_key=API_KEY)

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
# response = client.workspaces.delete_users_from_workspace("123", ["123", "345"])
# response = client.columns.fetch_columns(
#     board_ids="6463935543",
#     types="text",
#     # column_ids="short_text__1",
# )
# response = client.workspaces.fetch_workspaces(
#     ids="684056", kind="open", state="active", order_by="created_at", limit=5, page=1
# )
# response = client.workspaces.fetch_workspaces(
#     state="archived",
#     limit=5,
#     page=1,
# )
# response = client.workspaces.update_workspace(
#     workspace_id="123",
#     name="name",
#     kind="open",
#     description="description",
# )
# print(response)


# response = client.webhooks.fetch_webhooks(board_id="6463935543")
# response = client.versions.fetch_versions()


# response = client.workspaces.fetch_workspaces()
# print(response)


async def tests():
    # response = await client.workspaces.fetch_workspaces()
    # response = await client.webhooks.fetch_webhooks(board_id="6463935543")
    # response = await client.users.fetch_users()
    # response = await client.updates.fetch_updates(ids=[3367775030, 3367665206])
    # response = await client.updates.create_update(123456, "dsfgkjlgdfgflg", 565469675)
    # response = await client.updates.like_update(357394857)
    # response = await client.
    # response = await client.workspaces.fetch_workspaces(page=2, all_fields=True)
    # response = await client.columns.fetch_columns(
    #     board_ids="6463935543",
    #     types="status",
    # )
    # response = await client.workspaces.add_users_to_workspace(
    #     workspace_id="1234456", user_ids=["123", "345"], kind="subscriber"
    # )
    response = await client.groups.fetch_groups(
        board_ids=["120818187", "7392166160"],
        group_ids=["feedback", "topics"],
    )
    print(response)


import asyncio

asyncio.run(tests())
