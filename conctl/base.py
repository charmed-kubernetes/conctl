from logging import getLogger
from subprocess import PIPE, CalledProcessError, CompletedProcess
from subprocess import run as sub_run  # noqa: F401
from typing import Dict, List, Optional

log = getLogger("conctl")


class ContainerRuntimeCtlBase(object):
    """
    Base class for Container Runtime ctls.
    """

    def __init__(self, pipe=True) -> None:
        """
        :param pipe: Boolean pipe std*
        :return: None
        """
        self.pipe = pipe
        self.runtime = None

    def _exec(self, *args: List[str]) -> CompletedProcess:
        """
        Call the underlying CLI.

        :param args: List arguments
        :return: CompletedProcess
        """
        kw = dict(stdout=PIPE, stderr=PIPE, check=True) if self.pipe else {}
        try:
            return sub_run(args, **kw)
        except CalledProcessError as e:
            log.error(f"rc:     {e.returncode}")
            log.error(f"stdout: {e.stdout and e.stdout.decode()}")
            log.error(f"stderr: {e.stderr and e.stderr.decode()}")
            raise

    def run(
        self,
        name: str,
        image: str,
        mounts: Dict[str, str] = {},
        environment: Dict[str, str] = {},
        net_host: bool = False,
        privileged: bool = False,
        remove: bool = True,
        command: Optional[str] = None,
        args: List[str] = [],
    ) -> str:
        """
        Run a container.

        :param name: String
        :param image: String
        :param mounts: Dictionary String host path String container path
        :param environment:  Dictionary String key String value
        :param net_host: Boolean
        :param privileged: Boolean
        :param remove: Boolean
        :param command: String
        :param args: List String
        :return: String output
        """
        raise NotImplementedError

    def stop(self, *container_ids: List[str]) -> CompletedProcess:
        """
        Stop containers.

        :param container_ids: List String
        :return: CompletedProcess
        """
        raise NotImplementedError

    def delete(self, *container_ids: List[str]) -> CompletedProcess:
        """
        Delete containers.

        :param container_ids: List String
        :return: CompletedProcess
        """
        raise NotImplementedError

    def pull(
        self,
        urls: List[str],
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> CompletedProcess:
        """
        Pull images.

        :param urls: List String
        :param username: String
        :param password: String
        :return: CompletedProcess
        """
        raise NotImplementedError

    def load(self, path: str) -> CompletedProcess:
        """
        Load an image.

        :param path: String file path
        :return: CompletedProcess
        """
        raise NotImplementedError
