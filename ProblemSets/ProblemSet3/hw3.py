# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset directly from raw GitHub URL
url = ("https://raw.githubusercontent.com/luminati-io/eCommerce-dataset-samples/"
       "main/walmart-products.csv")
df = pd.read_csv(url)

# Quick peek
print(df.head())
print(df.info())

# Convert price-related fields to numeric if needed
if 'final_price' in df.columns:
    df['final_price'] = pd.to_numeric(df['final_price'], errors='coerce')

# Visualization 1: Price Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['final_price'].dropna(), bins=30, kde=True)
plt.title("Distribution of Final Prices")
plt.xlabel("Final Price")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("walmart_price_distribution.png")
plt.show()

# Visualization 2: Top Brands by Product Count
if 'brand' in df.columns:
    top_brands = df['brand'].value_counts().nlargest(10)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_brands.values, y=top_brands.index, palette="coolwarm")
    plt.title("Top 10 Brands by Number of Products")
    plt.xlabel("Number of Products")
    plt.ylabel("Brand")
    plt.tight_layout()
    plt.savefig("top_brands.png")
    plt.show()

# Visualization 3: Ratings vs Reviews Count (if available)
if 'rating' in df.columns and 'reviews_count' in df.columns:
    df['reviews_count'] = pd.to_numeric(df['reviews_count'], errors='coerce')
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x='reviews_count', y='rating', data=df, alpha=0.6)
    plt.xscale('log')
    plt.title("Reviews Count vs Rating")
    plt.xlabel("Reviews Count (log scale)")
    plt.ylabel("Rating")
    plt.tight_layout()
    plt.savefig("reviews_vs_rating.png")
    plt.show()

# Visualization 4: Products per Category
if 'category_name' in df.columns:
    top_categories = df['category_name'].value_counts().nlargest(10)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_categories.values, y=top_categories.index, palette="viridis")
    plt.title("Top 10 Categories by Product Count")
    plt.xlabel("Number of Products")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig("top_categories.png")
    plt.show()

