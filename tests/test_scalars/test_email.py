import pytest


@pytest.mark.django_db()
def test_email_mutation(client_query):
    response = client_query(
        """
        mutation {
            email(input: {email: "test@test.com"}) {
                message
            }
        }
        """,
    )
    assert response['data']['email']['message'] == 'OK'


@pytest.mark.django_db()
def test_login_required_mutation_without_user(client_query):
    response = client_query(
        """
        mutation {
            email(input: {email: "test@."}) {
                message
            }
        }
        """,
    )
    assert response['errors'][0]['message'] == 'Invalid email address.'
