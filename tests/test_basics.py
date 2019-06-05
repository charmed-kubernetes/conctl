import unittest

from conctl import getContainerRuntimeCtl


class BasicTests(unittest.TestCase):
    def setUp(self):
        self.ctl = getContainerRuntimeCtl()

    def tearDown(self):
        pass

    def assert_valid_runtime(self):
        self.assertIn(self.ctl.runtime, ['docker', 'containerd'])


if __name__ == '__main__':
    unittest.main()
