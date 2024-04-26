import requests

api_key = 'fbf3c021ba9a4b8ba073913062c1d144'  # Replace 'YOUR_API_KEY' with your Spoonacular API key
meal = input("Enter the meal you want a recipe for: ")
endpoint = "https://api.spoonacular.com/recipes/random"
params = {
    "number": 1,  # Number of recipes to retrieve
    "tags": meal,  # Tag to search for (e.g., "dinner", "breakfast", "chicken")
     "apiKey": api_key
    }
response = requests.get(endpoint, params=params)
    
if response.status_code == 200:
    data = response.json()
    if 'recipes' in data and len(data['recipes']) > 0:
        recipe = data['recipes'][0]
        recipe_name = recipe['title']
        recipe_instructions = recipe['instructions']
        print(f"Recipe for {meal}:")
        print(f"Name: {recipe_name}")
        print("Instructions:")
        print(recipe_instructions)
    else:
       print("No recipe found for this meal.")
else:
    print("Failed to retrieve recipe. Please try again later.")


        