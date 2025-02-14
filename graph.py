import matplotlib.pyplot as graph  # Renamed plt to graph

# Function to generate Fibonacci sequence up to a given number of terms
def generate_fibonacci(n):
    if n < 1:
        return []
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Function to calculate the sum of Fibonacci sequence
def sum_fibonacci(sequence):
    return sum(sequence)

# Function to plot the Fibonacci sequence
def plot_fibonacci(sequence):
    graph.plot(sequence, marker='o', color='blue', linestyle='-', markersize=6)
    graph.title('Fibonacci Sequence')
    graph.xlabel('Index')
    graph.ylabel('Value')
    graph.grid(True)
    graph.show()

# Main function to execute the program
def main():
    n = 15  # Number of Fibonacci numbers to generate
    fibonacci_numbers = generate_fibonacci(n)

    print("Fibonacci Sequence:", fibonacci_numbers)
    print("Sum of Fibonacci Sequence:", sum_fibonacci(fibonacci_numbers))

    plot_fibonacci(fibonacci_numbers)

if __name__ == "__main__":
    main()