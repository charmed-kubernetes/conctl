from subprocess import check_call, CalledProcessError, DEVNULL

from conctl.containerd import ContainerdCtl
from conctl.docker import DockerCtl


def _detectContainerRuntime():
    """
    Attempt to detect the container runtime.

    It seems the `docker.io` package now ships
    with `ctr`, so we've reversed these until
    we figure a better way to do the detection.

    :return: String name
    """
    try:
        check_call(['docker'], stdout=DEVNULL, stderr=DEVNULL)
    except (FileNotFoundError, CalledProcessError):
        pass
    else:
        return 'docker'

    try:
        check_call(['ctr'], stdout=DEVNULL, stderr=DEVNULL)
    except (FileNotFoundError, CalledProcessError):
        pass
    else:
        return 'containerd'

    raise RuntimeError('Cannot detect a container runtime')


def getContainerRuntimeCtl(runtime=None, pipe=True):
    """
    Factory method which returns a
    Container Runtime ctl.

    :param runtime: String runtime
    :param pipe: Boolean pipe std*
    :return: ContainerRuntimeCtl
    """
    supported = {
        'containerd': ContainerdCtl,
        'docker': DockerCtl
    }

    if not runtime:
        runtime = _detectContainerRuntime()

    try:
        return supported[runtime](pipe)
    except IndexError:
        raise NotImplementedError(
            '{} runtime is not supported'.format(runtime))
