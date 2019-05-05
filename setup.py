from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='PyRDW',
    version='1.1',
    description='PyRDW gives a basic way of fetching licensenumber-data from the RDW, the dutch department of road transport.',
    long_description=readme(),
    url='http://github.com/rense/pyrdw',
    author='Rense VanderHoek',
    author_email='vanderhoek@gmail.com',
    license='MIT',
    packages=['pyrdw'],
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
