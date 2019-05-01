# conctl

Drive Containerd and Docker from one CLI.

## Installation

`conctl` requires Python 3.5 and up.

```bash
sudo pip install conctl
```

## Motivation

It's currently a pain to have to 'if' every script that needs to drive either
Docker or Containerd.  It'd be nice to have a single CLI that can drive at
least basic funtionality in both.

## Current State

This is in super early stages, just enough to run and delete containers. The
to do list would be massive, but here are the highlights:

* Complete API and CLI for basic operations.
* Better way to detect runtimes.
* Drive via CRI, rather than shell calls.
* Tests!

## Example

Running the same command, on differnt hosts.  One with Docker installed,
the other with Containerd.

```bash
$ sudo conctl --verbose run --name hi docker.io/library/hello-world:latest
Runtime docker selected

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

```bash
$ sudo conctl --verbose run --name hi docker.io/library/hello-world:latest
Runtime containerd selected

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

We can also import the factory method if we want to use it in code.

```python
from conctl import getContainerRuntimeCtl

ctl = getContainerRuntimeCtl()
ctl.run(name='hi', image='docker.io/library/hello-world:latest', mounts={}, environment={})
```
