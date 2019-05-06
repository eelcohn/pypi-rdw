from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='Rdw',
    version='3.0.0',
    description='(Unofficial) Python wrapper for the rdw.nl website (Netherlands Vehicle Authority) which can be used to check vehicle information.',
    long_description=readme(),
    url='http://github.com/eelcohn/pypi-rdw',
    author='Eelco Huininga',
    author_email='eelcohn@github.com',
    license='MIT',
    packages=['rdw'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Dutch',
        'Programming Language :: Python :: 2 :: Only'
    ],
)
