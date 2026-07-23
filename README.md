# dynamo_avaluation_task

# Dynamo / log-report

This task repairs a broken Terminal-Bench 2 / Harbor task that parses an Apache-style access log and produces a JSON summary report.

## What the task tests

The task checks whether an agent can:
- Read a log file from the working directory.
- Compute summary statistics from access-log lines.
- Write a structured JSON report to the required absolute output path.

## Expected output

The task produces a single file at:

`/app/report.json`

The JSON report contains:
- `total_requests`
- `unique_clients`
- `top_path`
- `top_path_count`

## Verification logic

The verifier checks the actual JSON values produced by the task, not just whether the file exists.
The expected report is based on the provided `access.log` sample:
- 6 total requests.
- 3 unique client IPs.
- `/index.html` as the most requested path.
- 3 requests for that path.

## Fixed issues

This repository version corrects the following problems:
- The task artifact path now matches the instruction and verifier.
- The Docker image no longer uses an unpinned base image.
- The agent image no longer leaks the reference solution.
- The verifier checks the real report values.
- The verifier writes reward and CTRF output to the required `/logs/verifier/` paths.
- The instruction now states clear, numbered success criteria aligned with the verifier.

## Local validation

Run the task locally with Harbor:

```bash
harbor run -p log-report -a oracle
harbor run -p log-report --agent nop
```

The oracle run should pass with reward `1`, and the no-op agent should fail with reward `0`.
