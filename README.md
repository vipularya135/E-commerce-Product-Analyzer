# E-commerce Product Analyzer

A Streamlit application that analyzes products from major e-commerce platforms using LangChain and Groq LLM. The application provides insights about product categories, including price ranges, key features, and customer sentiment analysis.

## Features

- Analyze products from Amazon.in and Flipkart
- Get detailed information about top products in a category
- View price range analysis
- Understand customer sentiment from reviews
- Identify common positive and negative points

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)
3. Select an e-commerce platform and enter a product category
4. Adjust the price range if needed
5. Click "Analyze Products" to get insights

## Sample Queries

- "Analyze budget gaming laptops under ₹60000 on Flipkart"
- "Summarize customer reviews for the top 3 wireless earbuds on Amazon India"
- "Compare features and prices of popular smartwatches available online"

## Note

This is a demonstration application. The product scraping functionality is currently using placeholder data. In a production environment, you would need to:

1. Implement proper web scraping with rate limiting and error handling
2. Consider using official APIs if available
3. Add more robust error handling and input validation
4. Implement caching to improve performance
5. Add user authentication if needed

## License

MIT License 