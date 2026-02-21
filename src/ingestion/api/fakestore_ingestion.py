import requests
import json
from datetime import datetime
from pathlib import Path
from utils.logger import get_logger
from config.settings import API_URL, RAW_BASE_PATH, REQUEST_TIMEOUT

logger = get_logger(__name__)

logger.info("Starting product ingestion...")


def ingest_products():
    try:
      response = requests.get(API_URL, timeout=REQUEST_TIMEOUT)
      response.raise_for_status()
    except requests.exceptions.RequestException as e:
      logger.error(f"API request failed: {e}")
      raise

    data = response.json()
    data = response.json()

if not isinstance(data, list):
    logger.error("Unexpected API response format")
    raise ValueError("API did not return a list")

if len(data) == 0:
    logger.warning("API returned empty dataset")

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("data/raw/api/products")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"products_{timestamp}.json"

    with open(output_file, "w") as f:
        json.dump(data, f)

    print(f"Saved {len(data)} records to {output_file}")

if __name__ == "__main__":
    ingest_products()