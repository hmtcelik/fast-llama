# Fastapi - Llama Service Implementation

Using FastAPI to create a llama service that can be use anywhere to talk with model.

### (the docker usage will be here soon)

> - (will be here a simple chat service that can be used to talk with model, with also considering message history)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
cd app
python main.py
```

When you run first time, the init_modal function will download Llama model from huggingface so it will take some time to download the model.

## Request Example for asking simple question:

```bash
curl -X POST \
  'http://localhost:8000/question/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"q": "What is the capital of France?"}'
```

## Response Example

```json
{ "answer": " The capital of France is Paris." }
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
