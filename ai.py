from openai import OpenAI

client = OpenAI(
    # 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
    api_key = "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"
   # api_key="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"  # Replace with your actual API key
)

def chat():
    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        response = completion.choices[0].message.content
        print("Bot:", response)

if __name__ == "__main__":
    chat()
