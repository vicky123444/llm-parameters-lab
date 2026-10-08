# LLM Parameters Lab

Practical Python experiments for understanding LLM tokens, context windows, temperature, and generation parameters.

This repository accompanies the blog article **Tokens, Context Windows & Temperature Explained: What Software Engineers Need to Know**.

## Experiments

- Tokenization with `tiktoken`
- Context-window budget calculations
- Temperature and output-variability simulation
- Optional LLM API parameter example using `temperature`, `max_tokens`, and `top_p`
- Automated tests with pytest

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

python token_demo.py
python context_demo.py
python temperature_demo.py
```

Run tests:

```bash
python -m pytest test_llm_parameters.py -q
```

## API example

`api_demo.py` is optional and requires an `OPENAI_API_KEY` environment variable. Do not commit API keys.

## Note about temperature demo

The temperature experiment is intentionally a local simulation so readers can run it without an API key. It demonstrates the concept of increasing/decreasing output variability; it is not a real model-sampling implementation.

## Project structure

- `token_demo.py` — tokenization examples
- `context_demo.py` — context budget calculations
- `temperature_demo.py` — temperature variability simulation
- `api_demo.py` — optional API parameter example
- `test_llm_parameters.py` — pytest tests
- `temperature_variability.png` — sample visualization
- `.github/workflows/python-tests.yml` — CI test workflow

## Author

Vikram Singh — Practical AI, Cloud & Software Engineering
