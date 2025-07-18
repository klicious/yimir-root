# How to Add Knowledge to this Domain

This directory contains the factual knowledge for the **{domain_name}** domain. To add new information, please follow these patterns:

## Adding to Slices

For time-sensitive or frequently updated data (e.g., weekly reports, new tasks), add to the current slice in the `slices/` directory.

1.  **Identify the current slice**: This is usually the file with the most recent date (e.g., `2025-07.yaml`).
2.  **Append new data**: Add the new information to the end of the file, following the existing YAML structure.
3.  **Create a new slice if needed**: If the current slice is becoming too large (e.g., over 500 lines), create a new file with the next logical name (e.g., `2025-08.yaml`) and start adding new data there.

## Adding to Projects

For data that is specific to a particular project, create a new file in the `projects/` directory.

-   The filename should be the project's identifier (e.g., `alpha-trader.yaml`).
-   The content should conform to the schema defined in the domain's `ontology/`.
