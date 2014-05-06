from setuptools import setup

setup(
    name='theano-bpr',
    version='0.1.0',
    description='Bayesian Personalised Ranking implemented in Theano',
    author='Yves Raimond',
    author_email='yves.raimond@bbc.co.uk',
    url='https://github.com/bbcrd/theano-bpr',
    license='Apache License 2.0',
    packages=['theano_bpr'],
    install_requires=[
        'numpy',
        'theano',
    ],
)
