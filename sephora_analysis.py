"""
Sephora Product Analysis
Author: Sofia Herrmann
Description: Analyzes beauty product pricing, ratings, and consumer preferences
from Sephora's product catalog
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style for professional plots
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 6)

class SephoraAnalyzer:
    """
    Analyze Sephora product data including pricing, ratings, and categories.
    """
    
    def __init__(self):
        """Initialize with sample product data."""
        self.data = self.create_sample_data()
        
    def create_sample_data(self):
        """
        Create realistic Sephora product dataset.
        In production, this would scrape or use API data.
        """
        products = {
            'product_name': [
                'Fenty Beauty Foundation', 'Fenty Beauty Lipgloss', 'Fenty Beauty Highlighter',
                'Rare Beauty Blush', 'Rare Beauty Concealer', 'Charlotte Tilbury Mascara',
                'Charlotte Tilbury Foundation', 'Dior Lipstick', 'Dior Foundation',
                'The Ordinary Serum', 'The Ordinary Moisturizer', 'The Ordinary Retinol',
                'Drunk Elephant Moisturizer', 'Urban Decay Eyeshadow', 'Urban Decay Primer',
                'Huda Beauty Palette', 'Huda Beauty Lipstick', 'MAC Lipstick',
                'MAC Foundation', 'MAC Powder', 'NARS Blush', 'NARS Concealer',
                'Too Faced Primer', 'Too Faced Mascara', 'Benefit Brow Pencil',
                'Tarte Concealer', 'Tarte Foundation', 'Anastasia Brow Gel',
                'Anastasia Palette', 'La Mer Cream', 'Tatcha Cleanser',
                'YSL Lipstick', 'Clinique Moisturizer', 'Hourglass Foundation',
                'Pat McGrath Lipstick', 'Laura Mercier Powder', 'Bobbi Brown Concealer',
                'Tom Ford Lipstick', 'Estee Lauder Serum', 'NARS Lipstick'
            ],
            'brand': [
                'Fenty Beauty', 'Fenty Beauty', 'Fenty Beauty',
                'Rare Beauty', 'Rare Beauty', 'Charlotte Tilbury',
                'Charlotte Tilbury', 'Dior', 'Dior',
                'The Ordinary', 'The Ordinary', 'The Ordinary',
                'Drunk Elephant', 'Urban Decay', 'Urban Decay',
                'Huda Beauty', 'Huda Beauty', 'MAC',
                'MAC', 'MAC', 'NARS', 'NARS',
                'Too Faced', 'Too Faced', 'Benefit',
                'Tarte', 'Tarte', 'Anastasia',
                'Anastasia', 'La Mer', 'Tatcha',
                'YSL', 'Clinique', 'Hourglass',
                'Pat McGrath', 'Laura Mercier', 'Bobbi Brown',
                'Tom Ford', 'Estee Lauder', 'NARS'
            ],
            'category': [
                'Face', 'Lips', 'Face',
                'Face', 'Face', 'Eyes', 'Face', 'Lips', 'Face',
                'Skincare', 'Skincare', 'Skincare',
                'Skincare', 'Eyes', 'Face',
                'Eyes', 'Lips', 'Lips',
                'Face', 'Face', 'Face', 'Face',
                'Face', 'Eyes', 'Eyes',
                'Face', 'Face', 'Eyes',
                'Eyes', 'Skincare', 'Skincare',
                'Lips', 'Skincare', 'Face',
                'Lips', 'Face', 'Face',
                'Lips', 'Skincare', 'Lips'
            ],
            'price': [
                38, 20, 32, 23, 27, 29, 44, 42, 52,
                7, 9, 12, 68, 54, 35, 67, 29, 20,
                39, 32, 32, 31, 34, 26, 24,
                29, 41, 23, 49, 185, 35,
                39, 31, 49, 40, 41, 32, 57, 78, 28
            ],
            'rating': [
                4.5, 4.4, 4.6, 4.7, 4.5, 4.3, 4.5, 4.6, 4.4,
                4.4, 4.3, 4.5, 4.2, 4.5, 4.4, 4.8, 4.3, 4.4,
                4.5, 4.4, 4.6, 4.5, 4.3, 4.4, 4.5,
                4.4, 4.5, 4.7, 4.6, 4.1, 4.5,
                4.5, 4.3, 4.6, 4.4, 4.5, 4.5, 4.3, 4.2, 4.6
            ],
            'num_reviews': [
                15234, 9845, 7651, 8901, 6234, 6543, 8932, 4231, 5678,
                12045, 8934, 9123, 5678, 9876, 7234, 11234, 5432, 7890,
                10234, 6543, 6789, 7456, 5432, 6789, 8765,
                9012, 7890, 10123, 8456, 3456, 7654,
                5678, 6543, 8901, 7234, 6543, 7890, 4567, 5678, 5234
            ]
        }
        
        df = pd.DataFrame(products)
        
        # Add derived columns
        df['value_score'] = df['rating'] / (df['price'] / 10)
        df['price_range'] = pd.cut(df['price'], 
                                   bins=[0, 20, 40, 70, 200],
                                   labels=['Budget', 'Mid-Range', 'Premium', 'Luxury'])
        
        return df
    
    def summary_statistics(self):
        """Calculate key summary statistics."""
        print("\n" + "="*70)
        print("SEPHORA PRODUCT ANALYSIS - SUMMARY STATISTICS")
        print("="*70)
        
        print(f"\nTotal Products Analyzed: {len(self.data)}")
        print(f"\nPrice Statistics:")
        print(f"  Average Price: ${self.data['price'].mean():.2f}")
        print(f"  Median Price: ${self.data['price'].median():.2f}")
        print(f"  Price Range: ${self.data['price'].min():.2f} - ${self.data['price'].max():.2f}")
        
        print(f"\nRating Statistics:")
        print(f"  Average Rating: {self.data['rating'].mean():.2f} stars")
        print(f"  Median Rating: {self.data['rating'].median():.2f} stars")
        print(f"  Rating Range: {self.data['rating'].min():.2f} - {self.data['rating'].max():.2f} stars")
        
        print(f"\nReview Statistics:")
        print(f"  Total Reviews: {self.data['num_reviews'].sum():,}")
        print(f"  Average Reviews per Product: {self.data['num_reviews'].mean():.0f}")
        
        # Most expensive and best value
        most_expensive = self.data.loc[self.data['price'].idxmax()]
        best_value = self.data.loc[self.data['value_score'].idxmax()]
        
        print(f"\nMost Expensive Product:")
        print(f"  {most_expensive['product_name']} - ${most_expensive['price']:.2f}")
        
        print(f"\nBest Value Product:")
        print(f"  {best_value['product_name']} - ${best_value['price']:.2f} ({best_value['rating']} stars)")
        
    def category_analysis(self):
        """Analyze products by category."""
        print("\n" + "-"*70)
        print("CATEGORY ANALYSIS")
        print("-"*70)
        
        category_stats = self.data.groupby('category').agg({
            'price': ['count', 'mean', 'min', 'max'],
            'rating': 'mean',
            'num_reviews': 'sum'
        }).round(2)
        
        print("\nCategory Statistics:")
        print(category_stats)
        
        # Most popular category
        most_products = self.data['category'].value_counts().idxmax()
        print(f"\nMost Products: {most_products} ({self.data['category'].value_counts().max()} products)")
        
        # Highest rated category
        highest_rated = self.data.groupby('category')['rating'].mean().idxmax()
        print(f"Highest Rated: {highest_rated} ({self.data.groupby('category')['rating'].mean().max():.2f} stars)")
        
    def top_products(self):
        """Identify top performing products."""
        print("\n" + "-"*70)
        print("TOP PRODUCTS")
        print("-"*70)
        
        print("\nTop 5 Highest Rated Products:")
        top_rated = self.data.nlargest(5, 'rating')[['product_name', 'brand', 'rating', 'price']]
        for idx, row in top_rated.iterrows():
            print(f"  {row['product_name']} ({row['brand']}) - {row['rating']}⭐ (${row['price']})")
        
        print("\nTop 5 Most Reviewed Products:")
        most_reviewed = self.data.nlargest(5, 'num_reviews')[['product_name', 'brand', 'num_reviews', 'rating']]
        for idx, row in most_reviewed.iterrows():
            print(f"  {row['product_name']} ({row['brand']}) - {row['num_reviews']:,} reviews ({row['rating']}⭐)")
        
        print("\nTop 5 Best Value Products:")
        best_value = self.data.nlargest(5, 'value_score')[['product_name', 'price', 'rating', 'value_score']]
        for idx, row in best_value.iterrows():
            print(f"  {row['product_name']} - ${row['price']:.2f} ({row['rating']}⭐)")
    
    def price_analysis(self):
        """Analyze pricing patterns."""
        print("\n" + "-"*70)
        print("PRICE ANALYSIS")
        print("-"*70)
        
        print("\nPrice Range Distribution:")
        price_dist = self.data['price_range'].value_counts().sort_index()
        for range_name, count in price_dist.items():
            percentage = (count / len(self.data)) * 100
            print(f"  {range_name}: {count} products ({percentage:.1f}%)")
        
        # Correlation between price and rating
        correlation = self.data['price'].corr(self.data['rating'])
        print(f"\nPrice-Rating Correlation: {correlation:.3f}")
        if abs(correlation) < 0.3:
            print("  → Weak correlation: Price doesn't strongly predict rating")
        
    def visualize_data(self):
        """Create professional visualizations."""
        print("\n" + "-"*70)
        print("GENERATING VISUALIZATIONS")
        print("-"*70)
        
        # 1. Price Distribution by Category
        fig, ax = plt.subplots(figsize=(12, 6))
        category_prices = self.data.groupby('category')['price'].mean().sort_values(ascending=False)
        category_prices.plot(kind='bar', color='#FF6B9D', ax=ax)
        ax.set_title('Average Price by Category', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Category', fontsize=12)
        ax.set_ylabel('Average Price ($)', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('sephora_price_by_category.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: sephora_price_by_category.png")
        plt.close()
        
        # 2. Rating vs Price Scatter Plot
        fig, ax = plt.subplots(figsize=(12, 6))
        categories = self.data['category'].unique()
        colors = sns.color_palette('husl', len(categories))
        
        for i, category in enumerate(categories):
            category_data = self.data[self.data['category'] == category]
            ax.scatter(category_data['price'], category_data['rating'], 
                      s=100, alpha=0.6, label=category, color=colors[i])
        
        ax.set_title('Product Rating vs Price by Category', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Price ($)', fontsize=12)
        ax.set_ylabel('Rating (stars)', fontsize=12)
        ax.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(alpha=0.3)
        plt.tight_layout()
        plt.savefig('sephora_rating_vs_price.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: sephora_rating_vs_price.png")
        plt.close()
        
        # 3. Price Range Distribution
        fig, ax = plt.subplots(figsize=(10, 6))
        price_range_counts = self.data['price_range'].value_counts().sort_index()
        colors_range = ['#A8E6CF', '#FFD3B6', '#FFAAA5', '#FF8B94']
        price_range_counts.plot(kind='bar', color=colors_range, ax=ax)
        ax.set_title('Product Distribution by Price Range', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Price Range', fontsize=12)
        ax.set_ylabel('Number of Products', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('sephora_price_distribution.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: sephora_price_distribution.png")
        plt.close()
        
        # 4. Top Brands Comparison
        fig, ax = plt.subplots(figsize=(14, 6))
        top_brands = self.data['brand'].value_counts().head(10)
        top_brands.plot(kind='barh', color='#C44569', ax=ax)
        ax.set_title('Top 10 Brands by Number of Products', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Number of Products', fontsize=12)
        ax.set_ylabel('Brand', fontsize=12)
        ax.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig('sephora_top_brands.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: sephora_top_brands.png")
        plt.close()
        
        # 5. Heatmap of Category Performance
        fig, ax = plt.subplots(figsize=(10, 6))
        heatmap_data = self.data.groupby('category').agg({
            'price': 'mean',
            'rating': 'mean',
            'num_reviews': 'mean'
        }).round(2)
        
        # Normalize for heatmap
        heatmap_normalized = (heatmap_data - heatmap_data.min()) / (heatmap_data.max() - heatmap_data.min())
        
        sns.heatmap(heatmap_normalized.T, annot=heatmap_data.T, fmt='.1f',
                   cmap='RdYlGn', center=0.5, cbar_kws={'label': 'Normalized Score'},
                   linewidths=1, linecolor='white', ax=ax)
        ax.set_title('Category Performance Heatmap', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Category', fontsize=12)
        ax.set_ylabel('Metric', fontsize=12)
        plt.tight_layout()
        plt.savefig('sephora_category_heatmap.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: sephora_category_heatmap.png")
        plt.close()
        
    def generate_insights(self):
        """Generate business insights."""
        print("\n" + "="*70)
        print("KEY BUSINESS INSIGHTS")
        print("="*70)
        
        # Insight 1: Price-Quality Relationship
        expensive_avg_rating = self.data[self.data['price'] > 50]['rating'].mean()
        affordable_avg_rating = self.data[self.data['price'] <= 30]['rating'].mean()
        
        print("\n1. PRICE-QUALITY RELATIONSHIP:")
        print(f"   Expensive products (>$50): {expensive_avg_rating:.2f}⭐ average rating")
        print(f"   Affordable products (≤$30): {affordable_avg_rating:.2f}⭐ average rating")
        print(f"   → Higher price does NOT guarantee higher ratings")
        
        # Insight 2: Category Insights
        skincare_avg = self.data[self.data['category'] == 'Skincare']['price'].mean()
        makeup_categories = ['Face', 'Eyes', 'Lips']
        makeup_avg = self.data[self.data['category'].isin(makeup_categories)]['price'].mean()
        
        print("\n2. CATEGORY PRICING:")
        print(f"   Skincare average: ${skincare_avg:.2f}")
        print(f"   Makeup average: ${makeup_avg:.2f}")
        print(f"   → {'Skincare' if skincare_avg > makeup_avg else 'Makeup'} products command higher prices")
        
        # Insight 3: Sweet Spot
        sweet_spot = self.data[(self.data['price'] >= 20) & (self.data['price'] <= 40)]
        print("\n3. OPTIMAL PRICE RANGE ($20-$40):")
        print(f"   Products in range: {len(sweet_spot)} ({len(sweet_spot)/len(self.data)*100:.1f}%)")
        print(f"   Average rating: {sweet_spot['rating'].mean():.2f}⭐")
        print(f"   → Best balance of quality and value")
        
        # Insight 4: Top Performers
        high_rated = self.data[self.data['rating'] >= 4.5]
        print("\n4. HIGH-RATED PRODUCTS (≥4.5 stars):")
        print(f"   Count: {len(high_rated)} products")
        print(f"   Average price: ${high_rated['price'].mean():.2f}")
        print(f"   Most common category: {high_rated['category'].mode()[0]}")


def main():
    """Run the complete Sephora analysis."""
    
    print("\n" + "="*70)
    print("SEPHORA BEAUTY PRODUCTS ANALYSIS")
    print("Analyzing pricing, ratings, and consumer preferences")
    print("="*70)
    
    # Create analyzer
    analyzer = SephoraAnalyzer()
    
    # Run analyses
    analyzer.summary_statistics()
    analyzer.category_analysis()
    analyzer.price_analysis()
    analyzer.top_products()
    analyzer.generate_insights()
    analyzer.visualize_data()
    
    print("\n" + "="*70)
    print("✅ ANALYSIS COMPLETE!")
    print("="*70)
    print("\nGenerated Files:")
    print("  • sephora_price_by_category.png")
    print("  • sephora_rating_vs_price.png")
    print("  • sephora_price_distribution.png")
    print("  • sephora_top_brands.png")
    print("  • sephora_category_heatmap.png")
    print("\nNext Steps:")
    print("  • Add this project to your GitHub")
    print("  • Update your portfolio website")
    print("  • Include in your CV projects section")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
