from urllib.parse import quote

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_get_activities_returns_known_activity():
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in data
    assert "participants" in data[expected_activity]
    assert isinstance(data[expected_activity]["participants"], list)


def test_signup_activity_adds_participant():
    # Arrange
    activity = "Chess Club"
    email = "test_signup_student@mergington.edu"
    url = f"/activities/{quote(activity)}/signup?email={quote(email)}"

    # Act
    response = client.post(url)
    data_after = client.get("/activities").json()

    # Assert
    assert response.status_code == 200
    assert f"Signed up {email} for {activity}" in response.json()["message"]
    assert email in data_after[activity]["participants"]

    # Cleanup
    client.delete(f"/activities/{quote(activity)}/participants?email={quote(email)}")


def test_signup_duplicate_participant_returns_400():
    # Arrange
    activity = "Chess Club"
    email = "test_duplicate_student@mergington.edu"
    signup_url = f"/activities/{quote(activity)}/signup?email={quote(email)}"
    cleanup_url = f"/activities/{quote(activity)}/participants?email={quote(email)}"

    client.delete(cleanup_url)
    response_first = client.post(signup_url)

    try:
        # Act
        response_second = client.post(signup_url)

        # Assert
        assert response_first.status_code == 200
        assert response_second.status_code == 400
        assert response_second.json()["detail"] == "Student already signed up for this activity"
    finally:
        client.delete(cleanup_url)


def test_remove_participant_from_activity():
    # Arrange
    activity = "Science Club"
    email = "test_remove_student@mergington.edu"
    signup_url = f"/activities/{quote(activity)}/signup?email={quote(email)}"
    delete_url = f"/activities/{quote(activity)}/participants?email={quote(email)}"

    client.delete(delete_url)
    client.post(signup_url)

    # Act
    response = client.delete(delete_url)
    data_after = client.get("/activities").json()

    # Assert
    assert response.status_code == 200
    assert f"Removed {email} from {activity}" in response.json()["message"]
    assert email not in data_after[activity]["participants"]


def test_remove_nonexistent_participant_returns_404():
    # Arrange
    activity = "Chess Club"
    email = "nonexistent_student@mergington.edu"
    delete_url = f"/activities/{quote(activity)}/participants?email={quote(email)}"

    # Act
    response = client.delete(delete_url)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
