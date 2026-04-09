import ollama


response = ollama.chat(model='gemma4:e4b', messages=[
    {
        'role': 'user',
        'content': 'Write a short and clever Python script to reverse a string.',
    },
])

# Print the model's response
print(response['message']['content'])
