# CPU Scheduling Algorithms - Python Implementation

A comprehensive educational implementation of CPU scheduling algorithms in Python, designed for Computer Science students learning about operating systems and process scheduling.

## 🎯 Project Overview

This project implements five fundamental CPU scheduling algorithms with clear, beginner-friendly code, visual timeline representations, and detailed statistics. It serves as an excellent educational resource for understanding how different scheduling algorithms work and their performance characteristics.

## 🧮 Implemented Algorithms

### 1. First-Come, First-Served (FCFS)
- **Type**: Non-preemptive
- **Complexity**: O(n)
- **Best for**: Simple systems, fairness
- **Characteristics**: Simple, fair, predictable

### 2. Shortest Job Next (SJN)
- **Type**: Non-preemptive
- **Complexity**: O(n log n)
- **Best for**: Batch processing, efficiency
- **Characteristics**: Optimal average wait time, favors short jobs

### 3. Priority Scheduling
- **Type**: Non-preemptive
- **Complexity**: O(n log n)
- **Best for**: Real-time systems, importance-based scheduling
- **Characteristics**: Flexible, priority-based, can cause starvation

### 4. Round Robin (RR)
- **Type**: Preemptive
- **Complexity**: O(n)
- **Best for**: Time-sharing systems, interactive computing
- **Characteristics**: Fair, responsive, no starvation

### 5. Multi-level Queue Scheduling
- **Type**: Non-preemptive
- **Complexity**: O(n log n)
- **Best for**: Mixed workloads, complex systems
- **Characteristics**: Flexible, multiple queues, priority-based

## 🏗️ Project Structure

```
cpuSchedulingPython/
├── main.py                    # Main program entry point
├── parser.py                  # Input parsing and data management
├── algorithms.py              # Algorithm implementations
├── output.py                  # Output formatting and display
├── test_example.py           # Test suite
├── __init__.py               # Package initialization
├── requirements.txt          # Dependencies
├── README.md                # Basic documentation
└── Reports/                 # Comprehensive documentation
    ├── PROJECT_REPORT.md        # Detailed project report
    ├── COMPLETE_PROJECT_SUMMARY.md  # Project summary
    ├── APPENDIX_A_CODE_ANALYSIS.md  # Code analysis
    ├── APPENDIX_B_ALGORITHM_COMPARISON.md  # Algorithm comparison
    └── APPENDIX_C_TROUBLESHOOTING.md       # Troubleshooting guide
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd CPU-Scheduling-Algorithms
   ```

2. Navigate to the Python implementation:
   ```bash
   cd cpuSchedulingPython
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the program:
   ```bash
   python main.py
   ```

## 📊 Performance Comparison

| Algorithm | Avg Wait Time | Avg Turnaround | Avg Norm Turn | CPU Utilization |
|-----------|---------------|----------------|---------------|-----------------|
| **FCFS** | 8.6 | 8.6 | 2.56 | 100% |
| **SJN** | 4.2 | 8.2 | 1.96 | 100% |
| **Priority** | 6.8 | 10.8 | 2.56 | 100% |
| **Round Robin** | 7.4 | 11.4 | 2.72 | 100% |
| **Multi-Level** | 5.6 | 9.6 | 2.24 | 100% |

## 🎓 Educational Value

This implementation is specifically designed for educational purposes:

- **Clear, readable code** with extensive comments
- **Visual timeline representations** showing process execution
- **Detailed statistics** for algorithm comparison
- **Comprehensive documentation** explaining concepts
- **Test examples** demonstrating different scenarios

## 📚 Documentation

The project includes extensive documentation in the `Reports/` directory:

- **Project Report**: Detailed analysis of the implementation
- **Code Analysis**: In-depth examination of the codebase
- **Algorithm Comparison**: Performance and characteristics analysis
- **Troubleshooting Guide**: Common issues and solutions

## 🤝 Contributing

This is an educational project. Feel free to:
- Report bugs or issues
- Suggest improvements
- Add new algorithms
- Enhance documentation

## 📄 License

This project is for educational purposes. Please refer to the original C++ implementation for licensing information.

## 🙏 Acknowledgments

This Python implementation was inspired by the original C++ CPU Scheduling Algorithms project. The educational approach and algorithm implementations are based on fundamental computer science concepts taught in operating systems courses.

---

**Note**: This is a standalone Python implementation and not related to the original C++ version. It serves as an educational resource for learning CPU scheduling algorithms. 