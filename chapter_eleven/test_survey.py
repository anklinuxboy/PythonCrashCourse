import pytest

from survey import AnonymousSurvey

@pytest.fixture
def lang_survey():
    """A survey that will be available to all test functions"""
    question = "What language you learned?"
    lang_survey = AnonymousSurvey(question)
    return lang_survey

def test_store_single_response(lang_survey):
    """Test that a single response is stored properly"""
    lang_survey.store_response('English')
    assert 'English' in lang_survey.responses

def test_store_multiple_responses(lang_survey):
    """Test that multiple responses are stored"""
    responses = ['Kotlin', 'Python', 'Rust']

    for response in responses:
        lang_survey.store_response(response)

    for response in responses:
        assert response in lang_survey.responses