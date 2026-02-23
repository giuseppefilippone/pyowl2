# Summary

Provides a class decorator for timing method execution and a utility for displaying the accumulated performance metrics.

## Description

The core functionality revolves around a class decorator that automatically instruments public methods to track how long they take to run. By wrapping these methods, the system records high-precision timing data alongside truncated representations of the arguments passed during each invocation, accumulating the total duration for every unique method signature in a global dictionary. This approach allows developers to gain insight into performance bottlenecks without manually modifying the logic within the target classes. Once the instrumented code has executed, a separate utility function formats this collected data into a readable grid table, summarizing individual method times and the overall execution duration.
