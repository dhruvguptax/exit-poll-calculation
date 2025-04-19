import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

# Add parent directory to path to import modules from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.data_loader import load_exit_poll_data
from utils.calculator import calculate_weighted_results

def create_bar_chart(results, title="Exit Poll Results"):
    """
    Create a bar chart visualization of exit poll results
    
    Args:
        results (dict): Dictionary with candidates as keys and vote percentages as values
        title (str): Title of the chart
    """
    candidates = list(results.keys())
    percentages = list(results.values())
    
    # Sort by percentage (descending)
    sorted_data = sorted(zip(candidates, percentages), key=lambda x: x[1], reverse=True)
    candidates = [x[0] for x in sorted_data]
    percentages = [x[1] for x in sorted_data]
    
    plt.figure(figsize=(12, 8))
    bars = plt.bar(candidates, percentages, color=['blue', 'red', 'green', 'orange', 'purple', 'brown'][:len(candidates)])
    
    # Add percentage labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                 f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.ylabel('Vote Percentage (%)', fontsize=12)
    plt.xlabel('Candidates', fontsize=12)
    plt.ylim(0, max(percentages) * 1.15)  # Add some space for percentage labels
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    return plt

def create_pie_chart(results, title="Exit Poll Results by Candidate"):
    """
    Create a pie chart visualization of exit poll results
    
    Args:
        results (dict): Dictionary with candidates as keys and vote percentages as values
        title (str): Title of the chart
    """
    candidates = list(results.keys())
    percentages = list(results.values())
    
    plt.figure(figsize=(10, 8))
    plt.pie(percentages, labels=candidates, autopct='%1.1f%%', 
            startangle=90, shadow=True, 
            colors=['blue', 'red', 'green', 'orange', 'purple', 'brown'][:len(candidates)])
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title(title, fontsize=16, fontweight='bold')
    
    return plt

def create_demographic_breakdown(data, demographic_column, candidates):
    """
    Create a demographic breakdown visualization showing how different demographics voted
    
    Args:
        data (pd.DataFrame): DataFrame containing exit poll data
        demographic_column (str): Column name for the demographic to analyze
        candidates (list): List of candidate names
    """
    # Group data by demographic and calculate average support for each candidate
    demographic_breakdown = {}
    
    for demo_value in data[demographic_column].unique():
        filtered_data = data[data[demographic_column] == demo_value]
        demo_results = {}
        
        for candidate in candidates:
            if f"vote_{candidate}" in data.columns:
                demo_results[candidate] = filtered_data[f"vote_{candidate}"].mean() * 100
        
        demographic_breakdown[demo_value] = demo_results
    
    # Create a grouped bar chart
    demographics = list(demographic_breakdown.keys())
    x = np.arange(len(demographics))
    width = 0.8 / len(candidates)
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    for i, candidate in enumerate(candidates):
        values = [demographic_breakdown[demo][candidate] for demo in demographics]
        offset = width * i - width * (len(candidates) - 1) / 2
        ax.bar(x + offset, values, width, label=candidate)
    
    ax.set_xlabel('Demographics')
    ax.set_ylabel('Support (%)')
    ax.set_title(f'Exit Poll Results by {demographic_column}')
    ax.set_xticks(x)
    ax.set_xticklabels(demographics)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    return plt

def save_visualization(plt, filename):
    """
    Save the visualization to a file
    
    Args:
        plt: Matplotlib plot object
        filename (str): Output filename
    """
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, filename)
    plt.savefig(output_path)
    print(f"Visualization saved to {output_path}")
    
    return output_path

def visualize_results(data=None, weighted_results=None):
    """
    Main function to create and save visualizations
    
    Args:
        data (pd.DataFrame, optional): Exit poll data 
        weighted_results (dict, optional): Pre-calculated weighted results
    
    Returns:
        dict: Paths to saved visualization files
    """
    if data is None:
        data = load_exit_poll_data()
    
    if weighted_results is None:
        weighted_results = calculate_weighted_results(data)
    
    output_files = {}
    
    # Create and save bar chart
    bar_chart = create_bar_chart(weighted_results)
    bar_chart_path = save_visualization(bar_chart, 'exit_poll_bar_chart.png')
    output_files['bar_chart'] = bar_chart_path
    
    # Create and save pie chart
    pie_chart = create_pie_chart(weighted_results)
    pie_chart_path = save_visualization(pie_chart, 'exit_poll_pie_chart.png')
    output_files['pie_chart'] = pie_chart_path
    
    # Identify candidate columns and extract candidate names
    candidate_cols = [col for col in data.columns if col.startswith('vote_')]
    candidates = [col.replace('vote_', '') for col in candidate_cols]
    
    # Create demographic breakdowns if demographic data is available
    demographic_columns = ['age_group', 'gender', 'education', 'income', 'ethnicity']
    for demo_col in demographic_columns:
        if demo_col in data.columns:
            demo_chart = create_demographic_breakdown(data, demo_col, candidates)
            demo_chart_path = save_visualization(demo_chart, f'exit_poll_{demo_col}_breakdown.png')
            output_files[f'{demo_col}_breakdown'] = demo_chart_path
    
    return output_files

if __name__ == "__main__":
    # Load data
    data = load_exit_poll_data()
    
    # Calculate weighted results
    weighted_results = calculate_weighted_results(data)
    
    # Create visualizations
    visualize_results(data, weighted_results)
    
    print("Visualization complete!")