import shutil
from datetime import datetime
from pathlib import Path

def ingest_csv(source_path: str, entity: str):
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(f"data/raw/files/{entity}")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{entity}_{timestamp}.csv"
    shutil.copy(source_path, output_file)

    print(f"Ingested file into {output_file}")