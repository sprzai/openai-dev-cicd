import openai
openai.api_key = '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'

def generate_text(prompt, temperature=0.5, max_tokens=100, stop=None):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop
    )
    message = completions.choices[0].text.strip()
    return message

def generate_multiple_text(prompt, temperature=0.5, max_tokens=50, n=3, stop=None):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=n,
        stop=stop
    )
    messages = [choice.text.strip() for choice in completions.choices]
    return messages

'''prompt = "creame un dockerfile para api rest de flask?"
response = generate_text(prompt)
print(response)'''