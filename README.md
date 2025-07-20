# Yimir: AI-Powered Knowledge Base & Live Documentation System

Yimir is an intelligent knowledge base template that combines structured data management with AI-powered automation. Originally designed as a universal HR framework, the project has evolved into a sophisticated system for automating the creation of personalized interview kits and maintaining live documentation that automatically reflects the current state of your project.

## Key Features & Capabilities

| Feature | Description |
|---------|-------------|
| **Live Documentation** | Automatically generates and updates README.md based on project state and commit history |
| **Automated Data Integration** | Intelligently processes and integrates new data sources into structured knowledge bases |
| **Multi-Domain Context Management** | Supports multiple knowledge domains (HR, Finance, etc.) with graduated scaling patterns |
| **AI-Native Workflow** | Built-in prompts and templates for AI-driven content generation and maintenance |
| **Secure Data Lifecycle** | Implements timestamped archiving and clear separation between public/private data |

## Directory Layout

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
│       │   ├── entities/
│       │   │   └── User.yaml
│       │   └── relations.yaml
│       └── knowledge/           # Actual knowledge data
│           ├── README.md
│           └── slices/          # Time-based data partitions
│               └── 2025-07.yaml
├── scripts/
│   ├── validate_context.py     # Context validation
│   └── generate_readme.py      # README generation script
├── .gemini/
│   └── GEMINI.md               # AI system configuration
├── dvc.yaml                    # Data versioning (placeholder)
└── pyproject.toml              # Project configuration
```

## Quick-Start & Example Workflow

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
gemini run --prompt "Integrate new_data.yaml into the 'hr' knowledge base" \
           --context "ai_docs/prompts/system/integrate_new_data_prompt.md"
```

**3. Validate Context:**
```bash
# Validate all context files for schema compliance
python scripts/validate_context.py
```


## Workflows & Guard-rails

### Core Development Principles

- **AI-Native Design**: Built around the Gemini CLI with ReAct loop patterns (Reason → Act → Observe → Repeat)
- **Executive-Grade Output**: Concise, professional documentation suitable for technical leadership
- **Context-Driven Intelligence**: Loads all context files to maintain working memory and derive insights
- **Live Documentation**: README.md serves as a true "live document" that tracks with project evolution
- **Graduated Scaling**: Supports multiple patterns from simple YAML files to database + vector store architectures

### Data Management

- **Secure Lifecycle**: Clear separation between public/private data with timestamped archiving
- **Schema Validation**: Built-in validation scripts ensure data integrity across all context files
- **Version Control**: Git-based tracking with commit-level documentation updates

## Current Focus & Next Steps

### Current State
The project is in active development with two core capabilities:

1. **Live Documentation System**: Fully implemented README generation that tracks commit history and intelligently updates documentation
2. **Knowledge Base Integration**: Framework for processing and integrating structured data into domain-specific knowledge bases

### Immediate Priorities
- **Template Refinement**: Enhancing the knowledge base template structure for better scalability
- **AI Integration**: Improving Gemini CLI integration for seamless AI-powered workflows  
- **Documentation Automation**: Expanding live documentation beyond README to include other project artifacts

### Architecture Evolution
The project demonstrates a clear evolution from a generic HR framework toward a sophisticated AI-powered knowledge management system with automated documentation capabilities.

<!-- README.md last updated from commit: a2451b80c1ba729eafe051da1468aaff647de079 -->