# [Graph Implementations for Nonsmooth Convex Programs (Grant 2008)](https://stanford.edu/~boyd/papers/pdf/graph_dcp.pdf)

**Nut graf**: Grant and Boyd describe a methodology to automatically reduce
nonsmooth convex programs to a form that is accepted by conic solvers. The
methodology requires that programs be specified using the *disciplined convex
programming* ruleset; it converts such programs into an epigraph-like form,
where the objective is affine and the constraints are conic composed with
affine. The implement this methodology in $$\texttt{cvx}$$, which passes
the reduced problem to a conic solver in order to obtain a solution to the
original problem. The main contribution of this paper is that its
implementation helps to bridge the \"gap between the theory and practice of
convex optimization.\"

**Commentary**: The pre-1.0 release of CVXPY is tightly coupled to graph
implementations. In CVXPY 1.0, we relax this coupling and introduce a
general purpose re-writing system that can target the practioner\'s back-end
of choice. In particular, this means that clients will no longer be restricted
to using conic solvers, and indeed they will no longer be necessarily
restricted to disciplined convex optimization or even to convex optimization
proper.
