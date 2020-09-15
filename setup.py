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
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
