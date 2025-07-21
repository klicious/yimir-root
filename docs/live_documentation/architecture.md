# Yimir: System Architecture

## High-Level Diagram

```mermaid
flowchart TD
    A[Raw Data] --> B(Data Ingestion)
    B --> C[AI-Powered Integration]
    C --> D[Knowledge Base (Context/)]
    D --> E[Live Documentation Generation]
    E --> F[README.md & Live Docs]
    D --> G[Context Validation]
    G --> H{Data Integrity Check}
    H -- Invalid --> B
    H -- Valid --> I[AI Agents & Users]
```

## Component Breakdown

*   **Data Ingestion**: Processes raw data from various sources, preparing it for integration into the knowledge base.
*   **AI-Powered Integration**: Leverages the Gemini CLI and specialized prompts (`ai_docs/prompts/system/integrate_new_data_prompt.md`) to intelligently process and integrate new data into the structured knowledge base.
*   **Knowledge Base (`context/`)**: The core data repository, organized into domains (e.g., `hr/`, `work_mgmt/`). It includes:
    *   **Ontology**: Defines data schemas, entities (e.g., `User.yaml`), and relationships (`relations.yaml`).
    *   **Knowledge Data**: Actual knowledge content, often organized into time-based slices (e.g., `2025-07.yaml`).
*   **Live Documentation Generation**: Utilizes scripts (`scripts/generate_readme.py`) and AI prompts (`ai_docs/prompts/system/update_readme_prompt.md`) to automatically generate and update project documentation, including `README.md` and other live documents.
*   **Context Validation**: Employs scripts (`scripts/validate_context.py`) to ensure the integrity and schema compliance of the knowledge base data.

## Data Flow

1.  **New Data**: Raw data is introduced into the system (e.g., into `data/private/`).
2.  **Integration**: The AI-powered integration process, guided by specific prompts, transforms and integrates this new data into the relevant sections of the `context/` knowledge base.
3.  **Documentation Update**: Changes in the project state or knowledge base trigger the live documentation generation process, updating `README.md` and other live documents.
4.  **Validation**: The context validation component continuously checks the integrity and consistency of the knowledge base.
5.  **Consumption**: Both AI agents and human users access the validated knowledge base and live documentation for information and insights.

## Deployment Model

Yimir is primarily a Python-based system, designed for flexible deployment:

*   **Local Development**: Can be set up and run locally for development and testing.
*   **Containerized (Docker)**: Components can be containerized for consistent deployment across various environments.
*   **Integrated with CI/CD**: Workflows can be automated within CI/CD pipelines for continuous updates and validation of the knowledge base and documentation.

<!-- architecture.md last updated from commit: c5ab8e0cb41409725ca2a11a208e3e4922346158 -->