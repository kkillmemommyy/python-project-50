from gendiff.gendiff import generate_diff


FLAT_JSON_1 = 'tests/fixtures/flat1.json'
FLAT_JSON_2 = 'tests/fixtures/flat2.json'
FLAT_YML_1 = 'tests/fixtures/flat1.yml'
FLAT_YML_2 = 'tests/fixtures/flat2.yml'
FLAT_YAML_1 = 'tests/fixtures/flat1.yaml'
FLAT_YAML_2 = 'tests/fixtures/flat2.yaml'
FLAT_ANSWER = 'tests/fixtures/flat_diff'


def get_expected_text(path):
    with open(path) as answer:
        answer = answer.read()
    return answer


def test_generate_diff():
    assert generate_diff(FLAT_JSON_1, FLAT_JSON_2) == \
           get_expected_text(FLAT_ANSWER)
    assert generate_diff(FLAT_YML_1, FLAT_YML_2) == \
           get_expected_text(FLAT_ANSWER)
    assert generate_diff(FLAT_YAML_1, FLAT_YAML_2) == \
           get_expected_text(FLAT_ANSWER)
    assert generate_diff(FLAT_YML_1, FLAT_YAML_2) == \
           get_expected_text(FLAT_ANSWER)
