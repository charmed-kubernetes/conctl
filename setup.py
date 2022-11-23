from setuptools import setup


setup(
    name='conctl',
    version='0.1.4',
    url='https://github.com/charmed-kubernetes/conctl',
    license='Apache License 2.0',
    author='Joe Borg',
    author_email='joseph.borg@canonical.com',
    description='Drive Containerd and Docker from one CLI',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=['conctl', 'conctl/bin'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'conctl=conctl.bin.conctl:cli',
        ],
    }
)
