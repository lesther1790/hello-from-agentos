# hello-from-agentos

A minimal FastAPI project scaffolded by AgentOS.

## Requirements
- Python 3.9+

## Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/[YOUR_USER]/hello-from-agentos.git
cd hello-from-agentos

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
uvicorn main:app --reload
```

Open your browser at http://127.0.0.1:8000 — you should see:
```json
{"hello": "agentos"}
```

## API Docs
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc:       http://127.0.0.1:8000/redoc
