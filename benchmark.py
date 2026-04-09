import ollama

# Define the models you want to compare
models_to_test = ['gemma4:e2b', 'gemma4:e4b',
                  'gemma4:26b']  # You can also add gemma4:31b

# The standard prompt to test across all models
prompt = "Explain the concept of recursion in programming using a real-world analogy. Keep it under 2 paragraphs."

results = []

print("Starting the Gemma Benchmark...")
print("-" * 65)

for model in models_to_test:
    print(f"Loading and testing {model} (this may take a moment)...")

    try:
        # Send the prompt to the model
        response = ollama.chat(model=model, messages=[
            {'role': 'user', 'content': prompt}
        ])

        # Ollama returns durations in nanoseconds. We convert them to seconds.
        # eval_duration is the time spent actively generating the response
        eval_duration_sec = response['eval_duration'] / 1e9

        # Extract token counts
        prompt_tokens = response.get('prompt_eval_count', 0)
        gen_tokens = response.get('eval_count', 0)

        # Calculate Speed (Tokens per Second)
        speed_tps = gen_tokens / eval_duration_sec if eval_duration_sec > 0 else 0

        # Save the metrics
        results.append({
            'Model': model,
            'Prompt Tokens': prompt_tokens,
            'Generated Tokens': gen_tokens,
            'Time (s)': round(eval_duration_sec, 2),
            'Speed (t/s)': round(speed_tps, 2)
        })

        print(f"✅ Finished {model} at {round(speed_tps, 2)} tokens/sec")

    except Exception as e:
        print(f"❌ Error running {model}. Did you pull it first?")
        print(f"Error details: {e}")

# Print the final comparison table
print("\n" + "="*65)
print("BENCHMARK RESULTS")
print("="*65)
print(f"{'Model':<15} | {'Gen Tokens':<12} | {'Time (s)':<10} | {'Speed (t/s)':<12}")
print("-" * 65)

for res in results:
    print(f"{res['Model']:<15} | {res['Generated Tokens']:<12} | {res['Time (s)']:<10} | {res['Speed (t/s)']:<12}")

print("="*65)
