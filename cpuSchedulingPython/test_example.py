#!/usr/bin/env python3
"""
Test script for CPU Scheduling Algorithms
Demonstrates how to use the program with different inputs
"""

import subprocess
import sys
import os

def test_fcfs():
    """Test First Come First Serve algorithm"""
    print("Testing FCFS algorithm...")
    input_data = """trace
1
20
5
A,0,3,1
B,2,6,2
C,4,4,1
D,6,5,3
E,8,2,2
"""
    
    result = subprocess.run([sys.executable, "main.py"], 
                          input=input_data, 
                          capture_output=True, 
                          text=True)
    
    print("Output:")
    print(result.stdout)
    return result.returncode == 0

def test_sjn():
    """Test Shortest Job Next algorithm"""
    print("\nTesting SJN algorithm...")
    input_data = """trace
2
20
5
A,0,3,1
B,2,6,2
C,4,4,1
D,6,5,3
E,8,2,2
"""
    
    result = subprocess.run([sys.executable, "main.py"], 
                          input=input_data, 
                          capture_output=True, 
                          text=True)
    
    print("Output:")
    print(result.stdout)
    return result.returncode == 0

def test_priority():
    """Test Priority Scheduling algorithm"""
    print("\nTesting Priority Scheduling algorithm...")
    input_data = """trace
3
20
5
A,0,3,1
B,2,6,2
C,4,4,1
D,6,5,3
E,8,2,2
"""
    
    result = subprocess.run([sys.executable, "main.py"], 
                          input=input_data, 
                          capture_output=True, 
                          text=True)
    
    print("Output:")
    print(result.stdout)
    return result.returncode == 0

def test_round_robin():
    """Test Round Robin algorithm"""
    print("\nTesting Round Robin algorithm...")
    input_data = """trace
4-2
20
5
A,0,3,1
B,2,6,2
C,4,4,1
D,6,5,3
E,8,2,2
"""
    
    result = subprocess.run([sys.executable, "main.py"], 
                          input=input_data, 
                          capture_output=True, 
                          text=True)
    
    print("Output:")
    print(result.stdout)
    return result.returncode == 0

def test_multi_level():
    """Test Multi-level Queue algorithm"""
    print("\nTesting Multi-level Queue algorithm...")
    input_data = """trace
5
20
5
A,0,3,1
B,2,6,2
C,4,4,1
D,6,5,3
E,8,2,2
"""
    
    result = subprocess.run([sys.executable, "main.py"], 
                          input=input_data, 
                          capture_output=True, 
                          text=True)
    
    print("Output:")
    print(result.stdout)
    return result.returncode == 0

def test_stats_mode():
    """Test statistics mode"""
    print("\nTesting statistics mode...")
    input_data = """stats
1
20
5
A,0,3,1
B,2,6,2
C,4,4,1
D,6,5,3
E,8,2,2
"""
    
    result = subprocess.run([sys.executable, "main.py"], 
                          input=input_data, 
                          capture_output=True, 
                          text=True)
    
    print("Output:")
    print(result.stdout)
    return result.returncode == 0

def main():
    """Run all tests"""
    print("CPU Scheduling Algorithms - Python Implementation")
    print("=" * 50)
    
    tests = [
        ("FCFS Algorithm", test_fcfs),
        ("SJN Algorithm", test_sjn),
        ("Priority Scheduling", test_priority),
        ("Round Robin", test_round_robin),
        ("Multi-level Queue", test_multi_level),
        ("Statistics Mode", test_stats_mode)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        try:
            if test_func():
                print("✓ PASSED")
                passed += 1
            else:
                print("✗ FAILED")
        except Exception as e:
            print(f"✗ ERROR: {e}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! 🎉")
        return 0
    else:
        print("Some tests failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 