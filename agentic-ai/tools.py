def web_search():
    return [
        {
            "title": "AI-Based Crop Yield Prediction",
            "year": 2024,
            "content": "Uses deep learning models to predict crop yield."
        },
        {
            "title": "Machine Learning for Precision Agriculture",
            "year": 2023,
            "content": "Optimizes irrigation and fertilizer using ML."
        },
        {
            "title": "Computer Vision in Smart Farming",
            "year": 2023,
            "content": "Detects crop diseases using image processing."
        }
    ]

def summarize(paper):
    return f"{paper['content']} (Published {paper['year']})"
