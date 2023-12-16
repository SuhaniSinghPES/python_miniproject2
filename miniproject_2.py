import matplotlib.pyplot as plt
import requests

API_KEY = "BR70lvg61mQzd/Ab6ysO7Q==d5aZ8mMEu633eVwL"
API_URL = "https://api.api-ninjas.com/v1/nutrition"

def get_nutrition_data(query):
    headers = {'X-Api-Key': API_KEY}
    params = {'query': query}

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def create_nutrition_graph(nutrition_data):
    if not nutrition_data:
        print("No nutrition data available.")
        return

    # Assuming the first item in the list contains the nutrition data
    first_food_item = nutrition_data[0]
    labels = list(first_food_item.keys())
    values = [float(value) if isinstance(value, (int, float)) else 0 for value in first_food_item.values()]

    # Plotting the bar chart
    plt.bar(labels, values, color=['blue', 'green', 'red', 'purple', 'orange'])
    plt.title('Nutrition Values')
    plt.xlabel('Nutrients')
    plt.ylabel('Amount (g)')
    plt.show()

if __name__ == '__main__':
    # Taking user input for food item
    food_query = input('Enter a food item: ')

    # Fetching nutrition data from the API
    nutrition_data = get_nutrition_data(food_query)

    # Creating and displaying the graph
    create_nutrition_graph(nutrition_data)
