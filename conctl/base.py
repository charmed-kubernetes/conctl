from typing import Dict, List
from subprocess import (
    run as sub_run,
    CompletedProcess,
    PIPE
)


class ContainerRuntimeCtlBase(object):
    """
    Base class for Container Runtime ctls.
    """
    def __init__(self) -> None:
        """
        :return: None
        """
        self.runtime = None

    def _exec(self, *args) -> CompletedProcess:
        """
        Call the underlying CLI.

        :param args: List arguments
        :return: CompletedProcess
        """
        return sub_run(args, stdout=PIPE, stderr=PIPE)

    def run(self,
            name: str,
            image: str,
            mounts: Dict[str, str],
            environment: Dict[str, str],
            command: str = None,
            *args: List[str]) -> str:
        """
        Run a container.

        :param name: String
        :param image: String
        :param mounts: Dictionary String host path String container path
        :param environment:  Dictionary String key String value
        :param command: String
        :param args: List String
        :return: String output
        """
        raise NotImplementedError

    def delete(self, *container_ids: List[str]) -> None:
        """
        Delete a container.

        :param container_ids: List String
        :return: String output
        """
        raise NotImplementedError
