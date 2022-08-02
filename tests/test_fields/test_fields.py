import pytest


@pytest.mark.django_db()
def test_field_query(client_query):
    response = client_query(
        """
        query {
            test
        }
        """,
    )
    assert response['data']['test'] == 'OK'


@pytest.mark.django_db()
def test_login_required_field_query(client_query, user_fixture):
    response = client_query(
        """
            query {
                loginRequiredTest
            }
        """,
        user=user_fixture,
    )
    assert response['data']['loginRequiredTest'] == 'OK'


@pytest.mark.django_db()
def test_login_required_field_query_without_user(client_query):
    response = client_query(
        """
        query {
            loginRequiredTest
        }
        """,
    )
    assert response['errors'][0]['message'] == (
        'You do not have permission to perform this action'
    )
