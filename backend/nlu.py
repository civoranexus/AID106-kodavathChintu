def detect_intent(text):
    if not text:
        return "unknown_intent"

    text = text.lower()

    weather_keywords = [
        "weather", "rain", "forecast",
        "मौसम", "बारिश",
        "వాతావరణం", "వర్షం"
    ]

    scheme_keywords = [
        "scheme", "yojana",
        "योजना",
        "పథకం", "స్కీమ్"
    ]

    for word in weather_keywords:
        if word in text:
            return "weather_query"

    for word in scheme_keywords:
        if word in text:
            return "scheme_query"

    return "unknown_intent"


def extract_entities(text):
    entities = {}

    if not text:
        return entities

    if any(word in text for word in ["tomorrow", "कल", "రేపు"]):
        entities["date"] = "tomorrow"
    elif any(word in text for word in ["today", "आज", "ఈరోజు"]):
        entities["date"] = "today"

    return entities
