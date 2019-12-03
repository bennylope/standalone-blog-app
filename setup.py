from setuptools import setup, find_packages

setup(
    name="blog",
    version="0.1.0",
    author="Ben Lopatin",
    author_email="ben@benlopatin.com",
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
    url="http://www.django-standalone-apps.com",
)
    #description="A standalone Django blog project",
