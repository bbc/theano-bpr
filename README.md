theano-bpr
==========

A library implementing Bayesian Personalised Ranking (BPR) for
Matrix Factorisation, as decribed by Rendle et al. in :

  http://arxiv.org/abs/1205.2618

This models tried to predict a ranking of items for each
user from a viewing history. It's also used in a variety
of other tasks, such as matrix completion, link prediction
and tag recommendation.

This library uses [Theano](http://deeplearning.net/software/theano/) and
can therefore run on a [GPU through CUDA](http://deeplearning.net/software/theano/tutorial/using_gpu.html) or on the CPU. 
In the latter case we recommend using [OpenBlas](http://www.openblas.net).

Installation
------------

    $ pip install theano-bpr

Usage
-----

See examples/

Testing
-------

    $ nosetests

Licensing terms and authorship
------------------------------

See 'COPYING' and 'AUTHORS' files
