import pytest


@pytest.mark.django_db()
def test_mutation(client_query):
    response = client_query(
        '''
        mutation {
            mutation(input: {test: "test"}) {
                message
            }
        }
        '''
    )
    assert response['data']['mutation']['message'] == 'OK'


@pytest.mark.django_db()
def test_login_required_mutation(client_query, user_fixture):
    response = client_query(
        '''
        mutation {
            loginRequired(input: {test: "test"}) {
                message
            }
        }
        ''',
        user=user_fixture
    )
    assert response['data']['loginRequired']['message'] == 'OK'


@pytest.mark.django_db()
def test_login_required_mutation(client_query, user_fixture):
    response = client_query(
        '''
        mutation {
            loginRequired(input: {test: "test"}) {
                message
            }
        }
        '''
    )
    assert response['errors'][0]['message'] == 'You do not have permission to perform this action'
