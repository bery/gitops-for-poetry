from transformers import pipeline

def initialize_poetry_generator():
    """Initializes the poetry generator using GPT-2."""
    print("Loading the poetry generator...")
    return pipeline("text-generation", model="gpt2")

def generate_poetry(prompt: str, generator, max_length: int = 50) -> str:
    """Generates poetry based on the provided prompt."""
    # Add a poetic framing to the prompt
    poetic_prompt = f"{prompt}\n\nWrite a poem:\n"

    print(f"\nGenerating poetry for the prompt: '{prompt}'")
    result = generator(
        poetic_prompt,
        max_length=max_length,
        num_return_sequences=1,
        temperature=0.8,  # Adjust for more creativity
        top_k=50          # Focus on more likely words for coherent poetry
    )
    return result[0]["generated_text"]

def main():
    """Main function to interact with the user and generate poetry."""
    print("Welcome to the Poetry AI application!")
    generator = initialize_poetry_generator()

    while True:
        prompt = input("\nEnter a theme or idea for your poem (or type 'exit' to quit): ").strip()
        if prompt.lower() == "exit":
            print("Goodbye! Keep creating poetry!")
            break

        poetry = generate_poetry(prompt, generator)
        # Post-process to remove overly verbose output
        poetic_lines = poetry.split('\n')[:8]  # Limit to 8 lines of poetry
        print("\nHere is your poem:")
        print("\n".join(poetic_lines))

if __name__ == "__main__":
    main()
