from distutils.core import setup


setup(
    name='pytest_graphql',
    version='0.0.1',
    author='uep backend team',
    author_email='uep_back_end_team@1000mercis.com',
    url='https://gitlab.numberly.in/team-uep/lib/pytest-graphql',
    packages=['pytest_graphql'],
    install_requires=[dep for dep in open('requirements.txt').readlines()],
)
