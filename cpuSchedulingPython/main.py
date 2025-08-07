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


def main():
    """
    Main function - this is where the program starts
    """
    try:
        # Step 1: Read all the input data
        parser.parse()
        
        # Step 2: Get the data we need
        operation = parser.operation  # "trace" or "stats"
        algorithms = parser.algorithms  # List of algorithms to run
        
        # Step 3: Run each algorithm
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


# This is where the program starts when you run it
if __name__ == "__main__":
    main() 