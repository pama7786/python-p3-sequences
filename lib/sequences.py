#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < length:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    print(fib_sequence[:length])

# Test the function
print_fibonacci(9)
