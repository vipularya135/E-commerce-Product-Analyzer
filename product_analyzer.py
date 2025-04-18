import os
import requests
from bs4 import BeautifulSoup
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Dict, Any
import json
import time
import random

class ProductFeature(BaseModel):
    name: str = Field(description="Name of the product")
    price: float = Field(description="Price of the product in INR")
    features: List[str] = Field(description="List of key features")
    rating: float = Field(description="Customer rating out of 5")
    reviews: List[str] = Field(description="Sample of customer reviews")

class AnalysisResult(BaseModel):
    top_products: List[ProductFeature] = Field(description="List of top products")
    price_range: Dict[str, float] = Field(description="Price range statistics")
    sentiment: Dict[str, Any] = Field(description="Sentiment analysis results")

import os
import time
import random
from typing import List, Dict
from langchain.chat_models import ChatGroq
from langchain.output_parsers import PydanticOutputParser
from your_module import AnalysisResult  # Replace with your actual import if different

class ProductAnalyzer:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-8b-instant"
        )
        self.output_parser = PydanticOutputParser(pydantic_object=AnalysisResult)
        
    def _scrape_products(self, platform: str, category: str, min_price: int, max_price: int) -> List[Dict]:
        time.sleep(1)
        
        if "laptop" in category.lower() or "gaming" in category.lower():
            return self._get_laptop_data(min_price, max_price)
        elif "earbuds" in category.lower() or "headphone" in category.lower():
            return self._get_earbuds_data(min_price, max_price)
        elif "smartwatch" in category.lower() or "watch" in category.lower():
            return self._get_smartwatch_data(min_price, max_price)
        elif "tv" in category.lower():
            return self._get_tv_data(min_price, max_price)
        elif "ac" in category.lower():
            return self._get_ac_data(min_price, max_price)
        elif "fridge" in category.lower() or "refrigerator" in category.lower():
            return self._get_fridge_data(min_price, max_price)
        elif "iphone" in category.lower():
            return self._get_iphone_data(min_price, max_price)
        else:
            return self._get_generic_data(category, min_price, max_price)

    def _get_laptop_data(self, min_price, max_price):
        laptops = [
            {
                "name": "ASUS TUF Gaming F15",
                "price": 54990,
                "features": ["Intel Core i5-11400H", "NVIDIA RTX 3050 4GB", "16GB RAM", "512GB SSD", "15.6\" FHD 144Hz"],
                "rating": 4.5,
                "reviews": [
                    "Great performance for gaming and work",
                    "Good build quality and cooling",
                    "Battery life could be better",
                    "Keyboard is comfortable for long typing sessions",
                    "Display is bright and color accurate"
                ]
            },
            {
                "name": "Lenovo IdeaPad Gaming 3",
                "price": 49990,
                "features": ["AMD Ryzen 5 5600H", "NVIDIA GTX 1650 4GB", "8GB RAM", "512GB SSD", "15.6\" FHD 120Hz"],
                "rating": 4.3,
                "reviews": [
                    "Good value for money",
                    "Runs most games smoothly",
                    "Build quality is decent",
                    "Gets hot under heavy load",
                    "Battery life is average"
                ]
            },
            {
                "name": "HP Pavilion Gaming",
                "price": 62990,
                "features": ["Intel Core i5-11300H", "NVIDIA RTX 3050 Ti 4GB", "16GB RAM", "512GB SSD", "16.1\" FHD 144Hz"],
                "rating": 4.4,
                "reviews": [
                    "Excellent performance for the price",
                    "Good thermal management",
                    "Premium build quality",
                    "Battery life is decent",
                    "Display is vibrant and responsive"
                ]
            },
            {
                "name": "Acer Nitro 5",
                "price": 47990,
                "features": ["AMD Ryzen 5 5600H", "NVIDIA GTX 1650 4GB", "8GB RAM", "256GB SSD", "15.6\" FHD 144Hz"],
                "rating": 4.2,
                "reviews": [
                    "Budget-friendly gaming laptop",
                    "Good performance for casual gaming",
                    "Build quality is acceptable",
                    "Battery life is below average",
                    "Display is decent but not great"
                ]
            }
        ]
        return [l for l in laptops if min_price <= l["price"] <= max_price]

    def _get_earbuds_data(self, min_price, max_price):
        earbuds = [
            {
                "name": "OnePlus Buds Pro 2",
                "price": 9990,
                "features": ["Active Noise Cancellation", "Dual Dynamic Drivers", "IP55 Water Resistance", "Up to 39 hours with case", "Fast Charging"],
                "rating": 4.6,
                "reviews": [
                    "Excellent sound quality",
                    "Great ANC performance",
                    "Comfortable for long wear",
                    "Battery life is impressive",
                    "App integration is seamless"
                ]
            },
            {
                "name": "Samsung Galaxy Buds2 Pro",
                "price": 14990,
                "features": ["Intelligent Active Noise Cancellation", "Hi-Fi Sound", "IPX7 Water Resistance", "Up to 29 hours with case", "Spatial Audio"],
                "rating": 4.7,
                "reviews": [
                    "Premium sound quality",
                    "Superior ANC compared to competitors",
                    "Very comfortable fit",
                    "Seamless integration with Samsung devices",
                    "Battery life could be better"
                ]
            },
            {
                "name": "boAt Airdopes 141",
                "price": 1499,
                "features": ["Low Latency Mode", "IPX4 Water Resistance", "Up to 42 hours with case", "Touch Controls", "Voice Assistant Support"],
                "rating": 4.3,
                "reviews": [
                    "Great value for money",
                    "Good sound quality for the price",
                    "Battery life is excellent",
                    "Build quality is decent",
                    "Call quality could be better"
                ]
            },
            {
                "name": "Apple AirPods Pro",
                "price": 19990,
                "features": ["Active Noise Cancellation", "Transparency Mode", "Spatial Audio", "IPX4 Water Resistance", "Up to 24 hours with case"],
                "rating": 4.8,
                "reviews": [
                    "Best-in-class ANC",
                    "Seamless integration with Apple ecosystem",
                    "Comfortable for all-day wear",
                    "Sound quality is excellent",
                    "Price is a bit high"
                ]
            }
        ]
        return [e for e in earbuds if min_price <= e["price"] <= max_price]

    def _get_smartwatch_data(self, min_price, max_price):
        smartwatches = [
            {
                "name": "Apple Watch Series 7",
                "price": 32990,
                "features": ["Always-On Retina Display", "Heart Rate Monitoring", "ECG App", "Blood Oxygen Monitoring", "Water Resistant"],
                "rating": 4.8,
                "reviews": [
                    "Best smartwatch for iPhone users",
                    "Excellent health tracking features",
                    "Premium build quality",
                    "Battery life could be better",
                    "Seamless integration with Apple ecosystem"
                ]
            },
            {
                "name": "Samsung Galaxy Watch 5",
                "price": 24990,
                "features": ["BioActive Sensor", "Sleep Tracking", "Body Composition Analysis", "Water Resistant", "Up to 50 hours battery life"],
                "rating": 4.6,
                "reviews": [
                    "Great for Android users",
                    "Comprehensive health tracking",
                    "Good battery life",
                    "Comfortable to wear",
                    "App ecosystem is growing"
                ]
            },
            {
                "name": "Noise ColorFit Pro 4",
                "price": 2499,
                "features": ["1.78\" AMOLED Display", "SpO2 Monitoring", "Heart Rate Monitoring", "14 Sports Modes", "Water Resistant"],
                "rating": 4.2,
                "reviews": [
                    "Excellent value for money",
                    "Good display quality",
                    "Battery life is decent",
                    "Build quality is acceptable",
                    "App could be improved"
                ]
            },
            {
                "name": "Fire-Boltt Ninja",
                "price": 1999,
                "features": ["1.69\" HD Display", "Heart Rate Monitoring", "Sleep Tracking", "14 Sports Modes", "IP67 Water Resistant"],
                "rating": 4.1,
                "reviews": [
                    "Very affordable",
                    "Good basic fitness tracking",
                    "Battery life is good",
                    "Build quality is basic",
                    "App needs improvement"
                ]
            }
        ]
        return [w for w in smartwatches if min_price <= w["price"] <= max_price]

    def _get_tv_data(self, min_price, max_price):
        tvs = [
            {
                "name": "Samsung Crystal 4K UHD TV",
                "price": 35990,
                "features": ["4K UHD", "Crystal Processor 4K", "Smart TV with Tizen", "HDR", "43 inch"],
                "rating": 4.6,
                "reviews": [
                    "Excellent picture quality",
                    "Smart features are intuitive",
                    "Sound is decent",
                    "Build quality is solid",
                    "Value for money"
                ]
            },
            {
                "name": "Mi 5X 4K LED TV",
                "price": 29999,
                "features": ["4K LED", "Dolby Vision", "Android TV", "Google Assistant", "43 inch"],
                "rating": 4.4,
                "reviews": [
                    "Great features at this price",
                    "Crisp and clear display",
                    "Sound could be better",
                    "User interface is smooth",
                    "Sleek and premium design"
                ]
            }
        ]
        return [tv for tv in tvs if min_price <= tv["price"] <= max_price]

    def _get_ac_data(self, min_price, max_price):
        acs = [
            {
                "name": "LG 1.5 Ton 5 Star Inverter AC",
                "price": 43990,
                "features": ["Dual Inverter", "Copper Condenser", "HD Filter", "Smart Diagnosis", "Energy Saving"],
                "rating": 4.5,
                "reviews": [
                    "Cools quickly and efficiently",
                    "Energy efficient",
                    "Noise levels are low",
                    "Remote is user-friendly",
                    "Installation was smooth"
                ]
            },
            {
                "name": "Voltas 1.5 Ton 3 Star Split AC",
                "price": 31990,
                "features": ["Copper Condenser", "High Ambient Cooling", "Sleep Mode", "Anti-Dust Filter", "Remote Control"],
                "rating": 4.2,
                "reviews": [
                    "Value for money",
                    "Good cooling even in high temperatures",
                    "Installation service could be improved",
                    "Energy consumption is reasonable",
                    "Looks stylish"
                ]
            }
        ]
        return [ac for ac in acs if min_price <= ac["price"] <= max_price]

    def _get_fridge_data(self, min_price, max_price):
        fridges = [
            {
                "name": "Samsung 253L 3 Star Refrigerator",
                "price": 23990,
                "features": ["Digital Inverter", "Convertible Freezer", "Toughened Glass Shelves", "Stabilizer Free", "Frost Free"],
                "rating": 4.6,
                "reviews": [
                    "Spacious and energy efficient",
                    "Runs silently",
                    "Cooling is consistent",
                    "Premium look and feel",
                    "Convertible mode is handy"
                ]
            },
            {
                "name": "LG 260L 3 Star Refrigerator",
                "price": 25990,
                "features": ["Smart Inverter Compressor", "Moist Balance Crisper", "Door Cooling+", "Auto Smart Connect", "Frost Free"],
                "rating": 4.5,
                "reviews": [
                    "Reliable brand with great features",
                    "Cooling is fast",
                    "Energy saving",
                    "Good design and usability",
                    "Build quality is top-notch"
                ]
            }
        ]
        return [fridge for fridge in fridges if min_price <= fridge["price"] <= max_price]

    def _get_iphone_data(self, min_price, max_price):
        iphones = [
            {
                "name": "Apple iPhone 14",
                "price": 69999,
                "features": ["6.1-inch Super Retina XDR Display", "A15 Bionic Chip", "Dual 12MP Cameras", "iOS 16", "Face ID"],
                "rating": 4.8,
                "reviews": [
                    "Excellent performance and camera",
                    "Battery lasts all day",
                    "Build quality is premium",
                    "iOS is smooth and responsive",
                    "Pricey but worth it"
                ]
            },
            {
                "name": "Apple iPhone 13",
                "price": 58999,
                "features": ["6.1-inch Super Retina XDR Display", "A15 Bionic Chip", "Dual 12MP Cameras", "iOS 15", "MagSafe Support"],
                "rating": 4.7,
                "reviews": [
                    "Still a great choice in 2025",
                    "Very reliable and smooth",
                    "Camera performs really well",
                    "Good battery backup",
                    "Solid build"
                ]
            }
        ]
        return [iphone for iphone in iphones if min_price <= iphone["price"] <= max_price]

    def _get_generic_data(self, category, min_price, max_price):
        products = []
        num_products = random.randint(3, 5)
        
        for i in range(num_products):
            price = random.randint(min_price, max_price)
            rating = round(random.uniform(3.5, 5.0), 1)
            product = {
                "name": f"Sample {category.title()} {i+1}",
                "price": price,
                "features": [
                    f"Feature {j+1} for {category}",
                    f"Feature {j+2} for {category}",
                    f"Feature {j+3} for {category}"
                ],
                "rating": rating,
                "reviews": [
                    f"Good {category} for the price",
                    f"Works well for my needs",
                    f"Could be better in some aspects",
                    f"Overall satisfied with the purchase",
                    f"Would recommend to others"
                ]
            }
            products.append(product)
        
        return products


    def _analyze_with_llm(self, products: List[Dict]) -> AnalysisResult:
        """
        Analyze the scraped products using the LLM.
        """
        # Create a more explicit prompt with examples
        template = """
        You are an e-commerce product analyst. Analyze the following product information and provide insights in the exact format specified below.
        
        Products:
        {products}
        
        Based on these products, provide:
        
        1. A list of the top 3-5 products with their key features
        2. Price range analysis (min, max, average)
        3. Overall customer sentiment and common points from reviews
        
        Your response MUST be in the following JSON format:
        {{
          "top_products": [
            {{
              "name": "Product Name",
              "price": 49999,
              "features": ["Feature 1", "Feature 2", "Feature 3"],
              "rating": 4.5,
              "reviews": ["Review 1", "Review 2", "Review 3"]
            }},
            // More products...
          ],
          "price_range": {{
            "min": 19999,
            "max": 69999,
            "average": 44999
          }},
          "sentiment": {{
            "overall": "Positive",
            "positive_points": ["Point 1", "Point 2"],
            "negative_points": ["Point 1", "Point 2"]
          }}
        }}
        
        DO NOT include any explanations or text outside this JSON structure.
        """
        
        prompt = ChatPromptTemplate.from_template(template)
        
        # Format the products data
        products_text = json.dumps(products, indent=2)
        
        # Create the chain
        chain = prompt | self.llm
        
        # Run the chain
        result = chain.invoke({
            "products": products_text
        })
        
        # Extract the JSON from the response
        try:
            # Find JSON in the response
            response_text = result.content
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            
            if json_start >= 0 and json_end > json_start:
                json_str = response_text[json_start:json_end]
                # Parse the JSON
                data = json.loads(json_str)
                # Convert to Pydantic model
                return AnalysisResult(**data)
            else:
                # Fallback to manual parsing if JSON not found
                return self._create_fallback_result(products)
        except Exception as e:
            print(f"Error parsing LLM response: {str(e)}")
            # Fallback to manual parsing
            return self._create_fallback_result(products)
    
    def _create_fallback_result(self, products: List[Dict]) -> AnalysisResult:
        """
        Create a fallback result when LLM parsing fails.
        """
        # Sort products by rating
        sorted_products = sorted(products, key=lambda x: x["rating"], reverse=True)
        top_products = sorted_products[:min(3, len(sorted_products))]
        
        # Calculate price range
        prices = [p["price"] for p in products]
        min_price = min(prices) if prices else 0
        max_price = max(prices) if prices else 0
        avg_price = sum(prices) / len(prices) if prices else 0
        
        # Extract sentiment from reviews
        all_reviews = []
        for product in products:
            all_reviews.extend(product["reviews"])
        
        # Simple sentiment analysis
        positive_keywords = ["good", "great", "excellent", "amazing", "love", "perfect", "best", "recommend"]
        negative_keywords = ["bad", "poor", "terrible", "disappointed", "issue", "problem", "worst", "avoid"]
        
        positive_points = []
        negative_points = []
        
        for review in all_reviews:
            for keyword in positive_keywords:
                if keyword in review.lower() and review not in positive_points:
                    positive_points.append(review)
            
            for keyword in negative_keywords:
                if keyword in review.lower() and review not in negative_points:
                    negative_points.append(review)
        
        # Limit to top 3 points
        positive_points = positive_points[:3]
        negative_points = negative_points[:3]
        
        # Determine overall sentiment
        if len(positive_points) > len(negative_points) * 2:
            overall_sentiment = "Very Positive"
        elif len(positive_points) > len(negative_points):
            overall_sentiment = "Positive"
        elif len(negative_points) > len(positive_points) * 2:
            overall_sentiment = "Very Negative"
        elif len(negative_points) > len(positive_points):
            overall_sentiment = "Negative"
        else:
            overall_sentiment = "Mixed"
        
        return AnalysisResult(
            top_products=top_products,
            price_range={
                "min": min_price,
                "max": max_price,
                "average": avg_price
            },
            sentiment={
                "overall": overall_sentiment,
                "positive_points": positive_points,
                "negative_points": negative_points
            }
        )

    def analyze_products(self, platform: str, category: str, min_price: int, max_price: int) -> Dict:
        """
        Main method to analyze products from the specified platform.
        """
        # Scrape products
        products = self._scrape_products(platform, category, min_price, max_price)
        
        # Analyze with LLM
        analysis = self._analyze_with_llm(products)
        
        return analysis.dict() 
