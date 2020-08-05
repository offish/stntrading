from setuptools import setup, find_packages
import re


with open('README.rst', 'r') as f:
    long_description = f.read()


with open('stntrading/__init__.py') as f:
    version = re.search(
        r"^__version__\s*=\s*['']([^\'']*)['']", f.read(), re.MULTILINE).group(1)


setup(
    name='stntrading',
    version=version,
    author='offish',
    author_email='overutilization@gmail.com',
    description='Easily interact with STNTrading\'s public API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/offish/py-stntrading',
    download_url='https://github.com/offish/py-stntrading/tarball/v' + version,
    packages=['stntrading'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=['requests'],
    python_requires='>=3.6',
)
