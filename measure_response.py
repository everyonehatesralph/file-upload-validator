import time
from src.validator import validate_file

runs = 5
times = []

for i in range(runs):
    start = time.time()
    validate_file("example.pdf", 2)
    end = time.time()
    response_time = end - start
    times.append(response_time)
    print(f"Run {i+1}: {response_time:.6f} seconds")

average_time = sum(times) / len(times)
print(f"\nAverage response time: {average_time:.6f} seconds")