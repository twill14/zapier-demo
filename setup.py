from setuptools import setup, find_packages

setup(
    name='zapier-demo',
    version='1.0.1',
    description='A tiny automation framework for the zapier home page.',
    author='Thomas Williams',
    author_email='twill14@gmail.com',
    url='https://github.com/twill14/zapier-demo.git',
    packages=find_packages(), install_requires=['selenium', 'pytest', 'pytest-html', 'webdriver_manager']
)
