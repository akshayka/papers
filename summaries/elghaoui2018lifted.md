# [Lifted Neural Networks (El Ghaoui 2018)](https://arxiv.org/abs/1805.01532)

This paper introduces a family of feedforward neural networks in which
each activation function is represented as an argmin of a convex optimization
problem; these representations are encoded in the problem of training a
neural network via penalties. The key to arriving at such a representation
is to *lift* the standard neural network optimization problem into a
higher-dimensional space by introducing for each layer a variable representing
its output layer, representing each activation function as a argmin of a
divergence function that is convex in each argument (but not necessarily
jointly convex in both arguments), and by coercing the divergences to be small
via penalization. For this reason, El Ghaoui and his co-authors say that
instances of this family are "lifted" neural networks.

The upshot: Any lifted neural network can be optimized in a block-coordinate,
gradient-free fashion using well-known algorithms for convex optimization,
and, after training, the values of its optimization variables can be used
as initialization for the corresponding "unlifted" neural network.

This paper can be understood as part of an ongoing research effort to
simplify the mathematical structure of neural networks and to express them
in principled ways that are more amenable to training[^1][^2].

The experiments in this paper are not particularly compelling. MNIST
is used as a benchmark, and the results aren't great. What's more, training
time is not reported (only the number of epochs is reported). The main
contribution of this paper is its theoretical framework.

[^1]: 
    Amos, B., Xu, L., & Kolter, J. Z. (2016). Input convex neural networks.
    arXiv preprint arXiv:1609.07152.

[^2]: 
    Zhang, Y., Liang, P., & Wainwright, M. J. (2016). Convexified convolutional
    neural networks. arXiv preprint arXiv:1609.01000.
