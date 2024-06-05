from unittest.mock import MagicMock

import pytest  # type: ignore

from monday.resources.workspaces import WorkspaceResource

# Sample data for use in tests
WORKSPACE_ID = "123"
USER_IDS = ["456", "789"]
TEAM_IDS = ["101", "202"]
ATTRIBUTES = '{"name": "New Workspace", "description": "A new workspace description"}'
NEW_WORKSPACE_DATA = {
    "name": "Test Workspace",
    "kind": "open",
    "description": "This is a test workspace.",
}


@pytest.mark.parametrize(
    "workspace_id, user_ids, kind, expected_call",
    [
        ("123", ["456"], "subscriber", {"id": "123"}),
        ("123", "456", "owner", {"id": "123"}),
        ("123", ["456", "789"], "subscriber", {"id": "123"}),
    ],
    ids=["single_user", "user_as_str", "multiple_users"],
)
def test_add_users_to_workspace(workspace_id, user_ids, kind, expected_call):
    # Arrange
    resource = WorkspaceResource()
    resource.client = MagicMock()
    resource.client.execute.return_value = expected_call

    # Act
    result = resource.add_users_to_workspace(workspace_id, user_ids, kind)

    # Assert
    resource.client.execute.assert_called_once()
    assert result == expected_call


@pytest.mark.parametrize(
    "workspace_id, team_ids, kind, expected_call",
    [
        ("123", ["101"], "subscriber", {"id": "123"}),
        ("123", "101", "owner", {"id": "123"}),
        ("123", ["101", "202"], "subscriber", {"id": "123"}),
    ],
    ids=["single_team", "team_as_str", "multiple_teams"],
)
def test_add_teams_to_workspace(workspace_id, team_ids, kind, expected_call):
    # Arrange
    resource = WorkspaceResource()
    resource.client = MagicMock()
    resource.client.execute.return_value = expected_call

    # Act
    result = resource.add_teams_to_workspace(workspace_id, team_ids, kind)

    # Assert
    resource.client.execute.assert_called_once()
    assert result == expected_call


@pytest.mark.parametrize(
    "workspace_id, user_ids, expected_call",
    [
        ("123", ["456"], {"id": "123"}),
        ("123", "456", {"id": "123"}),
        ("123", ["456", "789"], {"id": "123"}),
    ],
    ids=["single_user", "user_as_str", "multiple_users"],
)
def test_delete_users_from_workspace(workspace_id, user_ids, expected_call):
    # Arrange
    resource = WorkspaceResource()
    resource.client = MagicMock()
    resource.client.execute.return_value = expected_call

    # Act
    result = resource.delete_users_from_workspace(workspace_id, user_ids)

    # Assert
    resource.client.execute.assert_called_once()
    assert result == expected_call


@pytest.mark.parametrize(
    "workspace_id, team_ids, expected_call",
    [
        ("123", ["101"], {"id": "123"}),
        ("123", "101", {"id": "123"}),
        ("123", ["101", "202"], {"id": "123"}),
    ],
    ids=["single_team", "team_as_str", "multiple_teams"],
)
def test_delete_teams_from_workspace(workspace_id, team_ids, expected_call):
    # Arrange
    resource = WorkspaceResource()
    resource.client = MagicMock()
    resource.client.execute.return_value = expected_call

    # Act
    result = resource.delete_teams_from_workspace(workspace_id, team_ids)

    # Assert
    resource.client.execute.assert_called_once()
    assert result == expected_call


@pytest.mark.parametrize(
    "name, kind, description, expected_call",
    [
        ("Test Workspace", "open", "A test workspace.", {"id": "new"}),
        ("Another Workspace", "closed", "", {"id": "newer"}),
    ],
    ids=["with_description", "without_description"],
)
def test_create_workspace(name, kind, description, expected_call):
    # Arrange
    resource = WorkspaceResource()
    resource.client = MagicMock()
    resource.client.execute.return_value = expected_call

    # Act
    result = resource.create_workspace(name, kind, description)

    # Assert
    resource.client.execute.assert_called_once()
    assert result == expected_call


@pytest.mark.parametrize(
    "workspace_id, attributes, expected_call",
    [
        (
            "123",
            '{"name": "Updated Workspace", "description": "Updated description"}',
            {"id": "123"},
        ),
    ],
    ids=["update_attributes"],
)
def test_update_workspace(workspace_id, attributes, expected_call):
    # Arrange
    resource = WorkspaceResource()
    resource.client = MagicMock()
    resource.client.execute.return_value = expected_call

    # Act
    result = resource.update_workspace(workspace_id, attributes)

    # Assert
    resource.client.execute.assert_called_once()
    assert result == expected_call


@pytest.mark.parametrize(
    "workspace_id, expected_call",
    [
        ("123", {"id": "123"}),
    ],
    ids=["delete_workspace"],
)
def test_delete_workspace(workspace_id, expected_call):
    # Arrange
    resource = WorkspaceResource()
    resource.client = MagicMock()
    resource.client.execute.return_value = expected_call

    # Act
    result = resource.delete_workspace(workspace_id)

    # Assert
    resource.client.execute.assert_called_once()
    assert result == expected_call


# Additional tests should be created following the same pattern for fetch_workspaces method,
# covering various combinations of arguments and their impacts on the generated query,
# as well as handling of different response scenarios from the client.execute method.
