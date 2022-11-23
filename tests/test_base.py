import unittest
from subprocess import PIPE, CalledProcessError
from unittest import mock

from conctl.containerd import ContainerdCtl


class BaseTests(unittest.TestCase):
    def setUp(self):
        self.ctr = ContainerdCtl()

    def tearDown(self):
        pass

    @mock.patch("conctl.base.sub_run")
    def test_pull(self, mock_run):
        cmd = ("ctr", "image", "pull", "fancy/dancy:v0.1.2")
        stderr, stdout = b"my error", b"my stdout"
        kw = dict(cmd=cmd, stderr=stderr, output=stdout)
        mock_run.side_effect = CalledProcessError(-1, **kw)
        with self.assertLogs(level="ERROR") as log:
            with self.assertRaises(CalledProcessError):
                self.ctr.pull("fancy/dancy:v0.1.2")
        calls = [mock.call(cmd, stdout=PIPE, stderr=PIPE, check=True)]
        mock_run.assert_has_calls(calls)
        self.assertIn("ERROR:conctl:rc:     -1", log.output)
        self.assertIn(f"ERROR:conctl:stdout: {stdout.decode()}", log.output)
        self.assertIn(f"ERROR:conctl:stderr: {stderr.decode()}", log.output)


if __name__ == "__main__":
    unittest.main()
