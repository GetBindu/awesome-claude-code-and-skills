# Awesome Claude Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated collection of Claude AI skills, agents, and tools to supercharge your AI-powered development workflow. This repository features production-ready skills for coding, security, marketing, and specialized domains.

## Why Awesome Claude Skills?

Claude skills are modular capabilities that extend Claude's functionality for specific tasks. Think of them as plugins or specialized knowledge modules that help Claude become an expert in particular domains. Whether you're building software, analyzing security vulnerabilities, or creating marketing content, there's a skill to enhance your workflow.

This list focuses on verified, actively maintained projects that provide real value to developers and teams working with Claude AI.

---

## Contents

- [Getting Started](#getting-started)
- [Official Resources](#official-resources)
- [Comprehensive Skill Collections](#comprehensive-skill-collections)
- [Development & Engineering](#development--engineering)
- [Multi-Agent Systems](#multi-agent-systems)
- [Security & Compliance](#security--compliance)
- [Marketing & Content](#marketing--content)
- [Productivity Tools](#productivity-tools)
- [Learning & Documentation](#learning--documentation)

---

## Getting Started

### What are Claude Skills?

Claude skills are structured instructions and configurations that guide Claude to perform specialized tasks. They typically include:

- **Context and expertise**: Domain-specific knowledge and best practices
- **Workflows**: Step-by-step processes for complex tasks
- **Templates**: Reusable patterns for common operations
- **Tool integrations**: Connections to external services and APIs

### Installation

Most skills can be installed by placing them in your Claude configuration directory:

```bash
# Clone a skill repository
git clone https://github.com/username/skill-name ~/.claude/skills/skill-name

# Or use a package manager
npx antigravity-awesome-skills
```

---

## Official Resources

Start here for official tools and documentation from Anthropic.

- [anthropics/skills](https://github.com/anthropics/skills) ![Stars](https://img.shields.io/github/stars/anthropics/skills?style=flat-square)
  - Official repository for Claude Agent Skills
  - Includes document processing (docx, pdf, pptx, xlsx)
  - Art and design capabilities
  - MCP (Model Context Protocol) builder

---

## Comprehensive Skill Collections

These repositories offer extensive collections of skills across multiple domains. Great starting points if you want a broad toolkit.

- [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) ![Stars](https://img.shields.io/github/stars/rohitg00/awesome-claude-code-toolkit?style=flat-square)
  - Most comprehensive toolkit available
  - 135 agents, 35 skills, 42 commands
  - 150+ plugins, 19 hooks, 7 templates
  - Covers development, DevOps, and productivity

- [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) ![Stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=flat-square)
  - 192+ professional skills and agent plugins
  - Engineering, marketing, product management
  - Compliance and C-level advisory capabilities
  - Compatible with 11 different tools

- [wshobson/agents](https://github.com/wshobson/agents) ![Stars](https://img.shields.io/github/stars/wshobson/agents?style=flat-square)
  - 112 specialized agents across 72 focused plugins
  - 16 orchestrators for complex workflows
  - 146 skills and 79 tools
  - Well-organized by use case

- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) ![Stars](https://img.shields.io/github/stars/VoltAgent/awesome-agent-skills?style=flat-square)
  - 1000+ agent skills from official dev teams
  - Contributions from Sentry, Trail of Bits, Expo, DuckDB, Figma, Google
  - Community-driven with regular updates

- [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) ![Stars](https://img.shields.io/github/stars/sickn33/antigravity-awesome-skills?style=flat-square)
  - 1,326+ installable agentic skills
  - CLI installer for easy setup
  - Bundled workflows for common tasks

---

## Development & Engineering

Skills focused on software development, code quality, and engineering workflows.

### Core Development Skills

- [obra/superpowers](https://github.com/obra/superpowers) ![Stars](https://img.shields.io/github/stars/obra/superpowers?style=flat-square)
  - 20+ battle-tested development skills
  - TDD (Test-Driven Development) workflows
  - Debugging patterns and collaboration tools
  - Git workflows and best practices

- [mattpocock/skills](https://github.com/mattpocock/skills) ![Stars](https://img.shields.io/github/stars/mattpocock/skills?style=flat-square)
  - 17 professional dev workflow skills
  - PRD (Product Requirements Document) writing
  - Codebase architecture guidance
  - Git guardrails and issue triage

- [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) ![Stars](https://img.shields.io/github/stars/affaan-m/everything-claude-code?style=flat-square)
  - Agent harness performance optimization
  - Research-first development approach
  - Memory management and security patterns

### Specialized Agents

- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) ![Stars](https://img.shields.io/github/stars/VoltAgent/awesome-claude-code-subagents?style=flat-square)
  - 100+ specialized subagents
  - Full-stack development coverage
  - Research and DevOps automation

- [vijaythecoder/awesome-claude-agents](https://github.com/vijaythecoder/awesome-claude-agents) ![Stars](https://img.shields.io/github/stars/vijaythecoder/awesome-claude-agents?style=flat-square)
  - 24 specialized development agents
  - Tech Lead Orchestrator for team coordination
  - Code Archaeologist for legacy code analysis
  - Performance Optimizer for bottleneck detection

- [lst97/claude-code-sub-agents](https://github.com/lst97/claude-code-sub-agents) ![Stars](https://img.shields.io/github/stars/lst97/claude-code-sub-agents?style=flat-square)
  - Domain-expert subagents
  - Multi-agent orchestration capabilities
  - Automatic task delegation

### Framework-Specific

- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) ![Stars](https://img.shields.io/github/stars/nextlevelbuilder/ui-ux-pro-max-skill?style=flat-square)
  - Professional UI/UX design skill
  - Modern design patterns and accessibility
  - Component library integration

---

## Multi-Agent Systems

Orchestrate multiple Claude agents to work together on complex tasks.

### Orchestration Platforms

- [steveyegge/gastown](https://github.com/steveyegge/gastown) ![Stars](https://img.shields.io/github/stars/steveyegge/gastown?style=flat-square)
  - Multi-agent workspace manager
  - Persistent agent identity across sessions
  - Convoy system for coordinated tasks
  - Git-backed state tracking

- [dlorenc/multiclaude](https://github.com/dlorenc/multiclaude) ![Stars](https://img.shields.io/github/stars/dlorenc/multiclaude?style=flat-square)
  - Multi-agent orchestrator with flexible modes
  - Singleplayer and multiplayer coordination
  - Supervisor-subagent pattern implementation

- [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) ![Stars](https://img.shields.io/github/stars/ComposioHQ/agent-orchestrator?style=flat-square)
  - Agent-agnostic parallel orchestrator
  - Git worktrees for isolated environments
  - CI auto-fix and review routing

### Parallel Processing

- [Dicklesworthstone/claude_code_agent_farm](https://github.com/Dicklesworthstone/claude_code_agent_farm) ![Stars](https://img.shields.io/github/stars/Dicklesworthstone/claude_code_agent_farm?style=flat-square)
  - Run 20-50 Claude agents in parallel
  - Lock-based coordination system
  - tmux monitoring dashboard

- [disler/infinite-agentic-loop](https://github.com/disler/infinite-agentic-loop) ![Stars](https://img.shields.io/github/stars/disler/infinite-agentic-loop?style=flat-square)
  - Two-prompt system for spawning parallel agents
  - Evolving iterations for complex problem-solving
  - Self-improving agent patterns

- [ruvnet/ruflo](https://github.com/ruvnet/ruflo) ![Stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=flat-square)
  - Multi-agent swarm orchestration
  - Self-learning capabilities
  - RAG (Retrieval-Augmented Generation) integration
  - Hive mind topology for distributed intelligence

---

## Security & Compliance

Professional-grade security skills for vulnerability detection, code auditing, and compliance.

### Security Analysis

- [BehiSecc/vibesec](https://github.com/BehiSecc/vibesec) ![Stars](https://img.shields.io/github/stars/BehiSecc/vibesec?style=flat-square)
  - Prevents IDOR, XSS, SQL injection, SSRF
  - Weak authentication detection
  - Bug hunter's perspective on security

- [wrsmith108/varlock-claude-skill](https://github.com/wrsmith108/varlock-claude-skill) ![Stars](https://img.shields.io/github/stars/wrsmith108/varlock-claude-skill?style=flat-square)
  - Secure environment variable management
  - Ensures secrets never appear in sessions, terminals, logs, or git
  - Production-ready secret handling

### Compliance & Auditing

- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) ![Stars](https://img.shields.io/github/stars/BehiSecc/awesome-claude-skills?style=flat-square)
  - Security-focused skill collection
  - Document handling with security in mind
  - Development and data analysis tools

---

## Marketing & Content

Skills for marketing professionals, content creators, and growth teams.

- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) ![Stars](https://img.shields.io/github/stars/coreyhaines31/marketingskills?style=flat-square)
  - 23 professional marketing skills
  - CRO (Conversion Rate Optimization)
  - Copywriting and SEO strategies
  - Paid advertising and growth tactics

- [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) ![Stars](https://img.shields.io/github/stars/zarazhangrui/codebase-to-course?style=flat-square)
  - Transform codebases into interactive HTML courses
  - Beautiful, educational content generation
  - Perfect for developer education and onboarding

---

## Productivity Tools

Utilities and tools to enhance your Claude workflow.

### Monitoring & Observability

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) ![Stars](https://img.shields.io/github/stars/disler/claude-code-hooks-multi-agent-observability?style=flat-square)
  - Real-time agent monitoring
  - Hook event tracking with SQLite dashboard
  - Visual tool event indicators

### Configuration & Templates

- [abhishekray07/claude-md-templates](https://github.com/abhishekray07/claude-md-templates) ![Stars](https://img.shields.io/github/stars/abhishekray07/claude-md-templates?style=flat-square)
  - CLAUDE.md best practices and templates
  - Global, project, and local configurations
  - Framework-specific templates (Next.js, Python/FastAPI)

- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) ![Stars](https://img.shields.io/github/stars/shanraisshan/claude-code-best-practice?style=flat-square)
  - Comprehensive best practices guide
  - Prompting, planning, and agent strategies
  - Commands, skills, hooks, and workflows

### Cost Optimization

- [Sagargupta16/claude-cost-optimizer](https://github.com/Sagargupta16/claude-cost-optimizer) ![Stars](https://img.shields.io/github/stars/Sagargupta16/claude-cost-optimizer?style=flat-square)
  - Save 30-60% on Claude API costs
  - 6 guides and 15 optimization strategies
  - Token estimator and usage analyzer
  - 12 CLAUDE.md templates for efficiency

- [nadimtuhin/claude-token-optimizer](https://github.com/nadimtuhin/claude-token-optimizer) ![Stars](https://img.shields.io/github/stars/nadimtuhin/claude-token-optimizer?style=flat-square)
  - Up to 90% token savings
  - Progressive disclosure patterns
  - Framework-specific optimization
  - 4-file architecture for minimal context

---

## Learning & Documentation

Resources for mastering Claude skills and understanding best practices.

### Comprehensive Guides

- [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) ![Stars](https://img.shields.io/github/stars/FlorianBruniaux/claude-code-ultimate-guide?style=flat-square)
  - 22,000+ lines of documentation
  - Beginner to power user progression
  - 225 templates and 41 diagrams
  - 271 quiz questions for learning validation

- [rosmur/claudecode-best-practices](https://github.com/rosmur/claudecode-best-practices) ![Stars](https://img.shields.io/github/stars/rosmur/claudecode-best-practices?style=flat-square)
  - Evidence-based practices with 58 citations
  - Hooks, skills, and automation scripts
  - Task queue management with claude-loop

- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) ![Stars](https://img.shields.io/github/stars/shareAI-lab/learn-claude-code?style=flat-square)
  - "Bash is all you need" philosophy
  - Build a Claude-like agent harness from scratch
  - 12 progressive learning sessions

### Curated Lists

- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) ![Stars](https://img.shields.io/github/stars/hesreallyhim/awesome-claude-code?style=flat-square)
  - Gold-standard curated list
  - Skills, hooks, slash-commands
  - Agent orchestrators and plugins

- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) ![Stars](https://img.shields.io/github/stars/travisvn/awesome-claude-skills?style=flat-square)
  - Excellent FAQ and getting-started section
  - Tools for customizing AI workflows
  - Community-driven resources

- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) ![Stars](https://img.shields.io/github/stars/ComposioHQ/awesome-claude-skills?style=flat-square)
  - Well-organized by category
  - Clear descriptions for each skill
  - Regular updates and maintenance

---

## Skill Development

Tools and frameworks for creating your own Claude skills.

- [alirezarezvani/claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) ![Stars](https://img.shields.io/github/stars/alirezarezvani/claude-code-skill-factory?style=flat-square)
  - Complete toolkit for building production-ready skills
  - Deployment automation
  - Best practices and templates
  - Scale from prototype to production

---

## Contributing

We welcome contributions! To add a skill or tool to this list:

1. Ensure the project is actively maintained
2. Verify it provides clear documentation
3. Check that it offers real value to Claude users
4. Submit a pull request with a clear description

**Quality over quantity** - we prioritize well-documented, production-ready skills over experimental projects.

---

## Security Notice

Skills can execute code and access your system. Always:
- Review source code before installation
- Use skills from trusted sources
- Test in isolated environments first
- Keep skills updated

---

## License

CC0 - Public Domain

This curated list is maintained by the community for the community.