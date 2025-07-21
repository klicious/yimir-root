# Yimir: API & External Interfaces

## CLI Commands

The primary interfaces to the Yimir system are through command-line interface (CLI) commands, primarily utilizing the Gemini CLI for AI-driven operations and custom Python scripts for data management.

*   **Update Live Documentation:**

    ```bash
    python scripts/generate_readme.py
    ```
    This command triggers the automated process to update `README.md` and other live documentation files based on the current project state.

*   **Integrate New Data:**

    ```bash
    gemini run --prompt "Integrate new_data.yaml into the 'hr' knowledge base" \
               --context "ai_docs/prompts/system/integrate_new_data_prompt.md"
    ```
    This command leverages the Gemini CLI to process and integrate new data files into the specified knowledge base domain.

*   **Validate Context:**

    ```bash
    python scripts/validate_context.py
    ```
    This command executes a script to validate the structure and content of the knowledge base files within the `context/` directory.

## Data Formats

*   **Input Data**: Primarily YAML files for structured data, but can be extended to support other formats as needed for data ingestion.
*   **Knowledge Base Data**: Stored in YAML format within the `context/` directory, adhering to predefined ontologies and schemas.
*   **Output Documentation**: Generated in Markdown format (`.md` files) for human readability and version control.

## Integration Points

Yimir integrates with the following key components:

*   **Gemini CLI**: The primary tool for orchestrating AI-powered workflows, including prompt execution and context loading.
*   **Git**: For version control of the entire knowledge base and live documentation, enabling tracking of changes and collaboration.
*   **File System**: Reads input data from `data/` and manages the `context/` and `ai_docs/` directories.
*   **DVC (Data Version Control)**: (Placeholder) For versioning large data files and models, ensuring reproducibility.

<!-- interfaces.md last updated from commit: c5ab8e0cb41409725ca2a11a208e3e4922346158 -->