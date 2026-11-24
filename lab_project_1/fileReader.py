import gzip

def stream_dataset(filepath):
        opener = gzip.open if filepath.endswith(".gz") else open
        with opener(filepath, "rt", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield sorted(set(int(item) for item in line.split()))