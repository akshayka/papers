# [JuMP: A Modeling Language for Mathematical Optimization (Duninng 2016)](https://arxiv.org/pdf/1508.01982.pdf)

**Nut graf**: [JuMP](https://jump.readthedocs.io/en/latest/index.html) is a
Julia-embedded modeling language for mathematical optimization that was written
with performance in mind; its salient features include automatic differentiation
of user-defined functions, efficient parsing of updated problems, support for
user-defined problems and solve methods, and solver callbacks. JuMP targets
linear, mixed-integer, quadratic, conic-quadratic, semidefinite, and nonlinear
programs; unlike CVX*, JuMP does not verify convexity of nonlinear programs,
which means that it cannot provide optimality certificates for them.

## Background
Software packages for mathematical optimization can be organized into two
substrates. The **solving substrate** takes as input a mathematical program
and solves it; the substrate only accepts programs that are specified in
a particular standard form, and it is the responsibility of the client to
express her problem in an acceptable fashion. It is often not
at all obvious to clients how to encode their problems using the solving
substrate\'s standard form; this encoding proces may require
clever re-expressions of the original problem or onerous stuffing of
the problem\'s constraints into a rigid matrix structure.

The **modeling substrate** abstracts away the solving substrate: it takes
as input natural algebraic expressions and compiles them to the solving
substrate\'s standard form, allowing clients to encode their optimization
problems with minimal effort. A key observation is that the modeling substrate
does not *solve* problems; it simply compiles them for a particular target,
or solver, which then does the work required to produce a solution.

William-Orchard Hays and George Dantzig implemented one of the first software
packages for solving linear programs. The modeling substrate (that is,
domain specific languages for mathematical optimization) came into existence
in the late 1970s. JuMP is one of the latest additions to the modeling
substrate. It supports linear, mixed-integer, quadratic, second-order cone,
semidefinite, and non-linear programs. Part of its stated appeal is its
efficiency and the ease with which developers can extend it for custom problem
classes.

## Syntactic Macros and Code Generation
JuMP employs
[metaprogramming](https://docs.julialang.org/en/stable/manual/metaprogramming/)
to generate code for LPs and SOCPs. Expressions are specified using macros,
which process the code in a manner that circumvents the overhead of operator
overloading (the motivating example is a nested sum: expressing this
in a non-vectorized format can take considerable time).

## Nonlinear Problems and Automatic Differentiation
JuMP provides exact gradients and hessians to nonlinear solvers via
reverse mode automatic differentation (a generalization of backpropagation).
Custom functions defined by clients are also automatically differentiated,
albeit in a forward manner. JuMP diverges from CVX* in that is cannot
verify convexity of expressions; this means in particular that it cannot
provide proofs of optimality or infeasibility.

## Extensibility
The authors state that JuMP is easily to extend; i.e., it is easy to
build further specialized DSLs on top of JuMP. The API is not discussed, so
it\'s hard to evaluate this claim.

## Solver Callbacks
Though the paper does not discuss it much, solver callbacks are JuMP\'s most
interesting feature. Clients can register
[callbacks](https://jump.readthedocs.io/en/latest/callbacks.html) through which
they can communicate with a solver while it is solving a problem. In
particular, this means that a client can alter the solver\'s behavior on the
fly, adding, for example, cutting planes of her own choice, or dictating the
control flow of a branch-and-bound method. This is a very cool capability, one
that I could see myself using during algorithm development and evaluation; such
callbacks could also be useful in customizing a solver for a particular problem
instance.
