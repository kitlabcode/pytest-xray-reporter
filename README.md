# pytest-xray-reporter

A pytest plugin that generates Xray JSON reports for test results.

## Installation

```bash
pip install pytest-xray-reporter
```

## Usage

The plugin can be used with pytest to generate Xray JSON reports. It supports various command line options to configure the report generation.

### Basic Usage

```bash
pytest --xray-output=xray-report.json
```

### Command Line Options

- `--xray-output`: Output file for Xray JSON report (default: "xray-report.json")
- `--xray-project`: Xray project key
- `--xray-test-plan`: Xray test plan key
- `--xray-test-execution`: Xray test execution key
- `--xray-test-key`: Xray test key to use for all tests (if not provided, uses test function name and logs a warning)

### Example

```bash
# Using a specific test key
pytest --xray-output=xray-report.json \
       --xray-project=PROJ \
       --xray-test-plan=PROJ-123 \
       --xray-test-execution=PROJ-456 \
       --xray-test-key=PROJ-789

# Using test function names as test keys (will show a warning)
pytest --xray-output=xray-report.json \
       --xray-project=PROJ \
       --xray-test-plan=PROJ-123 \
       --xray-test-execution=PROJ-456
```

## Report Format

The plugin generates a JSON report in the following format:

```json
{
  "tests": [
    {
      "testKey": "PROJ-789",  // Or test function name if --xray-test-key is not provided
      "start": "2024-03-21T10:00:00+00:00",
      "finish": "2024-03-21T10:00:01+00:00",
      "status": "PASSED",
      "comment": "",
      "evidence": [
        {
          "data": "base64_encoded_data",
          "filename": "stdout.txt",
          "contentType": "text/plain"
        }
      ],
      "customFields": [
        {
          "id": "test_path",
          "name": "Test Path",
          "value": "test_file.py::test_function"
        }
      ]
    }
  ],
  "info": {
    "summary": {
      "total": 1,
      "passed": 1,
      "failed": 0,
      "errors": 0,
      "skipped": 0,
      "duration": 1.0
    },
    "testEnvironments": [
      "Linux",
      "5.4.0",
      "Python 3.9.0"
    ],
    "project": "PROJ",
    "testPlanKey": "PROJ-123",
    "testExecutionKey": "PROJ-456"
  }
}
```

## Features

- Generates Xray-compatible JSON reports
- Captures test output (stdout, stderr)
- Includes test duration
- Supports test execution keys
- Supports test plan keys
- Supports project keys
- Supports custom test keys (optional, falls back to test function name with warning)
- Captures test evidence (output, logs, stack traces)
- Includes test environment information
- Supports custom fields from pytest markers

## Test Status Mapping

The plugin maps pytest outcomes to Xray statuses:

- `passed` → `PASSED`
- `failed` → `FAILED`
- `error` → `ERROR`
- `skipped` → `SKIPPED`
- Other outcomes → `UNKNOWN`

## Custom Fields

The plugin automatically includes the following custom fields:

- `test_path`: The full path to the test function
- Any pytest markers with values (except internal pytest markers)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.