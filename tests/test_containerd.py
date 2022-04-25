import unittest
from unittest import mock

from subprocess import CalledProcessError
from conctl.containerd import ContainerdCtl


class ContainerdTests(unittest.TestCase):
    def setUp(self):
        self.ctl = ContainerdCtl()

    def tearDown(self):
        pass

    def test_valid_runtime(self):
        self.assertEqual(self.ctl.runtime, 'containerd')

    @mock.patch("conctl.containerd.ContainerdCtl._exec")
    def test_delete(self, mock_exec):
        self.ctl.delete()

        mock_exec.side_effect = CalledProcessError(1, cmd=['bad'])
        calls = [
            mock.call('task', 'kill', '--all'),
            mock.call('container', 'delete'),
            mock.call('snapshot', 'rm'),
        ]
        mock_exec.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
