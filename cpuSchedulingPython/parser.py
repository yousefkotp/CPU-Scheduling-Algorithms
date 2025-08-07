"""
Parser module for CPU Scheduling Algorithms
This file reads the input and stores all the data we need
"""

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


def clear_timeline():
    """Clear the timeline - fill it with spaces"""
    global timeline
    timeline = [[' ' for _ in range(process_count)] for _ in range(last_instant)]


def fill_in_wait_time():
    """Fill in the wait times in the timeline with dots"""
    for i in range(process_count):
        arrival_time = get_arrival_time(processes[i])
        for k in range(arrival_time, finish_time[i]):
            if timeline[k][i] != '*':  # If not executing, then waiting
                timeline[k][i] = '.' 