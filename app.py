import ollama


response = ollama.chat(model='gemma4:e4b', messages=[
    {
        'role': 'user',
        'content': 'Give me a good name for a github repository where i explore Gemma4. I am thinking of "Gemma4Playground".',
        # 'content': 'Write a short and clever Python script to reverse a string.',
    },
])

# Print the model's response
print(response['message']['content'])
