# langchain-single-agent

A minimal LangChain-based single-agent application that demonstrates how to build an AI-powered assistant using a language model and optional tools. This project is intended as a simple starting point for chat-driven workflows, tool calling, and experimentation with LangChain in a clean, production-friendly structure.

## Description

This project provides a lightweight template for creating a LangChain agent that:
- accepts user input
- passes it to an LLM
- optionally calls tools or external functions
- returns a final response in a conversational format

It is designed to be easy to extend for personal projects, prototypes, and learning workflows. The project follows a standard single-agent patterns typical in LangChain apps, where one model is orchestrating reasoning, tool use, and final output generation.

## Features

- Simple LangChain agent setup
- Environment-based configuration
- Support for model selection and tool integration
- Easy local development workflow
- Minimal structure for rapid prototyping
- Suitable for experimentation with OpenAI or compatible LLM providers

## Project Structure

```text
langchain-single-agent/
├── README.md
├── requirements.txt
├── .env.example
├── app.py
├── src/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   └── tools.py
├── .gitignore
└── .venv/
```

If your workspace layout differs slightly, the same structure can be adapted without changing the core workflow.

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or newer
- pip
- A valid API key for the LLM provider you plan to use (for example OpenAI)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd langchain-single-agent
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If you need to install the required packages manually, use:

```bash
pip install langchain python-dotenv openai
```

Depending on the model provider and LangChain version you use, additional packages may be required.

## Configuration

Create a `.env` file in the project root based on `.env.example`:

```bash
copy .env.example .env
```

or:

```bash
cp .env.example .env
```

Example `.env`:

```env
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
TEMPERATURE=0.7
```

Update the values to match your environment and model preferences.

## Usage

Run the application:

```bash
python app.py
```

If your project uses a module-based entry point, you may also run:

```bash
python -m src
```

Once the app starts, it will prompt for input or process a configured query depending on the implementation. The agent will use the model and tools to generate a response.

### Example

```python
from src.agent import build_agent

agent = build_agent()

response = agent.invoke({"input": "What is the weather in Paris?"})
print(response)
```

The exact usage may vary depending on the implementation of the app, but the core model is consistent:
- accept user input
- run through agent logic
- use tools if needed
- return a final answer

## How the Agent Works

The project follows a standard LangChain single-agent pattern:

1. The user enters a prompt.
2. The agent sends the prompt to an LLM.
3. The model decides whether it needs to use tools.
4. If a tool is needed, the agent invokes it.
5. The result is fed back into the model.
6. The model returns the final answer to the user.

This pattern makes the app useful for simple assistants, function calling workflows, and task-specific tools.

## Features in More Detail

### Tool Integration
The project can be extended with custom tools such as:
- calculator
- API client
- file lookup
- web search
- database query
- local document retrieval

### Prompt Engineering
The agent behavior can be modified by changing the system prompt or instructions passed to the model.

### Model Swapping
The project is designed to be flexible enough for different providers or model names, which makes testing alternate models easy.

## Development

To work on the project locally:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Then run the app or any tests you add while iterating on functionality.

## Testing

If the project includes tests, run them with:

```bash
pytest
```

If no tests are yet present, consider adding unit tests for:
- tool behavior
- prompt formatting
- model configuration loading
- error handling

## Contribution Guidelines

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature/my-improvement
```

3. Make your changes with clear, focused updates.
4. Run tests or validate the app behavior locally.
5. Commit your changes:

```bash
git commit -m "Add my improvement"
```

6. Open a pull request with:
- a summary of the change
- why it is needed
- any validation steps performed

### Contribution Expectations

- Keep code readable and maintainable
- Follow the project's style and conventions
- Document new features or configuration changes
- Avoid committing secrets or API keys
- Prefer small, well-tested pull requests

## Security Notes

- Do not commit `.env` files containing API keys
- Add sensitive files to `.gitignore`
- Review tool implementations carefully before using them in production
- Validate all external API calls and user inputs

## License

This project does not define a specific license in the workspace yet. If you plan to share or distribute it publicly, add an appropriate license such as MIT or Apache-2.0.

## Troubleshooting

Common issues include:

- missing `OPENAI_API_KEY`
- wrong model name or unsupported provider
- dependency mismatch
- invalid tool definitions
- environment variables not loaded from `.env`

To debug:
- verify the `.env` file exists and contains valid values
- reinstall dependencies
- check the LangChain and provider package versions
- inspect tool schemas and function arguments

## Summary

`langchain-single-agent` is a practical starting point for building a straightforward LangChain-based assistant with model reasoning and optional tool execution. It is intentionally lightweight, easy to understand, and simple to extend for learning, experimentation, or prototype applications.