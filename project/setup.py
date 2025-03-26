from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="clinicasf_automation",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    install_requires=requirements,
    python_requires='>=3.6',
)