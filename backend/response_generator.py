import json

def load_knowledge_base():
    with open("data/knowledge_base.json", "r", encoding="utf-8") as f:
        return json.load(f)

def generate_response(intent, entities):
    kb = load_knowledge_base()

    if intent == "weather_query":
        date = entities.get("date", "today")
        return kb["weather"].get(date, "Weather information is currently unavailable.")

    if intent == "scheme_query":
        return kb["schemes"].get("general", "Scheme information is not available.")

    return "Sorry, I could not understand your request clearly."
