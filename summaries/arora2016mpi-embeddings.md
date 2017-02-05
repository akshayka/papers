# [A Latent Variable Model Approach to PMI-based Word Embeddings (Arora 2016)](https://transacl.org/ojs/index.php/tacl/article/viewFile/742/204)

## Background
There are two popular classes of word embedding techniques:

1. Compute a low-rank approximation of a re-weighted co-occurrence matrix
   (i.e., PCA via SVD).
2. Use a neural network language model's representation of a word (e.g.,
   word2vec, GloVe).

A re-weighting scheme used in (1) is to replace the co-occurrence statistics
with the *pointwise mutual information* between two words.

<p hidden>
$$
\newcommand{\pmi}{\operatorname{pmi}}
\newcommand{\inner}[2]{\langle{#1}, {#2}\rangle}
\newcommand{\Pb}{\operatorname{Pr}}
$$
</p>

The pointwise mutual information (PMI) of a pair of outcomes $$x \in X$$,
$$y \in Y$$, $$X$$, $$Y$$ discrete random variables measures the extent to
which their joint distribution differs from the product of the marginal
distributions:

$$\pmi(x;y) := \log\frac{p(x,y)}{p(x)p(y)} = \log \frac{p(x \mid y)}{p(x)}
= \log \frac{p(y \mid x)}{p(y)}$$

Note that $$\pmi(x;y)$$ attains its maximum when $$p(x \mid y) = 1$$ or $$p(y \mid x) = 1$$.

It is observed empirically that

$$
\begin{align}
\inner{v_w}{v_{w'}} \approx \pmi(w, w') \label{low-rank-pmi}.
\end{align}
$$

## Key Contribution 
*This paper proposes a generative model for word embeddings that provides a
theoretical justification of* $$(\ref{low-rank-pmi})$$ *and word2vec
and GloVe*. The key assumption it makes is that word vectors, the latent
variables of the model, are spatially isotropic (intuition: "no preferred
direction in space"). Isotropy of low-dimensional vectors helps explain
the linear structure of word vectors as well.

## The Generative Model
A time-step model: at time $$t$$, word $$t$$ is produced by a random walk of
a discourse vector $$c_t \in \mathbb{R}^d$$ that represents the topic of
conversation. Each generated word has a latent vector $$v_w \in \mathbb{R}^d$$
that measures the correlation with the discourse vector. In particular:

$$\Pb(w $$ is the  $$t$$-th word $$\mid c_t) \propto \exp \inner{c_t}{v_w}$$.

$$c_{t+1} := c_t +$$ a small random displacement. *Under this model, the authors
prove that the co-occurrence probabilities and marginal probabilities
are functions of the word vectors; this is useful when optimizing the
likelihood function* $$\ell = \log \prod_{w, w'} p(w, w')^{X_{w,w'}}$$.


## Commentary
* This paper answers an interesting question: Why is it that a nonlinear model
  like word2vec produces outputs that have linear structures
  (e.g., king - man = woman)?
* It's really cool that a relatively simple generative model grounded in a
  solid theoretical foundation produces results that are competitive with
  neural network models.
  

