from stt import listen_and_transcribe

if __name__ == "__main__":
    print("Select language:")
    print("1. Hindi")
    print("2. Telugu")

    choice = input("Enter choice (1 or 2): ")

    if choice == "2":
        language = "te-IN"
    else:
        language = "hi-IN"

    result = listen_and_transcribe(language=language)
    print("Final Output:", result)
