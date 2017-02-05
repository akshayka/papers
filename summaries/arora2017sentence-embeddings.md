# [A Simple but Tough-to-Beat Baseline for Sentence Embeddings (Arora 2017)](https://openreview.net/pdf?id=SyK00v5xx)

The thesis:

> Use word embeddings computed using one of the popular methods on unlabeled
> corpus like Wikipedia, represent the sentence by a weighted average of the
> word vectors, and then modify them a bit using PCA/SVD. This weighting
> improves performance by about 10% to 30% in textual similarity tasks, and
> beats sophisticated supervised methods including RNN's and LSTMs … This
> simple method should be used as the baseline to beat in the future,
> especially when labeled training data is scarce or nonexistent.

This paper uses a modified version of the generative model proposed
in [Arora 2016](arora2016pmi-embeddings.html) in order to obtain a closed
form estimate of the sentence vector. The sentence vector $$c_s$$ is assumed to
be time-invariant. Two modifications are made that account
for the observation that words appear out of context at times, and that
some frequent words appear very often and without regard to the topic
of conversation. In math:

$$
\begin{align*}
\Pb[w \in s \mid c_s] &= \alpha p(w) + (1-\alpha) \exp
\inner{\tilde{c}_s}{v_w}/Z_{\tilde{c}_s}, \\
\tilde{c}_s &= \beta c_0 + (1-\beta)c_s
\end{align*}
$$

The MLE derivation is short, and the upshot is nice:

$$
\begin{align*}
\hat{c}_{s} &= \sum_{w \in s} \frac{a}{p(w) + a}v_w \\
a &= \frac{1 - \alpha}{\alpha Z}.
\end{align*}
$$

In practice, $$a$$ is treated as a hyper-parameter. The final sentence vector
is obtained by subtracting out the first principal component in order to
"denoise" the data:

$$
\hat{c}_{s} := \hat{c}_{s} - \inner{\hat{c}_s}{u} u.
$$

The experimental upshot is also nice: the obtained sentence vectors either match
or outperform neural methods on similarity, entailment, and sentiment tasks.

## Commentary
* Arora observes that the average of word vectors "have huge components along
semantically meaningless directions." I don't fully grasp his explanation
as to why this is the case.
* From the paper: "We see that the model allows a word w unrelated to the discourse
 $$c_s$$ to be omitted for two reasons: a) by chance from the term
 $$\alpha p(w)$$ b) if $$w$$ is correlated with the common discourse vector
 $$c_0$$." I believe "omitted" should actually be *emitted*.

