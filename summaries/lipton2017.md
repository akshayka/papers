# [The Mythos of Model Interpretability (Lipton 2017)](https://arxiv.org/pdf/1606.03490.pdf)

This paper addresses three questions:

1. Why do we want interpretability in the context of supervised machine
   learning?
1. What is meant by _interpretability_ in the context of supervised machine
   learning?
2. What tools do we have to study the interpretability of machine
   learning and especially deep neural network models?

Its thesis is three-fold:

1. The desire for interpretability arises from a desire to _trust_ machine
   learning systems, to demonstrate _causality_, to be assured of
   _transferability_ to unseen data, to uncover latent structure in the
   data (_informativeness_, and to facilitate _ethical decision-making_.
2. There are two types of useful interprations: those that afford
   _transparency_ and those that provide for _post-hoc_ explanations.
3. Linear models are not necessarily more interpretable than deep neural
   networks.

## Desiderata 
Of the desiderata in (1), trust is ill-defined and causality, I think,
a straw-man. Ethical decision-making is crucial --- the ethics of machine
learning algorithms and are woefully underexamined when such algorithms
are deployed. Lipton mentions the questionable use of machine learning models
for predicting the chances of recidivism in courts of law. Also pressing, in
my mind, is the use of machine learning to create hyper-personalized
information filters that would cast individuals into static molds and more
worrisome as objects to be optimized. But in this latter example,
ethical decision-making is not a matter of _interpretability_ --- the
models for filtering information are interpretable enough, at least at a macro
level; it is rather a matter of whether filtering _as such_ is ethical.

## Types of Interpretability
The paper proposes two types of interpretability.

*Transparency* takes the forms of _simulatibility_, in that a _human_ should
be able to simulate the model by hand, and _decomposability_, in that
each part of the model admits an intuitive explanation, and _algorithmic_, 
in that the model should converge to a unique solution. The first point is
somewhat silly --- the point of computers is to automate tasks that humans cannot
do in a reasonable amount of time; the second point is fine; the third point
is silly --- unique solutions (one example of algorithmic transparency provided
by the author) are not even guaranteed in convex land, and
algorithmic determinism (another example provided by the author) is besides the
point in machine learning. 

A model is *post-hoc interpretable* if its predictions admit retrospective
explanations. This section surveys a few standard techniques for querying the
activations of a trained model (t-SNE of learned representations, sensitivity
analyses, etc.). All of these post-hoc techniques are also _ad hoc_.

## Linear Models
Lipton makes a wholly unconvincing argument that linear models are not
more interpretable than neural networks. He qualifies his argument by saying
that they are not _strictly_ more interpretable, but this much is of course
obvious, for deep neural networks include linear models as a special case.
Lipton makes absolutely no appeal to the statistical properties that
accompany linear models, a surprising oversight. He states that we do not
have a theoretical reason why neural networks underperform linear models
in studying the natural world. This is false; the parameters in
a linear regression, for example, carry with them information about statistical
significance (if certain assumptions about the data hold true).

Lipton also argues that linear models are just as succeptible to spoofing
as deep neural networks. This too is false. As a rule of thumb, the more
complex your system, the easier it is to spoof it.

## Commentary
In my mind, there are two things that matter with respect to interpretability:

1. Does this model generalize to unseen data? A model is _interpretable_ if
hypotheses about generalization hold true after attempts to falsify them.
I suppose this is more or less the same as Lipton's transferability.
2. Is the model _secure_, i.e., is it resistant to spoofing?

Determing the degree to which a model is secure is an open question; perhaps
it can be studied by using some of the tools that Lipton surveys in his paper.
It is clear to me, however, that validating the security of a neural network
model is _significantly_ harder than doing the same for linear ones.
