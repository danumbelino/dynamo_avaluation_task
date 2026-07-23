Read the access log in the working directory and write a JSON report to /app/report.json.

1. Count the total number of requests in the log.
2. Count the number of unique client IP addresses.
3. Identify the most requested path.
4. Count how many times that path appears.
5. Write valid JSON with exactly these keys: total_requests, unique_clients, top_path, top_path_count.
6. Use integers for the counts and a string for top_path.