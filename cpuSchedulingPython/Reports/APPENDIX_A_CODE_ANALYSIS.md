# Appendix A: Detailed Code Analysis

## Line-by-Line Code Explanation

### A.1 Parser Module (parser.py) - Complete Analysis

#### Global Variables Section (Lines 1-20)
```python
# These are the variables that store all our data
# Think of them as boxes where we keep our information
operation = ""  # Will be "trace" or "stats"
last_instant = 0  # How long to run the simulation
process_count = 0  # How many processes we have
algorithms = []  # List of which algorithms to run
processes = []  # List of all our processes
timeline = []  # 2D array to show what happens at each time
process_to_index = {}  # Dictionary to find process by name

# These arrays store the results for each process
finish_time = []  # When each process finishes
turn_around_time = []  # Total time from arrival to finish
norm_turn = []  # Normalized turnaround time
```

**Explanation:**
- **Lines 1-2**: Comments explaining the purpose of global variables
- **Line 3**: `operation` stores the output mode ("trace" for timeline, "stats" for statistics)
- **Line 4**: `last_instant` stores the simulation duration (e.g., 20 time units)
- **Line 5**: `process_count` stores the number of processes to simulate
- **Line 6**: `algorithms` is a list of tuples: [(algorithm_id, quantum), ...]
- **Line 7**: `processes` stores process data as tuples: (name, arrival, service, priority)
- **Line 8**: `timeline` is a 2D array: timeline[time][process] shows what process is doing
- **Line 9**: `process_to_index` maps process names to their array indices
- **Lines 11-13**: Arrays to store results for each process

#### parse_algorithms() Function (Lines 22-40)
```python
def parse_algorithms(algorithm_chunk):
    """Read the algorithm string and figure out which algorithms to run"""
    global algorithms
    algorithms = []  # Start with empty list
    
    # Split by comma if there are multiple algorithms
    for alg in algorithm_chunk.split(','):
        if '-' in alg:
            # This is an algorithm with a number (like Round Robin)
            parts = alg.split('-')
            algorithm_id = parts[0]  # The algorithm number
            quantum = int(parts[1]) if len(parts) > 1 and parts[1] else -1  # The quantum
        else:
            # This is an algorithm without a number
            algorithm_id = alg
            quantum = -1
        
        # Add this algorithm to our list
        algorithms.append((algorithm_id, quantum))
```

**Line-by-line explanation:**
- **Line 22**: Function definition with parameter `algorithm_chunk` (e.g., "1,4-2,3")
- **Line 23**: Docstring explaining function purpose
- **Line 24**: Declare we're modifying the global `algorithms` variable
- **Line 25**: Initialize `algorithms` as empty list
- **Line 27**: Split input by commas to handle multiple algorithms
- **Line 28**: Check if algorithm has quantum parameter (contains "-")
- **Line 29**: Split on "-" to separate algorithm ID from quantum
- **Line 30**: Extract algorithm ID (e.g., "4" from "4-2")
- **Line 31**: Extract quantum, convert to int, handle empty case
- **Line 32**: If no quantum parameter, set quantum to -1
- **Line 33**: Extract algorithm ID from simple format (e.g., "1")
- **Line 34**: Set quantum to -1 for algorithms without quantum
- **Line 37**: Add tuple to algorithms list

#### parse_processes() Function (Lines 42-60)
```python
def parse_processes():
    """Read all the process information from input"""
    global processes, process_to_index
    
    processes = []  # Start with empty list
    process_to_index = {}  # Start with empty dictionary
    
    for i in range(process_count):
        # Read one line of process data
        process_chunk = input().strip()
        parts = process_chunk.split(',')
        
        # Extract the information from the line
        # Format: name,arrival_time,service_time,priority
        process_name = parts[0]
        process_arrival_time = int(parts[1])
        process_service_time = int(parts[2])
        process_priority = int(parts[3]) if len(parts) > 3 else 1
        
        # Store this process
        processes.append((process_name, process_arrival_time, process_service_time, process_priority))
        process_to_index[process_name] = i  # Remember which number this process is
```

**Line-by-line explanation:**
- **Line 42**: Function definition
- **Line 43**: Docstring
- **Line 44**: Declare we're modifying global variables
- **Line 46**: Initialize processes list
- **Line 47**: Initialize name-to-index mapping
- **Line 49**: Loop through each process
- **Line 51**: Read one line of input (e.g., "A,0,3,1")
- **Line 52**: Split by commas to get individual values
- **Line 55**: Extract process name (e.g., "A")
- **Line 56**: Extract arrival time, convert to int (e.g., 0)
- **Line 57**: Extract service time, convert to int (e.g., 3)
- **Line 58**: Extract priority, default to 1 if not provided
- **Line 61**: Store process data as tuple
- **Line 62**: Map process name to its index in the array

#### parse() Function (Lines 64-85)
```python
def parse():
    """Main function that reads all the input and sets up everything"""
    global operation, last_instant, process_count, finish_time, turn_around_time, norm_turn, timeline
    
    # Read the first 4 lines of input
    operation = input().strip()  # "trace" or "stats"
    algorithm_chunk = input().strip()  # Which algorithms to run
    last_instant = int(input().strip())  # How long to run
    process_count = int(input().strip())  # How many processes
    
    # Parse the algorithms and processes
    parse_algorithms(algorithm_chunk)
    parse_processes()
    
    # Set up the result arrays - one slot for each process
    finish_time = [0] * process_count
    turn_around_time = [0] * process_count
    norm_turn = [0.0] * process_count
    
    # Set up the timeline - this is a 2D array like a grid
    # timeline[time][process] shows what process is doing at that time
    timeline = [[' ' for _ in range(process_count)] for _ in range(last_instant)]
```

**Line-by-line explanation:**
- **Line 64**: Function definition
- **Line 65**: Docstring
- **Line 66**: Declare all global variables we'll modify
- **Line 68**: Read operation mode ("trace" or "stats")
- **Line 69**: Read algorithm string (e.g., "1,4-2")
- **Line 70**: Read simulation duration, convert to int
- **Line 71**: Read number of processes, convert to int
- **Line 73**: Call function to parse algorithm string
- **Line 74**: Call function to parse process data
- **Line 76**: Create arrays with one slot per process, initialized to 0
- **Line 77**: Same for turnaround time array
- **Line 78**: Same for normalized turnaround time array (float)
- **Line 80**: Create 2D timeline array: rows = time units, columns = processes
- **Line 81**: Initialize all timeline cells with space character

#### Helper Functions (Lines 87-105)
```python
def get_process_name(process):
    """Get the name of a process"""
    return process[0]

def get_arrival_time(process):
    """Get when a process arrives"""
    return process[1]

def get_service_time(process):
    """Get how long a process needs to run"""
    return process[2]

def get_priority(process):
    """Get the priority of a process"""
    return process[3]
```

**Explanation:**
These are simple accessor functions that extract data from process tuples:
- `process[0]` = name (string)
- `process[1]` = arrival time (integer)
- `process[2]` = service time (integer)
- `process[3]` = priority (integer)

### A.2 Main Module (main.py) - Complete Analysis

#### Imports and Function Definitions (Lines 1-25)
```python
"""
Main module for CPU Scheduling Algorithms
This is the main program that runs everything
"""

import parser
from algorithms import (
    first_come_first_serve, shortest_job_next, priority_scheduling,
    round_robin, multi_level_queue
)
from output import print_timeline, print_stats
```

**Explanation:**
- **Lines 1-4**: Module docstring
- **Line 6**: Import parser module for data access
- **Lines 7-10**: Import all algorithm functions
- **Line 11**: Import output functions

#### execute_algorithm() Function (Lines 14-35)
```python
def execute_algorithm(algorithm_id, quantum, operation):
    """
    Execute the specified algorithm
    This function decides which algorithm to run based on the algorithm_id
    """
    # Print the algorithm name if we're in trace mode
    if operation == "trace":
        if algorithm_id == "1":
            print("FCFS  ", end="")  # First Come First Serve
        elif algorithm_id == "2":
            print("SJN   ", end="")  # Shortest Job Next
        elif algorithm_id == "3":
            print("Priority ", end="")  # Priority Scheduling
        elif algorithm_id == "4":
            print(f"RR-{quantum}  ", end="")  # Round Robin with quantum
        elif algorithm_id == "5":
            print("Multi-Level ", end="")  # Multi-level Queue
    
    # Run the appropriate algorithm based on the algorithm_id
    if algorithm_id == "1":
        first_come_first_serve()
    elif algorithm_id == "2":
        shortest_job_next()
    elif algorithm_id == "3":
        priority_scheduling()
    elif algorithm_id == "4":
        round_robin(quantum)
    elif algorithm_id == "5":
        multi_level_queue()
```

**Line-by-line explanation:**
- **Line 14**: Function definition with three parameters
- **Lines 15-17**: Docstring explaining function purpose
- **Line 19**: Check if we're in trace mode (show timeline)
- **Lines 20-30**: Print appropriate algorithm name for display
- **Line 32**: Comment explaining algorithm selection
- **Lines 33-41**: Call appropriate algorithm function based on ID

#### main() Function (Lines 43-75)
```python
def main():
    """
    Main function - this is where the program starts
    """
    try:
        # Step 1: Read and parse input
        parser.parse()
        
        # Step 2: Extract configuration
        operation = parser.operation
        algorithms = parser.algorithms
        
        # Step 3: Execute each algorithm
        for idx in range(len(algorithms)):
            # Clear the timeline for this algorithm
            parser.clear_timeline()
            
            # Get which algorithm to run and its parameters
            algorithm_id = algorithms[idx][0]  # Which algorithm (1-5)
            quantum = algorithms[idx][1]  # Quantum for Round Robin
            
            # Run the algorithm
            execute_algorithm(algorithm_id, quantum, operation)
            
            # Show the results
            if operation == "trace":
                print_timeline(idx)  # Show the timeline
            elif operation == "stats":
                print_stats(idx)  # Show the statistics
            
            print()  # Empty line between algorithms
            
    except Exception as e:
        # If something goes wrong, show the error
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
```

**Line-by-line explanation:**
- **Line 43**: Function definition
- **Lines 44-46**: Docstring
- **Line 47**: Start try-catch block for error handling
- **Line 49**: Call parser to read and process all input
- **Line 51**: Get operation mode from parser
- **Line 52**: Get algorithm list from parser
- **Line 54**: Loop through each algorithm to run
- **Line 56**: Clear timeline for fresh start
- **Line 58**: Extract algorithm ID from tuple
- **Line 59**: Extract quantum parameter from tuple
- **Line 61**: Call function to run the algorithm
- **Line 63**: Check operation mode
- **Line 64**: Show timeline if in trace mode
- **Line 65**: Show statistics if in stats mode
- **Line 66**: Print empty line for separation
- **Line 68**: Catch any exceptions
- **Line 69**: Print error message
- **Line 70**: Import traceback module
- **Line 71**: Print detailed error information

### A.3 Algorithm Module (algorithms.py) - Key Functions

#### FCFS Algorithm (Lines 8-35)
```python
def first_come_first_serve():
    """
    First Come First Serve (FCFS) algorithm
    The simplest algorithm - just run processes in the order they arrive
    """
    # Start time is when the first process arrives
    current_time = parser.get_arrival_time(parser.processes[0])
    
    # Go through each process in order
    for i in range(parser.process_count):
        process_index = i
        arrival_time = parser.get_arrival_time(parser.processes[i])
        service_time = parser.get_service_time(parser.processes[i])
        
        # Calculate when this process finishes
        parser.finish_time[process_index] = current_time + service_time
        
        # Calculate turnaround time (finish time - arrival time)
        parser.turn_around_time[process_index] = parser.finish_time[process_index] - arrival_time
        
        # Calculate normalized turnaround time
        parser.norm_turn[process_index] = parser.turn_around_time[process_index] / service_time
        
        # Fill in the timeline - mark when process is executing
        for j in range(current_time, parser.finish_time[process_index]):
            parser.timeline[j][process_index] = '*'
        
        # Fill in the timeline - mark when process is waiting
        for j in range(arrival_time, current_time):
            parser.timeline[j][process_index] = '.'
        
        # Move to next process
        current_time += service_time
```

**Key concepts:**
- **Line 10**: Start simulation when first process arrives
- **Line 13**: Process each job in arrival order (FCFS principle)
- **Line 18**: Calculate completion time
- **Line 21**: Calculate total time from arrival to completion
- **Line 24**: Calculate normalized turnaround time (turnaround/service)
- **Lines 26-27**: Mark execution periods with '*'
- **Lines 29-30**: Mark waiting periods with '.'
- **Line 32**: Advance time to next process

#### SJN Algorithm (Lines 37-65)
```python
def shortest_job_next():
    """
    Shortest Job Next (SJN) algorithm
    Always run the process that needs the least time to complete
    """
    # List to keep track of processes that are ready to run
    ready_queue = []
    process_index = 0
    
    # Go through each time step
    for current_time in range(parser.last_instant):
        # Add any newly arrived processes to our ready queue
        while process_index < parser.process_count and parser.get_arrival_time(parser.processes[process_index]) <= current_time:
            service_time = parser.get_service_time(parser.processes[process_index])
            # Add to queue with service time first (so shortest comes first)
            ready_queue.append((service_time, process_index))
            process_index += 1
        
        # Sort the queue so shortest job is first
        ready_queue.sort()
        
        # If there's a process ready, run it
        if ready_queue:
            service_time, process_index_to_execute = ready_queue.pop(0)  # Get the shortest job
            arrival_time = parser.get_arrival_time(parser.processes[process_index_to_execute])
            
            # Fill in wait time in timeline
            for temp in range(arrival_time, current_time):
                parser.timeline[temp][process_index_to_execute] = '.'
            
            # Fill in execution time in timeline
            for temp in range(current_time, current_time + service_time):
                parser.timeline[temp][process_index_to_execute] = '*'
            
            # Calculate metrics
            parser.finish_time[process_index_to_execute] = current_time + service_time
            parser.turn_around_time[process_index_to_execute] = parser.finish_time[process_index_to_execute] - arrival_time
            parser.norm_turn[process_index_to_execute] = parser.turn_around_time[process_index_to_execute] / service_time
            
            # Skip time to when this process finishes
            current_time = current_time + service_time - 1
```

**Key concepts:**
- **Line 42**: Ready queue stores processes waiting to run
- **Line 45**: Check each time step for new arrivals
- **Line 48**: Add new processes to queue with service time first
- **Line 52**: Sort by service time (shortest first)
- **Line 55**: Execute shortest available job
- **Line 56**: Remove shortest job from queue
- **Lines 58-62**: Fill timeline with wait and execution periods
- **Lines 64-66**: Calculate completion metrics
- **Line 68**: Skip time to completion (non-preemptive)

### A.4 Output Module (output.py) - Key Functions

#### print_timeline() Function (Lines 110-130)
```python
def print_timeline(algorithm_index):
    """Print timeline for an algorithm"""
    # Print time header
    for i in range(parser.last_instant + 1):
        print(f"{i % 10} ", end="")
    print()
    
    print("-" * 48)
    
    # Print process timelines
    for i in range(parser.process_count):
        print(f"{parser.get_process_name(parser.processes[i])}     |", end="")
        for j in range(parser.last_instant):
            print(f"{parser.timeline[j][i]}|", end="")
        print()
    
    print("-" * 48)
```

**Line-by-line explanation:**
- **Line 110**: Function definition with algorithm index parameter
- **Line 111**: Docstring
- **Lines 113-115**: Print time numbers (0-9 repeating)
- **Line 117**: Print separator line
- **Line 119**: Loop through each process
- **Line 120**: Print process name and start of timeline
- **Line 121**: Loop through each time unit
- **Line 122**: Print timeline character ('*', '.', or ' ') with border
- **Line 123**: End of process line
- **Line 125**: Print bottom separator line

This detailed analysis shows how every line of code contributes to the overall functionality of the CPU scheduling simulation system. 