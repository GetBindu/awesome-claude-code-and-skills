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
- [Domain-Specific Skills](#domain-specific-skills)
- [Productivity Tools](#productivity-tools)
- [Learning & Documentation](#learning--documentation)
- [Skill Development](#skill-development)

---

## Getting Started

### What are Claude Skills?

Claude skills are structured instructions and configurations that guide Claude to perform specialized tasks. They typically include:

- **Context and expertise**: Domain-specific knowledge and best practices
- **Workflows**: Step-by-step processes for complex tasks
- **Templates**: Reusable patterns for common operations
- **Tool integrations**: Connections to external services and APIs

---

## Official Resources

Start here for official tools and documentation from Anthropic.

- [anthropics/claude-code](https://github.com/anthropics/claude-code) ![Stars](https://img.shields.io/github/stars/anthropics/claude-code?style=flat-square)
  - Official Claude Code agentic coding tool
  - Lives in your terminal and understands your codebase
  - AI-powered development assistant
  - Built by Anthropic

- [anthropics/skills](https://github.com/anthropics/skills) ![Stars](https://img.shields.io/github/stars/anthropics/skills?style=flat-square)
  - Official repository for Claude Agent Skills
  - Includes document processing (docx, pdf, pptx, xlsx)
  - Art and design capabilities
  - MCP (Model Context Protocol) builder

- [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) ![Stars](https://img.shields.io/github/stars/anthropics/claude-code-action?style=flat-square)
  - GitHub Action for Claude Code integration
  - Automated code review and analysis
  - CI/CD pipeline integration
  - Official Anthropic GitHub Actions support

- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-official?style=flat-square)
  - Official Anthropic-managed plugin directory
  - Curated collection of high-quality Claude Code plugins
  - Verified and maintained by Anthropic
  - Includes internal and external plugins

- [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) ![Stars](https://img.shields.io/github/stars/anthropics/claude-code-security-review?style=flat-square)
  - AI-powered security review GitHub Action
  - Analyze code changes for security vulnerabilities
  - Context-aware security analysis for pull requests
  - Deep semantic security analysis using Claude
  - Official Anthropic security tooling

- [anthropics/claude-code-base-action](https://github.com/anthropics/claude-code-base-action) ![Stars](https://img.shields.io/github/stars/anthropics/claude-code-base-action?style=flat-square)
  - Base GitHub Action for custom Claude Code workflows
  - Build any custom workflow on top of Claude Code
  - Settings and MCP configuration support
  - Cloud provider integration (AWS Bedrock, GCP Vertex AI)
  - Official foundation for Claude Code automation

- [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) ![Stars](https://img.shields.io/github/stars/anthropics/claude-for-legal?style=flat-square)
  - Official Anthropic suite of plugins for legal workflows
  - Targets common legal-team tasks across drafting, review, and search
  - Python-based; maintained by Anthropic

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

- [JasonColapietro/suede-creator-skills](https://github.com/JasonColapietro/suede-creator-skills) ![Stars](https://img.shields.io/github/stars/JasonColapietro/suede-creator-skills?style=flat-square)
  - 67 MIT-licensed skills for Claude Code and Codex
  - Covers code review and ship grading, design, marketing, agent workflows, and mobile release preparation
  - Installable through the Claude and Codex plugin marketplaces or the skills CLI

- [Claude Code Skills 中文精选集](https://claude-skills.bt199.com/)
  - Chinese directory for Claude Code Skills, agents, and plugins
  - 140+ curated resources for Chinese-speaking developers
  - Useful for discovering practical skills by category

- [Remote OpenClaw Claude Skills](https://www.remoteopenclaw.com/skills/claude)
  - Claude-focused skills directory with reviewed GitHub listings, plugins, and agents
  - Includes adjacent Codex, Hermes, and OpenClaw hubs for cross-agent comparison
  - Useful when you want a Claude-specific entry point without losing the broader ecosystem view

- [CreatorSkills](https://creatorskills.co)
  - Curated marketplace of 30+ downloadable AI skills for content creators
  - Covers YouTube scripting, sponsorship analysis, content repurposing, and audience growth
  - Skills use the open SKILL.md format and work with Claude, ChatGPT, and 20+ AI platforms
  - Paid marketplace; skills are domain-specific and ready to install

- [garrytan/gstack](https://github.com/garrytan/gstack) ![Stars](https://img.shields.io/github/stars/garrytan/gstack?style=flat-square)
  - Garry Tan's exact Claude Code setup
  - 6 opinionated tools for startup leadership
  - Includes CEO, Engineering Manager, Release Manager, QA agents
  - Production-tested by Y Combinator president

- [wshobson/agents](https://github.com/wshobson/agents) ![Stars](https://img.shields.io/github/stars/wshobson/agents?style=flat-square)
  - 112 specialized agents across 72 focused plugins
  - 16 orchestrators for complex workflows
  - 146 skills and 79 tools
  - Well-organized by use case

- [swarmclawai/andrej-karpathy-skills](https://github.com/swarmclawai/andrej-karpathy-skills) ![Stars](https://img.shields.io/github/stars/swarmclawai/andrej-karpathy-skills?style=flat-square)
  - Npm-installable Karpathy-inspired coding-agent guidelines
  - Adapters for Claude Code, Codex, Cursor, Gemini CLI, OpenCode, OpenClaw, Windsurf, Aider, and more
  - Installs with `npx @swarmclawai/andrej-karpathy-skills --agent claude --dest .`

- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) ![Stars](https://img.shields.io/github/stars/VoltAgent/awesome-agent-skills?style=flat-square)
  - 1000+ agent skills from official dev teams
  - Contributions from Sentry, Trail of Bits, Expo, DuckDB, Figma, Google
  - Community-driven with regular updates

- [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) ![Stars](https://img.shields.io/github/stars/sickn33/agentic-awesome-skills?style=flat-square)
  - 1,326+ installable agentic skills
  - CLI installer for easy setup
  - Bundled workflows for common tasks

- [SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) ![Stars](https://img.shields.io/github/stars/SuperClaude-Org/SuperClaude_Framework?style=flat-square)
  - Configuration framework for structured development
  - 30 slash commands covering complete development lifecycle
  - Cognitive personas and behavioral modes
  - Deep research capabilities with autonomous web research
  - MCP server integration and workflow automation

- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) ![Stars](https://img.shields.io/github/stars/hesreallyhim/awesome-claude-code?style=flat-square)
  - One of the largest community-curated Claude Code lists
  - Indexes skills, hooks, slash commands, agent orchestrators, applications, and plugins
  - Tagged for agentic coding and AI workflow optimization
  - Frequently referenced as a starting point for Claude Code newcomers

- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) ![Stars](https://img.shields.io/github/stars/ComposioHQ/awesome-claude-skills?style=flat-square)
  - Composio-curated directory of Claude Skills, plugins, and workflow integrations
  - Covers agent skills, MCP servers, Claude Code, Codex, Cursor, Gemini CLI, and Antigravity
  - Sections for SaaS automation, developer tools, and Rube integrations
  - Active community contributions with Python-driven generator scripts

- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) ![Stars](https://img.shields.io/github/stars/travisvn/awesome-claude-skills?style=flat-square)
  - Curated list focused on Claude Skills with a Claude Code emphasis
  - Includes Claude Code, Claude Desktop, and Claude AI tooling
  - Lightweight directory designed for fast scanning

- [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) ![Stars](https://img.shields.io/github/stars/muratcankoylan/Agent-Skills-for-Context-Engineering?style=flat-square)
  - Open collection of agent skills focused on context engineering principles
  - Foundational, architectural, operational, and methodology skill tracks
  - Skills cover context compression, degradation patterns, memory systems, tool design, and LLM-as-judge evaluation
  - Designed for production-grade agent systems on any agent platform

- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) ![Stars](https://img.shields.io/github/stars/VoltAgent/awesome-openclaw-skills?style=flat-square)
  - 5,400+ skills filtered and categorized from the OpenClaw Skills Registry
  - Indexed by domain with quality and recency filters
  - Companion to VoltAgent's awesome-agent-skills and awesome-claude-code-subagents lists

- [huggingface/skills](https://github.com/huggingface/skills) ![Stars](https://img.shields.io/github/stars/huggingface/skills?style=flat-square)
  - Skills for plugging the Hugging Face ecosystem into AI coding agents
  - Covers model search, dataset access, Spaces, and Inference Endpoints
  - Python-driven, maintained by Hugging Face

- [microsoft/skills](https://github.com/microsoft/skills) ![Stars](https://img.shields.io/github/stars/microsoft/skills?style=flat-square)
  - Microsoft-published skills, MCP servers, and Custom Agents
  - Ships `AGENTS.md` bundles for grounding coding agents
  - TypeScript-driven; useful starting point for enterprise teams

- [antfu/skills](https://github.com/antfu/skills) ![Stars](https://img.shields.io/github/stars/antfu/skills?style=flat-square)
  - Anthony Fu's curated collection of agent skills
  - Skills cover web tooling, build configuration, and developer ergonomics
  - TypeScript implementation

- [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) ![Stars](https://img.shields.io/github/stars/ConardLi/garden-skills?style=flat-square)
  - ConardLi's open-source skills collection
  - Web design, knowledge retrieval, and image generation skills
  - CSS-driven visual assets

- [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) ![Stars](https://img.shields.io/github/stars/heilcheng/awesome-agent-skills?style=flat-square)
  - Tutorials, guides, and agent-skills directories in one place
  - Aggregates resources across the agent-skills ecosystem
  - TypeScript-based site for browsing

- [libukai/awesome-agent-skills](https://github.com/libukai/awesome-agent-skills) ![Stars](https://img.shields.io/github/stars/libukai/awesome-agent-skills?style=flat-square)
  - Chinese-language ultimate guide to Agent Skills
  - Quick start, resource recommendations, curated skills, and tooling
  - Python-driven generator

- [langgptai/awesome-claude-prompts](https://github.com/langgptai/awesome-claude-prompts) ![Stars](https://img.shields.io/github/stars/langgptai/awesome-claude-prompts?style=flat-square)
  - Curated Claude prompts for everyday use cases
  - Helps non-developers get more from Claude
  - Maintained by LangGPT

- [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude) ![Stars](https://img.shields.io/github/stars/davepoon/buildwithclaude?style=flat-square)
  - Hub for Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections
  - Extends Claude Code and Claude Desktop
  - Python-driven discovery layer

- [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) ![Stars](https://img.shields.io/github/stars/jnMetaCode/superpowers-zh?style=flat-square)
  - Chinese expansion of obra/superpowers
  - Translates the upstream skill bundle and adds six original Chinese skills
  - Shell-based installer

- [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) ![Stars](https://img.shields.io/github/stars/mergisi/awesome-openclaw-agents?style=flat-square)
  - 162 production-ready AI agent templates with `SOUL.md` configs
  - Templates organized into 19 categories
  - HTML-driven gallery

- [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) ![Stars](https://img.shields.io/github/stars/clawdbot-ai/awesome-openclaw-skills-zh?style=flat-square)
  - Chinese-language OpenClaw skill library
  - Translated and reorganized by scenario for natural-language invocation
  - Companion to the official Clawdbot skills directory

---

- [connerkward/ckw-skills](https://github.com/connerkward/ckw-skills) ![Stars](https://img.shields.io/github/stars/connerkward/ckw-skills?style=flat-square)
  - Human-in-the-loop visual studios and deterministic design tooling by Conner K. Ward
  - lookdev / lookdev-auto (tune AI output by eye or via a vision model), deterministic-design, ckw-design
  - screenstudio-alt and macOS system-audio screen recorder, web-media-getter
  - Install: `/plugin marketplace add connerkward/ckw-skills`
- [mailtrap/mailtrap-skills](https://github.com/mailtrap/mailtrap-skills) ![Stars](https://img.shields.io/github/stars/mailtrap/mailtrap-skills?style=flat-square)
  - Agent skills for Mailtrap email sending, sandbox testing, and contact management
  - Covers email sending, sandbox testing, templates, domain setup, and contacts
  - Follows the Agent Skills open standard (Anthropic, Dec 2025)

- [abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection) ![Stars](https://img.shields.io/github/stars/abubakarsiddik31/claude-skills-collection?style=flat-square)
  - Curated collection of official and community Claude Skills
  - Spans productivity, creativity, coding, and content workflows
  - Actively maintained general-purpose skills library

- [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) ![Stars](https://img.shields.io/github/stars/karanb192/awesome-claude-skills?style=flat-square)
  - Curated "awesome" list of 50+ verified skills
  - Covers Claude Code, Claude.ai, and the API
  - Document processing, git workflows, TDD, and debugging; MIT licensed

- [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) ![Stars](https://img.shields.io/github/stars/borghei/Claude-Skills?style=flat-square)
  - 368 skills, 76 expert agents, and 859 standard-library Python tools
  - Spans engineering, PM, marketing, C-level, compliance, and research
  - Persona system (`startup-cto`, `growth-marketer`, etc.); works with Claude Code, Cursor, Codex, Gemini, and Copilot

- [levnikolaevich/claude-code-skills](https://github.com/levnikolaevich/claude-code-skills) ![Stars](https://img.shields.io/github/stars/levnikolaevich/claude-code-skills?style=flat-square)
  - Standalone engineering skills organized by numbered categories
  - Review, audit, optimization, testing, product discovery, architecture, and safe publishing
  - Works with Claude Code and Codex; MIT licensed

- [glebis/claude-skills](https://github.com/glebis/claude-skills) ![Stars](https://img.shields.io/github/stars/glebis/claude-skills?style=flat-square)
  - ~100 skills covering meeting pipelines, research, image generation, and publishing
  - Also personal analytics and Claude Code operations
  - Each skill is a self-contained SKILL.md folder; installable via plugin marketplace or `npx skills add`

## Development & Engineering

Skills focused on software development, code quality, and engineering workflows.

### Core Development Skills

- [musoyangrigor/gitx-skill](https://github.com/musoyangrigor/gitx-skill) ![Stars](https://img.shields.io/github/stars/musoyangrigor/gitx-skill?style=flat-square)
  - Turns messy AI-generated changes into clean, reviewable Git history
  - Splits mixed working-tree changes into logical Conventional Commits
  - Safe branches, checks, pull/push, PRs, issues, secret scanning, and conflict resolution
  - Works with Claude Code, OpenAI Codex, Cursor, and Agent Skills-compatible tools

- [gyujeongion/claude-code-rootcause](https://github.com/gyujeongion/claude-code-rootcause) ![Stars](https://img.shields.io/github/stars/gyujeongion/claude-code-rootcause?style=flat-square)
  - Turns "never do X" bans into positive process gates
  - Audits your instruction file for ban bloat (rethink + deusex)

- [gyujeongion/claude-code-sandbox-gate](https://github.com/gyujeongion/claude-code-sandbox-gate) ![Stars](https://img.shields.io/github/stars/gyujeongion/claude-code-sandbox-gate?style=flat-square)
  - Verification gate before a change hits main
  - Stops the agent shipping "it works now" patches unchecked

- [gyujeongion/claude-code-request-modes](https://github.com/gyujeongion/claude-code-request-modes) ![Stars](https://img.shields.io/github/stars/gyujeongion/claude-code-request-modes?style=flat-square)
  - Classifies each request and activates only the rules that apply
  - Stops one global rulebook bleeding into everything

- [gyujeongion/claude-code-cold-tester](https://github.com/gyujeongion/claude-code-cold-tester) ![Stars](https://img.shields.io/github/stars/gyujeongion/claude-code-cold-tester?style=flat-square)
  - Runs a doc through a zero-context model
  - Finds where a real newcomer would get stuck

- [gyujeongion/claude-code-mix-compare](https://github.com/gyujeongion/claude-code-mix-compare) ![Stars](https://img.shields.io/github/stars/gyujeongion/claude-code-mix-compare?style=flat-square)
  - git diff for audio mixes — time-align two versions, phase-invert the change
  - Per-stem, per-band, stereo and phase, translated into engineer notes

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

- [YoungApple/growth-retrospective-skill](https://github.com/YoungApple/growth-retrospective-skill) ![Stars](https://img.shields.io/github/stars/YoungApple/growth-retrospective-skill?style=flat-square)
  - Personal growth retrospectives ranked by decision-velocity signals from git + chat history
  - Tracks 5 categories: domain knowledge, human skills, work habits, meta-cognition, productivity rhythm
  - Graduation markers required on every Tier 1/2 item so items leave the list instead of piling up
  - Step 0 Action Audit blocks new scans if prior level-up actions are untouched (anti-busywork forcing function)
  - Cross-agent: same SKILL.md works in Claude Code, OpenAI Codex CLI, and Google Antigravity
  - Try in 5 seconds: `git clone … && bash examples/demo-fixture/demo.sh` (no LLM needed)

- [ggrigo/align](https://github.com/ggrigo/align) ![Stars](https://img.shields.io/github/stars/ggrigo/align?style=flat-square)
  - Personal evals trio for Claude Code and Cowork — capture, diagnose, synthesize
  - `/align` rates each LLM claim in a local HTML form (6-shape canonical: correct / wrong / almost / needs-nuance / can't-verify / skipped); archives corrections as structured markdown
  - `/diagnose` traces wrong claims back to the stale instruction that caused them — quoted-evidence citations + 0–100 confidence + threshold-80 filtering (read-only)
  - `/retro` clusters patterns across sessions and opens patch PRs with per-patch human gates
  - MIT, runs locally, no service. Single-plugin marketplace at `ggrigo/align`; installs via `/plugin marketplace add ggrigo/align`

- [affaan-m/ECC](https://github.com/affaan-m/ECC) ![Stars](https://img.shields.io/github/stars/affaan-m/ECC?style=flat-square)
  - Agent harness performance optimization
  - Research-first development approach
  - Memory management and security patterns

- [SawyerHood/dev-browser](https://github.com/SawyerHood/dev-browser) ![Stars](https://img.shields.io/github/stars/SawyerHood/dev-browser?style=flat-square)
  - Give Claude agents web browser capabilities
  - Headless browser automation with Playwright
  - Sandboxed QuickJS WASM environment
  - CLI tool with full LLM usage guide
  - Works with Claude Code, Amp, and Codex

- [arun-mosai/claude-code-slice-skills](https://github.com/arun-mosai/claude-code-slice-skills) ![Stars](https://img.shields.io/github/stars/arun-mosai/claude-code-slice-skills?style=flat-square)
  - Three composable skills (`/slice`, `/slice-resume`, `/slice-build`) for vertical-slice feature development
  - Turns a one-line feature idea into 11 validated design docs (persona, journey, UI, API, data, security, observability, AI, seed, tests, index)
  - Then implements the slice as migrations, handlers, UI, events, and tests
  - 12 validator sub-agents enforce specificity; atomic cycle commit; project-stage-calibrated ceremony
  - Stack-neutral structure with TypeScript/Postgres/Zod/React defaults and a porting guide for Django/Rails/Go/Next.js

- [mturac/recsys-pipeline-architect](https://github.com/mturac/recsys-pipeline-architect) ![Stars](https://img.shields.io/github/stars/mturac/recsys-pipeline-architect?style=flat-square)
  - Designs composable recommendation, ranking, and feed pipelines using the six-stage **Source → Hydrator → Filter → Scorer → Selector → SideEffect** framework
  - Pattern popularized by xAI's open-sourced [X For You algorithm](https://github.com/xai-org/x-algorithm) — independent MIT reimplementation
  - Walks Claude through eight clarifying steps and surfaces architectural trade-offs (multi-action vs single-score, candidate isolation vs joint, online vs offline batch)
  - Emits runnable scaffolds for Strapi v5 (TypeScript / Jest), Go (with generics), or Python / FastAPI — all three example suites green
  - Vendor-agnostic: works with Claude Code, Codex CLI, Cursor, Gemini CLI, and 13 more agents via `npx skills add mturac/recsys-pipeline-architect`

- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) ![Stars](https://img.shields.io/github/stars/addyosmani/agent-skills?style=flat-square)
  - Production-grade engineering skills aimed at AI coding agents
  - Targets Claude Code, Cursor, and Antigravity IDE workflows
  - Shell-driven and MIT licensed
  - Maintained by Addy Osmani

- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) ![Stars](https://img.shields.io/github/stars/EveryInc/compound-engineering-plugin?style=flat-square)
  - Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more
  - Loop of `/ce-brainstorm`, `/ce-plan`, `/ce-work`, `/ce-code-review`, and `/ce-compound`
  - `/ce-strategy` anchors a `STRATEGY.md` and `/ce-product-pulse` writes time-windowed pulse reports
  - Published as `@every-env/compound-plugin` on npm; documented by Every Inc

- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) ![Stars](https://img.shields.io/github/stars/OthmanAdi/planning-with-files?style=flat-square)
  - Claude Code skill implementing Manus-style persistent markdown planning
  - Plans live as files so they survive context resets and span sessions
  - Compatible with Claude Code, Hermes Agent, OpenClaw, Kilocode, Copilot, and Mastra
  - Python-backed and MIT licensed

- [bo-cao/breaking-coding-chaos](https://github.com/bo-cao/breaking-coding-chaos) ![Stars](https://img.shields.io/github/stars/bo-cao/breaking-coding-chaos?style=flat-square)
  - Human-in-the-loop dual-loop control-plane skill suite for coding agents
  - throughline (progress cockpit) → plan-spar (align+lock PLAN) → clean-cut (minimal implement + verify)
  - Standard Agent Skills layout; works with Claude Code, Codex, Cursor, Grok, OpenCode, Hermes, OpenClaw
  - MIT licensed

- [mturac/pluginpool](https://github.com/mturac/pluginpool) ![Stars](https://img.shields.io/github/stars/mturac/pluginpool?style=flat-square)
  - Ten focused Claude Code plugins for everyday developer productivity
  - Includes **commit-narrator**, **pr-storyteller**, **test-gap**, **deps-doctor**, **env-lint**, **secret-guard**, **standup-gen**, **todo-harvest**, **flaky-detector**, **changelog-forge**
  - 89 hermetic tests across the suite, Python standard library only at runtime
  - Each plugin is a self-contained repo; install all via marketplace: `/plugin marketplace add mturac/pluginpool`. MIT licensed.

- [innovestrum/keelson](https://github.com/innovestrum/keelson) ![Stars](https://img.shields.io/github/stars/innovestrum/keelson?style=flat-square)
  - Tracker-agnostic, issue-driven operating model for AI coding agents
  - `adopt-keelson` interviews you and writes an AGENTS.md plus a selectable lifecycle skill-pack
  - `tune-gates` establishes or refines just the quality gates, standalone
  - Agents run mechanical work autonomously but escalate any move touching the original design, plan, or strategy to a human
  - Works with GitHub, GitLab, Jira, Linear, or any API/CLI/MCP. MIT licensed.

- [laki-arnsteinlarsen/strategistkit-skills](https://github.com/laki-arnsteinlarsen/strategistkit-skills) ![Stars](https://img.shields.io/github/stars/laki-arnsteinlarsen/strategistkit-skills?style=flat-square)
  - Socratic Code Reviewer — interrogates intent, edge cases, and trade-offs; a senior reviewer's questions, not a checklist
  - Systematic Bug Debugger — root-cause debugging from symptoms and stack traces; handles heisenbugs and "works locally, fails in prod"
  - TDD Loop Master — drives red-green-refactor: builds a test list, writes tests first, keeps the discipline tight
  - Free and MIT-licensed; a taste of the larger StrategistKit catalog

- [zenlee123/routerbase-agent-skills](https://github.com/zenlee123/routerbase-agent-skills) ![Stars](https://img.shields.io/github/stars/zenlee123/routerbase-agent-skills?style=flat-square)
  - Three agent skills for using [routerbase](https://routerbase.com/) as an OpenAI-compatible API gateway
  - Covers API integration, model routing and fallback planning, and media generation workflows
  - SKILL.md-based, MIT licensed, and compatible with Claude Code, Codex, OpenClaw, and other agent skill consumers

- [github/spec-kit](https://github.com/github/spec-kit) ![Stars](https://img.shields.io/github/stars/github/spec-kit?style=flat-square)
  - GitHub's toolkit for Spec-Driven Development (spec → plan → tasks → implement)
  - Drives agents from a written specification rather than ad-hoc prompts
  - Works with Claude Code, Copilot, Cursor, and Gemini CLI; Python, MIT licensed

- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) ![Stars](https://img.shields.io/github/stars/eyaltoledano/claude-task-master?style=flat-square)
  - AI task-management system that parses a PRD into structured, dependency-aware tasks
  - Ships both a CLI and an MCP server; drives step-by-step implementation
  - Integrates with Claude Code, Cursor, Windsurf, and Roo

- [yamadashy/repomix](https://github.com/yamadashy/repomix) ![Stars](https://img.shields.io/github/stars/yamadashy/repomix?style=flat-square)
  - Packs an entire repository into a single AI-friendly file
  - Feed whole codebases to Claude and other LLMs for analysis
  - Token counting, compression, and remote-repo support; TypeScript, MIT licensed

- [Pimzino/claude-code-spec-workflow](https://github.com/Pimzino/claude-code-spec-workflow) ![Stars](https://img.shields.io/github/stars/Pimzino/claude-code-spec-workflow?style=flat-square)
  - Spec-driven workflow: Requirements → Design → Tasks → Implementation
  - Plus a Report → Analyze → Fix → Verify bug workflow, with a live dashboard
  - TypeScript, MIT licensed

- [awesome-skills/code-review-skill](https://github.com/awesome-skills/code-review-skill) ![Stars](https://img.shields.io/github/stars/awesome-skills/code-review-skill?style=flat-square)
  - Comprehensive single code-review Skill for Claude Code
  - Covers 20+ languages/frameworks (React 19, Vue 3, Rust, TypeScript, TanStack Query v5)
  - ~21k lines of review guidelines; MIT licensed

- [carlrannaberg/claudekit](https://github.com/carlrannaberg/claudekit) ![Stars](https://img.shields.io/github/stars/carlrannaberg/claudekit?style=flat-square)
  - Toolkit of custom slash commands, hooks, and utilities for Claude Code
  - Hooks enforce type-checking and lint on edits
  - TypeScript, MIT licensed

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

- [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) ![Stars](https://img.shields.io/github/stars/Jeffallan/claude-skills?style=flat-square)
  - 66 specialized skills for full-stack developers
  - Turns Claude Code into a domain-aware pair programmer
  - Python-driven; covers frontend, backend, data, and ops

- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) ![Stars](https://img.shields.io/github/stars/Orchestra-Research/AI-Research-SKILLs?style=flat-square)
  - Open-source library of AI research and engineering skills
  - Vendor-neutral: works with Claude Code, Codex, and Gemini CLI
  - LaTeX-driven docs; built for research-oriented teams

- [revfactory/harness](https://github.com/revfactory/harness) ![Stars](https://img.shields.io/github/stars/revfactory/harness?style=flat-square)
  - Meta-skill that designs domain-specific agent teams
  - Generates specialized agents and the skills they use
  - HTML-based interface for team composition

- [0xfurai/claude-code-subagents](https://github.com/0xfurai/claude-code-subagents) ![Stars](https://img.shields.io/github/stars/0xfurai/claude-code-subagents?style=flat-square)
  - 100+ production-ready development subagents
  - Roughly one per language, framework, or domain
  - Drop into `~/.claude/agents/`; MIT licensed

- [hesreallyhim/a-list-of-claude-code-agents](https://github.com/hesreallyhim/a-list-of-claude-code-agents) ![Stars](https://img.shields.io/github/stars/hesreallyhim/a-list-of-claude-code-agents?style=flat-square)
  - Community-submitted directory of Claude Code subagents
  - Companion to the maintainer's awesome-claude-code list
  - Browse and contribute agents by category

- [qdhenry/Claude-Command-Suite](https://github.com/qdhenry/Claude-Command-Suite) ![Stars](https://img.shields.io/github/stars/qdhenry/Claude-Command-Suite?style=flat-square)
  - Professional slash-command suite for structured dev workflows
  - Code review, feature creation, security audit, and architecture commands
  - Bundles agents and skills alongside the commands

- [wshobson/commands](https://github.com/wshobson/commands) ![Stars](https://img.shields.io/github/stars/wshobson/commands?style=flat-square)
  - Production-ready slash-command collection for Claude Code
  - Split into multi-step workflows and single-purpose tools
  - Companion to the popular `wshobson/agents`; MIT licensed

- [composio-community/awesome-claude-plugins](https://github.com/composio-community/awesome-claude-plugins) ![Stars](https://img.shields.io/github/stars/composio-community/awesome-claude-plugins?style=flat-square)
  - Curated list of Claude Code plugins and marketplaces
  - Custom commands, agents, hooks, and MCP servers via the plugin system
  - Community-maintained directory

### Framework-Specific

- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) ![Stars](https://img.shields.io/github/stars/nextlevelbuilder/ui-ux-pro-max-skill?style=flat-square)
  - Professional UI/UX design skill
  - Modern design patterns and accessibility
  - Component library integration

- [conorluddy/ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill) ![Stars](https://img.shields.io/github/stars/conorluddy/ios-simulator-skill?style=flat-square)
  - iOS Simulator automation for Claude Code
  - 21 production scripts for building and testing
  - Semantic navigation using accessibility APIs
  - 96% token reduction vs raw tools
  - CI/CD ready with JSON output

- [IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) ![Stars](https://img.shields.io/github/stars/IvanMurzak/Unity-MCP?style=flat-square)
  - AI skills, MCP tools, and CLI for the Unity engine
  - Full AI develop-and-test loop with efficient token usage
  - C# implementation; quick CLI-based setup

- [htdt/godogen](https://github.com/htdt/godogen) ![Stars](https://img.shields.io/github/stars/htdt/godogen?style=flat-square)
  - Autonomous game development for Godot and Bevy
  - Designed to run with Claude Code and Codex
  - Python-driven; assists across engine, gameplay, and asset workflows

- [coder/claudecode.nvim](https://github.com/coder/claudecode.nvim) ![Stars](https://img.shields.io/github/stars/coder/claudecode.nvim?style=flat-square)
  - Claude Code Neovim IDE extension
  - Embeds Claude Code into the Neovim workflow
  - Lua-based; maintained by Coder

---

## Multi-Agent Systems

Orchestrate multiple Claude agents to work together on complex tasks.

### Orchestration Platforms

- [supernovae-st/nika](https://github.com/supernovae-st/nika) ![Stars](https://img.shields.io/github/stars/supernovae-st/nika?style=flat-square)
  - Workflow engine for AI: Claude Code captures repeatable work as `.nika.yaml` DAG files
  - Statically checked before execution (schema, permits, cost floor), tamper-evident traces after
  - Ships a Claude Code plugin (authoring skill + read-only MCP oracle)

- [gyujeongion/llm-council-no-api](https://github.com/gyujeongion/llm-council-no-api) ![Stars](https://img.shields.io/github/stars/gyujeongion/llm-council-no-api?style=flat-square)
  - Claude chairs a panel of Gemini + GPT for a second opinion
  - Runs through your logged-in CLIs, so no API keys

- [gyujeongion/claude-code-goal-loop](https://github.com/gyujeongion/claude-code-goal-loop) ![Stars](https://img.shields.io/github/stars/gyujeongion/claude-code-goal-loop?style=flat-square)
  - Autonomous goal loop with a verification gate each iteration
  - Rollback snapshots and stall detection

- [gastownhall/gastown](https://github.com/gastownhall/gastown) ![Stars](https://img.shields.io/github/stars/gastownhall/gastown?style=flat-square)
  - Multi-agent workspace manager
  - Persistent agent identity across sessions
  - Convoy system for coordinated tasks
  - Git-backed state tracking

- [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) ![Stars](https://img.shields.io/github/stars/agentlas-ai/Agentlas-OS?style=flat-square)
  - Open Agent OS for Claude Code, Codex, and Cursor
  - Packages agents, skills, memory, routing rules, and security gates
  - Includes Hephaestus Network MCP for Agentlas Hub search, runtime bundles, and plugin resolution
  - Local-first by default with Hub fallback for public agents

- [dlorenc/multiclaude](https://github.com/dlorenc/multiclaude) ![Stars](https://img.shields.io/github/stars/dlorenc/multiclaude?style=flat-square)
  - Multi-agent orchestrator with flexible modes
  - Singleplayer and multiplayer coordination
  - Supervisor-subagent pattern implementation

- [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) ![Stars](https://img.shields.io/github/stars/Untrivial-ai/agent-orchestrator?style=flat-square)
  - Agent-agnostic parallel orchestrator
  - Git worktrees for isolated environments
  - CI auto-fix and review routing

- [nyldn/claude-octopus](https://github.com/nyldn/claude-octopus) ![Stars](https://img.shields.io/github/stars/nyldn/claude-octopus?style=flat-square)
  - Surface AI blindspots by running up to 8 AI models on every task
  - Targets research, design, and coding workflows
  - Shell-based orchestration layer

- [RunMaestro/Maestro](https://github.com/RunMaestro/Maestro) ![Stars](https://img.shields.io/github/stars/RunMaestro/Maestro?style=flat-square)
  - Agent orchestration command center
  - Coordinates multi-agent runs across coding tasks
  - TypeScript-driven; designed for fleet-scale agent operations

- [stellarlinkco/myclaude](https://github.com/stellarlinkco/myclaude) ![Stars](https://img.shields.io/github/stars/stellarlinkco/myclaude?style=flat-square)
  - Multi-agent orchestration workflow across Claude Code, Codex, Gemini, and OpenCode
  - Go-based runtime distributed as a single binary
  - Targets cross-agent collaboration on the same task

- [generalaction/emdash](https://github.com/generalaction/emdash) ![Stars](https://img.shields.io/github/stars/generalaction/emdash?style=flat-square)
  - Open-source agentic development environment (Y Combinator W26)
  - Runs multiple coding agents in parallel across any provider
  - TypeScript-driven

- [ymxlx/polis-protocol](https://github.com/ymxlx/polis-protocol) ![Stars](https://img.shields.io/github/stars/ymxlx/polis-protocol?style=flat-square)
  - Markdown coordination protocol for multi-vendor agent teams
  - Signed capability cards, ε-greedy bandit routing that learns from settled contracts
  - Chavruta paired review for high-stakes work; self-amending constitution
  - Vendor-agnostic — works across Claude Code, Codex, Gemini CLI

- [Varalix-Digitech-Solutions/clone-team](https://github.com/Varalix-Digitech-Solutions/clone-team) ![Stars](https://img.shields.io/github/stars/Varalix-Digitech-Solutions/clone-team?style=flat-square)
  - Agent team (Manager, Frontend Developer, Backend Architect, Tester) that clones any website into a pixel-perfect UI in your chosen stack
  - Deterministic build/test Workflow with an unskippable Tester gate; agent fan-out sized to host RAM
  - Pausable/resumable across sessions; also outputs a reverse-engineered ARCHITECTURE.md

- [Varalix-Digitech-Solutions/game-build-team-skill](https://github.com/Varalix-Digitech-Solutions/game-build-team-skill) ![Stars](https://img.shields.io/github/stars/Varalix-Digitech-Solutions/game-build-team-skill?style=flat-square)
  - Agent team (Manager, Creative Director, Logic & Animation Developers, Tester) that builds Godot 4 / GDScript game features
  - Two unskippable gates — headless test gate + "is it fun" creative gate — then an on-device final pass
  - Deterministic build/test Workflow; pausable/resumable across sessions and usage-limit cutoffs

- [5dive-ai/5dive](https://github.com/5dive-ai/5dive) ![Stars](https://img.shields.io/github/stars/5dive-ai/5dive?style=flat-square)
  - Run a company of AI coding agents on a server you own
  - One-command spin-up of named agents (Claude Code, Codex, Grok, and more)
  - Cron + heartbeat scheduling, shared task queue with human-escalation gates, Telegram control
  - Babysit and needs-you triage dashboard; self-hosted, MIT

- [ofekron/better-agent](https://github.com/ofekron/better-agent) ![Stars](https://img.shields.io/github/stars/ofekron/better-agent?style=flat-square)
  - Local workspace for Claude, Codex, and Gemini coding-agent sessions
  - Fork and delegate work across providers with persistent session state
  - Detached runners and restart recovery keep long-running work inspectable
  - Source-available for non-commercial use; commercial use requires permission

- [beastlabai/multi-llm-plugin](https://github.com/beastlabai/multi-llm-plugin) ![Stars](https://img.shields.io/github/stars/beastlabai/multi-llm-plugin?style=flat-square)
  - Multi-LLM orchestration plugin for Claude Code
  - Parallel plan review, task generation, implementation, and code review across 12 coding harnesses (Codex, Cursor, opencode, pi, aider, Antigravity…)

- [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) ![Stars](https://img.shields.io/github/stars/bmad-code-org/BMAD-METHOD?style=flat-square)
  - "Breakthrough Method for Agile AI-Driven Development"
  - Role-based agent team (analyst, PM, architect, dev, QA) in a plan-then-build flow
  - Tool-agnostic framework used heavily with Claude Code, Cursor, and others

- [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) ![Stars](https://img.shields.io/github/stars/BloopAI/vibe-kanban?style=flat-square)
  - Kanban-style board to run and manage multiple coding agents
  - Orchestrates Claude Code, Codex, and other agents from one UI
  - Rust-based; Apache-2.0 licensed

- [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) ![Stars](https://img.shields.io/github/stars/humanlayer/humanlayer?style=flat-square)
  - Framework for steering coding agents through complex codebases
  - Human-in-the-loop approvals and advanced context-engineering workflows
  - TypeScript-based

- [stravu/crystal](https://github.com/stravu/crystal) ![Stars](https://img.shields.io/github/stars/stravu/crystal?style=flat-square)
  - Desktop app to run multiple Claude Code / Codex sessions in parallel git worktrees
  - Compare competing approaches side by side
  - TypeScript, MIT licensed

### Parallel Processing

- [Dicklesworthstone/claude_code_agent_farm](https://github.com/Dicklesworthstone/claude_code_agent_farm) ![Stars](https://img.shields.io/github/stars/Dicklesworthstone/claude_code_agent_farm?style=flat-square)
  - Run 20-50 Claude agents in parallel
  - Lock-based coordination system
  - tmux monitoring dashboard

- [disler/infinite-agentic-loop](https://github.com/disler/infinite-agentic-loop) ![Stars](https://img.shields.io/github/stars/disler/infinite-agentic-loop?style=flat-square)
  - Two-prompt system for spawning parallel agents
  - Evolving iterations for complex problem-solving
  - Self-improving agent patterns

- [AutomateLab-tech/agency-os](https://github.com/AutomateLab-tech/agency-os) ![Stars](https://img.shields.io/github/stars/AutomateLab-tech/agency-os?style=flat-square)
  - Run your work like an AI agency from a single Notion board
  - Plans ideas into dependency-sequenced subtasks
  - Dispatches each task to the right model (Haiku/Sonnet/Opus)
  - Collects results back in Notion via MCP
  - Pluggable to Claude Code, Cursor, Cline, or any MCP-compatible agent

- [ruvnet/ruflo](https://github.com/ruvnet/ruflo) ![Stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=flat-square)
  - Multi-agent swarm orchestration
  - Self-learning capabilities
  - RAG (Retrieval-Augmented Generation) integration
  - Hive mind topology for distributed intelligence

- [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) ![Stars](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-claudecode?style=flat-square)
  - Teams-first multi-agent orchestration
  - Zero configuration with intelligent defaults
  - Natural language interface, no commands to memorize
  - Automatic parallelization and cost optimization
  - Real-time HUD statusline for visibility

- [mikeyobrien/ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator) ![Stars](https://img.shields.io/github/stars/mikeyobrien/ralph-orchestrator?style=flat-square)
  - Improved implementation of the Ralph Wiggum technique for autonomous AI agents
  - Rust-based runtime for managing long-running agent loops
  - Built for fleet-style autonomous coding

- [michaelshimeles/ralphy](https://github.com/michaelshimeles/ralphy) ![Stars](https://img.shields.io/github/stars/michaelshimeles/ralphy?style=flat-square)
  - Bash-style Ralph Wiggum setup that runs agents in a loop
  - Supports Claude Code, Codex, OpenCode, Cursor agent, Qwen, and Droid
  - TypeScript implementation; lightweight harness

- [subsy/ralph-tui](https://github.com/subsy/ralph-tui) ![Stars](https://img.shields.io/github/stars/subsy/ralph-tui?style=flat-square)
  - Terminal UI on top of the Ralph autonomous-loop technique
  - TypeScript-driven; provides visibility into iteration cycles

- [smtg-ai/claude-squad](https://github.com/smtg-ai/claude-squad) ![Stars](https://img.shields.io/github/stars/smtg-ai/claude-squad?style=flat-square)
  - Manage multiple AI terminal agents like Claude Code, Codex, OpenCode, and Amp
  - Go-based runner with per-agent session control
  - Built for keeping several agents alive in parallel

- [SeemSeam/claude_codex_bridge](https://github.com/SeemSeam/claude_codex_bridge) ![Stars](https://img.shields.io/github/stars/SeemSeam/claude_codex_bridge?style=flat-square)
  - Visible multi-agent CLI teams for Claude, Codex, Gemini, OpenCode, and Droid
  - Project memory plus tmux-based supervision
  - Python-driven runtime

- [avelikiy/great_cto](https://github.com/avelikiy/great_cto) ![Stars](https://img.shields.io/github/stars/avelikiy/great_cto?style=flat-square)
  - Multi-agent SDLC plugin for Claude Code
  - 34 specialist reviewer agents across 25 archetypes (fintech, voice-AI, clinical, robotics, and more)
  - 10 compliance packs auto-attach by archetype (PCI, HIPAA, FDA SaMD, NYC AEDT, GDPR, etc.)
  - Two human gates per feature plus memory feedback loop that persists decisions across sessions

---
- [dazuiba/handoff](https://github.com/dazuiba/handoff) ![Stars](https://img.shields.io/github/stars/dazuiba/handoff?style=flat-square)
  - Skill/subagent that delegates tasks to DeepSeek V4, Codex, or Opus without leaving your session
  - Runs tasks in the background; result returns automatically when done
  - Backed by handoff-cli; supports parallel tasks and session resume

- [dagger/container-use](https://github.com/dagger/container-use) ![Stars](https://img.shields.io/github/stars/dagger/container-use?style=flat-square)
  - Sandboxed, isolated development environments for coding agents
  - Lets multiple agents work in parallel without touching the host
  - Go-based; Apache-2.0 licensed

## Security & Compliance

Professional-grade security skills for vulnerability detection, code auditing, and compliance.

### Security Analysis
n- [GiulioDER/cca-audit](https://github.com/GiulioDER/cca-audit) ![Stars](https://img.shields.io/github/stars/GiulioDER/cca-audit?style=flat-square)
  - 6-layer parallel code audit pipeline with non-overlapping scopes
  - Runs 6 specialized LLM auditors (code quality, bugs, security, performance, docs, config)
  - Deduplicates findings, auto-fixes P1+P2, re-verifies tests, architect review gate
  - Three variants: Claude Code, Codex CLI, OpenRouter Python CLI

- [moltenbit/should-i-care](https://github.com/moltenbit/should-i-care) ![Stars](https://img.shields.io/github/stars/moltenbit/should-i-care?style=flat-square)
  - Single-CVE applicability triage: does this CVE actually affect your environment
  - Reasons about exploitation conditions against a self-maintained environment profile, every verdict cited to its source
  - Markdown-driven; built and tested on Claude Code and Codex

- [wrsmith108/varlock-claude-skill](https://github.com/wrsmith108/varlock-claude-skill) ![Stars](https://img.shields.io/github/stars/wrsmith108/varlock-claude-skill?style=flat-square)
  - Secure environment variable management
  - Ensures secrets never appear in sessions, terminals, logs, or git
  - Production-ready secret handling

- [trailofbits/skills](https://github.com/trailofbits/skills) ![Stars](https://img.shields.io/github/stars/trailofbits/skills?style=flat-square)
  - Trail of Bits Claude Code skills for security research and audit work
  - Vulnerability detection patterns from real engagement experience
  - Python-driven

- [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ![Stars](https://img.shields.io/github/stars/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)
  - 754 structured cybersecurity skills for AI agents
  - Mapped to MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, and NIST AI RMF
  - Python-driven; large-scale skill bundle

- [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) ![Stars](https://img.shields.io/github/stars/vercel-labs/deepsec?style=flat-square)
  - Security harness for finding vulnerabilities using coding agents
  - TypeScript-based; integrates with the agent loop
  - Maintained by Vercel Labs

- [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) ![Stars](https://img.shields.io/github/stars/SimoneAvogadro/android-reverse-engineering-skill?style=flat-square)
  - Claude Code skill for Android application reverse engineering
  - Shell-driven tooling around standard RE workflows
  - Useful for security researchers and CTF teams

- [gadievron/raptor](https://github.com/gadievron/raptor) ![Stars](https://img.shields.io/github/stars/gadievron/raptor?style=flat-square)
  - Turns Claude Code into a general-purpose offensive and defensive security agent
  - Uses `CLAUDE.md`, sub-agents, and rules for opinionated workflows
  - Python-driven

- [Darkmoon](https://github.com/ASCIT31/Dark-Moon) - Open source (GPL-3.0) autonomous AI penetration testing platform covering web, API, Active Directory and Kubernetes, with proof of exploitation.
- [LoRexxar/Kunlun-M](https://github.com/LoRexxar/Kunlun-M) ![Stars](https://img.shields.io/github/stars/LoRexxar/Kunlun-M?style=flat-square)
  - Fully open-source static white-box scanner for PHP and JavaScript
  - Semantic scanning combined with AI Agent integration (OpenClaw and Claude Code)
  - Python-driven; useful for application-security teams

- [SpicyNoodles3/claude-code-file-guard](https://github.com/SpicyNoodles3/claude-code-file-guard) ![Stars](https://img.shields.io/github/stars/SpicyNoodles3/claude-code-file-guard?style=flat-square)
  - PreToolUse hook that blocks the agent from writing to files you declare protected
  - Covers Edit/Write/NotebookEdit, any tool carrying a file_path, plus a Bash write-heuristic and a destructive-git blocklist
  - One auditable bash script, jq-only, fail-closed; README is explicit about what it cannot stop
  - Tested on ubuntu and macos (39-case harness + shellcheck)

### Compliance & Auditing

- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) ![Stars](https://img.shields.io/github/stars/BehiSecc/awesome-claude-skills?style=flat-square)
  - Security-focused skill collection
  - Document handling with security in mind
  - Development and data analysis tools

---

## Marketing & Content

Skills for marketing professionals, content creators, and growth teams.

- [humanpen/humanpen-skill](https://github.com/humanpen/humanpen-skill) ![Stars](https://img.shields.io/github/stars/humanpen/humanpen-skill?style=flat-square)
  - Document-level AI humanizer for .docx/.pptx — whole file, selected passages, or detector-flagged text
  - Keeps every fact, number, table and all formatting intact
  - The document never enters the model's context — upload, then get a result path back
  - Works with Claude Code, Codex, Cursor, and other SKILL.md clients

- [cognyai/claude-code-marketing-skills](https://github.com/cognyai/claude-code-marketing-skills) ![Stars](https://img.shields.io/github/stars/cognyai/claude-code-marketing-skills?style=flat-square)
  - 5 free marketing skills, no account required
  - SEO Audit, Landing Page Review, Competitor Analysis
  - Ad Copy Writer and Lead Qualification
  - Works with Claude Code, Cursor, and Windsurf

- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) ![Stars](https://img.shields.io/github/stars/coreyhaines31/marketingskills?style=flat-square)
  - 23 professional marketing skills
  - CRO (Conversion Rate Optimization)
  - Copywriting and SEO strategies
  - Paid advertising and growth tactics

- [nowork-studio/NotFair](https://github.com/nowork-studio/NotFair) ![Stars](https://img.shields.io/github/stars/nowork-studio/NotFair?style=flat-square)
  - Open-source Claude Code skills for SEO, GEO, Google Ads, and Meta Ads (MIT)
  - [SEO skills](https://github.com/nowork-studio/NotFair/tree/main/seo): site analysis, keyword research, meta tags, schema markup, GEO optimization, and content writing
  - [Google Ads skills](https://github.com/nowork-studio/NotFair/tree/main/google-ads): audits, wasted-spend detection, search-term cleanup, keyword and bid management
  - [Meta Ads skills](https://github.com/nowork-studio/NotFair/tree/main/meta-ads): ROAS analysis, creative fatigue, and audience overlap detection
  - Connects to live data via Google Ads MCP, Meta Ads MCP, Google Search Console MCP, and Google Analytics (GA4) MCP

- [salespeak-ai/buyer-eval-skill](https://github.com/salespeak-ai/buyer-eval-skill) ![Stars](https://img.shields.io/github/stars/salespeak-ai/buyer-eval-skill?style=flat-square)
  - Structured B2B software vendor evaluation skill (MIT)
  - Domain-expert questions per software category
  - Engages vendor AI agents for verified due diligence
  - Evidence-tracked scoring across 7 dimensions; comparative scorecards for procurement and build-vs-buy decisions

- [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) ![Stars](https://img.shields.io/github/stars/zarazhangrui/codebase-to-course?style=flat-square)
  - Transform codebases into interactive HTML courses
  - Beautiful, educational content generation
  - Perfect for developer education and onboarding

- [ndesv21/socialclaw](https://github.com/ndesv21/socialclaw) ![Stars](https://img.shields.io/github/stars/ndesv21/socialclaw?style=flat-square)
  - Schedule and publish social media posts across 13 platforms via SocialClaw
  - Supports X, LinkedIn (profile + page), Instagram, Facebook Pages, TikTok, YouTube, Reddit, WordPress, Pinterest
  - One workspace API key (`SC_API_KEY`) for campaigns, media upload, and analytics
  - Install: `npx skills add ndesv21/socialclaw`

- [Sequenzy/skills](https://github.com/Sequenzy/skills/tree/main/skills/sequenzy-email-marketing) ![Stars](https://img.shields.io/github/stars/Sequenzy/skills?style=flat-square)
  - Agent skill for operating Sequenzy lifecycle email marketing and transactional/product email workflows
  - Manage subscribers, lists, segments, tags, templates, campaigns, sequences, stats, API keys, websites, and transactional sends
  - Includes CLI/MCP decision trees, supported-workflow caveats, dashboard URL patterns, and safe execution guidance for AI agents
  - Install: `npx skills add Sequenzy/skills`

- [Get-Maito/newsletter-skills](https://github.com/Get-Maito/newsletter-skills) ![Stars](https://img.shields.io/github/stars/Get-Maito/newsletter-skills?style=flat-square)
  - Open-source SKILL.md pack for newsletter operators using Claude Code, Codex, Cursor, and compatible agents
  - Covers local event research, source audits, issue building, sponsor operations, monetization strategy, ROI checks, social repurposing, and launch cadence
  - Product-agnostic by default, with optional Maito-connected persistence for sources, issues, approvals, analytics, and sponsor history
  - Instruction-only v0.1.0 pack with no executable scripts or runtime dependencies
  - Install: `npx skills add Get-Maito/newsletter-skills`

- [clockless-org/html-anything](https://github.com/clockless-org/html-anything) ![Stars](https://img.shields.io/github/stars/clockless-org/html-anything?style=flat-square)
  - Turn any file, folder, URL, or service export into a polished single-file HTML page
  - Auto picks one of 16 design systems (lesson lab, map atlas, timeline story, relationship rhythm, network map, dashboard, document review, terminal evidence, living essay, editorial carousel, paper trail, …)
  - 34 source parsers — CSV, PDF, DOCX, JSON/JSONL, log, GPX/KML, WhatsApp/WeChat/Slack/Discord/Telegram, Amazon orders, Kindle highlights, Spotify, Apple Health, LinkedIn, Google Photos Takeout, vCard, Venmo/PayPal, browser history, …
  - Self-contained — inline CSS/JS, no CDN, works offline; [22-demo live gallery](https://clockless-org.github.io/html-anything/examples/)
  - Cross-agent — Claude Code, Codex, Cursor, Cline, Windsurf via `npx skills add clockless-org/html-anything`

- [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) ![Stars](https://img.shields.io/github/stars/AgriciDaniel/claude-ads?style=flat-square)
  - Paid advertising audit and optimization skill for Claude Code
  - 250+ checks across Google, Meta, YouTube, LinkedIn, and TikTok ads
  - Python-driven

- [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) ![Stars](https://img.shields.io/github/stars/AgriciDaniel/claude-seo?style=flat-square)
  - Universal SEO skill for Claude Code
  - 25 sub-skills plus 18 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, backlinks, and local SEO
  - Python-driven

- [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) ![Stars](https://img.shields.io/github/stars/zubair-trabzada/geo-seo-claude?style=flat-square)
  - GEO-first SEO skill for Claude Code
  - Citability scoring, AI crawler analysis, and brand-mention tracking
  - Python-driven

- [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) ![Stars](https://img.shields.io/github/stars/op7418/guizang-ppt-skill?style=flat-square)
  - Agent skill for generating polished HTML slide decks
  - Editorial-magazine and Swiss layouts with social-cover variants
  - Image prompts and WebGL/low-poly visual options

- [nexu-io/open-design](https://github.com/nexu-io/open-design) ![Stars](https://img.shields.io/github/stars/nexu-io/open-design?style=flat-square)
  - Local-first, open-source alternative to Anthropic's Claude Design
  - 19 skills with 71 brand-grade design systems
  - Generates web, desktop, and mobile prototypes; BYOK

- [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) ![Stars](https://img.shields.io/github/stars/alchaincyf/huashu-design?style=flat-square)
  - HTML-native design skill for Claude Code
  - High-fidelity prototypes, slide decks, and animation with MP4 export
  - 20 design philosophies and a 5-axis review; agent-agnostic

- [ZSeven-W/openpencil](https://github.com/ZSeven-W/openpencil) ![Stars](https://img.shields.io/github/stars/ZSeven-W/openpencil?style=flat-square)
  - Open-source AI-native vector design tool
  - First to feature concurrent agent teams for design-as-code
  - TypeScript-driven

- [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) ![Stars](https://img.shields.io/github/stars/yizhiyanhua-ai/fireworks-tech-graph?style=flat-square)
  - Generate production-quality SVG and PNG technical diagrams from natural language
  - 7 styles, UML support, and AI/Agent workflow patterns
  - Python-driven

- [aislinn-yang/rednote-writing-skill](https://github.com/aislinn-yang/rednote-writing-skill) ![Stars](https://img.shields.io/github/stars/aislinn-yang/rednote-writing-skill?style=flat-square)
  - Writes Rednote (Xiaohongshu / 小红书) posts in your own voice, never fabricating content
  - Collage / co-create / review modes turn rough ideas into a finished draft
  - Scans for AI-tells and platform-throttling words, then a "reads like a real person" pass before title and cover
  - MIT licensed, instruction-only (no executable scripts); tune `examples.md` to match your own writing

- [outreachmagic/outreachmagic](https://github.com/outreachmagic/outreachmagic) ![Stars](https://img.shields.io/github/stars/outreachmagic/outreachmagic?style=flat-square)
  - **GTM pipeline agent** that syncs Smartlead, Instantly, HeyReach, PlusVibe, EmailBison, Prosp, and Calendly into a local SQLite database your agent can query directly
  - Every send, reply, bounce, and stage change lands on your machine
  - Install: `npx skills add outreachmagic/outreachmagic`

- [sergebulaev/facebook-skills](https://github.com/sergebulaev/facebook-skills) ![Stars](https://img.shields.io/github/stars/sergebulaev/facebook-skills?style=flat-square)
  - 8 Claude Code and Codex skills for Facebook Pages
  - High-share posts, hook extractor, humanizer, engagement drafter, and content planner
  - Note: publishing depends on the commercial Publora API
  - MIT licensed
  - Install: `/plugin marketplace add sergebulaev/facebook-skills`

- [fjilvvi/growthlens](https://github.com/fjilvvi/growthlens) ![Stars](https://img.shields.io/github/stars/fjilvvi/growthlens?style=flat-square)
  - 12 business-analysis skills for marketers, growth & business analysts (not just coders)
  - Competitor teardown, funnel audit, pricing analysis, offer/value ladder, ICP segmentation, SEO content-gap
  - Installable as a Claude Code plugin (`/plugin marketplace add fjilvvi/growthlens`); MIT

- [Linked-API/linkedin-skills](https://github.com/Linked-API/linkedin-skills/tree/main/linkedin) ![Stars](https://img.shields.io/github/stars/Linked-API/linkedin-skills?style=flat-square)
  - Fetch LinkedIn profiles, search people and companies, send messages, manage connections, create posts, react, and comment
  - Custom LinkedIn workflows from Claude Code, Codex, Cursor, and Windsurf

- [aragossa/ai-tell-detector](https://github.com/aragossa/ai-tell-detector) ![Stars](https://img.shields.io/github/stars/aragossa/ai-tell-detector?style=flat-square)
  - Audits a finished draft for the patterns that make text read as AI-generated (24 checks, MIT)
  - Flags rhetorical symmetry, filler transitions, uniform sentence rhythm, canned CTAs, and em-dash overload
  - Also catches fabricated personal experience, which is a factual problem rather than a stylistic one
  - Reports patterns with line numbers and a suggested fix instead of a single confidence score
  - English and Russian versions included

---

## Domain-Specific Skills

- [Uhudsavasindankacanokcu2/finance-skills-for-claude](https://github.com/Uhudsavasindankacanokcu2/finance-skills-for-claude) ![Stars](https://img.shields.io/github/stars/Uhudsavasindankacanokcu2/finance-skills-for-claude?style=flat-square) - Cash flow, runway, invoices, budgets & scenario modeling for founders/finance teams
- [Uhudsavasindankacanokcu2/legal-skills-for-claude](https://github.com/Uhudsavasindankacanokcu2/legal-skills-for-claude) ![Stars](https://img.shields.io/github/stars/Uhudsavasindankacanokcu2/legal-skills-for-claude?style=flat-square) - Contract review, summarization, drafting & negotiation redlines in plain English
- [Uhudsavasindankacanokcu2/recruiting-skills-for-claude](https://github.com/Uhudsavasindankacanokcu2/recruiting-skills-for-claude) ![Stars](https://img.shields.io/github/stars/Uhudsavasindankacanokcu2/recruiting-skills-for-claude?style=flat-square) - Job descriptions, bias-aware resume screening & structured interview kits

Specialized skills for specific industries and use cases.

- [dhosruiasn/accessible-dark-mode-design-expert](https://github.com/dhosruiasn/accessible-dark-mode-design-expert) ![Stars](https://img.shields.io/github/stars/dhosruiasn/accessible-dark-mode-design-expert?style=flat-square)
  - Accessible light/dark theme design, implementation, review, and audit skill for Claude Code and OpenAI Codex
  - Covers user preference precedence, semantic design tokens, WCAG text and non-text contrast, theme-aware assets, Material and Apple conventions, and reduced-motion-safe transitions
  - Ships a deterministic contrast calculator, safe cross-runtime installation sync, automated tests, and bilingual Traditional Chinese/English documentation
  - MIT licensed; invoked as `/accessible-dark-mode-design-expert`

- [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) ![Stars](https://img.shields.io/github/stars/Donchitos/Claude-Code-Game-Studios?style=flat-square)
  - Turn Claude Code into a full game development studio
  - 48 AI agents and 37 workflow skills
  - Complete coordination system mirroring real studio hierarchy
  - Engine specialists, designers, and production agents
  - Perfect for game development projects
    
- [Miscodings/paper-plugin](https://github.com/Miscodings/paper-plugin) ![Stars](https://img.shields.io/github/stars/Miscodings/paper-plugin?style=flat-square)
  - Complete Minecraft Paper plugin development suite for Claude Code
  - 1 comprehensive skill + 8 specialized subagents (architect, debugger, reviewer, data, commands, events, performance, publisher)
  - Enforces modern practices: Adventure API, Display entities, config-driven items/GUIs, lang files, LuckPerms permission trees
  - MythicMobs, ModelEngine, PlaceholderAPI, WorldGuard, Vault, LuckPerms integrations
  - Kotlin/Java, Paper 1.21.x, Gradle Kotlin DSL

- [fruitwyatt/puzzlegenio-claude-skill](https://github.com/fruitwyatt/puzzlegenio-claude-skill) ![Stars](https://img.shields.io/github/stars/fruitwyatt/puzzlegenio-claude-skill?style=flat-square)
  - Generate free printable puzzles (crossword, word search, sudoku, jigsaw, bingo, nonogram)
  - Deep links with URL parameters for pre-filled puzzle settings
  - 8 languages with native word generation
  - AI-powered clue and word list generation
  - Perfect for teachers, event planners, and makers

- [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) ![Stars](https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat-square)
  - Ready-to-fork template for academic research
  - LaTeX/Beamer + R workflow optimization
  - Multi-agent review and adversarial QA
  - Quality gates and replication protocols
  - Extracted from production PhD course

- [takechanman1228/claude-ecom](https://github.com/takechanman1228/claude-ecom) ![Stars](https://img.shields.io/github/stars/takechanman1228/claude-ecom?style=flat-square)
  - Ecommerce business review skill for D2C stores
  - Multi-horizon KPI decomposition across 30d/90d/365d
  - ~30 automated health checks across revenue, customer, and product
  - RFM cohorts and prioritized action plan with impact estimates
  - Hybrid Python-backend + Claude-LLM architecture for deterministic KPIs

- [Ericyoung-183/alpha-insights](https://github.com/Ericyoung-183/alpha-insights) ![Stars](https://img.shields.io/github/stars/Ericyoung-183/alpha-insights?style=flat-square)
  - Business research skill for Claude Code and Codex
  - Encodes 19 consulting frameworks and 9 thinking methods
  - Uses evidence grading, source confidence checks, and stage gates to reduce unsupported AI research claims
  - Generates decision-ready HTML reports with interactive charts
  - MIT licensed; installable from GitHub

- [Xquik-dev/tweetclaw](https://github.com/Xquik-dev/tweetclaw) ![Stars](https://img.shields.io/github/stars/Xquik-dev/tweetclaw?style=flat-square)
  - OpenClaw plugin and agent skill for X/Twitter automation
  - Search tweets and tweet replies, post tweets and replies, and export followers
  - Includes media upload, media download, direct messages, monitors, webhooks, and giveaway draws
  - Ships GitHub docs, npm install, ClawHub listing, and Context7 reference docs

- [Xquik-dev/hermes-tweet](https://github.com/Xquik-dev/hermes-tweet) ![Stars](https://img.shields.io/github/stars/Xquik-dev/hermes-tweet?style=flat-square)
  - Native Hermes Agent plugin for X/Twitter research, monitoring, and gated actions
  - Ships a PyPI package, Hermes plugin entry point, bundled skill, and `.claude-plugin/plugin.json`
  - Install with `hermes plugins install Xquik-dev/hermes-tweet --enable`
  - Read tools use `XQUIK_API_KEY`; write actions also require `HERMES_TWEET_ENABLE_ACTIONS=true`

- [blader/humanizer](https://github.com/blader/humanizer) ![Stars](https://img.shields.io/github/stars/blader/humanizer?style=flat-square)
  - Claude Code and OpenCode skill that removes signs of AI-generated writing
  - Installs by cloning into `~/.claude/skills/humanizer` or `~/.config/opencode/skills/humanizer`
  - Single-file `SKILL.md` invoked via `/humanizer` in either tool
  - MIT licensed

- [santifer/career-ops](https://github.com/santifer/career-ops) ![Stars](https://img.shields.io/github/stars/santifer/career-ops?style=flat-square)
  - End-to-end job-search system built on Claude Code with 14 skill modes
  - Resume tailoring, batch outreach, interview prep, and PDF generation
  - Go dashboard for tracking applications and pipeline status
  - MIT licensed; site at career-ops.org

- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) ![Stars](https://img.shields.io/github/stars/mvanhorn/last30days-skill?style=flat-square)
  - Agent skill that researches topics across Reddit, X, YouTube, Hacker News, TikTok, Polymarket, Bluesky, and the open web
  - Synthesizes findings into a grounded recency summary, weighted toward the last 30 days
  - Targets deep research, social-media monitoring, and trend tracking
  - Compatible with Claude Code, OpenClaw, and ClawHub

- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) ![Stars](https://img.shields.io/github/stars/K-Dense-AI/scientific-agent-skills?style=flat-square)
  - Ready-to-use agent skills for research, science, engineering, analysis, finance, and writing
  - Coverage includes bioinformatics, chemoinformatics, genomics, proteomics, and materials science
  - Targets Claude Code and Claude Skills runtimes
  - Maintained by K-Dense AI; MIT licensed

- [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) ![Stars](https://img.shields.io/github/stars/FreedomIntelligence/OpenClaw-Medical-Skills?style=flat-square)
  - Open-source medical AI skills library for OpenClaw
  - Skills tuned for clinical, research, and pharma workflows
  - Python-driven

- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) ![Stars](https://img.shields.io/github/stars/Imbad0202/academic-research-skills?style=flat-square)
  - Academic research skills for Claude Code
  - Research, write, review, revise, finalize pipeline
  - Python-driven

- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) ![Stars](https://img.shields.io/github/stars/Master-cai/Research-Paper-Writing-Skills?style=flat-square)
  - Skill package for ML, CV, and NLP paper writing
  - Adapted from Prof. Peng Sida's open notes
  - Works with Codex, Claude Code, and Gemini CLI

- [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) ![Stars](https://img.shields.io/github/stars/Galaxy-Dawn/claude-scholar?style=flat-square)
  - Semi-automated research assistant for academic and software work
  - Supports Claude Code, OpenCode, and Codex CLI
  - Python-driven

- [SamurAIGPT/Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills) ![Stars](https://img.shields.io/github/stars/SamurAIGPT/Generative-Media-Skills?style=flat-square)
  - Multi-modal generative media skills for AI agents
  - High-quality image, video, and audio generation
  - Works with Claude Code, Cursor, and Gemini CLI

- [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) ![Stars](https://img.shields.io/github/stars/alchaincyf/nuwa-skill?style=flat-square)
  - Distill anyone's thinking — mental models, decision heuristics, and expression DNA
  - Python-driven Claude skill
  - English/Chinese bilingual

- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) ![Stars](https://img.shields.io/github/stars/op7418/Humanizer-zh?style=flat-square)
  - Chinese localization of the Humanizer Claude Code skill
  - Removes AI-generated signals from Chinese text
  - Companion to blader/humanizer for English

- [alchaincyf/darwin-skill](https://github.com/alchaincyf/darwin-skill) ![Stars](https://img.shields.io/github/stars/alchaincyf/darwin-skill?style=flat-square)
  - Skill that lets your skills evolve through evaluate, improve, test, and keep-or-rollback cycles
  - Autoresearch-inspired iteration loop
  - HTML-driven; Chinese-language project

- [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) ![Stars](https://img.shields.io/github/stars/nidhinjs/prompt-master?style=flat-square)
  - Claude skill that writes accurate prompts for any AI tool
  - Aims to keep context and memory across iterations
  - Token-conscious by design

- [longbridge/skills](https://github.com/longbridge/skills) ![Stars](https://img.shields.io/github/stars/longbridge/skills?style=flat-square)
  - 125+ agent skills for Longbridge Securities — real-time quotes, charts, fundamentals, portfolio analytics, and valuation
  - Covers HK, US, A-share (SH/SZ), and Singapore markets
  - Trilingual support: Simplified Chinese, Traditional Chinese, and English
  - Includes options (US/HK), warrants, DeFi yields, ETF analysis, and advanced portfolio tools

- [Three-Pillar Personal Finance](https://github.com/nontravis/personal-finance-whitepaper) ![Stars](https://img.shields.io/github/stars/nontravis/personal-finance-whitepaper?style=flat-square)
  - A reasoning-lens skill that makes any AI advise through the Three-Pillar system (Income − Expenses = Freedom Fund; Cashflow, Investment, Savings; discipline over strategy)
  - MIT licensed; installable via plugin/degit

---

- [twzrd-sol/wzrd-final](https://intel.twzrd.xyz)
  - Solana-native trust scoring MCP server for AI agents
  - Free preflight endpoint + paid signed V5 trust receipt via x402 protocol
  - Streamable-HTTP MCP at https://intel.twzrd.xyz/mcp
  - On-chain trust verification and payment receipts for Web3 workflows

- [Alisa0808/vibe-creating-skill](https://github.com/Alisa0808/vibe-creating-skill) ![Stars](https://img.shields.io/github/stars/Alisa0808/vibe-creating-skill?style=flat-square)
  - Bilingual EN/中文 skill that rewrites a rough idea or over-specified shot script into a model-ready text-to-video prompt
  - Works with Seedance 2.0, Kling, Veo, Hailuo, Wan, Vidu
  - Judgment-first: won't flatten prompts that need precise control
  - One SKILL.md, open Agent Skills standard; MIT

- [abe238/claude-video-plus](https://github.com/abe238/claude-video-plus) ![Stars](https://img.shields.io/github/stars/abe238/claude-video-plus?style=flat-square)
  - Ask a video a question — retrieves only the chapters, numeric facts, and on-screen moments that answer it instead of sampling the whole timeline
  - Sealed, receipt-gated benchmark matched the original's blind-judged answer quality (8.83 vs 8.80) at ~56% fewer tokens; 338 deterministic tests
  - Fails open: reverts to the original pipeline on no captions, local file, short video, or any error
  - Install with `npx skills add abe238/claude-video-plus -g`; attributed MIT fork of bradautomates/claude-video with upstream authorship preserved

- [b1rdmania/claude-plain-english-skill](https://github.com/b1rdmania/claude-plain-english-skill) ![Stars](https://img.shields.io/github/stars/b1rdmania/claude-plain-english-skill?style=flat-square)
  - Strips AI writing tics and applies Orwell/Gowers plain-English rules
  - Audit, rewrite, and in-place file-edit modes, plus a second self-check pass on its own rewrites
  - Reference table of banned LLM vocabulary and constructions with before/after examples
  - No license file in repo

- [b1rdmania/claude-premortem-skill](https://github.com/b1rdmania/claude-premortem-skill) ![Stars](https://img.shields.io/github/stars/b1rdmania/claude-premortem-skill?style=flat-square)
  - Klein-method premortem: assumes a plan has already failed and works backward to find why
  - Spawns parallel sub-agents to generate independent failure narratives, then synthesizes them
  - Outputs most-likely failure, most-dangerous failure, hidden assumptions, and a revised plan as a single HTML report
  - No license file in repo

- [b1rdmania/hinge-profile-optimizer](https://github.com/b1rdmania/hinge-profile-optimizer) ![Stars](https://img.shields.io/github/stars/b1rdmania/hinge-profile-optimizer?style=flat-square)
  - Dating-profile optimization skill grounded in 45+ peer-reviewed sources on attraction and online-dating signaling
  - Structured research-backed process for prompt selection, photo ordering, and bio writing
  - MIT licensed

- [fcavalcantirj/claude-code-eyes](https://github.com/fcavalcantirj/claude-code-eyes) ![Stars](https://img.shields.io/github/stars/fcavalcantirj/claude-code-eyes?style=flat-square)
  - Give Claude Code eyes — look at real hardware, displays, LCDs and wiring through a camera (Android IP Webcam, Pi cam, or any snapshot URL)
  - Visual-verify a rendered panel and catch bugs that live on the glass, not in the logs; check wiring before power-on
  - ~100 lines of bash + a SKILL.md, MIT, one-command setup

- [tfriedel/claude-office-skills](https://github.com/tfriedel/claude-office-skills) ![Stars](https://img.shields.io/github/stars/tfriedel/claude-office-skills?style=flat-square)
  - Office-document skills for Claude Code: PPTX, DOCX, XLSX, and PDF
  - HTML-to-PPTX conversion, DOCX tracked-changes editing, XLSX financial models
  - Community suite beyond Anthropic's official document skills

- [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) ![Stars](https://img.shields.io/github/stars/ndpvt-web/latex-document-skill?style=flat-square)
  - Universal LaTeX document skill for Claude Code
  - 27 templates, 27 scripts, and 26 reference guides
  - Papers, reports, and Beamer slides for academic/technical writing

- [nimrodfisher/data-analytics-skills](https://github.com/nimrodfisher/data-analytics-skills) ![Stars](https://img.shields.io/github/stars/nimrodfisher/data-analytics-skills?style=flat-square)
  - Claude skills focused specifically on data-analytics tasks
  - Customizable reference materials for analytics workflows
  - Python-based

- [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills) ![Stars](https://img.shields.io/github/stars/lingzhi227/agent-research-skills?style=flat-square)
  - Skills for the full academic research lifecycle
  - Systematic literature review through slide generation
  - Includes GitHub repository analysis for research topics

- [boraoztunc/skills](https://github.com/boraoztunc/skills) ![Stars](https://img.shields.io/github/stars/boraoztunc/skills?style=flat-square)
  - Claude Code skills for copywriting, SEO, and design
  - Includes an AI-writing-pattern remover for humanizer-style prose cleanup
  - Apache-2.0 licensed

## Productivity Tools

Utilities and tools to enhance your Claude workflow.

### Desktop Applications & GUI Tools

- [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) ![Stars](https://img.shields.io/github/stars/CherryHQ/cherry-studio?style=flat-square)
  - AI productivity studio with smart chat and autonomous agents
  - 300+ built-in assistants for various tasks
  - Unified access to frontier LLMs
  - Cross-platform desktop application

- [farion1231/cc-switch](https://github.com/farion1231/cc-switch) ![Stars](https://img.shields.io/github/stars/farion1231/cc-switch?style=flat-square)
  - All-in-one desktop assistant for Claude Code, Codex, OpenCode
  - Skills management and provider configuration
  - Cross-platform with WSL support
  - Built with Rust and Tauri for performance

- [winfunc/opcode](https://github.com/winfunc/opcode) ![Stars](https://img.shields.io/github/stars/winfunc/opcode?style=flat-square)
  - Powerful GUI app and toolkit for Claude Code
  - Create custom agents and manage interactive sessions
  - Run secure background agents
  - Built with Rust and Tauri

- [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) ![Stars](https://img.shields.io/github/stars/iOfficeAI/AionUi?style=flat-square)
  - Free, local, open-source 24/7 cowork app
  - OpenClaw alternative for multiple AI coding assistants
  - Supports Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code
  - Web UI for easy access

- [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) ![Stars](https://img.shields.io/github/stars/siteboon/claudecodeui?style=flat-square)
  - Desktop and mobile UI for Claude Code, Cursor CLI, Codex
  - Manage sessions and projects remotely
  - Responsive design works on desktop, tablet, and mobile
  - Built-in chat, shell terminal, file explorer, and git integration
  - Plugin system for custom extensions

- [jazzyalex/agent-sessions](https://github.com/jazzyalex/agent-sessions) ![Stars](https://img.shields.io/github/stars/jazzyalex/agent-sessions?style=flat-square)
  - Native macOS app for searching, browsing, and resuming Claude Code sessions alongside Codex, Antigravity, OpenCode, and other agents
  - Agent Cockpit provides live iTerm2 orchestration and monitoring for active local agent sessions
  - Local-first transcript indexing with no telemetry

- [tristan666666/agent-island](https://github.com/tristan666666/agent-island) ![Stars](https://img.shields.io/github/stars/tristan666666/agent-island?style=flat-square)
  - Free, MIT-licensed native companion for Claude, Codex, Antigravity, Grok, and Cursor
  - Combines local session status, your-turn alerts, and provider usage views
  - Works without an Agent Island account or product telemetry

- [automazeio/vibeproxy](https://github.com/automazeio/vibeproxy) ![Stars](https://img.shields.io/github/stars/automazeio/vibeproxy?style=flat-square)
  - Native macOS menu-bar app to use Claude Code and ChatGPT subscriptions with AI coding tools
  - Skips the need for API keys
  - Swift implementation

- [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) ![Stars](https://img.shields.io/github/stars/ValueCell-ai/ClawX?style=flat-square)
  - Desktop app providing a graphical interface for OpenClaw AI agents
  - Turns CLI-based AI orchestration into a desktop experience
  - TypeScript-driven Electron build

### Agent Harnesses & Meta-Tools

- [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) ![Stars](https://img.shields.io/github/stars/code-yeongyu/oh-my-openagent?style=flat-square)
  - Best-in-class agent harness (previously oh-my-opencode)
  - TUI for orchestration and management
  - Multi-provider support (OpenAI, Gemini, Claude)
  - TypeScript-based with excellent developer experience

- [intellectronica/ruler](https://github.com/intellectronica/ruler) ![Stars](https://img.shields.io/github/stars/intellectronica/ruler?style=flat-square)
  - Applies the same rules to every coding agent on your machine
  - One rule set propagates to Claude Code, Cursor, Codex, and others
  - TypeScript-driven

- [Battlelamb/claude-code-conversation-titler](https://github.com/Battlelamb/claude-code-conversation-titler) ![Stars](https://img.shields.io/github/stars/Battlelamb/claude-code-conversation-titler?style=flat-square)
  - Interactive skill that titles, names, and labels the current conversation
  - Multilingual: user language, English, or Chinese
  - 13+ title formats plus a recommended pick, description, and tags
  - Suggestion-only; installable as a Claude Code plugin or standalone skill

- [notlikeDev/CCPlugins](https://github.com/notlikeDev/CCPlugins) ![Stars](https://img.shields.io/github/stars/notlikeDev/CCPlugins?style=flat-square)
  - Claude Code framework focused on saving time on routine prompts
  - Built for developers tired of writing "please act like a senior engineer" every session
  - Python-driven

- [tailcallhq/forgecode](https://github.com/tailcallhq/forgecode) ![Stars](https://img.shields.io/github/stars/tailcallhq/forgecode?style=flat-square)
  - AI-enabled pair programmer with broad model support
  - Works with Claude, GPT, Grok, DeepSeek, Gemini, and 300+ more models
  - Rust-based binary

- [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) ![Stars](https://img.shields.io/github/stars/max-sixty/worktrunk?style=flat-square)
  - CLI for managing Git worktrees in parallel AI-agent workflows
  - Rust-based binary
  - Reduces friction when running multiple coding agents on the same repo

- [huangji6693-max/claude-code-dna](https://github.com/huangji6693-max/claude-code-dna) ![Stars](https://img.shields.io/github/stars/huangji6693-max/claude-code-dna?style=flat-square)
  - Behavioral OS for Claude Code agents distilled from 11 deeply-read libraries (179 skills + 99 agents + Karpathy anti-patterns + memory research)
  - 8 rule files codifying Karpathy's 4 laws plus 15 operating instincts (verification gate, TDD reflex, root cause before fix)
  - Three-layer memory architecture inspired by mem0 v3 (ADD-only), langmem (3 types × 2 timings), and Microsoft GraphRAG (community-summary indexing)
  - Portable Bash/Python tooling: `memory-health.sh`, `memory-search.sh` (BM25-style local retrieval), `skill-spec-audit.sh` (agentskills.io compliance — 168 PASS / 23 WARN / 3 FAIL on 194 community skills), and `dna-doctor.sh` (single-command health check)
  - Works across Claude Code, Cursor, Codex CLI, Gemini CLI, Aider, and Continue.dev — rules are model-agnostic markdown

- [thousandflowers/skillreaper](https://github.com/thousandflowers/skillreaper) ![Stars](https://img.shields.io/github/stars/thousandflowers/skillreaper?style=flat-square)
  - Reads real session transcripts to find skills, MCP servers, and agents that were loaded into context but never fired, then safely quarantines them
  - Supports Claude Code, Codex CLI, Hermes, OpenCode, Cursor, and OpenClaw; zero telemetry, single static Go binary
  - Scan / report / prune workflow keeps removals reversible; installable via Homebrew and npm (MIT)
- [KernelLord/pickysteve](https://github.com/KernelLord/pickysteve) ![Stars](https://img.shields.io/github/stars/KernelLord/pickysteve?style=flat-square)
  - Local-first skill router: a cheap local model (default Ollama qwen3:8b) routes each prompt to the right skill via hybrid BM25 + embedding retrieval (RRF-fused), cross-encoder rerank, and an LLM judge, then assembles a minimal context bundle for the execution model
  - Built-in ONNX prompt-injection gate scans both the raw request and every retrieved document, fail-closed — 100% detection / 0 bypasses on a 180-payload red-team corpus, 0/43 false positives on the real registry
  - MCP stdio server plus an OpenAI-compatible proxy (`:8077/v1`); one-command installer wires 18 coding agents including Claude Code, Codex, Cursor, and Windsurf
  - MIT licensed, Python 3.11; early-stage (v0.1.0, released 2026-07-06)

### Memory & Context Management

- [hjqcan/GoodMemory](https://github.com/hjqcan/GoodMemory) ![Stars](https://img.shields.io/github/stars/hjqcan/GoodMemory?style=flat-square)
  - Local-first, auditable memory layer for Claude Code, Codex, and MCP clients
  - One-command `goodmemory setup` installs managed hooks for scoped recall; governed writeback is opt-in, reviewable, and reversible
  - Uses durable SQLite by default, with Postgres support and read-only MCP inspection plus forget/export controls
  - Also exposes TypeScript, HTTP, and Python integration surfaces for product agents

- [caioribeiroclw-pixel/pluribus](https://github.com/caioribeiroclw-pixel/pluribus) ![Stars](https://img.shields.io/github/stars/caioribeiroclw-pixel/pluribus?style=flat-square)
  - Privacy-safe context receipts for Claude Code, Cursor, Codex, OpenClaw, and MCP/skill workflows
  - Proves what context crossed agent boundaries without copying private prompts or tool outputs
  - Includes an npm CLI plus copyable Context Receipts skill recipe and 60-second smoke checks
  - Focuses on audit evidence, not persistent memory or agent orchestration

- [maxbaluev/accreted-intelligence](https://github.com/maxbaluev/accreted-intelligence) ![Stars](https://img.shields.io/github/stars/maxbaluev/accreted-intelligence?style=flat-square)
  - Local-first MCP work memory for Claude Code, Codex, Cursor, and OpenCode
  - Scored retrieval, commitment tracking, and outcome-based credit help coding agents reuse lessons across sessions
  - Public installer, docs, MCP/plugin integration glue, and release artifacts; private engine binary

- [sunnja69/akephalos](https://github.com/sunnja69/akephalos) ![Stars](https://img.shields.io/github/stars/sunnja69/akephalos?style=flat-square)
  - Local-first, markdown-first `.akephalos` passport for portable agent preferences, tool notes, rules, project context, and durable memories
  - Works across Claude Code, Codex, Cursor, Hermes, OpenClaw, MCP clients, and machines
  - Sync is via plain files/Git; includes a local MCP stdio server
  - Early `v0.1.0` prerelease

- [TerminallyLazy/Tree-Ring-Memory](https://github.com/TerminallyLazy/Tree-Ring-Memory) ![Stars](https://img.shields.io/github/stars/TerminallyLazy/Tree-Ring-Memory?style=flat-square)
  - Local-first memory lifecycle framework for AI agents and coding assistants
  - Rust CLI with SQLite/FTS recall, consolidation, audit, redaction, and deletion workflows
  - Portable skill packages let Claude Code, Codex, and other SKILL.md-capable agents use the same memory guidance
  - Ships docs, tests, installer scripts, and terminal UX assets for production agent memory workflows

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) ![Stars](https://img.shields.io/github/stars/thedotmack/claude-mem?style=flat-square)
  - Automatic session capture and AI compression
  - Long-term memory with RAG integration
  - Uses Claude's agent-sdk for intelligent context injection
  - SQLite and ChromaDB for embeddings storage
  - Seamless integration with future Claude sessions

- [zilliztech/claude-context](https://github.com/zilliztech/claude-context) ![Stars](https://img.shields.io/github/stars/zilliztech/claude-context?style=flat-square)
  - Make entire codebase the context for Claude Code
  - Semantic code search MCP plugin
  - Vector database for efficient codebase storage
  - Cost-effective for large codebases
  - No multi-round discovery needed

- [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) ![Stars](https://img.shields.io/github/stars/Graphify-Labs/graphify?style=flat-square)
  - Knowledge-graph skill that ingests code, SQL schemas, R/shell scripts, docs, papers, images, and videos
  - One graph holds application code, database schema, and infrastructure side by side
  - Uses tree-sitter parsing and Leiden community detection for GraphRAG
  - Works with Claude Code, Codex, OpenCode, Cursor, and Gemini CLI

- [0xsarwagya/ontoly](https://github.com/0xsarwagya/ontoly) ![Stars](https://img.shields.io/github/stars/0xsarwagya/ontoly?style=flat-square)
  - Deterministic Software Graph for TypeScript repositories
  - Agent Skills and MCP capabilities for architecture summaries, route tracing, dependency analysis, configuration usage, and impact analysis
  - Graph-first workflow: query Ontoly evidence before broad source search
  - Works with Claude Code, Codex, and other SKILL.md-compatible coding agents

- [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) ![Stars](https://img.shields.io/github/stars/tirth8205/code-review-graph?style=flat-square)
  - Builds a persistent, incremental knowledge graph of your codebase for Claude Code
  - Claims roughly 6.8x fewer tokens on reviews and up to 49x on daily coding tasks
  - Tree-sitter static analysis exposed via MCP for graph queries
  - Python and MIT licensed; project site at code-review-graph.com

- [mksglu/context-mode](https://github.com/mksglu/context-mode) ![Stars](https://img.shields.io/github/stars/mksglu/context-mode?style=flat-square)
  - Sandboxes tool output to compress context for AI coding agents
  - Claims up to 98% context reduction across long sessions
  - Ships hooks, skills, and an MCP server for 15+ platforms (Claude Code, Codex, Cursor, Kiro, Zed, OpenClaw)
  - Project site at context-mode.com

- [gastownhall/beads](https://github.com/gastownhall/beads) ![Stars](https://img.shields.io/github/stars/gastownhall/beads?style=flat-square)
  - Memory upgrade for coding agents
  - Persists context across sessions for Claude Code and other agents
  - Go-based binary

- [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) ![Stars](https://img.shields.io/github/stars/NevaMind-AI/memU?style=flat-square)
  - Memory layer for 24/7 proactive agents like OpenClaw
  - Python-driven graph-based memory store
  - Targets long-running agent workflows

- [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) ![Stars](https://img.shields.io/github/stars/SamurAIGPT/llm-wiki-agent?style=flat-square)
  - Personal knowledge base that builds and maintains itself
  - Drop in sources and Claude (or Codex/Gemini) extracts and links knowledge
  - Python-driven

- [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) ![Stars](https://img.shields.io/github/stars/parcadei/Continuous-Claude-v3?style=flat-square)
  - Context management for Claude Code via hooks
  - Maintains state via ledgers and handoffs across sessions
  - MCP execution without context pollution

- [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) ![Stars](https://img.shields.io/github/stars/breferrari/obsidian-mind?style=flat-square)
  - Obsidian vault that gives AI coding agents persistent memory
  - Designed for Claude Code, Codex CLI, and Gemini CLI
  - TypeScript-driven

- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) ![Stars](https://img.shields.io/github/stars/DeusData/codebase-memory-mcp?style=flat-square)
  - High-performance code-intelligence MCP server
  - Indexes codebases into a persistent knowledge graph in milliseconds
  - C implementation for speed

- [agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta) ![Stars](https://img.shields.io/github/stars/agenticnotetaking/arscontexta?style=flat-square)
  - Claude Code plugin that builds individualized knowledge systems from conversation
  - You describe how you think and work; it captures and reuses that context
  - Shell-driven

- [fkiene/llmtrim](https://github.com/fkiene/llmtrim) ![Stars](https://img.shields.io/github/stars/fkiene/llmtrim?style=flat-square)
  - Local proxy that compresses each model request to cut token cost, with quality gating that reverts any step that does not save
  - Works with Claude Code via HTTPS_PROXY with no code changes
  - Trims resent tool schemas, history, MCP tool output, and scraped pages on every turn
  - Also ships an MCP server, CLI, libraries (Rust, Python, Ruby, Swift, Kotlin), and a WASM/JS npm package
  - Rust-based, MPL-2.0 licensed

- [bks-lab/open-bridge](https://github.com/bks-lab/open-bridge) ![Stars](https://img.shields.io/github/stars/bks-lab/open-bridge?style=flat-square)
  - Agent-agnostic context layer: a plain git repo of Markdown + YAML your coding agent reads at the start of every session
  - It begins each session knowing your repos, clients, and task conventions instead of restarting from zero
  - One `skills/` tree works across Claude Code, Codex, and Copilot CLI; sync is via plain files/Git
  - MIT licensed; single self-hosted instance so far — documents the method, not adoption

- [cremenescu/mem0ry4ai](https://github.com/cremenescu/mem0ry4ai) ![Stars](https://img.shields.io/github/stars/cremenescu/mem0ry4ai?style=flat-square)
  - Local-first persistent memory whose source of truth is plain markdown files versioned by git — no cloud, no DB server, no telemetry, no API keys
  - SessionStart hook injects the project-scoped slice of memory and SessionEnd captures new memories and commits them; also packaged as a Claude Code plugin
  - Built-in stdio MCP server (8 tools, including full-text search over past session transcripts) works with Claude Code, Gemini CLI, Cursor, and OpenCode
  - Hybrid SQLite FTS5 plus optional local Ollama embeddings fused with RRF, degrading to keyword search offline; secrets redacted on write and local-model proposals held in a human review queue
  - Pure Python stdlib with no pip install or third-party deps; macOS, Linux, and Windows; bilingual EN/RO web UI; GPL-2.0-or-later

- [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) ![Stars](https://img.shields.io/github/stars/supermemoryai/supermemory?style=flat-square)
  - Memory + context engine and API for AI apps and agents
  - Persistent memory across sessions and projects; can run fully locally
  - Frequently used as a Claude memory layer; TypeScript, MIT licensed

- [getzep/graphiti](https://github.com/getzep/graphiti) ![Stars](https://img.shields.io/github/stars/getzep/graphiti?style=flat-square)
  - Real-time, temporally-aware knowledge-graph framework for agent memory
  - Ships an MCP server: add/search episodes and entities backed by a Neo4j/FalkorDB graph
  - Popular long-term memory backend; Python, Apache-2.0 licensed

- [letta-ai/claude-subconscious](https://github.com/letta-ai/claude-subconscious) ![Stars](https://img.shields.io/github/stars/letta-ai/claude-subconscious?style=flat-square)
  - Background agent that watches Claude Code sessions
  - Builds memory and injects relevant context back into the session
  - From Letta AI; TypeScript, MIT licensed

### MCP Servers & Integrations

- [bekservice/Famulor-Skill](https://github.com/bekservice/Famulor-Skill/tree/main/claude-store/skills/famulor-assistants-history) ![Stars](https://img.shields.io/github/stars/bekservice/Famulor-Skill?style=flat-square)
  - Read-only Agent Skill for reviewing Famulor assistant configurations and omnichannel call, messaging, and email history
  - Uses exactly 11 list/get tools with the restricted `assistants:read` and `calls:read` OAuth scopes
  - Includes connected-channel history such as WhatsApp and Instagram when the authenticated workspace returns it

- [oraios/serena](https://github.com/oraios/serena) ![Stars](https://img.shields.io/github/stars/oraios/serena?style=flat-square)
  - Powerful coding agent toolkit with semantic capabilities
  - MCP server for retrieval and editing
  - Language server protocol integration
  - Advanced semantic code understanding

- [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) ![Stars](https://img.shields.io/github/stars/nanocoai/nanoclaw?style=flat-square)
  - Lightweight OpenClaw alternative for containers
  - Connects to WhatsApp, Telegram, Slack, Discord, Gmail
  - Built on Anthropic's Agents SDK
  - Memory and scheduled jobs support

- [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) ![Stars](https://img.shields.io/github/stars/RichardAtCT/claude-code-telegram?style=flat-square)
  - Telegram bot for remote Claude Code access
  - Chat naturally about projects from anywhere
  - Automatic session persistence per project
  - Proactive notifications from webhooks and CI/CD
  - Built-in authentication and audit logging

- [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) ![Stars](https://img.shields.io/github/stars/wonderwhy-er/DesktopCommanderMCP?style=flat-square)
  - MCP server for terminal control and file system management
  - Execute commands, search files, and diff-based editing
  - Native Excel, PDF, and DOCX support
  - Interactive process control and session management
  - Docker isolation for sandboxing

- [kubestellar/console](https://github.com/kubestellar/console) ![Stars](https://img.shields.io/github/stars/kubestellar/console?style=flat-square)
  - MCP server (`kc-agent`) bridging AI assistants to multi-cluster Kubernetes
  - Manage workloads, pods, namespaces, and RBAC across clusters via natural language
  - Built-in AI-powered dashboard with 250+ CNCF project integrations
  - Works with Claude Code, Claude Desktop, and any MCP-compatible client
  - Live demo: https://console.kubestellar.io

- [grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp) ![Stars](https://img.shields.io/github/stars/grab/cursor-talk-to-figma-mcp?style=flat-square)
  - MCP integration that lets AI agents talk to Figma
  - Supports Cursor and Claude Code for reading and editing designs
  - JavaScript-based; published by Grab's engineering team

- [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) ![Stars](https://img.shields.io/github/stars/atilaahmettaner/tradingview-mcp?style=flat-square)
  - MCP for real-time crypto and stock screening
  - Advanced technical indicators and Bollinger-band intelligence
  - Python implementation; works as a native Claude Code MCP

- [PleasePrompto/notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp) ![Stars](https://img.shields.io/github/stars/PleasePrompto/notebooklm-mcp?style=flat-square)
  - MCP server for Google NotebookLM
  - Lets agents (Claude Code, Codex) research documentation with grounded citations
  - TypeScript-driven

- [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) ![Stars](https://img.shields.io/github/stars/google-labs-code/stitch-skills?style=flat-square)
  - Library of agent skills designed to work with the Stitch MCP server
  - Follows the open Agent Skills standard
  - TypeScript-driven; published by Google Labs

- [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) ![Stars](https://img.shields.io/github/stars/chenhg5/cc-connect?style=flat-square)
  - Bridges local AI coding agents to messaging platforms
  - Supports Claude Code, Cursor, Gemini CLI, and Codex
  - Targets Feishu/Lark, DingTalk, Slack, Telegram, and Discord
  - Go-based runtime

- [op7418/Claude-to-IM-skill](https://github.com/op7418/Claude-to-IM-skill) ![Stars](https://img.shields.io/github/stars/op7418/Claude-to-IM-skill?style=flat-square)
  - Bridges Claude Code and Codex to IM platforms
  - Chat with AI coding agents from Telegram, Discord, or Feishu/Lark
  - TypeScript implementation

- [eze-is/web-access](https://github.com/eze-is/web-access) ![Stars](https://img.shields.io/github/stars/eze-is/web-access?style=flat-square)
  - Adds full internet access to Claude Code via a layered skill
  - Three-tier channel scheduling, browser CDP, and parallel divide-and-conquer
  - JavaScript-driven

- [officialzeroxyz/zero-plugins](https://github.com/officialzeroxyz/zero-plugins) ![Stars](https://img.shields.io/github/stars/officialzeroxyz/zero-plugins?style=flat-square)
  - Claude Code plugin (zero@zero-plugins) that gives your AI access to thousands of tools, APIs and services to use and pay for per use
  - No config, no API keys; services are discovered and paid for at runtime
  - Also ships a CLI (@zeroxyz/cli) and an MCP connector (mcp.zero.xyz)
  - Homepage: https://zero.xyz

- [skillselion/skillselion-mcp](https://github.com/skillselion/skillselion-mcp) ![Stars](https://img.shields.io/github/stars/skillselion/skillselion-mcp?style=flat)
  - MCP server for the [Skillselion](https://skillselion.com) catalog of community-vetted Claude Code skills, MCP servers & marketplaces
  - `load_skill` fetches a real SKILL.md (plus bundled scripts/refs) mid-task, ranked by real install counts + GitHub stars
  - Also indexes MCP servers and plugin marketplaces
  - `npx -y skillselion-mcp`; TypeScript

- [getformo/cli](https://github.com/getformo/cli/tree/main/skills/formo-analytics) ![Stars](https://img.shields.io/github/stars/getformo/cli?style=flat-square)
  - Official agent skill for [Formo](https://formo.so) product and onchain analytics
  - Queries KPIs, SQL, funnels, retention, revenue, users, and wallet profiles
  - Supports MCP, CLI, and REST workflows
  - Read-only analytics operations with project-scoped authentication

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=flat-square)
  - Official Anthropic reference collection of MCP servers
  - Bundles Filesystem, Git, Fetch, Memory, Sequential Thinking, and Time
  - The canonical starting point for the MCP ecosystem; TypeScript and Python

- [upstash/context7](https://github.com/upstash/context7) ![Stars](https://img.shields.io/github/stars/upstash/context7?style=flat-square)
  - Pulls up-to-date, version-specific library docs and code examples into the model
  - Exposes `resolve-library-id` and `get-library-docs`; runs remotely or via npx
  - A near-ubiquitous "must-have" Claude Code MCP; TypeScript, MIT licensed

- [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) ![Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=flat-square)
  - Official Chrome DevTools MCP server for real-browser control and debugging
  - Performance tracing, network/console inspection, and DOM/page automation
  - Maintained by the Google Chrome DevTools team; Apache-2.0 licensed

- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) ![Stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=flat-square)
  - Microsoft's official browser-automation MCP server built on Playwright
  - Drives pages via the structured accessibility tree, not screenshots
  - De facto standard for end-to-end testing and web automation; Apache-2.0 licensed

- [github/github-mcp-server](https://github.com/github/github-mcp-server) ![Stars](https://img.shields.io/github/stars/github/github-mcp-server?style=flat-square)
  - GitHub's official MCP server for repos, issues, PRs, and Actions
  - Offered as a hosted remote server and a local Go binary
  - Supports OAuth and PAT auth; MIT licensed

- [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) ![Stars](https://img.shields.io/github/stars/GLips/Figma-Context-MCP?style=flat-square)
  - Framelink MCP server that feeds Figma layout and design data to coding agents
  - Fetches a file/node's layout, styles, and component structure for accurate UI code
  - Widely used for design-to-code; TypeScript, MIT licensed

- [awslabs/mcp](https://github.com/awslabs/mcp) ![Stars](https://img.shields.io/github/stars/awslabs/mcp?style=flat-square)
  - AWS's official open-source suite of MCP servers for AWS services
  - Includes servers for docs, CDK, Cost Explorer, Bedrock Knowledge Bases, and DynamoDB
  - Installable per-service; Python, Apache-2.0 licensed

- [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) ![Stars](https://img.shields.io/github/stars/firecrawl/firecrawl-mcp-server?style=flat-square)
  - Official Firecrawl MCP server for web scraping, crawling, and search
  - Scrape/crawl/map/search tools return clean, LLM-ready markdown
  - Works hosted (API key) or self-hosted; MIT licensed

- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) ![Stars](https://img.shields.io/github/stars/sooperset/mcp-atlassian?style=flat-square)
  - Most popular MCP server for Atlassian Jira and Confluence
  - Create/search/update issues and read/write Confluence pages
  - Supports Cloud and Server/Data Center; distributed via Docker and uvx

- [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) ![Stars](https://img.shields.io/github/stars/makenotion/notion-mcp-server?style=flat-square)
  - Notion's official MCP server for reading and writing workspace content
  - Query databases and create/update pages and blocks via the Notion API
  - Supports a hosted remote endpoint and local stdio deployment

### API & Integration Tools

- [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) ![Stars](https://img.shields.io/github/stars/router-for-me/CLIProxyAPI?style=flat-square)
  - Wrap multiple AI CLIs as OpenAI-compatible API
  - Support for Gemini CLI, Claude Code, ChatGPT Codex, Qwen Code
  - Access free models through standardized API interface
  - Built with Go for performance

- [madhavajay/alex](https://github.com/madhavajay/alex) ![Stars](https://img.shields.io/github/stars/madhavajay/alex?style=flat-square)
  - Local Rust LLM proxy with an optional UI for Claude Code and other coding agents
  - Routes provider subscriptions and API keys through compatible endpoints
  - Captures requests, costs, sessions, and supported tool execution locally
  - Adds scriptable middleware, subscription bonding, failover, and messenger-assisted re-authentication

- [1rgs/claude-code-proxy](https://github.com/1rgs/claude-code-proxy) ![Stars](https://img.shields.io/github/stars/1rgs/claude-code-proxy?style=flat-square)
  - Run Claude Code on OpenAI and Gemini models
  - Anthropic API proxy for multiple model providers
  - Powered by LiteLLM for model routing
  - Transparent proxy with custom model mapping
  - Use any Anthropic client with alternative models

- [sozercan/vekil](https://github.com/sozercan/vekil) ![Stars](https://img.shields.io/github/stars/sozercan/vekil?style=flat-square)
  - Go reverse proxy exposing Anthropic, Gemini, and OpenAI-compatible APIs behind one local endpoint
  - Multi-provider routing across GitHub Copilot, Azure OpenAI, and OpenAI Codex
  - Zero-config Copilot mode plus JSON/YAML provider configs for explicit routing
  - macOS/Linux menubar tray app and distroless container
  - MIT licensed, single static Go binary, no frameworks

- [runapi-ai/cli-skill](https://github.com/runapi-ai/cli-skill) ![Stars](https://img.shields.io/github/stars/runapi-ai/cli-skill?style=flat-square)
  - Agent skill for generating AI images, videos, and music/audio from Claude Code and compatible SKILL.md agents
  - Also covers JSON-first requests, async polling, and other model API jobs through the RunAPI CLI
  - JSON-first requests, async task polling, and terminal/CI-friendly workflows
  - Apache-2.0 licensed; install with `git clone https://github.com/runapi-ai/cli-skill ~/.claude/skills/runapi-cli`

### CLI Configuration Tools

- [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) ![Stars](https://img.shields.io/github/stars/davila7/claude-code-templates?style=flat-square)
  - CLI tool for configuring and monitoring Claude Code
  - Template management system
  - Configuration automation
  - Python-based for easy customization

- [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) ![Stars](https://img.shields.io/github/stars/musistudio/claude-code-router?style=flat-square)
  - Use Claude Code as foundation for coding infrastructure
  - Route requests to different models based on needs
  - Multi-provider support (OpenRouter, DeepSeek, Ollama, Gemini)
  - Dynamic model switching with /model command
  - GitHub Actions integration

- [MohamedAbdallah-14/unslop](https://github.com/MohamedAbdallah-14/unslop) ![Stars](https://img.shields.io/github/stars/MohamedAbdallah-14/unslop?style=flat-square)
  - CLI and MCP server that removes AI writing patterns from text
  - Strips tricolons, em-dash overuse, sycophancy openers, and overused vocabulary
  - Works with Claude Code, Codex, Gemini CLI, and Cursor via PostToolUse hooks
  - Five intensity levels plus a lint-only audit mode

- [UfoMiao/zcf](https://github.com/UfoMiao/zcf) ![Stars](https://img.shields.io/github/stars/UfoMiao/zcf?style=flat-square)
  - Zero-Config Code Flow for Claude Code and Codex
  - TypeScript-driven configuration wrapper

- [ainova-systems/intelligence-sync](https://github.com/ainova-systems/intelligence-sync) ![Stars](https://img.shields.io/github/stars/ainova-systems/intelligence-sync?style=flat-square)
  - One source of truth for AI coding rules across every IDE
  - Author rules, agents, and skills once in plain Markdown
  - Routes them into each tool's native formats (Claude Code, Cursor, GitHub Copilot, Codex, AGENTS.md)
  - Zero-dependency, bash and awk, MIT licensed

### Autonomous Development

- [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code) ![Stars](https://img.shields.io/github/stars/frankbria/ralph-claude-code?style=flat-square)
  - Autonomous AI development loop with intelligent exit detection
  - Continuous development cycles until project completion
  - Built-in safeguards to prevent infinite loops
  - Rate limiting and circuit breaker protection
  - Global command available in any directory

- [evalstate/fast-agent](https://github.com/evalstate/fast-agent) ![Stars](https://img.shields.io/github/stars/evalstate/fast-agent?style=flat-square)
  - Build and evaluate agents with model, Skills, MCP, and ACP support
  - Python-based research-grade harness
  - Designed for fast agent-iteration cycles

### Monitoring & Observability

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) ![Stars](https://img.shields.io/github/stars/disler/claude-code-hooks-multi-agent-observability?style=flat-square)
  - Real-time agent monitoring
  - Hook event tracking with SQLite dashboard
  - Visual tool event indicators

- [Maciek-roboblog/Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) ![Stars](https://img.shields.io/github/stars/Maciek-roboblog/Claude-Code-Usage-Monitor?style=flat-square)
  - Real-time terminal monitoring for token usage
  - Machine learning-based predictions and analytics
  - Burn rate tracking and cost analysis
  - Rich UI with intelligent session limit warnings
  - Track consumption across different Claude plans

- [steipete/CodexBar](https://github.com/steipete/CodexBar) ![Stars](https://img.shields.io/github/stars/steipete/CodexBar?style=flat-square)
  - macOS menu bar app for usage stats
  - Track Codex, Claude, Cursor, Gemini, and more
  - Session and weekly limits visibility
  - Reset timer for each provider
  - Minimal UI with dynamic bar icons

- [luoyuctl/agenttrace](https://github.com/luoyuctl/agenttrace) ![Stars](https://img.shields.io/github/stars/luoyuctl/agenttrace?style=flat-square)
  - Local-first TUI observability for AI coding agent sessions
  - Supports Claude Code, Codex CLI, Gemini CLI, Aider, Cursor exports, Hermes, OpenCode, Kimi, and Copilot-style logs
  - Tracks cost, tokens, tool failures, latency, anomalies, health, diffs, and CI gates
  - Exports JSON, Markdown, and self-contained HTML reports
  - Ships as a single Go binary with Homebrew and one-line installer support

- [Necmttn/ax](https://github.com/Necmttn/ax) ![Stars](https://img.shields.io/github/stars/Necmttn/ax?style=flat-square)
  - Local-first telemetry and memory graph for AI coding agents
  - Ingests Claude Code, Codex, Pi, OpenCode, Cursor, and installed skills
  - Exposes session search, cost analytics, skill usage, workflow evidence, dashboard, and MCP queries

- [Yuyz0112/claude-code-reverse](https://github.com/Yuyz0112/claude-code-reverse) ![Stars](https://img.shields.io/github/stars/Yuyz0112/claude-code-reverse?style=flat-square)
  - Visualize Claude Code's LLM interactions
  - Runtime behavior and API data analysis
  - Interactive log visualization tool
  - Understand core agent workflow and architecture
  - Context compaction and task/sub-agent analysis

- [jakemarsh/ccthread](https://github.com/jakemarsh/ccthread) ![Stars](https://img.shields.io/github/stars/jakemarsh/ccthread?style=flat-square)
  - Read, search, and have Claude summarize your Claude Code conversation logs from the CLI
  - Reads session `.jsonl` files from `~/.claude/projects/` and renders clean markdown
  - Cross-project keyword search with `find` and `search` commands
  - `current` keyword resolves the session you're in right now (`--before-last-compact` supported)
  - Ships as both a Claude Code plugin and a standalone binary

- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square)
  - Claude Code plugin that surfaces context usage, active tools, running agents, and todo progress
  - Statusline-style HUD that updates while the agent works
  - TypeScript implementation; MIT licensed

- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) ![Stars](https://img.shields.io/github/stars/sirmalloc/ccstatusline?style=flat-square)
  - Customizable statusline for the Claude Code CLI
  - Powerline support, themes, and rich layouts
  - TypeScript-driven

- [getagentseal/codeburn](https://github.com/getagentseal/codeburn) ![Stars](https://img.shields.io/github/stars/getagentseal/codeburn?style=flat-square)
  - Interactive TUI dashboard for token-cost observability
  - Shows where Claude Code, Codex, and Cursor tokens go
  - TypeScript-driven

- [hamed-elfayome/Claude-Usage-Tracker](https://github.com/hamed-elfayome/Claude-Usage-Tracker) ![Stars](https://img.shields.io/github/stars/hamed-elfayome/Claude-Usage-Tracker?style=flat-square)
  - Native macOS menu-bar app for tracking Claude AI usage limits in real time
  - Built with Swift and SwiftUI

- [matt1398/claude-devtools](https://github.com/matt1398/claude-devtools) ![Stars](https://img.shields.io/github/stars/matt1398/claude-devtools?style=flat-square)
  - DevTools-style inspector for Claude Code
  - Session logs, tool calls, token usage, sub-agents, and context window
  - TypeScript-driven

- [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) ![Stars](https://img.shields.io/github/stars/junhoyeo/tokscale?style=flat-square)
  - CLI for tracking token usage across OpenCode, Claude Code, OpenClaw, Codex, Gemini, and Cursor
  - Single Rust binary

- [backnotprop/plannotator](https://github.com/backnotprop/plannotator) ![Stars](https://img.shields.io/github/stars/backnotprop/plannotator?style=flat-square)
  - Annotate and review coding-agent plans and diffs visually
  - Share with your team; send feedback to agents with one click
  - TypeScript-driven

- [PeonPing/peon-ping](https://github.com/PeonPing/peon-ping) ![Stars](https://img.shields.io/github/stars/PeonPing/peon-ping?style=flat-square)
  - Warcraft III Peon voice notifications for Claude Code, Codex, and other agents
  - Shell-driven; stops you from babysitting the terminal

- [ZeframLou/call-me](https://github.com/ZeframLou/call-me) ![Stars](https://img.shields.io/github/stars/ZeframLou/call-me?style=flat-square)
  - Minimal plugin that lets Claude Code call you on the phone
  - TypeScript-based
  - Useful for long-running autonomous runs

- [eltonylfgi-blip/claude-session-triage](https://github.com/eltonylfgi-blip/claude-session-triage) ![Stars](https://img.shields.io/github/stars/eltonylfgi-blip/claude-session-triage?style=flat-square)
  - Local-first CLI and Claude Code plugin that finds idle sessions and surfaces what each was waiting on
  - Ranks pending decisions ahead of active work and scheduled routines; reads local JSONL with no network calls
  - Zero dependencies, MIT licensed, with a 10-check synthetic self-test

- [ccusage/ccusage](https://github.com/ccusage/ccusage) ![Stars](https://img.shields.io/github/stars/ccusage/ccusage?style=flat-square)
  - `npx ccusage` CLI that parses local Claude Code JSONL logs
  - Reports token usage and cost by day, month, session, and model
  - The most-referenced usage/cost tool in the community; Rust, very actively maintained

### Configuration & Templates

- [abhishekray07/claude-md-templates](https://github.com/abhishekray07/claude-md-templates) ![Stars](https://img.shields.io/github/stars/abhishekray07/claude-md-templates?style=flat-square)
  - CLAUDE.md best practices and templates
  - Global, project, and local configurations
  - Framework-specific templates (Next.js, Python/FastAPI)

- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) ![Stars](https://img.shields.io/github/stars/shanraisshan/claude-code-best-practice?style=flat-square)
  - Comprehensive best practices guide
  - Prompting, planning, and agent strategies
  - Commands, skills, hooks, and workflows

- [sneg55/agent-starter](https://github.com/sneg55/agent-starter) ![Stars](https://img.shields.io/github/stars/sneg55/agent-starter?style=flat-square)
  - Skills, hooks, templates, and engineering guides for AI-agent-friendly projects
  - `/new-project` scaffolding and `/adopt-project` for existing repos
  - AI-tuned lint rules, hooks reference, and a per-project self-improvement loop

- [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) ![Stars](https://img.shields.io/github/stars/centminmod/my-claude-code-setup?style=flat-square)
  - Shared starter configuration and CLAUDE.md "memory bank" system
  - Bundles hooks and subagents; frequently forked as a reference setup
  - Python, MIT licensed

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

- [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) ![Stars](https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat-square)
  - Claude Code skill that rewrites prompts and responses in compressed caveman-style language
  - Claims roughly 65% token reduction by stripping function words and filler
  - JavaScript implementation; MIT licensed
  - Project site at getcaveman.dev

- [AutomateLab-tech/publishing-skills](https://github.com/AutomateLab-tech/publishing-skills) ![Stars](https://img.shields.io/github/stars/AutomateLab-tech/publishing-skills?style=flat-square)
  - Four composable skills for end-to-end SEO blog publishing
  - Topic research, writing pipeline, SVG figures, editorial calendar
  - Platform-agnostic: Ghost, WordPress, or any static site
  - MIT-0 licensed; installs into Claude Code, Cursor, Codex, and 50+ runtimes

---

## Learning & Documentation

Resources for mastering Claude skills and understanding best practices.

### Learning & Tutoring Skills

- [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) ![Stars](https://img.shields.io/github/stars/Li-Evan/Bloom?style=flat-square)
  - One-on-one Socratic tutor skill based on Benjamin Bloom's "2 Sigma" research
  - Writes a syllabus, then teaches one lesson at a time, adapting each next lesson to your inline written feedback
  - The opposite of "dump the full answer" — guides you to derive it yourself
  - Responds in Chinese; skill at `skills/bloom-tutor`

### Comprehensive Guides

- [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) ![Stars](https://img.shields.io/github/stars/FlorianBruniaux/claude-code-ultimate-guide?style=flat-square)
  - 22,000+ lines of documentation
  - Beginner to power user progression
  - 225 templates and 41 diagrams
  - 271 quiz questions for learning validation

- [zebbern/claude-code-guide](https://github.com/zebbern/claude-code-guide) ![Stars](https://img.shields.io/github/stars/zebbern/claude-code-guide?style=flat-square)
  - Complete guide from beginner to power user
  - Setup, commands, workflows, agents, and skills
  - Comprehensive MCP integration documentation
  - Hooks system, security, and troubleshooting
  - Tips, tricks, and best practices

- [Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide) ![Stars](https://img.shields.io/github/stars/Cranot/claude-code-guide?style=flat-square)
  - Complete CLI guide auto-updated every 2 days
  - Official docs, releases, and changelog integration
  - Skills, hooks, MCP, sub-agents, and plugins
  - Tool synergies and workflow examples
  - Optimized for both humans and AI agents

- [rosmur/claudecode-best-practices](https://github.com/rosmur/claudecode-best-practices) ![Stars](https://img.shields.io/github/stars/rosmur/claudecode-best-practices?style=flat-square)
  - Evidence-based practices with 58 citations
  - Hooks, skills, and automation scripts
  - Task queue management with claude-loop

- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) ![Stars](https://img.shields.io/github/stars/shareAI-lab/learn-claude-code?style=flat-square)
  - "Bash is all you need" philosophy
  - Build a Claude-like agent harness from scratch
  - 12 progressive learning sessions

- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) ![Stars](https://img.shields.io/github/stars/Piebald-AI/claude-code-system-prompts?style=flat-square)
  - Complete collection of Claude Code's system prompts
  - 18 builtin tool descriptions and sub-agent prompts
  - Updated within minutes of each Claude Code release
  - Includes changelog across 136+ versions
  - Essential for understanding Claude Code internals

- [diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) ![Stars](https://img.shields.io/github/stars/diet103/claude-code-infrastructure-showcase?style=flat-square)
  - Production-tested infrastructure patterns
  - Auto-activating skills via hooks
  - Modular skill pattern with 500-line rule
  - Specialized agents for complex tasks
  - 6 months of iteration, 15-30 min to integrate

- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) ![Stars](https://img.shields.io/github/stars/ykdojo/claude-code-tips?style=flat-square)
  - 45 tips from basics to advanced techniques
  - Custom status line script and system prompt optimization
  - Voice input, container workflows, multi-model orchestration
  - Includes dx plugin for enhanced developer experience
  - Practical strategies for daily Claude Code usage

- [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) ![Stars](https://img.shields.io/github/stars/ChrisWiles/claude-code-showcase?style=flat-square)
  - Comprehensive project configuration example
  - Hooks, skills, agents, and commands setup
  - GitHub Actions workflows for automation
  - Best practices and anti-patterns guide
  - Complete directory structure reference

- [OneRedOak/claude-code-workflows](https://github.com/OneRedOak/claude-code-workflows) ![Stars](https://img.shields.io/github/stars/OneRedOak/claude-code-workflows?style=flat-square)
  - Production workflows from AI-native startup
  - Code review, security review, and design review workflows
  - Battle-tested configurations since Claude Code launch
  - Video tutorials and demos available
  - Real-world applied learnings

- [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) ![Stars](https://img.shields.io/github/stars/disler/claude-code-hooks-mastery?style=flat-square)
  - Master Claude Code hooks for deterministic control
  - Complete hook lifecycle and payload documentation
  - Sub-agents, meta-agents, and team-based validation
  - Flow control, error codes, and security implementations
  - Custom status lines and output styles

- [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) ![Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat-square)
  - Visual, example-driven guide to Claude Code
  - Progresses from basic concepts to advanced agent patterns
  - Ships copy-paste templates for immediate use
  - Hosted at luongnv.com/claude-howto; MIT licensed

- [Windy3f3f3f3f/how-claude-code-works](https://github.com/Windy3f3f3f3f/how-claude-code-works) ![Stars](https://img.shields.io/github/stars/Windy3f3f3f3f/how-claude-code-works?style=flat-square)
  - Deep dive into Claude Code internals
  - Covers architecture, the agent loop, and context engineering
  - Bilingual English/Chinese write-up

- [lintsinghua/claude-code-book](https://github.com/lintsinghua/claude-code-book) ![Stars](https://img.shields.io/github/stars/lintsinghua/claude-code-book?style=flat-square)
  - Long-form analysis of Claude Code's agent-harness skeleton
  - In-depth architectural breakdown, structured as a book
  - Chinese-language

- [KimYx0207/AI-Coding-Guide-Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh) ![Stars](https://img.shields.io/github/stars/KimYx0207/AI-Coding-Guide-Zh?style=flat-square)
  - Chinese tutorial covering Claude Code, OpenClaw, and Codex
  - 36 complete tutorials, three learning paths from beginner to enterprise
  - Markdown-only bundle

- [jamesmurdza/awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools) ![Stars](https://img.shields.io/github/stars/jamesmurdza/awesome-ai-devtools?style=flat-square)
  - Curated list of AI-powered developer tools
  - Useful adjacent reading when shopping for Claude Code integrations

- [Meirtz/Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) ![Stars](https://img.shields.io/github/stars/Meirtz/Awesome-Context-Engineering?style=flat-square)
  - Comprehensive survey on context engineering
  - From prompt engineering to production-grade AI systems
  - Hundreds of papers and frameworks referenced

- [KhazP/vibe-coding-prompt-template](https://github.com/KhazP/vibe-coding-prompt-template) ![Stars](https://img.shields.io/github/stars/KhazP/vibe-coding-prompt-template?style=flat-square)
  - Templates and workflow for generating PRDs, tech designs, and MVPs
  - Designed for use with AI IDEs and Claude Code
  - Markdown-only bundle

---

- [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) ![Stars](https://img.shields.io/github/stars/anthropics/prompt-eng-interactive-tutorial?style=flat-square)
  - Anthropic's official interactive prompt-engineering course
  - Hands-on Jupyter notebooks from basics to advanced techniques
  - First-party learning resource

- [anthropics/courses](https://github.com/anthropics/courses) ![Stars](https://img.shields.io/github/stars/anthropics/courses?style=flat-square)
  - Anthropic's official educational course collection
  - Covers the API, prompt engineering, evaluations, and tool use
  - First-party, broadly cited learning material

- [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs) ![Stars](https://img.shields.io/github/stars/ericbuess/claude-code-docs?style=flat-square)
  - Local, auto-updating mirror of the official Claude Code documentation
  - Exposed through a `/docs` command for fast, offline lookup
  - Shell-based; actively maintained

## Skill Development

Tools and frameworks for creating your own Claude skills.

- [alirezarezvani/claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) ![Stars](https://img.shields.io/github/stars/alirezarezvani/claude-code-skill-factory?style=flat-square)
  - Complete toolkit for building production-ready skills
  - Deployment automation
  - Best practices and templates
  - Scale from prototype to production

- [agentskills/agentskills](https://github.com/agentskills/agentskills) ![Stars](https://img.shields.io/github/stars/agentskills/agentskills?style=flat-square)
  - Open specification, documentation, and reference SDK for Agent Skills
  - Defines the `SKILL.md` format used across Claude Code and compatible agents
  - Maintained by Anthropic with community contributions
  - Apache 2.0 licensed (code) and CC-BY-4.0 (docs); companion site at agentskills.io

- [numman-ali/openskills](https://github.com/numman-ali/openskills) ![Stars](https://img.shields.io/github/stars/numman-ali/openskills?style=flat-square)
  - Universal `SKILL.md` loader installable via `npm i -g openskills`
  - Brings Anthropic's skills system to Claude Code, Cursor, Windsurf, Aider, Codex, and any tool that reads `AGENTS.md`
  - Project-local installs default to `./.claude/skills`; `--global` writes to `~/.claude/skills`
  - Supports private git repos and local paths

- [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) ![Stars](https://img.shields.io/github/stars/yusufkaraaslan/Skill_Seekers?style=flat-square)
  - Converts documentation sites, GitHub repositories, and PDFs into Claude AI skills
  - Automatic conflict detection between overlapping skill definitions
  - AST parsing, OCR for PDFs, and web scraping pipelines
  - MIT licensed; hosted version at skillseekersweb.com

- [refly-ai/refly](https://github.com/refly-ai/refly) ![Stars](https://img.shields.io/github/stars/refly-ai/refly?style=flat-square)
  - Open-source agent-skills builder
  - Define skills by workflow and run on Claude Code, Cursor, Codex, and others
  - TypeScript-driven

- [microsoft/apm](https://github.com/microsoft/apm) ![Stars](https://img.shields.io/github/stars/microsoft/apm?style=flat-square)
  - Microsoft's Agent Package Manager
  - Distributes agent skills, MCP servers, and custom agents
  - Python-driven

- [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) ![Stars](https://img.shields.io/github/stars/tech-leads-club/agent-skills?style=flat-square)
  - Secure, validated skill registry for professional AI coding agents
  - Extends Antigravity, Claude Code, Cursor, and Copilot
  - TypeScript-driven

- [gotalab/cc-sdd](https://github.com/gotalab/cc-sdd) ![Stars](https://img.shields.io/github/stars/gotalab/cc-sdd?style=flat-square)
  - Spec-driven development harness for Claude Code
  - Turns approved specs into long-running autonomous implementation
  - TypeScript-driven, minimal and adaptable

---

## Contributing

We welcome contributions! To add a skill or tool to this list:

1. Ensure the project is actively maintained
2. Verify it provides clear documentation
3. Check that it offers real value to Claude users
4. Submit a pull request with a clear description

**Quality over quantity** - we prioritize well-documented, production-ready skills over experimental projects.

---

## License

CC0 - Public Domain

This curated list is maintained by the community for the community.
