"""
Output module for CPU Scheduling Algorithms
Handles printing statistics and timeline
"""

import parser

# Algorithm names for display
ALGORITHMS = ["", "FCFS", "SJN", "Priority", "RR", "Multi-Level"]


def print_algorithm(algorithm_index):
    """Print algorithm name with parameters if applicable"""
    algorithm_id = int(parser.algorithms[algorithm_index][0])
    quantum = parser.algorithms[algorithm_index][1]
    
    if algorithm_id == 4:  # Round Robin
        print(f"RR-{quantum}")
    else:
        print(ALGORITHMS[algorithm_id])


def print_processes():
    """Print process names header"""
    print("Process    ", end="")
    for i in range(parser.process_count):
        print(f"|  {parser.get_process_name(parser.processes[i])}  ", end="")
    print("|")


def print_arrival_time():
    """Print arrival times"""
    print("Arrival    ", end="")
    for i in range(parser.process_count):
        print(f"|{parser.get_arrival_time(parser.processes[i]):3d}  ", end="")
    print("|")


def print_service_time():
    """Print service times with mean"""
    print("Service    |", end="")
    sum_service = 0
    for i in range(parser.process_count):
        service_time = parser.get_service_time(parser.processes[i])
        print(f"{service_time:3d}  |", end="")
        sum_service += service_time
    
    mean_service = sum_service / parser.process_count
    print(f" {mean_service:.1f}|")


def print_priority():
    """Print priority levels"""
    print("Priority   |", end="")
    for i in range(parser.process_count):
        priority = parser.get_priority(parser.processes[i])
        print(f"{priority:3d}  |", end="")
    print("|")


def print_finish_time():
    """Print finish times"""
    print("Finish     ", end="")
    for i in range(parser.process_count):
        print(f"|{parser.finish_time[i]:3d}  ", end="")
    print("|-----|")


def print_turn_around_time():
    """Print turnaround times with mean"""
    print("Turnaround |", end="")
    sum_turnaround = 0
    for i in range(parser.process_count):
        print(f"{parser.turn_around_time[i]:3d}  |", end="")
        sum_turnaround += parser.turn_around_time[i]
    
    mean_turnaround = sum_turnaround / len(parser.turn_around_time)
    if mean_turnaround >= 10:
        print(f"{mean_turnaround:.2f}|")
    else:
        print(f" {mean_turnaround:.2f}|")


def print_norm_turn():
    """Print normalized turnaround times with mean"""
    print("NormTurn   |", end="")
    sum_norm_turn = 0
    for i in range(parser.process_count):
        if parser.norm_turn[i] >= 10:
            print(f"{parser.norm_turn[i]:.2f}|", end="")
        else:
            print(f" {parser.norm_turn[i]:.2f}|", end="")
        sum_norm_turn += parser.norm_turn[i]
    
    mean_norm_turn = sum_norm_turn / len(parser.norm_turn)
    if mean_norm_turn >= 10:
        print(f"{mean_norm_turn:.2f}|")
    else:
        print(f" {mean_norm_turn:.2f}|")


def print_stats(algorithm_index):
    """Print complete statistics for an algorithm"""
    print_algorithm(algorithm_index)
    print_processes()
    print_arrival_time()
    print_service_time()
    print_priority()
    print_finish_time()
    print_turn_around_time()
    print_norm_turn()


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