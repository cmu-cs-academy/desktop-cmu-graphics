# In order for the tests to work, you should first run `maturin develop` in the cmu_graphics_rust directory and then run this file using uv
import unittest
import cmu_graphics_rust


class TestUnion(unittest.TestCase):
    # a square with no holes
    global multipoly
    multipoly = [[[(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0)]]]

    def test_union(self):
        self.assertEqual(
            cmu_graphics_rust.union(multipoly, multipoly),
            [[[(0.0, 1.0), (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]]],
        )

    def test_union_alt(self):
        self.assertEqual(
            cmu_graphics_rust.union_alt([multipoly]),
            [[[(0.0, 1.0), (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]]],
        )


if __name__ == '__main__':
    unittest.main()
