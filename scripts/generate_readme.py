#!/usr/bin/env python3
"""
README.md Generator Script
Implements the live README generation logic as specified in update_readme_prompt.md
"""

import os
import subprocess
import re
from pathlib import Path

def get_current_commit_hash():
    """Get the current HEAD commit hash"""
    try:
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def extract_commit_from_readme(readme_path):
    """Extract the last commit hash from README.md if it exists"""
    if not os.path.exists(readme_path):
        return None
    
    try:
        with open(readme_path, 'r') as f:
            content = f.read()
        
        # Look for commit tracking comment at the end
        match = re.search(r'<!-- README\.md last updated from commit: ([a-f0-9]+) -->', content)
        if match:
            return match.group(1)
    except Exception:
        pass
    
    return None

def determine_update_strategy(readme_path):
    """Determine whether to do full generation or incremental update"""
    current_commit = get_current_commit_hash()
    if not current_commit:
        return "full", None, current_commit
    
    if not os.path.exists(readme_path):
        return "full", None, current_commit
    
    last_commit = extract_commit_from_readme(readme_path)
    if not last_commit:
        return "full", None, current_commit
    
    if last_commit == current_commit:
        return "none", last_commit, current_commit
    
    return "incremental", last_commit, current_commit

def generate_project_title_and_mission():
    """Generate the project title and mission section"""
    return """# Yimir: AI-Powered Knowledge Base & Live Documentation System

Yimir is an intelligent knowledge base template that combines structured data management with AI-powered automation. Originally designed as a universal HR framework, the project has evolved into a sophisticated system for automating the creation of personalized interview kits and maintaining live documentation that automatically reflects the current state of your project."""

def generate_key_features():
    """Generate the key features table"""
    return """## Key Features & Capabilities

| Feature | Description |
|---------|-------------|
| **Live Documentation** | Automatically generates and updates README.md based on project state and commit history |
| **Automated Data Integration** | Intelligently processes and integrates new data sources into structured knowledge bases |
| **Multi-Domain Context Management** | Supports multiple knowledge domains (HR, Finance, etc.) with graduated scaling patterns |
| **AI-Native Workflow** | Built-in prompts and templates for AI-driven content generation and maintenance |
| **Secure Data Lifecycle** | Implements timestamped archiving and clear separation between public/private data |"""

def generate_directory_layout():
    """Generate the directory layout section"""
    return """## Directory Layout

```
yimir-root/
├── README.md                    # Live document (auto-updated)
├── ai_docs/                     # AI prompts and templates
│   └── prompts/
│       └── system/              # Core system prompts
│           ├── update_readme_prompt.md
│           └── integrate_new_data_prompt.md
├── context/                     # Knowledge base domains
│   ├── org.yaml                 # Organization context
│   └── hr/                      # HR domain example
│       ├── ontology/            # Data schemas and relationships
│       └── knowledge/           # Actual knowledge data
│           └── slices/          # Time-based data partitions
├── scripts/
│   ├── validate_context.py     # Context validation
│   └── generate_readme.py      # README generation script
├── .gemini/
│   └── GEMINI.md               # AI system configuration
├── dvc.yaml                    # Data versioning (placeholder)
└── pyproject.toml              # Project configuration
```"""

def generate_quick_start():
    """Generate the quick-start section"""
    return """## Quick-Start & Example Workflow

### Setup
```bash
# Clone and setup the project
git clone <repository-url>
cd yimir-root
pip install -e .  # Install in development mode
```

### Core Workflows

**1. Update Live Documentation:**
```bash
# Automatically update README.md based on current project state
python scripts/generate_readme.py
```

**2. Integrate New Data:**
```bash
# Add new data file to private data directory
cp ~/Downloads/new_data.yaml data/private/
# Use Gemini CLI to integrate (when configured)
gemini run --prompt "Integrate new_data.yaml into the 'hr' knowledge base" \\
           --context "ai_docs/prompts/system/integrate_new_data_prompt.md"
```

**3. Validate Context:**
```bash
# Validate all context files for schema compliance
python scripts/validate_context.py
```"""

def generate_workflows_and_guardrails():
    """Generate the workflows and guard-rails section"""
    return """## Workflows & Guard-rails

### Core Development Principles

- **AI-Native Design**: Built around the Gemini CLI with ReAct loop patterns (Reason → Act → Observe → Repeat)
- **Executive-Grade Output**: Concise, professional documentation suitable for technical leadership
- **Context-Driven Intelligence**: Loads all context files to maintain working memory and derive insights
- **Live Documentation**: README.md serves as a true "live document" that tracks with project evolution
- **Graduated Scaling**: Supports multiple patterns from simple YAML files to database + vector store architectures

### Data Management

- **Secure Lifecycle**: Clear separation between public/private data with timestamped archiving
- **Schema Validation**: Built-in validation scripts ensure data integrity across all context files
- **Version Control**: Git-based tracking with commit-level documentation updates"""

def generate_current_focus():
    """Generate the current focus section"""
    return """## Current Focus & Next Steps

### Current State
The project is in active development with two core capabilities:

1. **Live Documentation System**: Fully implemented README generation that tracks commit history and intelligently updates documentation
2. **Knowledge Base Integration**: Framework for processing and integrating structured data into domain-specific knowledge bases

### Immediate Priorities
- **Template Refinement**: Enhancing the knowledge base template structure for better scalability
- **AI Integration**: Improving Gemini CLI integration for seamless AI-powered workflows  
- **Documentation Automation**: Expanding live documentation beyond README to include other project artifacts

### Architecture Evolution
The project demonstrates a clear evolution from a generic HR framework toward a sophisticated AI-powered knowledge management system with automated documentation capabilities."""

def generate_full_readme(current_commit):
    """Generate a complete README.md"""
    sections = [
        generate_project_title_and_mission(),
        "",
        generate_key_features(),
        "",
        generate_directory_layout(),
        "",
        generate_quick_start(),
        "",
        generate_workflows_and_guardrails(),
        "",
        generate_current_focus(),
        "",
        f"<!-- README.md last updated from commit: {current_commit} -->"
    ]
    
    return "\n".join(sections)

def main():
    """Main function to generate or update README.md"""
    readme_path = "README.md"
    
    # Determine update strategy
    strategy, last_commit, current_commit = determine_update_strategy(readme_path)
    
    print(f"Update strategy: {strategy}")
    print(f"Current commit: {current_commit}")
    if last_commit:
        print(f"Last commit: {last_commit}")
    
    if strategy == "none":
        print("README.md is already up to date.")
        return
    
    if strategy == "full":
        print("Generating complete README.md...")
        new_content = generate_full_readme(current_commit)
        
        with open(readme_path, 'w') as f:
            f.write(new_content)
        
        print(f"README.md generated successfully with commit tracking: {current_commit}")
    
    elif strategy == "incremental":
        print("Incremental updates not yet implemented. Falling back to full generation...")
        new_content = generate_full_readme(current_commit)
        
        with open(readme_path, 'w') as f:
            f.write(new_content)
        
        print(f"README.md updated successfully with commit tracking: {current_commit}")

if __name__ == "__main__":
    main()