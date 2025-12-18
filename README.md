# Recipe Generator 🍳

A fun Streamlit application that generates creative meal recipes from your ingredients and rewrites them in the style of a 1920s New York Mafia gangster using LangChain and OpenAI.

## Features

- 🥘 **Recipe Generation**: Input ingredients and get meal suggestions powered by OpenAI
- 🎭 **Gangster Style Transformation**: Automatically rewrites recipes in 1920s gangster slang
- ⛓️ **Sequential Chain Processing**: Uses LangChain's LCEL (LangChain Expression Language) to chain prompts without LLMChain
- 🎨 **Interactive UI**: Built with Streamlit for a smooth user experience

## How It Works

The application uses a sequential chain that:
1. Takes your ingredients as input
2. Generates a meal recipe using the first prompt template
3. Passes the recipe through a lambda function to format it
4. Transforms it into gangster-style language using the second prompt template
5. Returns the final gangster-styled recipe

## Tech Stack

- **Python 3.x**
- **Streamlit**: Web interface
- **LangChain**: Prompt chaining and orchestration
- **OpenAI API**: Language model for generation
- **python-dotenv**: Environment variable management

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd recipe_generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run src/main.py
```

2. Enter your ingredients in the text input (comma-separated)
3. Click "Generate Recipe"
4. Watch as the app generates a meal and rewrites it in gangster style!

## Example

**Input:** `chicken, rice, broccoli`

**Output:** 
```
Listen here, see? You're gonna make yourself a real classy dish, 
capisce? Take that chicken, rough it up real good, then mix it 
with the rice and that green stuff - broccoli, they call it. 
Cook it up nice, or you'll be sleepin' with the fishes, ya hear?
```

## Project Structure

```
recipe_generator/
├── src/
│   └── main.py          # Main application code
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .env                # Environment variables (not tracked)
```

## Key Code Pattern

The application uses LangChain's modern pipe operator (`|`) to create a sequential chain:

```python
sequential_chain = (
    prompt_template 
    | llm 
    | (lambda output: {"meals": output})
    | gangster_template_prompt 
    | llm
)
```

This approach eliminates the need for the deprecated `LLMChain` class.

## Requirements

See [requirements.txt](requirements.txt) for full dependencies.

## License

MIT License

## Contributing

Feel free to submit issues or pull requests!

## Acknowledgments

Built as part of a LangChain learning project demonstrating sequential prompt chaining.
