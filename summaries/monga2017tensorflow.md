# [TensorFlow: A System for Large-Scale Machine Learning (Mongat 2016)](https://www.usenix.org/system/files/conference/osdi16/osdi16-abadi.pdf)

## Overview
TensorFlow uses a dataflow graph to represent both computation and state.
Nodes represent computation upon mutable data, and edges carry tensors, or
multi-dimensional arrays, between nodes. The system uses synchronous replication
successfully, contradicting the folklore that asynchronous replication is
needed for scalability.

DistBelief, the prequel to TensorFlow, was limited by its parameter server
architecture; at times it is desirable to offload computation onto the
server that owns the data. As such, TensorFlow eschews the separation
of workers and parameter servers in favor of a hybrid model. The key design
principles of TensorFlow are

1. graphs are composed of primitive operators,
2. execution is deferred, and
3. a common abstraction supports any accelerator that implements its interface.

Note that a batch dataflow model, which favors large batches of computation and
requires immutable inputs and deterministic computation, is not appropriate
if stochastic gradient descent is your optimization method of choice. 
TensorFlow allows for mutable state ''that can be shared between different
executions of the graph'' and ''concurrect executions or overlapping
subgraphs.''

## The Graph Elements

### Tensors
A **tensor** is a multi-dimensional array that stores primitive types; one
of those primitive types is a string, which holds arbitrary binary data.
All tensors are dense in order to ensure that memory allocation and
serialization can be implemented efficiently. Spare vectors can be encoded
as either variable-length string elements or tuples of dense tensors. The
shape of a tensor can vary along its dimensions.

### Stateless Operations
**Stateless operations** map one list of tensors to another list of
tensors. The simplest way to think of such an operation is as a mathematical
function.

### Variables
A **variable** is a stateful operation. Each variable owns a mutable
buffer that, for example, holds the model parameters as it is trained.
Variables take no inputs. They instead expose a `read` operation and various
write operations. An example of a write operation is `AssignAdd`, which
is semantically equivalent to the familiar ''plus-equals.''

### Queues
Queues allow for concurrent access to the tensors that they hold. They can
provide backpressure when they are full and are used to implement streaming
computation between subgraphs.

## Distributed Execution and Dynamic Control Flow
Every operation is placed on a *device*, and each device assembles its
operations into a subgraph. TensorFlow is ''optimized for executing large
subgraphs repeatedly with low latency.''

Conditional statements and other control flow primitives are supported.

## Automatic Differentiation and Optimization
Users can handroll their gradients if they so desire, or they can rely on
the automatic differentiation. It is simple to implement new optimization
algorithms using the TensorFlow framework; no code changes are required.

## Synchronous Replica Coordination
Both asynchronous and synchronous SGD are supported; the latter converges
to a good solution faster than the former (both in practice and, I assume,
in theory). In the synchronous scheme, firing up redundant workers and
taking the updates from those who finish first improves throughput by up to
10 percent.

## Commentary
* The authors list improved models, larger datasets, and software platforms
  that allow for better use of hardware as the primary drivers of the machine
  learning renaissance, in that order. I am surprised that improved models
  is first in that list.
* I like the decision to encode sparse data as assemblages of dense tensors.
  But does this representation allow for the underlying linear algebra
  to make use of sparse matrix structure?
* An interesting problem that remains unsolved (at Google, at the time of
  writing the paper): How can we accommodate dynamic dataflow graphs for
  tasks like deep reinforcement learning?
* I think it would be useful if TensorFlow & researchers were together
  working on the problem of intelligent initialization for nonconvex problems.
