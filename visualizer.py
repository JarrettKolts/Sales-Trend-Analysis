# converter.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scraper import get_product_data

def convert_and_visualize():
    """
    Converts the product data into a Pandas DataFrame and visualizes it.
    """
    # Get the hardcoded data from scraper.py
    product_data = get_product_data()

    # Convert the hardcoded data into a Pandas DataFrame
    df = pd.DataFrame(product_data)

    # Clean up the 'Price' column to make it numeric for visualization
    df['Price'] = df['Price'].replace({r'\$': '', r',': ''}, regex=True).astype(float)

    # Clean up the 'Rating' column to make it numeric
    df['Rating'] = df['Rating'].replace({' out of 5 stars': '', ' ': ''}, regex=True).astype(float)

    # Create a simple bar plot showing Price vs. Rating using Seaborn
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='Name', y='Price', hue='Rating')

    # Show the plot
    plt.title("Product Price vs Rating")
    plt.xlabel("Product")
    plt.ylabel("Price ($)")
    plt.xticks(rotation=0)
    plt.show()

if __name__ == "__main__":
    convert_and_visualize()
