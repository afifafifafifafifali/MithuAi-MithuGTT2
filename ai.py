from openai import OpenAI

client = OpenAI(
    api_key="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"  # Replace with your actual API key
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
