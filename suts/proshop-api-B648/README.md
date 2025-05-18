## Set up environment
```bash
git clone https://anonymous.4open.science/r/proshop-api-B648.git
cd proshop-api
pip install -r requirements.txt
```

## Run with uvicorn

```bash
uvicorn src.main:app --host=0.0.0.0 --port=8000 
```
