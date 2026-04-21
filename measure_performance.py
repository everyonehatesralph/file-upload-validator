import time
from src.validator import validate_file

filename = "example.pdf"
file_size_mb = 2

iterations = 100000

start = time.time()
for _ in range(iterations):
    validate_file(filename, file_size_mb)
end = time.time()

print(f"Execution time for {iterations} runs: {end - start:.6f} seconds")