# Python Coding Style Guide for This Project

This project follows PEP8 as the main Python style guide. Key points:

- Use 4 spaces per indentation level (no tabs).
- Maximum line length: 79 characters.
- Use snake_case for variable and function names.
- Use PascalCase for class names.
- Use UPPER_CASE for constants.
- Imports should be grouped: standard library, third-party, local.
- Add docstrings for all public modules, functions, classes, and methods.
- Use type hints for function signatures.
- Leave two blank lines before top-level function and class definitions.
- Use single blank lines to separate methods within a class.
- Avoid unused imports and variables.
- Use f-strings for string formatting.
- Handle exceptions explicitly and log errors where appropriate.
- Use environment variables for secrets (never hardcode tokens).

Example function:

```python
import os
from typing import List


def get_nasabah_by_id(nasabah_id: int) -> dict:
    """Get nasabah data by ID from Supabase."""
    # ...implementation...
    return {}
```

Refer to https://peps.python.org/pep-0008/ for full details.
