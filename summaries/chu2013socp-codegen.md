# [Code Generation for Embedded Second-Order Cone Programming (Chu 2013)](https://web.stanford.edu/~boyd/papers/pdf/ecos_codegen_ecc.pdf)

Key idea: Chu, et. al describe a *parser/generator* that takes a parametrized
convex program, converts it to an equivalent SOCP, and generates code that can
be used to solve the problem.

## Novel contributions

1. SOCPs encompass a large class of convex programs; previous canonicalization
   suites targeted smaller problem classes, like QPs or QCQPs. Recall
  that linear programs, QPs, and QCQPs are all SOCPs.
2. Problem parameters must enter through specific functions; this interface
   allows the code generator to circumvent all floating point operations.

Problem convexity is verified via disciplined convex programming.

## Problem Statement: Canonicalization

The canonicalization takes as input a convex optimization problem and outputs
an equivalent SOCP.

**Input**: convex optimization problem description.

$$
\optmin{x}{f_{0}(x; \alpha)}{f_i(x; \alpha) \leq g_i(x; \alpha),
\quad i=1\ldots,m \\ & & & u_i(x; \alpha) = v_i(x; \alpha)}
$$

**Output**: equivalent second-order cone program

$$
\optmin{x, s}{c^Tx}{Ax + s = b, \quad s \in \mathcal{K},}
$$

where $$\mathcal{K}$$ is the cross product of $$q$$
second-order cones and $$\{0\}^r$$.

## Background: Disciplined Convex Programming

The three building blocks of DCP are atoms, expressions, and convex problems;
atoms are the atomic units, expressions build from atoms, and convex problems
build from expressions.

### Atoms
An atom is a built-in function like plus, minus, sum, maximum, square, or norm.
There are three classes of atoms: parametric atoms, scalar atoms, and
vector atoms. All atoms return scalars, except scalar atoms evaluated at
vector arguments return elementwise-transformed vectors.

Atoms have three key properties: (1) output sign, (2) monotonicity per argument,
and (3) curvature. The output sign can depend upon the signs of inputs;
a vector is positive if and only if every entry is positive. The monotonicity
of parametric atoms depends upon the sign of their parameters.

### Expressions
An expression is a vector variable or an atom evaluated at a subexpression
(note the recursive definition); the leaves of expressions are the variables,
internal nodes are atoms, and each atom is evaluated at its children. For
example, $$\phi^{\operatorname{square}}$$ is an atom, but
$$\phi^{\operatorname{square}}(x)$$ a subexpression. The sign of an expression
is computed bottom-up; variables have unknown sign (but some atoms,
like the square atom, have sign independent of its inputs).

Convexity is also verified in a bottom-up fashion. All variables are affine;
$$\phi(g_1(x), \ldots, g_n(x); \alpha)$$ is convex if $$\phi$$ is convex and
one of the following holds for each $$i$$: (1) $$g_i$$ is affine,
(2) $$\phi$$ is increasing in the $$i$$th argument and $$g_i$$ is convex,
or (3) $$\phi$$ is decreasing in the $$i$$th argument and
$$g_i$$ is concave.

### Convexity
Convexity can be determined by the curvature of all its expressions and atoms.
Note that DCP-compliance is sound but not complete.

## Canonicalization

The first step is to convert the original problem into **Smith form**.
A new variable $$t_i$$ is introduced for each node $$i$$ in the expression
tree, with $$t_0$$ mapping to the root of the tree; then, the problem
is written as "minimize $$t_0$$" subject to $$t_i$$ equals the $$i$$-th
subexpression, for each subexpression $$i$$. In order to convexify
the smith problem, the equality constraints $$t_i = \phi_i(t_{i+1})$$
for convex $$\phi_i$$ are replaced with inequality constraints
$$t_i \geq \phi_i(t_{i+1})$$; this representation is known as *relaxed*
Smith form. It can be shown (this is key) that the optimal solution of
the relaxed Smith form of a DCP-compliant problem is optimal for the original
problem as well.

In the final step, nonlinear functions in the relaxed Smith form are
replaced with the "optimal value of a partially-specified convex optimization
problem." This is known as the graph implementation for convex problems.
Finally, the resulting SOCP is converted into standard form.

*Note that the only work done is copying problem data into SOCP data.*

## Commentary
CVXPY (version < 1.0) more or less implements this paper -- it canonicalizes
its problems by converting them into cone programs, including SOCPs. You can
see this in the source code (available on Github): each atom implements a
function named
graph_implementation, and this function is invoked during canonicalization.
