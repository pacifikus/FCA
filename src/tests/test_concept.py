from unittest import TestCase

from parameterized import parameterized

from src.fca.context import Concept


class ConceptTestCase(TestCase):
    """
    Concept class checks
    """

    @parameterized.expand([
        [[Concept(['girl'], ['female', 'juvenile']), Concept(['girl'], ['female', 'juvenile'])], True],
        [[Concept(['girl'], ['female', 'juvenile']), Concept(['girl'], ['female'])], False],
        [[Concept(['boy'], ['human']), Concept(['girl'], ['human'])], False],
    ])
    def test_eq(self, concepts, expected):
        """
        Test for the eq operator
        """
        result = concepts[0] == concepts[1]
        self.assertEqual(result, expected)
