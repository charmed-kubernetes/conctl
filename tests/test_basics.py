import unittest

from conctl import getContainerRuntimeCtl


class BasicTests(unittest.TestCase):
    def setUp(self):
        self.ctl = getContainerRuntimeCtl('containerd')

    def tearDown(self):
        pass

    def test_valid_runtime(self):
        self.assertEqual(self.ctl.runtime, 'containerd')


if __name__ == '__main__':
    unittest.main()
