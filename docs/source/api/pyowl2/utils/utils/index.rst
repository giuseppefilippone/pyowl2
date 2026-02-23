pyowl2.utils.utils
==================

.. py:module:: pyowl2.utils.utils



.. ── LLM-GENERATED DESCRIPTION START ──

Provides a class decorator for timing method execution and a utility for displaying the accumulated performance metrics.


Description
-----------


The core functionality revolves around a class decorator that automatically instruments public methods to track how long they take to run. By wrapping these methods, the system records high-precision timing data alongside truncated representations of the arguments passed during each invocation, accumulating the total duration for every unique method signature in a global dictionary. This approach allows developers to gain insight into performance bottlenecks without manually modifying the logic within the target classes. Once the instrumented code has executed, a separate utility function formats this collected data into a readable grid table, summarizing individual method times and the overall execution duration.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   pyowl2.utils.utils.execution_log


Functions
---------

.. autoapisummary::

   pyowl2.utils.utils.print_execution_log
   pyowl2.utils.utils.timer_decorator


Module Contents
---------------

.. py:function:: print_execution_log()

   Formats and displays the current execution log as a readable grid table using the tabulate library. The output includes the function name, execution time, arguments, and keyword arguments for each recorded method call, followed by a summary of the total elapsed time across all entries. If the execution log is empty, the function prints a message indicating that no timing data is available. This function performs side effects by writing to standard output and does not return a value.


.. py:function:: timer_decorator(cls)

   This class decorator instruments a class by wrapping its public, non-dunder methods to measure and log their execution performance. Upon application, it iterates through the class's attributes, identifying callable members that do not start with double underscores, and replaces them with a wrapper that records the elapsed time using high-resolution timers. The wrapper accumulates the total execution time for each method in a global dictionary named `execution_log`, associating it with the fully qualified method name and truncated representations of the passed arguments and keyword arguments. While the decorator modifies the global log state and the class's method attributes, it ensures the original method's behavior and return values are preserved.

   :param cls: The class whose methods will be timed and logged.
   :type cls: typing.Any


.. py:data:: execution_log
   :type:  dict[str, dict]
