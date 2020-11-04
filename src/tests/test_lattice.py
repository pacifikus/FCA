# from src.fca.lattice import Lattice
# from unittest import TestCase
# from parameterized import parameterized
#
#
# class LatticeTestCase(TestCase):
#     """
#     Lattice class checks
#     """
#     def setUp(self):
#         C = ['girl', 'woman', 'boy', 'man']
#         E = ['female', 'juvenile', 'adult', 'male', 'human']
#         self.lattice = Lattice(C, E)
#
#     @parameterized.expand([
#         [['girl'], {'girl'}],
#         [['girl', 'woman', 'boy', 'man'], {'girl', 'woman', 'boy', 'man'}],
#         [['boy'], {'boy'}]
#     ])
#     def test_get_cleared_edges(self, edges, expected):
#         """
#         Test for the extent closure operation (A'')
#         """
#
