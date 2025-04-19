import os
import sys

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.data_loader import load_exit_poll_data
from utils.calculator import calculate_weighted_results
from scripts.visualization import visualize_results

def main():
    """
    Main function to run the exit poll calculation and visualization
    """
    print("Starting exit poll calculation...")
    
    # Load the exit poll data
    data = load_exit_poll_data()
    
    # Calculate weighted results
    results = calculate_weighted_results(data)
    
    # Display the results
    print("\nExit Poll Results:")
    print("-----------------")
    for candidate, percentage in sorted(results.items(), key=lambda x: x[1], reverse=True):
        print(f"{candidate}: {percentage:.2f}%")
    
    # Generate visualizations
    print("\nGenerating visualizations...")
    visualization_files = visualize_results(data, results)
    
    print("\nExit poll calculation and visualization complete!")
    print(f"Visualization files saved in the 'output' directory.")
    
    return results, visualization_files

if __name__ == "__main__":
    main()