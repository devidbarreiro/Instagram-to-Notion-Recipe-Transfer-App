# nlp/recipe_extractor.py

import os
import openai
from typing import Dict, List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_recipe_with_gpt(transcription: str, description: str) -> Dict[str, any]:
    """
    Extract recipe information from transcription and description using ChatGPT.
    
    :param transcription: Transcribed audio from the Instagram Reel
    :param description: Description text from the Instagram Reel
    :return: Dictionary containing structured recipe information
    """
    # Combine transcription and description
    full_text = f"Transcription: {transcription}\n\nDescription: {description}"
    
    # Prepare the prompt for ChatGPT
    prompt = f"""
    Based on the following transcription and description from an Instagram Reel, please extract and structure the recipe information:

    {full_text}

    Please provide the following information in a structured format:
    1. Recipe Title
    2. List of Ingredients (with quantities if available)
    3. Step-by-step Instructions
    4. Cooking Time (if mentioned)
    5. Servings (if mentioned)
    6. Difficulty Level (Easy, Medium, Hard)
    7. Meal Type (Breakfast, Lunch, Dinner, Snack, Dessert)
    8. Cuisine (e.g., Italian, Mexican, Indian, etc.)
    9. Diet Categories (e.g., Vegetarian, Vegan, Gluten-free, Keto, etc.)
    10. Keywords or Tags (relevant words that describe the recipe)

    Please format your response as a Python dictionary.
    """

    # Call the ChatGPT API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts recipe information from text."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,  # Lower temperature for more focused and consistent output
        max_tokens=1000  # Adjust as needed
    )

    # Extract the response
    recipe_info = response.choices[0].message['content']

    # Convert the string response to a Python dictionary
    # Note: This assumes that ChatGPT returns a well-formatted Python dictionary string
    recipe_dict = eval(recipe_info)

    return recipe_dict

def classify_recipe(recipe_info: Dict[str, any]) -> List[str]:
    """
    Generate classification tags based on the recipe information.
    
    :param recipe_info: Dictionary containing structured recipe information
    :return: List of classification tags
    """
    tags = []

    # Add meal type
    if recipe_info.get('Meal Type'):
        tags.append(recipe_info['Meal Type'].lower())

    # Add cuisine
    if recipe_info.get('Cuisine'):
        tags.append(recipe_info['Cuisine'].lower())

    # Add diet categories
    if recipe_info.get('Diet Categories'):
        tags.extend([cat.lower() for cat in recipe_info['Diet Categories']])

    # Add difficulty level
    if recipe_info.get('Difficulty Level'):
        tags.append(recipe_info['Difficulty Level'].lower())

    # Add cooking time category
    cooking_time = recipe_info.get('Cooking Time', '')
    if cooking_time:
        time_value = int(''.join(filter(str.isdigit, cooking_time)))
        if time_value <= 15:
            tags.append('quick')
        elif time_value <= 30:
            tags.append('medium')
        else:
            tags.append('long')

    # Add any additional keywords or tags
    if recipe_info.get('Keywords or Tags'):
        tags.extend([tag.lower() for tag in recipe_info['Keywords or Tags']])

    return list(set(tags))  # Remove duplicates

def process_recipe(transcription: str, description: str) -> Dict[str, any]:
    """
    Process the recipe by extracting information and classifying it.
    
    :param transcription: Transcribed audio from the Instagram Reel
    :param description: Description text from the Instagram Reel
    :return: Dictionary containing processed recipe information
    """
    recipe_info = extract_recipe_with_gpt(transcription, description)
    tags = classify_recipe(recipe_info)

    processed_recipe = {
        'title': recipe_info['Recipe Title'],
        'ingredients': recipe_info['List of Ingredients'],
        'instructions': recipe_info['Step-by-step Instructions'],
        'cooking_time': recipe_info.get('Cooking Time', ''),
        'servings': recipe_info.get('Servings', ''),
        'tags': tags
    }

    return processed_recipe

# Example usage
if __name__ == "__main__":
    sample_transcription = "Today we're making a quick and easy pasta dish. You'll need spaghetti, garlic, olive oil, red pepper flakes, and parmesan cheese. First, cook the pasta. Then, in a pan, sauté minced garlic in olive oil. Add red pepper flakes. Toss the cooked pasta in the garlic oil. Top with grated parmesan. Enjoy your simple and delicious pasta!"
    sample_description = "Quick and easy spaghetti aglio e olio recipe! Perfect for a weeknight dinner. #ItalianFood #VegetarianRecipe #QuickMeals"

    result = process_recipe(sample_transcription, sample_description)
    print(result)