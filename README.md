# FastAPI Hello World

A simple FastAPI application with multiple endpoints, built as a submission for the MuLearn GECT CR task.

## Author

**Sooraj K R** — 3rd Year CSE Student

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Returns a hello message from the API |
| `GET` | `/about` | Returns author name and bio |
| `GET` | `/greet/{name}` | Returns a personalized greeting |

## Setup & Run

```bash
# Clone the repository
git clone https://github.com/PixelProgrammer4209/fastapi-hello-world.git
cd fastapi-hello-world

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

Interactive API docs are at `http://127.0.0.1:8000/docs`.

## Example Responses

**`GET /`**
```json
{"message": "Hello from my API"}
```

**`GET /about`**
```json
{"Name": "Sooraj K R", "Bio": "Hi i am a 3rd year CSE student who is constantly learning"}
```

**`GET /greet/Sooraj`**
```json
{"message": "Hello Sooraj, nice to meet you"}
```

## Tech Stack

- **Python** 3.x
- **FastAPI** — Modern, high-performance web framework
- **Uvicorn** — ASGI server
