from gendiff.gendiff import generate_diff


FLAT_JSON_1 = 'tests/fixtures/flat1.json'
FLAT_JSON_2 = 'tests/fixtures/flat2.json'
FLAT_ANSWER = 'tests/fixtures/flat_diff'


def get_expected_text(path):
    with open(path) as answer:
        answer = answer.read()
    return answer


def test_generate_diff():
    assert generate_diff(FLAT_JSON_1, FLAT_JSON_2) == \
           get_expected_text(FLAT_ANSWER)
