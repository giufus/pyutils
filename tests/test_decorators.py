from unittest import TestCase
import decorators


class Test(TestCase):
    def test_allows_only(self):
        # given
        _actual = {
            'queryStringParameters': {
                'foo': 'a',
                'bar': 'b',
                'baz': 'c',
            }
        }

        _expected = {
            'queryStringParameters': {
                'foo': 'a',
                'bar': 'b',
            }
        }

        # when
        _result = sample_decorated_function(_actual)

        # then
        self.assertDictEqual(_result, _expected, 'removed unwanted query params')
        print(_result)


@decorators.allows_only({'foo', 'bar'})
def sample_decorated_function(event):
    return event
