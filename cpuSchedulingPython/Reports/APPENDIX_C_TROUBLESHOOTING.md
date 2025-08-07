# Appendix C: Troubleshooting Guide and Advanced Topics

## C.1 Common Issues and Solutions

### C.1.1 Input Format Errors

#### Problem: "IndexError: list index out of range"
**Cause**: Process data format is incorrect
**Solution**: Ensure each process line has exactly 4 values: name,arrival,service,priority

```bash
# Correct format:
A,0,3,1
B,2,6,2
C,4,4,1

# Wrong format:
A,0,3    # Missing priority
A,0,3,1,extra  # Too many values
```

#### Problem: "ValueError: invalid literal for int()"
**Cause**: Non-numeric values in arrival time, service time, or priority
**Solution**: Ensure all numeric fields contain only digits

```bash
# Correct format:
A,0,3,1
B,2,6,2

# Wrong format:
A,zero,3,1  # "zero" is not a number
B,2,6,two   # "two" is not a number
```

### C.1.2 Algorithm Selection Errors

#### Problem: Algorithm not executing
**Cause**: Invalid algorithm ID
**Solution**: Use only algorithm IDs 1-5

```bash
# Valid algorithm IDs:
1  # FCFS
2  # SJN
3  # Priority
4  # Round Robin (requires quantum)
5  # Multi-level Queue

# Invalid:
6  # Not implemented
0  # Not valid
```

#### Problem: Round Robin quantum error
**Cause**: Missing or invalid quantum for Round Robin
**Solution**: Always specify quantum for algorithm 4

```bash
# Correct:
4-2  # Round Robin with quantum 2
4-5  # Round Robin with quantum 5

# Wrong:
4    # Missing quantum
4-0  # Quantum cannot be 0
```

### C.1.3 Output Issues

#### Problem: Timeline not displaying correctly
**Cause**: Timeline array not properly initialized
**Solution**: Check that last_instant and process_count are positive

```bash
# Correct input:
trace
1
20    # Must be > 0
5      # Must be > 0
A,0,3,1
B,2,6,2
C,4,4,1
D,6,5,3
E,8,2,2

# Wrong:
trace
1
0     # Cannot be 0
0     # Cannot be 0
```

#### Problem: Statistics showing incorrect values
**Cause**: Algorithm not calculating metrics properly
**Solution**: Check algorithm implementation for proper metric calculation

### C.1.4 Memory and Performance Issues

#### Problem: Program runs slowly with many processes
**Cause**: Large timeline array consuming memory
**Solution**: Reduce last_instant or process_count

```bash
# For better performance:
trace
1
100   # Reasonable time limit
10     # Reasonable process count
```

#### Problem: "MemoryError" with large inputs
**Cause**: Timeline array too large
**Solution**: Use smaller simulation parameters

## C.2 Advanced Topics

### C.2.1 Extending the System

#### Adding New Algorithms
To add a new algorithm (e.g., Shortest Remaining Time):

1. **Add algorithm function to algorithms.py**:
```python
def shortest_remaining_time():
    """Shortest Remaining Time (SRT) algorithm"""
    # Implementation here
    pass
```

2. **Update main.py**:
```python
from algorithms import (
    first_come_first_serve, shortest_job_next, priority_scheduling,
    round_robin, multi_level_queue, shortest_remaining_time  # Add new import
)

def execute_algorithm(algorithm_id, quantum, operation):
    # Add new case
    elif algorithm_id == "6":
        shortest_remaining_time()
```

3. **Update output.py**:
```python
ALGORITHMS = ["", "FCFS", "SJN", "Priority", "RR", "Multi-Level", "SRT"]
```

#### Adding New Metrics
To add new performance metrics:

1. **Add metric arrays to parser.py**:
```python
# New metric arrays
wait_time = []
response_time = []
```

2. **Calculate metrics in algorithms**:
```python
# Calculate wait time
parser.wait_time[process_index] = current_time - arrival_time
```

3. **Display metrics in output.py**:
```python
def print_wait_time():
    """Print wait times"""
    print("Wait Time  |", end="")
    for i in range(parser.process_count):
        print(f"{parser.wait_time[i]:3d}  |", end="")
    print()
```

### C.2.2 Performance Optimization

#### Optimizing Timeline Generation
Current approach: O(n×t) memory usage
Optimized approach: Generate timeline on-demand

```python
def get_timeline_at_time(time, process):
    """Get timeline state at specific time"""
    # Calculate what process should be running at this time
    # Return appropriate character
    pass
```

#### Optimizing Algorithm Performance
For large numbers of processes:

```python
# Use heap instead of list for better performance
import heapq

def optimized_sjn():
    ready_queue = []  # Use heap for O(log n) operations
    # Implementation with heapq.heappush/heappop
```

### C.2.3 Advanced Data Structures

#### Using Priority Queues
For better performance in priority-based algorithms:

```python
from queue import PriorityQueue

def priority_scheduling_with_queue():
    ready_queue = PriorityQueue()
    
    # Add processes to queue
    ready_queue.put((priority, process_index))
    
    # Get highest priority process
    priority, process_index = ready_queue.get()
```

#### Using Custom Process Classes
For more complex process management:

```python
class Process:
    def __init__(self, name, arrival, service, priority):
        self.name = name
        self.arrival_time = arrival
        self.service_time = service
        self.priority = priority
        self.remaining_time = service
        self.wait_time = 0
    
    def execute(self, time_slice):
        """Execute process for given time slice"""
        executed = min(time_slice, self.remaining_time)
        self.remaining_time -= executed
        return executed
```

### C.2.4 Visualization Enhancements

#### Creating ASCII Art Timelines
Enhanced timeline display:

```python
def print_enhanced_timeline():
    """Print enhanced timeline with better formatting"""
    # Print header with time markers
    print("Time:    ", end="")
    for i in range(0, parser.last_instant, 5):
        print(f"{i:5d}", end="")
    print()
    
    # Print process timelines with better symbols
    for i in range(parser.process_count):
        print(f"{parser.get_process_name(parser.processes[i]):8s}", end="")
        for j in range(parser.last_instant):
            if parser.timeline[j][i] == '*':
                print("█", end="")  # Solid block for execution
            elif parser.timeline[j][i] == '.':
                print("░", end="")  # Light block for waiting
            else:
                print(" ", end="")  # Space for not arrived
        print()
```

#### Adding Color Output
Using ANSI color codes:

```python
def print_colored_timeline():
    """Print timeline with colors"""
    colors = {
        '*': '\033[92m',  # Green for execution
        '.': '\033[93m',  # Yellow for waiting
        ' ': '\033[0m'    # Reset for not arrived
    }
    
    for i in range(parser.process_count):
        print(f"{parser.get_process_name(parser.processes[i]):8s}", end="")
        for j in range(parser.last_instant):
            char = parser.timeline[j][i]
            print(f"{colors[char]}{char}\033[0m", end="")
        print()
```

### C.2.5 Testing and Validation

#### Unit Testing
Create comprehensive test suite:

```python
import unittest

class TestSchedulingAlgorithms(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.processes = [
            ("A", 0, 3, 1),
            ("B", 2, 6, 2),
            ("C", 4, 4, 1)
        ]
    
    def test_fcfs_calculation(self):
        """Test FCFS algorithm calculations"""
        # Test implementation
        pass
    
    def test_sjn_optimality(self):
        """Test that SJN gives optimal average wait time"""
        # Test implementation
        pass
    
    def test_round_robin_fairness(self):
        """Test that RR gives fair time distribution"""
        # Test implementation
        pass
```

#### Performance Testing
Test algorithm performance with different inputs:

```python
def performance_test():
    """Test algorithm performance with various inputs"""
    test_cases = [
        (5, 20),   # Small test
        (10, 50),  # Medium test
        (20, 100), # Large test
    ]
    
    for processes, time in test_cases:
        print(f"Testing with {processes} processes, {time} time units")
        # Run performance test
        pass
```

### C.2.6 Advanced Algorithm Implementations

#### Preemptive SJN (Shortest Remaining Time)
```python
def shortest_remaining_time():
    """Preemptive version of SJN"""
    ready_queue = []  # (remaining_time, process_index)
    process_index = 0
    
    for current_time in range(parser.last_instant):
        # Add new arrivals
        while (process_index < parser.process_count and 
               parser.get_arrival_time(parser.processes[process_index]) <= current_time):
            service_time = parser.get_service_time(parser.processes[process_index])
            heapq.heappush(ready_queue, (service_time, process_index))
            process_index += 1
        
        if ready_queue:
            remaining_time, process_index_to_execute = heapq.heappop(ready_queue)
            
            # Execute for 1 time unit
            parser.timeline[current_time][process_index_to_execute] = '*'
            remaining_time -= 1
            
            if remaining_time > 0:
                # Put back in queue
                heapq.heappush(ready_queue, (remaining_time, process_index_to_execute))
            else:
                # Process completed
                parser.finish_time[process_index_to_execute] = current_time + 1
                # Calculate metrics
```

#### Aging Priority Scheduling
```python
def aging_priority_scheduling():
    """Priority scheduling with aging to prevent starvation"""
    ready_queue = []  # (priority, age, process_index)
    process_index = 0
    
    for current_time in range(parser.last_instant):
        # Add new arrivals
        while (process_index < parser.process_count and 
               parser.get_arrival_time(parser.processes[process_index]) <= current_time):
            priority = parser.get_priority(parser.processes[process_index])
            heapq.heappush(ready_queue, (priority, 0, process_index))
            process_index += 1
        
        # Age all waiting processes
        aged_queue = []
        for priority, age, proc_idx in ready_queue:
            new_age = age + 1
            new_priority = max(0, priority - (new_age // 10))  # Age every 10 time units
            heapq.heappush(aged_queue, (new_priority, new_age, proc_idx))
        ready_queue = aged_queue
        
        if ready_queue:
            priority, age, process_index_to_execute = heapq.heappop(ready_queue)
            # Execute process
            # ... implementation
```

## C.3 Debugging Techniques

### C.3.1 Adding Debug Output
```python
def debug_algorithm():
    """Algorithm with debug output"""
    print(f"Debug: Starting algorithm with {parser.process_count} processes")
    
    for i in range(parser.process_count):
        process = parser.processes[i]
        print(f"Debug: Process {i}: {process}")
    
    # ... algorithm implementation
```

### C.3.2 Timeline Visualization Debug
```python
def debug_timeline():
    """Print timeline with debug information"""
    print("Debug: Timeline array:")
    for time in range(parser.last_instant):
        print(f"Time {time:2d}: ", end="")
        for proc in range(parser.process_count):
            print(f"{parser.timeline[time][proc]} ", end="")
        print()
```

### C.3.3 Performance Profiling
```python
import time

def profile_algorithm(algorithm_func):
    """Profile algorithm execution time"""
    start_time = time.time()
    algorithm_func()
    end_time = time.time()
    
    print(f"Algorithm execution time: {end_time - start_time:.4f} seconds")
```

## C.4 Best Practices

### C.4.1 Code Organization
- Keep algorithms modular and independent
- Use clear variable names
- Add comprehensive comments
- Implement proper error handling

### C.4.2 Testing Strategy
- Test with edge cases (0 processes, 1 process, etc.)
- Test with various input sizes
- Validate algorithm correctness
- Performance testing with large inputs

### C.4.3 Documentation
- Document all functions and classes
- Include usage examples
- Explain algorithm complexity
- Provide troubleshooting guides

This comprehensive guide covers common issues, advanced topics, and best practices for working with the CPU scheduling algorithms project. 