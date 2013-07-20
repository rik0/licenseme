from setuptools import setup

setup(
    name='licenseme',
    version='0.1',
    # packages=['licenseme.py'],
    url='https://github.com/rik0/licenseme',
    license='MIT',
    author='Enrico Franchi',
    author_email='enrico.franchi@gmail.com',
    description='Simple tools to add license to your projects missing a license on github.',
    requires='githubpy'
)
