# plumbing

## Description

A (Python as a first class citizen) Pipeline programming architecture, with an emphasis on simplicity/ease of use over throughput/parallelisation. This is a programming architecture, not a data processing architecture (although it may be used as one). The
intent is to provide a structured scafolding around general computing, creating a semantic set of primitives to construct sets
of programmatic flows. The structure aims to encourage the use of unit based tasks that lend themselves to be modular and easily
testable. 

The plumbing library provides the following primatives, through which a program may be constructed:
        
<pre><li><b>System</b> : An interconnected series of pipelines, that may branch and join back together. This is the fundamental primitive with which complex behaviour may be composed out of smaller task specific primitive (pipelines)
<br>
<li><b>Pipeline</b> : A task specific primitive that serves a singular purpose. A pipeline may <b>not</b> branch and only has one flow path and direction. A pipeline takes an input (droplet) and processes it through a sequential set of smaller primitives (operations) intended to transform the input in one specific way.
<br>
<li><b>Droplet</b> : A structure containing the data input to and output from a pipeline. Droplets are type sensitive and can only grow (items can only be added not deleted). Once an item is added, it's the items type is set in the droplet and cannot change. Items can be added to droplets at any point and as many items can be added as necessary
<br>
<li><b>Operation</b> : Operations are the fundamental building blocks where the code of a system is actually run. They are, by definition, generators. Operations are required to always output something. If nothing is ready to be output, the operation must output a None. This follows the philosophy of <b>plumbing</b> where all operations and pipelines flow at the same rates. stage of the system, every stage of the pipeline, every single operation produces an output every cycle.
</pre>

The plumbing library also provides some higher level primitives to assist more complex behaviour (such as grouping, aggregation, delays, etc...)

<pre><li><b>Router</b> (system-level) : To be documented
<li><b>Splitter</b> (system-level) : To be documented
<li><b>Combiner</b> (system-level) : To be documented
<li><b>Collector</b> (system-level) : To be documented
<li><b>Register</b> (system-level): To be documented
<li><b>Router</b> (pipeline-level) : To be documented
<li><b>Collector</b> (pipeline-level) : To be documented
<li><b>Delay</b> (pipeline-level) : To be documented
<li><b>Register</b> (pipeline-level) : To be documented
</pre>

## Installation

`pip install plumbing`

or 

`conda install plumbing`

---

## Example

To be written

---

## Documentation

To be written