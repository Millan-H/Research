def next_collatz_number(n):
    """
    Calculate the next number in the Collatz sequence.
    If n is even, divide by 2.
    If n is odd, multiply by 3 and add 1.
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 2*n + 2

def check_412_loop(start_num, max_iterations=10000):
    """
    Check if the Collatz sequence starting from start_num enters the 4-1-2 loop.
    
    Parameters:
        start_num (int): The starting number to check
        max_iterations (int): Maximum number of iterations before giving up
        
    Returns:
        tuple: (bool, list) - (whether it enters the 4-1-2 loop, sequence until loop or max_iterations)
    """
    if not isinstance(start_num, int) or start_num < 1:
        raise ValueError("Starting number must be a positive integer")
        
    sequence = [start_num]
    seen_numbers = set([start_num])
    current = start_num
    
    for _ in range(max_iterations):
        current = next_collatz_number(current)
        sequence.append(current)
        
        # Check if we've entered the 4-1-2 loop
        if current in (4, 2, 1):
            # Look ahead to confirm it's the 4-1-2 loop
            next_num = next_collatz_number(current)
            if next_num in (4, 2, 1):
                return True, sequence
                
        # Check if we've seen this number before (caught in a different loop)
        if current in seen_numbers:
            return False, sequence
            
        seen_numbers.add(current)
    
    # If we reach max iterations without finding the 4-1-2 loop
    return False, sequence

def main():
    # Example usage
    anomalies=[]

    for num in range(1,500000000):
        enters_loop, sequence = check_412_loop(num)
        print(f"{num}: {enters_loop}")
        if not enters_loop:
            anomalies.append(num)
            print("added")
    return anomalies

if __name__ == "__main__":
    anomalies=main()
    print(f"Anomalies: {anomalies}")
    print("Anomaly Count: ", len(anomalies))
    if len(anomalies)==0:
        print("No anomalies")