import streamlit as st
import os
from dotenv import load_dotenv
from product_analyzer import ProductAnalyzer

# Load environment variables
load_dotenv()

# Initialize the product analyzer
analyzer = ProductAnalyzer()

# Set page config
st.set_page_config(
    page_title="E-commerce Product Analyzer",
    page_icon="🛍️",
    layout="wide"
)

# Title and description
st.title("🛍️ E-commerce Product Analyzer")
st.markdown("""
This tool analyzes products from major e-commerce platforms and provides insights about:
- Top products in a category
- Price ranges
- Key features
- Customer sentiment from reviews
""")

# Sidebar for input
with st.sidebar:
    st.header("Search Parameters")
    platform = st.selectbox(
        "Select E-commerce Platform",
        ["Amazon.in", "Flipkart"]
    )
    
    category = st.text_input(
        "Product Category",
        placeholder="e.g., gaming laptops, wireless earbuds"
    )
    
    price_range = st.slider(
        "Price Range (₹)",
        min_value=0,
        max_value=200000,
        value=(0, 200000),
        step=1000
    )
    
    search_button = st.button("Analyze Products")

# Main content area
if search_button and category:
    with st.spinner("Analyzing products..."):
        try:
            # Get analysis results
            results = analyzer.analyze_products(
                platform=platform,
                category=category,
                min_price=price_range[0],
                max_price=price_range[1]
            )
            
            # Display results
            st.header("Analysis Results")
            
            # Top Products
            st.subheader("Top Products")
            for product in results["top_products"]:
                with st.expander(f"📱 {product['name']} - ₹{product['price']:,}"):
                    st.write("**Key Features:**")
                    for feature in product["features"]:
                        st.write(f"- {feature}")
                    st.write("**Customer Rating:**", product["rating"])
            
            # Price Analysis
            st.subheader("Price Analysis")
            st.write(f"Price Range: ₹{results['price_range']['min']:,} - ₹{results['price_range']['max']:,}")
            st.write(f"Average Price: ₹{results['price_range']['average']:,.2f}")
            
            # Sentiment Analysis
            st.subheader("Customer Sentiment")
            st.write(f"Overall Sentiment: {results['sentiment']['overall']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Positive Points:**")
                for point in results['sentiment']['positive_points']:
                    st.write(f"✅ {point}")
            
            with col2:
                st.write("**Negative Points:**")
                for point in results['sentiment']['negative_points']:
                    st.write(f"❌ {point}")
                    
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
else:
    st.info("👈 Please select a platform and enter a product category to begin analysis.") 