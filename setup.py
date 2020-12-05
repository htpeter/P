import os
import sys

from setuptools import find_packages, setup
from setuptools.command.install import install


VERSION = "0.1.0"
DESCRIPTION = open("README.md", encoding="utf-8").read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


setup(
    name="pypi-project",
    version=VERSION,
    packages=find_packages(exclude=["tests"]),
    url="",
    project_urls={"Changelog": ()},
    license=None,
    author="Peter Kouvaris",
    author_email="peter@kouvaris.io",
    description="Abstractions for engineering and science.",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=["boto3"],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    cmdclass={"verify": VerifyVersionCommand},
)
