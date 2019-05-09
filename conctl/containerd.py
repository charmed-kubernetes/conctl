from typing import Dict, List, Optional

from conctl.base import ContainerRuntimeCtlBase, CompletedProcess


class ContainerdCtl(ContainerRuntimeCtlBase):
    """
    Control Containerd via `ctr`.
    """
    def __init__(self) -> None:
        """
        :return: None
        """
        super().__init__()
        self.runtime = 'containerd'

    def _exec(self, *args: List[str]) -> CompletedProcess:
        """
        Run `ctr`.

        :param args: List args
        :return: CompletedProcess
        """
        return super()._exec(*['ctr'] + list(args))

    def run(self,
            name: str,
            image: str,
            mounts: Dict[str, str] = {},
            environment: Dict[str, str] = {},
            net_host: bool = False,
            privileged: bool = False,
            command: Optional[str] = None,
            args: List[str] = []) -> str:
        """
        Run a container.

        :param name: String
        :param image: String
        :param mounts: Dictionary String host path String container path
        :param environment:  Dictionary String key String value
        :param net_host: Boolean
        :param privileged: Boolean
        :param command: String
        :param args: List String
        :return: String output
        """
        to_run: list = [
            'run'
        ]

        for host, container in mounts.items():
            to_run.append('--mount')
            to_run.append(
                'type=bind,src={},dst={},options=rbind:rw'.format(
                    host, container))

        for key, value in environment.items():
            to_run.append('--env')
            to_run.append('{}={}'.format(key, value))

        if net_host:
            to_run.append('--net-host')

        if privileged:
            to_run.append('--privileged')

        to_run.append(image)
        to_run.append(name)

        if command:
            to_run.append(command)

        if args:
            to_run += args

        return self._exec(*to_run)

    def delete(self, *container_ids) -> CompletedProcess:
        """
        Delete a container.

        :param container_ids: List String
        :return: CompletedProcess
        """
        return self._exec(
            'container', 'delete', *container_ids
        )

    def pull(self,
             urls: List[str],
             username: Optional[str] = None,
             password: Optional[str] = None) -> CompletedProcess:
        """
        Pull images.

        :param urls: List String
        :param username: String
        :param password: String
        """
        if isinstance(urls, str):
            urls = [urls]

        for url in urls:
            return self._exec(
                'image',
                'pull',
                '--user={}:{}'.format(
                    username,
                    password
                ),
                url
            )
