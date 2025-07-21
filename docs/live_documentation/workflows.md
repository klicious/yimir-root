# Yimir: Operational Workflows

## Setup Guide

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd yimir-root
    ```
2.  **Install dependencies**:
    ```bash
    pip install -e .  # Install in development mode
    ```

## Primary Workflows

### Update Live Documentation

Automatically update `README.md` and other live documentation files based on the current project state and commit history:

```bash
python scripts/generate_readme.py
```

### Integrate New Data

To process and integrate new data into the knowledge base:

1.  Add new data file to `data/private/` directory (e.g., `~/Downloads/new_data.yaml`).
2.  Use the Gemini CLI to integrate the data:
    ```bash
    gemini run --prompt "Integrate new_data.yaml into the 'hr' knowledge base" \
               --context "ai_docs/prompts/system/integrate_new_data_prompt.md"
    ```

## Development Workflows

### Validate Context

To ensure the integrity and schema compliance of all context files:

```bash
python scripts/validate_context.py
```

This script checks the structure and content of the YAML files within the `context/` directory against predefined schemas.

<!-- workflows.md last updated from commit: c5ab8e0cb41409725ca2a11a208e3e4922346158 -->
