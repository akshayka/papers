# [YALMIP: A Toolbox for Modeling and Optimization in MATLAB (Lofberg 2016)](http://ieeexplore.ieee.org/abstract/document/1393890/)

**Nut graf**: YALMIP is a MATLAB-embedded domain specific language for
mathematical optimization. It is among the oldest non-commerical modeling
langauges, and can target a variety of convex and non-convex solvers.

YALMIP, an orphaned acronym that once stood for \"Yet Another LMI Parser\",
supports a hodgepodge of problem classes: LPs, QPs, SOCPs, and SDPs among them.

The paper consists largely of examples that transcribe somewhat complex SDPs
into but a few lines of YALMIP. The thesis that motivated the creation of
YALMIP is: Many control problems can be reduced to SDPs, and SDPs can
be solved efficiently; however, converting problems into LMI/SDP form
and interfacing with software packages that solve SDPs is a tedious task.
YALMIP democraticizes this process by abstracting away the compilation of
naturally expressed mathematical programs to solver-defined standard forms.

Lofberg presents two applications that I find interesting: sum-of-squares 
(SOS) decompositions and multiparametric programming. In SOS, the goal is to
write a polynomial $$p(x)$$ as a positive semidefinite quadratic form with 
respect to some polynomial vector $$v(x)$$. Such a decomposition, if it were
to exist, would certify that $$p(x)$$ were non-negative. SOS is trending
in the theoretical computer science community, where it is being used to
prove lower bounds.

Multiparametric programming is a type of optimization where the goal is to
find an explicit solution to parametrized optimization problems, reducing
a sequence of optimization problems to a sequence of function evaluations.
Perhaps the simplest example of this is the orthogonal projection problem:
the projection onto a subspace is parametrized by the point that is being
projected. All that is needed for an explicit solution is to compute the
linear projector; with this operator in hand, every
projection onto the subspace can be computed via a matrix multiply.
