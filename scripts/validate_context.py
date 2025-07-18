import os
import yaml
from jsonschema import validate

# This is a placeholder for a more robust validation script.
# In a real-world scenario, you would have a master JSON schema to validate against.

def validate_yaml_file(file_path):
    """Validates a single YAML file."""
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        print(f"Successfully parsed {file_path}")
    except yaml.YAMLError as e:
        print(f"Error parsing {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred with {file_path}: {e}")

def main():
    """Main function to validate all context files."""
    for root, dirs, files in os.walk('context'):
        for file in files:
            if file.endswith('.yaml'):
                validate_yaml_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
