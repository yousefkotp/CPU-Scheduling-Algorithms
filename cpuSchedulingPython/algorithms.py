"""
CPU Scheduling Algorithms Implementation
This file contains the 5 basic scheduling algorithms
Each algorithm decides which process to run next
"""

import parser

# We'll use simple lists instead of complex data structures
# This makes it easier for beginners to understand


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


def priority_scheduling():
    """
    Priority Scheduling algorithm
    Always run the process with the highest priority (lowest number)
    """
    # List to keep track of processes that are ready to run
    ready_queue = []
    process_index = 0
    
    # Go through each time step
    for current_time in range(parser.last_instant):
        # Add any newly arrived processes to our ready queue
        while process_index < parser.process_count and parser.get_arrival_time(parser.processes[process_index]) <= current_time:
            priority = parser.get_priority(parser.processes[process_index])
            # Add to queue with priority first (so highest priority comes first)
            ready_queue.append((priority, process_index))
            process_index += 1
        
        # Sort the queue so highest priority is first
        ready_queue.sort()
        
        # If there's a process ready, run it
        if ready_queue:
            priority, process_index_to_execute = ready_queue.pop(0)  # Get the highest priority job
            arrival_time = parser.get_arrival_time(parser.processes[process_index_to_execute])
            service_time = parser.get_service_time(parser.processes[process_index_to_execute])
            
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


def round_robin(quantum):
    """
    Round Robin (RR) algorithm
    Each process gets a fixed amount of time (quantum) to run
    """
    # List to keep track of processes that are ready to run
    ready_queue = []
    process_index = 0
    
    # Add first process if it arrives at time 0
    if parser.get_arrival_time(parser.processes[0]) == 0:
        ready_queue.append((0, parser.get_service_time(parser.processes[0])))
        process_index += 1
    
    current_quantum = quantum
    
    # Go through each time step
    for current_time in range(parser.last_instant):
        if ready_queue:
            # Get next process from queue
            process_index_to_execute, remaining_time = ready_queue.pop(0)
            remaining_time -= 1  # Process runs for 1 time unit
            current_quantum -= 1  # Quantum decreases by 1
            
            arrival_time = parser.get_arrival_time(parser.processes[process_index_to_execute])
            service_time = parser.get_service_time(parser.processes[process_index_to_execute])
            
            # Mark this time slot as execution
            parser.timeline[current_time][process_index_to_execute] = '*'
            
            # Add any new arrivals to queue
            while process_index < parser.process_count and parser.get_arrival_time(parser.processes[process_index]) == current_time + 1:
                ready_queue.append((process_index, parser.get_service_time(parser.processes[process_index])))
                process_index += 1
            
            # Check if process finished or quantum expired
            if current_quantum == 0 and remaining_time == 0:
                # Process completed
                parser.finish_time[process_index_to_execute] = current_time + 1
                parser.turn_around_time[process_index_to_execute] = parser.finish_time[process_index_to_execute] - arrival_time
                parser.norm_turn[process_index_to_execute] = parser.turn_around_time[process_index_to_execute] / service_time
                current_quantum = quantum  # Reset quantum
            elif current_quantum == 0 and remaining_time != 0:
                # Quantum expired, add back to end of queue
                ready_queue.append((process_index_to_execute, remaining_time))
                current_quantum = quantum  # Reset quantum
            elif current_quantum != 0 and remaining_time == 0:
                # Process completed before quantum expired
                parser.finish_time[process_index_to_execute] = current_time + 1
                parser.turn_around_time[process_index_to_execute] = parser.finish_time[process_index_to_execute] - arrival_time
                parser.norm_turn[process_index_to_execute] = parser.turn_around_time[process_index_to_execute] / service_time
                current_quantum = quantum  # Reset quantum
        
        # Add any new arrivals to queue
        while process_index < parser.process_count and parser.get_arrival_time(parser.processes[process_index]) == current_time + 1:
            ready_queue.append((process_index, parser.get_service_time(parser.processes[process_index])))
            process_index += 1
    
    # Fill in wait times
    parser.fill_in_wait_time()


def multi_level_queue():
    """
    Multi-level Queue Scheduling algorithm
    We have 3 different queues for different priority levels
    Always check high priority first, then medium, then low
    """
    # Create three different queues for different priority levels
    high_priority_queue = []  # Priority 1 (highest)
    medium_priority_queue = []  # Priority 2
    low_priority_queue = []  # Priority 3 (lowest)
    
    process_index = 0
    
    # Go through each time step
    for current_time in range(parser.last_instant):
        # Add any newly arrived processes to the appropriate queue
        while process_index < parser.process_count and parser.get_arrival_time(parser.processes[process_index]) <= current_time:
            priority = parser.get_priority(parser.processes[process_index])
            service_time = parser.get_service_time(parser.processes[process_index])
            
            # Put process in the right queue based on priority
            if priority == 1:
                high_priority_queue.append((service_time, process_index))
            elif priority == 2:
                medium_priority_queue.append((service_time, process_index))
            else:
                low_priority_queue.append((service_time, process_index))
            
            process_index += 1
        
        # Sort each queue so shortest jobs come first
        high_priority_queue.sort()
        medium_priority_queue.sort()
        low_priority_queue.sort()
        
        # Execute from highest priority queue first
        if high_priority_queue:
            service_time, process_index_to_execute = high_priority_queue.pop(0)
            arrival_time = parser.get_arrival_time(parser.processes[process_index_to_execute])
            
            # Fill wait time
            for temp in range(arrival_time, current_time):
                parser.timeline[temp][process_index_to_execute] = '.'
            
            # Fill execution time
            for temp in range(current_time, current_time + service_time):
                parser.timeline[temp][process_index_to_execute] = '*'
            
            # Calculate metrics
            parser.finish_time[process_index_to_execute] = current_time + service_time
            parser.turn_around_time[process_index_to_execute] = parser.finish_time[process_index_to_execute] - arrival_time
            parser.norm_turn[process_index_to_execute] = parser.turn_around_time[process_index_to_execute] / service_time
            
            current_time = current_time + service_time - 1
            
        elif medium_priority_queue:
            service_time, process_index_to_execute = medium_priority_queue.pop(0)
            arrival_time = parser.get_arrival_time(parser.processes[process_index_to_execute])
            
            # Fill wait time
            for temp in range(arrival_time, current_time):
                parser.timeline[temp][process_index_to_execute] = '.'
            
            # Fill execution time
            for temp in range(current_time, current_time + service_time):
                parser.timeline[temp][process_index_to_execute] = '*'
            
            # Calculate metrics
            parser.finish_time[process_index_to_execute] = current_time + service_time
            parser.turn_around_time[process_index_to_execute] = parser.finish_time[process_index_to_execute] - arrival_time
            parser.norm_turn[process_index_to_execute] = parser.turn_around_time[process_index_to_execute] / service_time
            
            current_time = current_time + service_time - 1
            
        elif low_priority_queue:
            service_time, process_index_to_execute = low_priority_queue.pop(0)
            arrival_time = parser.get_arrival_time(parser.processes[process_index_to_execute])
            
            # Fill wait time
            for temp in range(arrival_time, current_time):
                parser.timeline[temp][process_index_to_execute] = '.'
            
            # Fill execution time
            for temp in range(current_time, current_time + service_time):
                parser.timeline[temp][process_index_to_execute] = '*'
            
            # Calculate metrics
            parser.finish_time[process_index_to_execute] = current_time + service_time
            parser.turn_around_time[process_index_to_execute] = parser.finish_time[process_index_to_execute] - arrival_time
            parser.norm_turn[process_index_to_execute] = parser.turn_around_time[process_index_to_execute] / service_time
            
            current_time = current_time + service_time - 1 