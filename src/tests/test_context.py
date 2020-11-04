from src.fca.context import Context
from unittest import TestCase
from parameterized import parameterized


class ContextTestCase(TestCase):
    """
    Context class checks
    """
    def setUp(self):
        G = ['girl', 'woman', 'boy', 'man']
        M = ['female', 'juvenile', 'adult', 'male', 'human']
        I = [[1, 1, 0, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 1], [0, 0, 1, 1, 1]]
        self.context = Context(G, M, I)

    @parameterized.expand([
        [['girl'], {'girl'}],
        [['girl', 'woman', 'boy', 'man'], {'girl', 'woman', 'boy', 'man'}],
        [['boy'], {'boy'}]
    ])
    def test_get_object_closure(self, objects, expected):
        """
        Test for the extent closure operation (A'')
        """
        result = self.context.get_object_closure(*objects)
        self.assertEqual(result, expected)

    @parameterized.expand([
        [['female'], {'female', 'human'}],
        [['female', 'juvenile', 'adult', 'male', 'human'], set()],
        [['human'], {'human'}]
    ])
    def test_get_attribute_closure(self, attributes, expected):
        """
        Test for the intent closure operation (B'')
        """
        result = self.context.get_attribute_closure(*attributes)
        self.assertEqual(result, expected)

    @parameterized.expand([
        [['girl'], {'female', 'juvenile', 'human'}],
        [['girl', 'woman'], {'human', 'female'}],
        [['girl', 'man'], {'human'}]
    ])
    def test_get_attributes(self, objects, expected):
        """
        Test for B' (a set of all objects sharing all attributes from B)
        """
        result = self.context.get_attributes(*objects)
        self.assertEqual(result, expected)

    @parameterized.expand([
        [['female'], {'girl', 'woman'}],
        [['female', 'juvenile'], {'girl'}],
        [['human'], {'girl', 'woman', 'boy', 'man'}]
    ])
    def test_get_objects(self, attributes, expected):
        """
        Test for B' (a set of all objects sharing all attributes from B)
        """
        result = self.context.get_objects(*attributes)
        self.assertEqual(result, expected)

