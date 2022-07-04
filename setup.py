import setuptools

base_packages = [
    "requests",
    "dataclasses>=0.7,<1; python_version<'3.7'",
    "dataclasses-json>=0.5.0,<1.0.0"]

dev_packages = [
    "black>=19.3b0",
    "flake8>=3.6.0",
    "flake8-annotations==2.1.0",
    "flake8-bandit==2.1.2",
    "flake8-bugbear==20.1.4",
    "flake8-docstrings==1.5.0",
    "darglint==1.4.0",
    "pre-commit>=2.2.0",
    "types-dataclasses>=0.1.3,<1; python_version<'3.7'",
    "types-requests>=0.1.8,<1",
    "pytest>=6.1.2,<7"]

setuptools.setup(
    name="okra-doccano-client",
    version="1.0",
    setup_requires=["setuptools_scm"],
    description="A simple client wrapper customised for okra doccano API.",
    long_description="This simple API wrapper forked from doccano customised for okra that allows users to easily get \
                     data from and send data to a doccano instance.",
    url='https://github.com/okraHQ/okra-ai-doccano-client',
    author="Okra Ds Team",
    author_email="chidera@okra.ng",
    packages=["doccano_api_client"],
    install_requires=base_packages,
    extras_require={"dev": dev_packages},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
