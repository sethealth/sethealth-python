from setuptools import setup

setup(
    name="sethealth",
    packages=["sethealth"],  # this must be the same as the name above
    version="1.8.0",
    description="Backend for sethealth authentication in python.",
    author="Sethealth team",
    author_email="team@set.health",
    url="https://github.com/sethealth/sethealth-py",
    keywords=["API", "authentication", "sethealth"],
    install_requires=[
        "certifi==2020.12.5",
        "chardet==4.0.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "requests==2.25.1",
        "urllib3==1.26.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
