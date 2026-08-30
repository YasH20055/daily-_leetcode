"""
Rectangle Pattern Generator using Nested Loops
Prints a rectangle pattern with configurable rows and columns.
"""

def print_rectangle(rows=3, cols=4, symbol="*"):
    """
    Print a rectangle pattern.
    
    Args:
        rows (int): Number of rows in the rectangle
        cols (int): Number of columns in the rectangle
        symbol (str): Character to use for the pattern
    """
    for i in range(rows):
        for j in range(cols):
            print(symbol, end=" ")
        print()


if __name__ == "__main__":
    # Example usage
    print_rectangle(3, 4, "*")