# Program to read data from file and plot graph
import matplotlib.pyplot as plt
import numpy as np

# Create sample data file
def create_sample_data():
    data = """Year,Sales,Profit
2020,100,20
2021,150,35
2022,200,50
2023,180,45
2024,250,70"""
    
    with open('sales_data.csv', 'w') as f:
        f.write(data)
    print("Sample data file 'sales_data.csv' created")

# Read and plot data
def plot_from_file():
    try:
        # Read data from file
        years = []
        sales = []
        profits = []
        
        with open('sales_data.csv', 'r') as f:
            lines = f.readlines()
            header = lines[0].strip().split(',')
            for line in lines[1:]:
                data = line.strip().split(',')
                years.append(int(data[0]))
                sales.append(float(data[1]))
                profits.append(float(data[2]))
        
        # Create figure with subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Line plot for sales
        ax1.plot(years, sales, 'b-o', linewidth=2, markersize=8, label='Sales')
        ax1.set_title('Sales Trend', fontsize=12, fontweight='bold')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Sales (in $K)')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Bar plot for profits
        ax2.bar(years, profits, color='green', alpha=0.7, edgecolor='black', label='Profit')
        ax2.set_title('Profit by Year', fontsize=12, fontweight='bold')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Profit (in $K)')
        ax2.grid(axis='y', alpha=0.3)
        ax2.legend()
        
        # Add value labels on bars
        for i, (year, profit) in enumerate(zip(years, profits)):
            ax2.text(year, profit + 2, f'{profit}', ha='center', fontsize=9)
        
        plt.suptitle('Company Performance Analysis', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        # Print statistics
        print("\n=== Data Summary ===")
        print(f"Years: {years}")
        print(f"Sales: {sales}")
        print(f"Profits: {profits}")
        print(f"Average Sales: ${np.mean(sales):.2f}K")
        print(f"Average Profit: ${np.mean(profits):.2f}K")
        print(f"Total Sales: ${sum(sales)}K")
        print(f"Total Profit: ${sum(profits)}K")
        
    except FileNotFoundError:
        print("Data file not found. Creating sample data...")
        create_sample_data()
        plot_from_file()
    except Exception as e:
        print(f"Error: {e}")

# Run the program
plot_from_file()