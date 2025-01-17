# Data points fo
# r training ML model with input query and expected output
import json
data_points = [
    {
        "query": "List 20 ML engineers in San Francisco with expertise in computer vision",
        "output": {
            "k": 20,
            "type": ["github"],
            "location": "San Francisco",
            "fields": ["Computer Vision"]
        }
    },
    {
        "query": "I need the top 30 data scientists in Seattle focusing on big data and analytics",
        "output": {
            "k": 30,
            "type": ["google scholar", "github"],
            "location": "Seattle",
            "fields": ["Big Data", "Analytics"]
        }
    },
    {
        "query": "Who are the leading 50 AI researchers in Boston working on self-driving cars?",
        "output": {
            "k": 50,
            "type": ["google scholar"],
            "location": "Boston",
            "fields": ["Self-Driving Cars"]
        }
    },
    {
        "query": "Find 15 machine learning engineers in New York with experience in reinforcement learning.",
        "output": {
            "k": 15,
            "type": ["github"],
            "location": "New York",
            "fields": ["Reinforcement Learning"]
        }
    },
    {
        "query": "Give me 25 data scientists in Los Angeles specializing in NLP and text analytics.",
        "output": {
            "k": 25,
            "type": ["google scholar", "github"],
            "location": "Los Angeles",
            "fields": ["NLP", "Text Analytics"]
        }
    },
    {
        "query": "Who are the top 10 deep learning researchers in San Francisco?",
        "output": {
            "k": 10,
            "type": ["google scholar"],
            "location": "San Francisco",
            "fields": ["Deep Learning"]
        }
    },
    {
        "query": "List 20 AI engineers in Toronto with expertise in image processing.",
        "output": {
            "k": 20,
            "type": ["github"],
            "location": "Toronto",
            "fields": ["Image Processing"]
        }
    },
    {
        "query": "I need 30 machine learning researchers in Chicago focusing on predictive analytics.",
        "output": {
            "k": 30,
            "type": ["google scholar"],
            "location": "Chicago",
            "fields": ["Predictive Analytics"]
        }
    },
    {
        "query": "Find 15 data scientists in Boston with experience in big data.",
        "output": {
            "k": 15,
            "type": ["github"],
            "location": "Boston",
            "fields": ["Big Data"]
        }
    },
    {
        "query": "List 20 AI researchers in Austin working on autonomous vehicles.",
        "output": {
            "k": 20,
            "type": ["google scholar"],
            "location": "Austin",
            "fields": ["Autonomous Vehicles"]
        }
    },
    {
        "query": "I need 25 machine learning engineers in Seattle specializing in computer vision.",
        "output": {
            "k": 25,
            "type": ["github"],
            "location": "Seattle",
            "fields": ["Computer Vision"]
        }
    },
    {
        "query": "Who are the leading 20 NLP researchers in New York?",
        "output": {
            "k": 20,
            "type": ["google scholar"],
            "location": "New York",
            "fields": ["NLP"]
        }
    },
    {
        "query": "Find 30 data scientists in San Diego with expertise in data mining.",
        "output": {
            "k": 30,
            "type": ["github"],
            "location": "San Diego",
            "fields": ["Data Mining"]
        }
    },
    {
        "query": "Give me 15 AI engineers in Vancouver focusing on robotics.",
        "output": {
            "k": 15,
            "type": ["github"],
            "location": "Vancouver",
            "fields": ["Robotics"]
        }
    },
    {
        "query": "Who are the top 25 machine learning researchers in London working on healthcare AI?",
        "output": {
            "k": 25,
            "type": ["google scholar"],
            "location": "London",
            "fields": ["Healthcare AI"]
        }
    },
    {
        "query": "List 20 data scientists in Melbourne specializing in bioinformatics.",
        "output": {
            "k": 20,
            "type": ["google scholar"],
            "location": "Melbourne",
            "fields": ["Bioinformatics"]
        }
    },
    {
        "query": "I need 30 machine learning engineers in Berlin with expertise in GANs.",
        "output": {
            "k": 30,
            "type": ["github"],
            "location": "Berlin",
            "fields": ["GANs"]
        }
    },
    {
        "query": "Find 10 AI researchers in Paris focusing on neural networks.",
        "output": {
            "k": 10,
            "type": ["google scholar"],
            "location": "Paris",
            "fields": ["Neural Networks"]
        }
    },
    {
        "query": "List 25 data scientists in Mumbai with experience in machine learning.",
        "output": {
            "k": 25,
            "type": ["github"],
            "location": "Mumbai",
            "fields": ["Machine Learning"]
        }
    },
    {
        "query": "I need 20 AI engineers in Singapore specializing in speech recognition.",
        "output": {
            "k": 20,
            "type": ["github"],
            "location": "Singapore",
            "fields": ["Speech Recognition"]
        }
    }
]

# Save to a JSON file
output_file_path = "datalog/data.json"

with open(output_file_path, 'w') as file:
    json.dump(data_points, file, indent=4)

