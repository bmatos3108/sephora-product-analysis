# 💄 Sephora Beauty Product Analysis

A comprehensive data analysis project examining beauty product pricing, ratings, and consumer preferences from Sephora's product catalog. This project demonstrates key data analysis skills including data cleaning, statistical analysis, and data visualization.

## 📊 Project Overview

This analysis explores the relationship between product pricing, customer ratings, and category performance across Sephora's beauty product lineup. Using Python and data visualization libraries, I uncovered insights about consumer preferences and pricing strategies in the beauty industry.

## 🎯 Key Findings

- **Price-Quality Relationship**: Higher prices don't guarantee higher ratings - many mid-range products ($20-40) achieve 4.5+ star ratings
- **Category Insights**: Skincare products command higher average prices than makeup categories
- **Sweet Spot**: Products in the $20-$40 range show the best balance of quality and value
- **Top Performers**: Face and Eyes categories dominate in both quantity and ratings

## 🛠️ Technologies Used

- **Python 3.9+**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical data visualization

## 📈 Visualizations Generated

1. **Average Price by Category** - Bar chart showing pricing across product categories
2. **Rating vs Price Analysis** - Scatter plot revealing the weak correlation between price and ratings
3. **Price Distribution** - Product count across different price ranges (Budget, Mid-Range, Premium, Luxury)
4. **Top Brands** - Horizontal bar chart of most represented brands
5. **Category Performance Heatmap** - Multi-metric comparison across categories

## 🚀 How to Run

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn
```

### Running the Analysis
```bash
python sephora_analysis.py
```

### Output
The script will generate:
- Detailed console report with statistics and insights
- 5 professional PNG visualizations
- Category-by-category breakdowns
- Top product rankings

## 📊 Analysis Sections

### 1. Summary Statistics
- Total products analyzed
- Price and rating distributions
- Review count analysis
- Most expensive and best value products

### 2. Category Analysis
- Performance metrics by category (Face, Eyes, Lips, Skincare)
- Average prices and ratings
- Product count distribution

### 3. Price Analysis
- Distribution across price ranges
- Price-rating correlation analysis
- Identification of pricing sweet spots

### 4. Top Products
- Highest rated products
- Most reviewed products
- Best value offerings

### 5. Business Insights
- Strategic pricing recommendations
- Category performance patterns
- Consumer preference trends

## 💡 Key Insights for Business

### Pricing Strategy
- Mid-range products ($20-40) represent 42% of offerings and maintain strong ratings
- Premium pricing (>$70) doesn't correlate with proportionally higher ratings
- Budget options (<$20) can achieve competitive ratings with right formulation

### Category Recommendations
- **Skincare**: Commands highest prices; focus on ingredient quality and efficacy claims
- **Makeup**: More price-sensitive; ratings driven by performance and shade ranges
- **Eyes**: Highest volume category with consistent ratings across price points

### Consumer Behavior
- Reviews concentrate on products in $20-40 range (highest engagement)
- Products with 4.5+ ratings occur across all price points
- Category matters less than brand reputation and reviews for purchasing decisions

## 📂 Project Structure

```
sephora-analysis/
│
├── sephora_analysis.py          # Main analysis script
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
│
└── output/
    ├── sephora_price_by_category.png
    ├── sephora_rating_vs_price.png
    ├── sephora_price_distribution.png
    ├── sephora_top_brands.png
    └── sephora_category_heatmap.png
```

## 🔮 Future Enhancements

- [ ] Integrate real-time Sephora API data
- [ ] Add sentiment analysis of product reviews
- [ ] Include seasonal trend analysis
- [ ] Compare across different retailers (Sephora vs Ulta)
- [ ] Implement machine learning for price prediction
- [ ] Add ingredient analysis and clean beauty trends

## 📝 Methodology

**Data Source**: Sample dataset created based on actual Sephora product patterns (In production, would use web scraping or Sephora API)

**Analysis Techniques**:
- Descriptive statistics (mean, median, distribution)
- Correlation analysis (price vs rating)
- Categorical aggregation (groupby operations)
- Data segmentation (price ranges, categories)
- Comparative analysis (brand and category performance)

**Visualization Approach**:
- Professional, presentation-ready charts
- Color-coded categories for clarity
- Annotations for key insights
- Multiple chart types for different perspectives

## 👤 Author

**Sofia Herrmann**
- Aspiring Data Analyst
- GitHub: [@bmatos3108](https://github.com/bmatos3108)
- LinkedIn: [sofia-herrmann3108](https://www.linkedin.com/in/sofia-herrmann3108/)

## 📄 License

This project is open source and available under the MIT License.

---

## 💬 What I Learned

- **Data Analysis**: How to structure and analyze retail product data
- **Statistical Insights**: Identifying meaningful patterns in consumer behavior
- **Visualization**: Creating clear, professional charts for business stakeholders
- **Python Skills**: Advanced pandas operations, groupby, and data aggregation
- **Domain Knowledge**: Understanding beauty industry pricing and consumer preferences

*This project demonstrates practical data analysis skills applicable to retail, e-commerce, and consumer goods industries.*
