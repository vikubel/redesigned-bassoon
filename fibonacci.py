"""
Fibonacci Series Program
Generates Fibonacci numbers and handles large numbers efficiently.
"""


def fibonacci_series(n):
    """
    Generate the first n Fibonacci numbers.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Returns:
        list: List containing the first n Fibonacci numbers
        
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("n must be greater than 0")
    
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    
    return fib_series


def fibonacci_nth(n):
    """
    Find the nth Fibonacci number (0-indexed).
    
    Args:
        n (int): Index of the Fibonacci number to find (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is less than 0
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def fibonacci_series_generator(n):
    """
    Generator function for Fibonacci series (memory efficient for large n).
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Yields:
        int: Next Fibonacci number in the series
        
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("n must be greater than 0")
    
    a, b = 0, 1
    count = 0
    
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def main():
    """Main function to demonstrate Fibonacci functions."""
    print("=" * 60)
    print("FIBONACCI SERIES PROGRAM")
    print("=" * 60)
    
    # Example 1: Generate first 10 Fibonacci numbers
    print("\n1. First 10 Fibonacci numbers:")
    print(fibonacci_series(10))
    
    # Example 2: Find the 15th Fibonacci number
    print("\n2. The 15th Fibonacci number (0-indexed):")
    print(fibonacci_nth(15))
    
    # Example 3: Generate first 20 Fibonacci numbers
    print("\n3. First 20 Fibonacci numbers:")
    series = fibonacci_series(20)
    print(series)
    
    # Example 4: Handle large numbers - 50th Fibonacci number
    print("\n4. The 50th Fibonacci number (0-indexed):")
    large_fib = fibonacci_nth(50)
    print(f"{large_fib}")
    
    # Example 5: Handle large numbers - 100th Fibonacci number
    print("\n5. The 100th Fibonacci number (0-indexed):")
    very_large_fib = fibonacci_nth(100)
    print(f"{very_large_fib}")
    
    # Example 6: Using generator for memory efficiency with large numbers
    print("\n6. First 25 Fibonacci numbers using generator (memory efficient):")
    fib_gen = list(fibonacci_series_generator(25))
    print(fib_gen)
    
    # Example 7: Interactive mode
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE")
    print("=" * 60)
    
    try:
        choice = input("\nWhat would you like to do?\n1. Generate first N Fibonacci numbers\n2. Find the Nth Fibonacci number\nEnter choice (1 or 2): ").strip()
        
        if choice == "1":
            n = int(input("Enter N (number of Fibonacci numbers to generate): "))
            result = fibonacci_series(n)
            print(f"\nFirst {n} Fibonacci numbers:")
            print(result)
        
        elif choice == "2":
            n = int(input("Enter N (index of Fibonacci number to find, 0-indexed): "))
            result = fibonacci_nth(n)
            print(f"\nThe {n}th Fibonacci number (0-indexed): {result}")
        
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
