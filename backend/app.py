from stt import listen_and_transcribe
from nlu import detect_intent, extract_entities
from response_generator import generate_response

if __name__ == "__main__":
    print("Select language:")
    print("1. Hindi")
    print("2. Telugu")

    choice = input("Enter choice (1 or 2): ")

    if choice == "2":
        language = "te-IN"
    else:
        language = "hi-IN"

    text = listen_and_transcribe(language=language)

    intent = detect_intent(text)
    entities = extract_entities(text)

    response = generate_response(intent, entities)

    print("🔍 Intent:", intent)
    print("📌 Entities:", entities)
    print("🗣️ Response:", response)
