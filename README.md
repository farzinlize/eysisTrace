# Trace Simulation
A trace simulation with [Booksim 2.0](https://github.com/booksim/booksim2) using Eyeriss Log file. This report includes our experiments on AlexaNet application and provided missing documentations about `workload` module in booksim.

## Trace file
Our trace file contains eyeriss logs, indicating multiprocessor running codes for a specific application including execution, communication and off-chip transfers. It could be found that any off-chip communication time are omitted and the corresponding log considered as finished cycle number. It's because there is only one cycle delay between an off-chip transfer and using on-chip information. Also it is considered that all processing elements (PE) can received their information (`input` and `weight`) in one clock cycle.

**One cycle load**: As the trace file shows, loaded data on PEs spend one clock cycle and there is no described module (sender) in charge of loading desired data from on-chip memory (SRAM) to PEs local memory (registers) 
To simulate the trace file in a way that matches eyeriss log, we consider a global node that is directly connected to all PEs.

## Topology
The trace file was captured on a 2D-mesh with different radix 12×14. First we ran the simulation on a 13×13 mesh to cover all its nodes and it shows that our simulation suffers from wrong node allocation due to integer ids of PEs differs in row and column between two topology. 

### Booksim Anynet
We use anynet configuration to simulate 12×14 mesh that matches the captured trace topology on eyeriss. There is a script in python called `maker.py` that generates anynet configuration of a 2D-mesh with different radix. 

## Results
