# CPU-Scheduling-Algorithms
Implementation of several CPU scheduling algorithms in C++
## Algorithms
1- First Come First Serve (FCFS)
2- Round Robin with varying time quantum (RR)
3- Shortest Process Next (SPN)
4- Shortest Remaining Time (SRT)
5- Highest Response Ratio Next (HRRN)
6- Feedback (FB)
7- Feedback with varying time quantum (FBV)
8- Aging

## Usage
1- Clone the repository
2- Install g++ compiler and make
```bash
sudo apt-get install g++ make
```
3- Compile the code using `make` command
4- Run the executable file

## Input Format
- Line 1: "trace" or "stats"
- Line 2: a comma-separated list telling which CPU scheduling policies to be analyzed/visualized along with
their parameters, if applicable. Each algorithm is represented by a number as listed in the
introduction section and as shown in the attached testcases.
Round Robin and Aging have a parameter specifying the quantum q to be used. Therefore, a policy
entered as 2-4 means Round Robin with q=4. Also, policy 8-1 means Aging with q=1.
- Line 3: An integer specifying the last instant to be used in your simulation and to be shown on the timeline.
- Line 4: An integer specifying the number of processes to be simulated.
- Line 5: Start of description of processes. Each process is to be described on a separate line. For algorithms 1 through 7, each process is described using a comma-separated list specifying:

    1- String specifying a process name\
    2- Arrival Time\
    3- Service Time

- **Note:** For Aging algorithm (algorithm 8), each process is described using a comma-separated list specifying:

    1- String specifying a process name\
    2- Arrival Time\
    3- Priority
- Check the attached (testcases)[] for more details.


## Contributors
