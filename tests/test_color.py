import unittest
from shirotsubaki import utils as stutils


class TestStUtils(unittest.TestCase):
    def test_lighten_color(self):
        color = stutils.lighten_color('#336699')
        self.assertEqual(color, '#99B2CC')
