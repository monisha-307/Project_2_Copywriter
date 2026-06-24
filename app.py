import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

# User Inputs
product_name = input("Enter Product Name: ")
platform = input("Enter Platform (LinkedIn/Instagram/Email): ")
tone = input("Enter Tone (Professional/Friendly/Casual): ")
description = input("Enter Product Description: ")

# Dynamic Prompt
prompt = f"""
You are a professional copywriter.

Create a {tone} marketing copy for {platform}.

Product Name: {product_name}

Product Description:
{description}

Generate an attractive marketing content.
"""

response = model.generate_content(
    prompt,
    generation_config={
        "temperature": 0.8,
        "top_p": 0.9
    }
)

print("\nGenerated Copy:\n")
print(response.text)