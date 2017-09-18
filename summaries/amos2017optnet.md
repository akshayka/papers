# [OptNet: Differentiable Optimization as a Layer in Neural Networks (Amos 2017)](https://arxiv.org/abs/1703.00443)

**Nut graf**: OptNet is a neural network architecture that includes
embedded within it _quadratic programs_. The paper's main contributions
are: (1) an architecture that contains as layers (the solutions to)
quadratic programs; (2) a method to differentiate through quadratic programs;
(3) a method that reuses a matrix factorization used in solving a quadratic
program to render insignificant the cost of computing gradients for said
program; and (4) an efficient GPU-accelerated implementation of a primal-dual
QP solver. The authors acknowledge that training OptNets can be quite
challenging (many parameter changes are just reductions between problems),
but provide evidence for their claim that OptNet might better suited
than traditional neural networks to learn hard constraints via experimental
validation on learning to play mini-Sudoku.

## Differentiating through quadratic programs
The method differentiates through the KKT optimality conditions for quadratic
programs. This method is well-defined because the solution of a quadratic
program is subdifferentiable almost everywhere. Backpropagation reuses the
LU factorization of the (symmetrized) KKT matrix (computed during the solve)
at the solution when obtaining gradients, making the complexity of gradient
computation quadratic.

## Limitations
* Solving a QP incurs cubic complexity layer; vanilla feedforward layers incur
quadratic complexity.
* Training is quite hard and requires significant tuning.

## Commentary
* Optimization layers will not be practical in, e.g., Google-scale
language / vision networks.
* Nonetheless the idea of automatically learning the parameters of an
optimization problem is extremely interesting, for two reasons. (1)
Optimization problems can encode hard constraints and (2) optimization problems
can be quite interpretable.
* Differentiating through optimization problems provides a compromise between
end-to-end learning and human expertise by providing a mechanism to encode
whatever knowledge the modeler may have about their problem in the form of a
mathematical program --- the learning algorithm can infer the rest.

