import requests
import json
from datetime import datetime
from pathlib import Path

API_URL = "https://fakestoreapi.com/products"

def ingest_products():
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("data/raw/api/products")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"products_{timestamp}.json"

    with open(output_file, "w") as f:
        json.dump(data, f)

    print(f"Saved {len(data)} records to {output_file}")

if __name__ == "__main__":
    ingest_products()