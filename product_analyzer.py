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

class ProductAnalyzer:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-8b-instant"
        )
        self.output_parser = PydanticOutputParser(pydantic_object=AnalysisResult)
        
    def _scrape_products(self, platform: str, category: str, min_price: int, max_price: int) -> List[Dict]:
        """
        Scrape product information from the specified platform.
        This is a placeholder implementation. In a real application, you would need to:
        1. Handle different platforms' specific HTML structures
        2. Implement proper rate limiting and error handling
        3. Consider using official APIs if available
        """
        # Simulate network delay
        time.sleep(1)
        
        # Generate sample data based on the category
        category_lower = category.lower()
        
        # Check for specific product categories
        if "laptop" in category_lower or "gaming" in category_lower:
            return self._get_laptop_data(min_price, max_price)
        elif "earbuds" in category_lower or "headphone" in category_lower or "earphone" in category_lower:
            return self._get_earbuds_data(min_price, max_price)
        elif "smartwatch" in category_lower or "watch" in category_lower:
            return self._get_smartwatch_data(min_price, max_price)
        elif "smartphone" in category_lower or "phone" in category_lower or "mobile" in category_lower:
            return self._get_smartphone_data(min_price, max_price)
        elif "tv" in category_lower or "television" in category_lower:
            return self._get_tv_data(min_price, max_price)
        elif "refrigerator" in category_lower or "fridge" in category_lower:
            return self._get_refrigerator_data(min_price, max_price)
        elif "washing" in category_lower or "washer" in category_lower:
            return self._get_washing_machine_data(min_price, max_price)
        elif "camera" in category_lower or "dslr" in category_lower:
            return self._get_camera_data(min_price, max_price)
        elif "tablet" in category_lower or "ipad" in category_lower:
            return self._get_tablet_data(min_price, max_price)
        elif "printer" in category_lower:
            return self._get_printer_data(min_price, max_price)
        else:
            return self._get_generic_data(category, min_price, max_price)
    
    def _get_laptop_data(self, min_price, max_price):
        laptops = [
            {
                "name": "ASUS ROG Strix G16 (2024)",
                "price": 159990,
                "features": [
                    "Intel Core i9-14900HX",
                    "NVIDIA RTX 4070 8GB",
                    "16GB DDR5 RAM",
                    "1TB PCIe 4.0 SSD",
                    "16\" QHD+ 240Hz"
                ],
                "rating": 4.7,
                "reviews": [
                    "Exceptional gaming performance",
                    "Beautiful display with high refresh rate",
                    "Great build quality",
                    "Effective cooling system",
                    "Premium features throughout"
                ]
            },
            {
                "name": "Lenovo Legion Pro 7i (2024)",
                "price": 189990,
                "features": [
                    "Intel Core i9-14900HX",
                    "NVIDIA RTX 4080 12GB",
                    "32GB DDR5 RAM",
                    "1TB PCIe 4.0 SSD",
                    "16\" Mini LED 240Hz"
                ],
                "rating": 4.8,
                "reviews": [
                    "Top-tier gaming performance",
                    "Mini LED display is stunning",
                    "Excellent build quality",
                    "Great keyboard and trackpad",
                    "Advanced cooling solution"
                ]
            },
            {
                "name": "HP Omen 16 (2024)",
                "price": 139990,
                "features": [
                    "AMD Ryzen 9 7940HS",
                    "NVIDIA RTX 4060 8GB",
                    "16GB DDR5 RAM",
                    "1TB PCIe 4.0 SSD",
                    "16\" QHD 165Hz"
                ],
                "rating": 4.6,
                "reviews": [
                    "Great value for performance",
                    "Solid build quality",
                    "Good battery life for a gaming laptop",
                    "Effective cooling",
                    "Nice display quality"
                ]
            },
            {
                "name": "MSI Katana 15 (2024)",
                "price": 89990,
                "features": [
                    "Intel Core i7-13620H",
                    "NVIDIA RTX 4050 6GB",
                    "16GB DDR5 RAM",
                    "512GB PCIe 4.0 SSD",
                    "15.6\" FHD 144Hz"
                ],
                "rating": 4.4,
                "reviews": [
                    "Good entry-level gaming performance",
                    "Decent build quality",
                    "144Hz display is smooth",
                    "Good value for money",
                    "Runs a bit warm under load"
                ]
            },
            {
                "name": "Acer Nitro V 15 (2024)",
                "price": 69990,
                "features": [
                    "Intel Core i5-13420H",
                    "NVIDIA RTX 3050 6GB",
                    "16GB DDR5 RAM",
                    "512GB PCIe SSD",
                    "15.6\" FHD 144Hz"
                ],
                "rating": 4.3,
                "reviews": [
                    "Great budget gaming laptop",
                    "Good performance for the price",
                    "Decent display",
                    "Adequate cooling",
                    "Value for money"
                ]
            },
            {
                "name": "Dell G15 Gaming (2024)",
                "price": 74990,
                "features": [
                    "AMD Ryzen 5 7535HS",
                    "NVIDIA RTX 3050 6GB",
                    "16GB DDR5 RAM",
                    "512GB PCIe SSD",
                    "15.6\" FHD 120Hz"
                ],
                "rating": 4.4,
                "reviews": [
                    "Reliable performance",
                    "Good build quality",
                    "Decent battery life",
                    "Effective cooling system",
                    "Good value proposition"
                ]
            }
        ]
        
        # Filter by price range
        filtered_laptops = [laptop for laptop in laptops if min_price <= laptop["price"] <= max_price]
        return filtered_laptops
    
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
        
        # Filter by price range
        filtered_earbuds = [earbud for earbud in earbuds if min_price <= earbud["price"] <= max_price]
        return filtered_earbuds
    
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
        
        # Filter by price range
        filtered_watches = [watch for watch in smartwatches if min_price <= watch["price"] <= max_price]
        return filtered_watches
    
    def _get_smartphone_data(self, min_price, max_price):
        smartphones = [
            {
                "name": "iPhone 15 Pro Max",
                "price": 159900,
                "features": ["A17 Pro chip", "6.7-inch Super Retina XDR display", "48MP Main + 12MP Ultra Wide + 12MP Telephoto", "Titanium design", "USB-C"],
                "rating": 4.8,
                "reviews": [
                    "Best iPhone camera system yet",
                    "Titanium build feels premium",
                    "Excellent performance",
                    "Great battery life",
                    "USB-C is a welcome addition"
                ]
            },
            {
                "name": "Samsung Galaxy S24 Ultra",
                "price": 129999,
                "features": ["Snapdragon 8 Gen 3", "6.8-inch QHD+ Dynamic AMOLED", "200MP Main + 12MP Ultra + Dual Telephoto", "Titanium frame", "AI features"],
                "rating": 4.7,
                "reviews": [
                    "Excellent camera system",
                    "Galaxy AI features are useful",
                    "S Pen functionality is great",
                    "Premium build quality",
                    "Impressive battery life"
                ]
            },
            {
                "name": "OnePlus 12",
                "price": 64999,
                "features": ["Snapdragon 8 Gen 3", "6.82-inch LTPO AMOLED", "50MP Main + 48MP Ultra + 64MP Telephoto", "100W charging", "Hasselblad cameras"],
                "rating": 4.6,
                "reviews": [
                    "Excellent value flagship",
                    "Super fast charging",
                    "Great display quality",
                    "Improved camera system",
                    "Strong performance"
                ]
            },
            {
                "name": "Nothing Phone (2)",
                "price": 44999,
                "features": ["Snapdragon 8+ Gen 1", "6.7-inch LTPO OLED", "50MP Main + 50MP Ultra", "Glyph Interface", "Wireless charging"],
                "rating": 4.4,
                "reviews": [
                    "Unique design with Glyph",
                    "Clean software experience",
                    "Good camera performance",
                    "Solid build quality",
                    "Decent battery life"
                ]
            },
            {
                "name": "Pixel 8 Pro",
                "price": 106999,
                "features": ["Google Tensor G3", "6.7-inch Super Actua display", "50MP Main + 48MP Ultra + 48MP Telephoto", "AI features", "7 years updates"],
                "rating": 4.7,
                "reviews": [
                    "Best camera experience",
                    "AI features are impressive",
                    "Clean Android experience",
                    "Great display quality",
                    "Long software support"
                ]
            },
            {
                "name": "Redmi Note 13 Pro+ 5G",
                "price": 31999,
                "features": ["Dimensity 7200 Ultra", "6.67-inch 1.5K AMOLED", "200MP Main camera", "120W charging", "IP68 rating"],
                "rating": 4.3,
                "reviews": [
                    "Great value for money",
                    "Premium build quality",
                    "Fast charging is amazing",
                    "Good camera performance",
                    "MIUI has some bloatware"
                ]
            }
        ]
        
        # Filter by price range
        filtered_phones = [phone for phone in smartphones if min_price <= phone["price"] <= max_price]
        return filtered_phones
    
    def _get_tv_data(self, min_price, max_price):
        tvs = [
            {
                "name": "Samsung 65-inch Neo QLED QN90C",
                "price": 189990,
                "features": ["4K Neo QLED", "Mini LED Technology", "Neural Quantum Processor 4K", "Gaming Hub", "Object Tracking Sound+"],
                "rating": 4.8,
                "reviews": [
                    "Exceptional picture quality",
                    "Great for gaming with low latency",
                    "Impressive brightness levels",
                    "Good sound system",
                    "Premium build quality"
                ]
            },
            {
                "name": "LG C3 65-inch OLED evo",
                "price": 209990,
                "features": ["4K OLED evo", "α9 AI Processor Gen6", "Dolby Vision IQ", "NVIDIA G-SYNC", "4 HDMI 2.1 ports"],
                "rating": 4.9,
                "reviews": [
                    "Perfect blacks and contrast",
                    "Excellent for gaming",
                    "WebOS is smooth",
                    "Great upscaling",
                    "Best-in-class picture quality"
                ]
            },
            {
                "name": "Sony Bravia XR X90L 65-inch",
                "price": 159990,
                "features": ["Full Array LED", "XR Cognitive Processor", "Google TV", "Acoustic Multi-Audio", "HDMI 2.1"],
                "rating": 4.7,
                "reviews": [
                    "Natural picture quality",
                    "Great motion handling",
                    "Good for PS5 gaming",
                    "Excellent upscaling",
                    "Google TV works well"
                ]
            },
            {
                "name": "OnePlus 65-inch Q2 Pro",
                "price": 99990,
                "features": ["QLED Technology", "4K Resolution", "Google TV", "Dolby Vision & Atmos", "HDMI 2.1"],
                "rating": 4.5,
                "reviews": [
                    "Great value for money",
                    "Good picture quality",
                    "Smooth performance",
                    "Decent sound output",
                    "Premium design"
                ]
            },
            {
                "name": "Hisense 65U7K QLED",
                "price": 84990,
                "features": ["QLED Technology", "144Hz Refresh Rate", "Full Array Local Dimming", "Dolby Vision IQ", "IMAX Enhanced"],
                "rating": 4.4,
                "reviews": [
                    "Excellent value proposition",
                    "Good gaming features",
                    "Bright HDR performance",
                    "Decent sound quality",
                    "Feature-rich for the price"
                ]
            },
            {
                "name": "TCL 65-inch QLED C645",
                "price": 69990,
                "features": ["4K QLED", "Google TV", "Dolby Vision", "HDMI 2.1", "Game Master 2.0"],
                "rating": 4.3,
                "reviews": [
                    "Great budget option",
                    "Good picture quality",
                    "Gaming features work well",
                    "Value for money",
                    "Google TV is smooth"
                ]
            }
        ]
        
        # Filter by price range
        filtered_tvs = [tv for tv in tvs if min_price <= tv["price"] <= max_price]
        return filtered_tvs
    
    def _get_refrigerator_data(self, min_price, max_price):
        refrigerators = [
            {
                "name": "LG 687L French Door Refrigerator",
                "price": 129990,
                "features": [
                    "Linear Inverter Compressor",
                    "Door-in-Door",
                    "Smart Diagnosis",
                    "Fresh Air Filter",
                    "Smart Connect"
                ],
                "rating": 4.8,
                "reviews": [
                    "Spacious and well-organized",
                    "Excellent cooling performance",
                    "Smart features are useful",
                    "Premium build quality",
                    "Energy efficient"
                ]
            },
            {
                "name": "Samsung 638L French Door Refrigerator",
                "price": 119990,
                "features": [
                    "Digital Inverter Technology",
                    "Twin Cooling Plus",
                    "Power Cool",
                    "LED Lighting",
                    "Frost Free"
                ],
                "rating": 4.7,
                "reviews": [
                    "Great storage space",
                    "Efficient cooling",
                    "Good organization",
                    "Quiet operation",
                    "Premium features"
                ]
            },
            {
                "name": "Whirlpool 340L Frost Free Double Door",
                "price": 32990,
                "features": [
                    "6th Sense Technology",
                    "IntelliSense Inverter",
                    "Microblock Technology",
                    "Stabilizer Free Operation",
                    "Frost Free"
                ],
                "rating": 4.5,
                "reviews": [
                    "Good value for money",
                    "Reliable performance",
                    "Spacious enough",
                    "Easy to maintain",
                    "Energy efficient"
                ]
            },
            {
                "name": "Haier 253L Frost Free Double Door",
                "price": 24990,
                "features": [
                    "Cooling on Wheels",
                    "Anti-Bacterial Gasket",
                    "Stabilizer Free Operation",
                    "Frost Free",
                    "Energy Efficient"
                ],
                "rating": 4.4,
                "reviews": [
                    "Compact and efficient",
                    "Good for small families",
                    "Cools well",
                    "Easy to maintain",
                    "Affordable option"
                ]
            },
            {
                "name": "Godrej 236L Frost Free Double Door",
                "price": 22990,
                "features": [
                    "Cool-Touch Technology",
                    "Stabilizer Free Operation",
                    "Frost Free",
                    "Energy Efficient",
                    "Spill-Proof Shelves"
                ],
                "rating": 4.3,
                "reviews": [
                    "Reliable brand",
                    "Good basic features",
                    "Value for money",
                    "Easy to clean",
                    "Suitable for Indian conditions"
                ]
            }
        ]
        
        # Filter by price range
        filtered_fridges = [fridge for fridge in refrigerators if min_price <= fridge["price"] <= max_price]
        return filtered_fridges
    
    def _get_washing_machine_data(self, min_price, max_price):
        washing_machines = [
            {
                "name": "LG 8kg Front Load",
                "price": 45990,
                "features": ["Inverter Direct Drive Motor", "Steam Function", "6 Motion DD", "Smart Diagnosis", "Child Lock"],
                "rating": 4.6,
                "reviews": [
                    "Excellent washing performance",
                    "Very quiet operation",
                    "Steam function works well",
                    "Energy efficient",
                    "Premium price but worth it"
                ]
            },
            {
                "name": "Samsung 7kg Front Load",
                "price": 39990,
                "features": ["Digital Inverter Motor", "Ecobubble Technology", "AddWash Door", "Smart Check", "Child Lock"],
                "rating": 4.5,
                "reviews": [
                    "Great washing results",
                    "Quiet operation",
                    "AddWash is convenient",
                    "Good for large loads",
                    "App connectivity is useful"
                ]
            },
            {
                "name": "Whirlpool 6.5kg Top Load",
                "price": 24990,
                "features": ["Power Clean Technology", "ZPF Technology", "Aqua Energie", "Magic Filter", "Child Lock"],
                "rating": 4.3,
                "reviews": [
                    "Good value for money",
                    "Cleans clothes well",
                    "Easy to use",
                    "Durable build",
                    "Suitable for Indian conditions"
                ]
            },
            {
                "name": "IFB 6.5kg Front Load",
                "price": 32990,
                "features": ["Aqua Energie", "Built-in Heater", "16 Programs", "Child Lock", "Delay End"],
                "rating": 4.4,
                "reviews": [
                    "Good washing performance",
                    "Built-in heater is useful",
                    "Multiple programs",
                    "Water efficient",
                    "After-sales service is good"
                ]
            }
        ]
        
        # Filter by price range
        filtered_machines = [machine for machine in washing_machines if min_price <= machine["price"] <= max_price]
        return filtered_machines
    
    def _get_camera_data(self, min_price, max_price):
        cameras = [
            {
                "name": "Canon EOS 250D",
                "price": 49990,
                "features": ["24.1MP APS-C Sensor", "4K Video Recording", "Dual Pixel CMOS AF", "Vari-angle Touch Screen", "Wi-Fi & Bluetooth"],
                "rating": 4.6,
                "reviews": [
                    "Great for beginners",
                    "Good image quality",
                    "Touch screen is responsive",
                    "Lightweight and portable",
                    "Battery life is decent"
                ]
            },
            {
                "name": "Nikon D3500",
                "price": 39990,
                "features": ["24.2MP DX Sensor", "1080p Video Recording", "11-point AF System", "Guide Mode", "Long Battery Life"],
                "rating": 4.5,
                "reviews": [
                    "Excellent for learning photography",
                    "Good image quality",
                    "Easy to use",
                    "Durable build",
                    "Great battery life"
                ]
            },
            {
                "name": "Sony Alpha A7 III",
                "price": 149990,
                "features": ["24.2MP Full-Frame Sensor", "4K Video Recording", "5-axis Stabilization", "Fast AF", "Weather Sealed"],
                "rating": 4.8,
                "reviews": [
                    "Professional-grade camera",
                    "Excellent low-light performance",
                    "Great video capabilities",
                    "Robust build quality",
                    "Expensive but worth it"
                ]
            },
            {
                "name": "Fujifilm X-T30",
                "price": 69990,
                "features": ["26.1MP APS-C Sensor", "4K Video Recording", "Fast AF", "Compact Design", "Film Simulation Modes"],
                "rating": 4.7,
                "reviews": [
                    "Great image quality",
                    "Compact and portable",
                    "Film simulations are excellent",
                    "Good for both photos and videos",
                    "Battery life could be better"
                ]
            }
        ]
        
        # Filter by price range
        filtered_cameras = [camera for camera in cameras if min_price <= camera["price"] <= max_price]
        return filtered_cameras
    
    def _get_tablet_data(self, min_price, max_price):
        tablets = [
            {
                "name": "iPad Pro 12.9-inch (2024)",
                "price": 119900,
                "features": [
                    "M2 chip",
                    "12.9-inch Liquid Retina XDR display",
                    "ProMotion & True Tone",
                    "12MP Wide + 10MP Ultra Wide cameras",
                    "Face ID"
                ],
                "rating": 4.9,
                "reviews": [
                    "Incredible performance",
                    "Best tablet display ever",
                    "Great for creative work",
                    "Premium build quality",
                    "Excellent for productivity"
                ]
            },
            {
                "name": "Samsung Galaxy Tab S9 Ultra",
                "price": 108999,
                "features": [
                    "Snapdragon 8 Gen 2",
                    "14.6-inch Dynamic AMOLED 2X",
                    "S Pen included",
                    "12MP + 12MP Dual front cameras",
                    "IP68 water resistance"
                ],
                "rating": 4.8,
                "reviews": [
                    "Massive beautiful display",
                    "Great for multitasking",
                    "S Pen works perfectly",
                    "Good battery life",
                    "Premium Android tablet"
                ]
            },
            {
                "name": "iPad Air (5th gen)",
                "price": 59900,
                "features": [
                    "M1 chip",
                    "10.9-inch Liquid Retina display",
                    "Touch ID",
                    "12MP Ultra Wide front camera",
                    "USB-C"
                ],
                "rating": 4.7,
                "reviews": [
                    "Great performance",
                    "Perfect size for most users",
                    "Good value for money",
                    "Nice display quality",
                    "Versatile device"
                ]
            },
            {
                "name": "Xiaomi Pad 6 Pro",
                "price": 29999,
                "features": [
                    "Snapdragon 8+ Gen 1",
                    "11-inch 144Hz LCD",
                    "8600mAh battery",
                    "13MP rear camera",
                    "Quad speakers"
                ],
                "rating": 4.5,
                "reviews": [
                    "Great value tablet",
                    "Smooth performance",
                    "Good display quality",
                    "Long battery life",
                    "MIUI optimized well"
                ]
            },
            {
                "name": "OnePlus Pad",
                "price": 37999,
                "features": [
                    "Dimensity 9000",
                    "11.61-inch 144Hz LCD",
                    "9510mAh battery",
                    "67W SUPERVOOC charging",
                    "Dolby Vision"
                ],
                "rating": 4.4,
                "reviews": [
                    "Premium build quality",
                    "Great performance",
                    "Good battery life",
                    "Nice display",
                    "Clean software"
                ]
            },
            {
                "name": "realme Pad 2",
                "price": 19999,
                "features": [
                    "MediaTek Helio G99",
                    "11-inch 2K display",
                    "8360mAh battery",
                    "Quad speakers",
                    "33W fast charging"
                ],
                "rating": 4.3,
                "reviews": [
                    "Good budget tablet",
                    "Nice display for price",
                    "Decent performance",
                    "Good battery life",
                    "Value for money"
                ]
            }
        ]
        
        # Filter by price range
        filtered_tablets = [tablet for tablet in tablets if min_price <= tablet["price"] <= max_price]
        return filtered_tablets
    
    def _get_printer_data(self, min_price, max_price):
        printers = [
            {
                "name": "HP LaserJet Pro M428",
                "price": 19990,
                "features": ["Laser Printing", "20 PPM Print Speed", "1200 x 1200 dpi", "Automatic Duplex", "Wi-Fi Connectivity"],
                "rating": 4.5,
                "reviews": [
                    "Fast printing speed",
                    "Good print quality",
                    "Reliable performance",
                    "Easy to set up",
                    "Toner lasts long"
                ]
            },
            {
                "name": "Canon PIXMA TS5370",
                "price": 12990,
                "features": ["Inkjet Printing", "Color Printing", "4800 x 1200 dpi", "Automatic Duplex", "Wi-Fi & Bluetooth"],
                "rating": 4.3,
                "reviews": [
                    "Good for home use",
                    "Color prints are vibrant",
                    "Easy to use",
                    "Ink can be expensive",
                    "Wi-Fi setup is simple"
                ]
            },
            {
                "name": "Epson L3150",
                "price": 15990,
                "features": ["EcoTank Technology", "Color Printing", "5760 x 1440 dpi", "Automatic Duplex", "Wi-Fi Connectivity"],
                "rating": 4.6,
                "reviews": [
                    "Very economical to run",
                    "Good print quality",
                    "Large ink capacity",
                    "Initial cost is high",
                    "Reliable performance"
                ]
            },
            {
                "name": "Brother DCP-T426W",
                "price": 17990,
                "features": ["Ink Tank System", "Color Printing", "1200 x 6000 dpi", "Automatic Duplex", "Wi-Fi & USB Connectivity"],
                "rating": 4.4,
                "reviews": [
                    "Cost-effective printing",
                    "Good for small office",
                    "Easy to refill",
                    "Print quality is good",
                    "Setup is straightforward"
                ]
            }
        ]
        
        # Filter by price range
        filtered_printers = [printer for printer in printers if min_price <= printer["price"] <= max_price]
        return filtered_printers
    
    def _get_generic_data(self, category, min_price, max_price):
        # Generate generic product data based on the category
        products = []
        num_products = random.randint(3, 5)
        
        # Common features for different product types
        feature_templates = {
            "kitchen": ["Durable construction", "Easy to clean", "Ergonomic design", "Heat resistant", "Space saving"],
            "furniture": ["Sturdy build", "Modern design", "Easy assembly", "Space efficient", "Durable material"],
            "clothing": ["Comfortable fit", "Durable fabric", "Easy to wash", "Stylish design", "Breathable material"],
            "shoes": ["Comfortable fit", "Durable sole", "Breathable material", "Stylish design", "Good grip"],
            "accessories": ["Durable material", "Stylish design", "Versatile use", "Good quality", "Value for money"],
            "electronics": ["Energy efficient", "User-friendly interface", "Durable build", "Good performance", "Value for money"],
            "beauty": ["Natural ingredients", "Effective results", "Suitable for all skin types", "Long-lasting", "Pleasant fragrance"],
            "sports": ["Durable construction", "Comfortable fit", "Good performance", "Lightweight", "Easy to maintain"],
            "books": ["Well-written", "Engaging content", "Good print quality", "Durable binding", "Value for money"],
            "toys": ["Safe materials", "Educational value", "Durable construction", "Age appropriate", "Fun to play with"]
        }
        
        # Determine product type based on category
        product_type = "electronics"  # Default
        for key in feature_templates:
            if key in category.lower():
                product_type = key
                break
        
        # Get features for this product type
        features = feature_templates.get(product_type, feature_templates["electronics"])
        
        for i in range(num_products):
            price = random.randint(min_price, max_price)
            rating = round(random.uniform(3.5, 5.0), 1)
            
            # Select random features
            selected_features = random.sample(features, min(3, len(features)))
            
            product = {
                "name": f"{category.title()} {i+1}",
                "price": price,
                "features": selected_features,
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

    def _get_ac_data(self, min_price, max_price):
        acs = [
            {
                "name": "LG 1.5 Ton 5 Star AI Dual Inverter Split AC",
                "price": 44990,
                "features": [
                    "AI Convertible 6-in-1",
                    "Dual Inverter Compressor",
                    "Ocean Black Protection",
                    "HD Filter with Anti-Virus",
                    "Smart AC with IoT"
                ],
                "rating": 4.7,
                "reviews": [
                    "Excellent cooling performance",
                    "Very energy efficient",
                    "Smart features work well",
                    "Quiet operation",
                    "Premium build quality"
                ]
            },
            {
                "name": "Samsung 1.5 Ton 5 Star WindFree™ Split AC",
                "price": 42990,
                "features": [
                    "WindFree™ Cooling",
                    "Digital Inverter Technology",
                    "Triple Protection Filter",
                    "Auto Clean",
                    "SmartThings App Control"
                ],
                "rating": 4.6,
                "reviews": [
                    "Gentle cooling is amazing",
                    "Great energy savings",
                    "Easy to maintain",
                    "Good app integration",
                    "Premium features"
                ]
            },
            {
                "name": "Daikin 1.5 Ton 5 Star Inverter Split AC",
                "price": 39990,
                "features": [
                    "Coanda Airflow",
                    "Inverter Technology",
                    "PM 2.5 Filter",
                    "Powerful Mode",
                    "Auto Restart"
                ],
                "rating": 4.8,
                "reviews": [
                    "Best cooling performance",
                    "Very reliable",
                    "Energy efficient",
                    "Easy to clean",
                    "Worth the investment"
                ]
            },
            {
                "name": "Voltas 1.5 Ton 5 Star Inverter Split AC",
                "price": 32990,
                "features": [
                    "iFeel Technology",
                    "Inverter Compressor",
                    "Anti-Dust Filter",
                    "Sleep Mode",
                    "Auto Restart"
                ],
                "rating": 4.4,
                "reviews": [
                    "Good value for money",
                    "Efficient cooling",
                    "Quiet operation",
                    "Easy to install",
                    "Reliable performance"
                ]
            },
            {
                "name": "Blue Star 1.5 Ton 5 Star Inverter Split AC",
                "price": 34990,
                "features": [
                    "Flexi Cool Technology",
                    "Inverter Compressor",
                    "PM 2.5 Filter",
                    "Sleep Mode",
                    "Auto Restart"
                ],
                "rating": 4.5,
                "reviews": [
                    "Great cooling performance",
                    "Energy efficient",
                    "Good build quality",
                    "Easy maintenance",
                    "Value for money"
                ]
            }
        ]
        
        # Filter by price range
        filtered_acs = [ac for ac in acs if min_price <= ac["price"] <= max_price]
        return filtered_acs 
