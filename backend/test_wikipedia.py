import sys
import os

# Add the current directory to sys.path to import wikipedia_service
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from wikipedia_service import get_wikipedia_image

def test_wikipedia_images():
    test_topics = [
        "Reinforcement Learning",
        "Transformer (machine learning model)",
        "Quantum Computing",
        "Blockchain",
        "Artificial Intelligence"
    ]
    
    print("      🧪 Testing Wikipedia Image Fetching")
    print("      " + "="*40)
    
    for topic in test_topics:
        print(f"      🔍 Searching for: {topic}")
        url = get_wikipedia_image(topic)
        if url:
            print(f"      ✅ Success! URL: {url}")
        else:
            print(f"      ❌ Failed to find image for: {topic}")
        print("      " + "-"*40)

if __name__ == "__main__":
    test_wikipedia_images()
