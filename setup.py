from setuptools import setup


setup(
    name='conctl',
    version='0.1.1',
    url='https://github.com/joedborg/conctl',
    license='Apache License 2.0',
    author='Joe Borg',
    author_email='joseph.borg@canonical.com',
    description='Drive Containerd and Docker from one CLI',
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
