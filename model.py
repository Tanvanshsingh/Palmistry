import openai
import cv2
import json
import os

# Load configuration from config.json
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
    with open(config_path) as config_file:
        return json.load(config_file)

config = load_config()
openai.api_key = config["GPT_API_KEY"]
client = openai.OpenAI(api_key=config["GPT_API_KEY"])

def process_image(file_path):
    # Example: Using OpenCV to process the image
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    # Further image processing steps go here
    return image

def generate_palmistry_reading(image_data):
    # Convert image_data to a format suitable for GPT-3.5 Turbo
    # For this example, we assume image_data is a placeholder
    prompt = f"Provide a palmistry reading based on this image data: {image_data}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a palmistry expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()
