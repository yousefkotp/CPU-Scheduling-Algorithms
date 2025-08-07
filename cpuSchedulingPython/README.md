# CPU Scheduling Algorithms - Python Implementation

A beginner-friendly Python implementation of 5 basic CPU scheduling algorithms.

## Algorithms Implemented

1. **First-Come, First-Served (FCFS)** - Processes are executed in order of arrival
2. **Shortest Job Next (SJN)** - Always executes the process with shortest service time
3. **Priority Scheduling** - Executes processes based on priority levels
4. **Round Robin (RR)** - Each process gets a fixed time slice (quantum)
5. **Multi-level Queue Scheduling** - Multiple priority queues with different scheduling policies

## How to Use

### Running the Program

```bash
python3 main.py
```

### Input Format

The program reads input from stdin:

1. **Line 1**: "trace" or "stats" - output mode
2. **Line 2**: Algorithm number (1-5) with quantum for RR (e.g., "1" or "4-2")
3. **Line 3**: Last time instant for simulation
4. **Line 4**: Number of processes
5. **Lines 5+**: Process descriptions (name,arrival_time,service_time,priority)

### Example Input

```
trace
1
20
5
A,0,3,1
B,2,6,2
C,4,4,1
D,6,5,3
E,8,2,2
```

### Algorithm Numbers

1. FCFS (First-Come, First-Served)
2. SJN (Shortest Job Next)
3. Priority Scheduling
4. Round Robin (RR) - requires quantum parameter
5. Multi-level Queue Scheduling

### Example Output

For trace mode:
- `*` = process is executing
- `.` = process is waiting
- ` ` (space) = process hasn't arrived yet

For stats mode:
- Process details, finish times, turnaround times, etc.

## File Structure

- `main.py` - Main program entry point
- `parser.py` - Input parsing
- `algorithms.py` - Algorithm implementations
- `output.py` - Output formatting
- `test_example.py` - Test script

## Requirements

- Python 3.6 or higher
- No external libraries needed 