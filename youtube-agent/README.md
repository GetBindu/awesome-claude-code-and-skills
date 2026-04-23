<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">youtube-agent</h1>
<h3 align="center">an AI agent that analyzes YouTube videos and creates structured summaries with accurate timestamps. This agent extracts key insights from video content, making it easy to navigate educational videos, tutorials, and presentations without watching them in full.</h3>

<p align="center">
  <strong>an AI agent that analyzes YouTube videos and creates structured summaries with accurate timestamps. This agent extracts key insights from video content, making it easy to navigate educational videos, tutorials, and presentations without watching them in full.</strong><br/>
  an AI agent that analyzes YouTube videos and creates structured summaries with accurate timestamps. This agent extracts key insights from video content, making it easy to navigate educational videos, tutorials, and presentations without watching them in full.
</p>

<p align="center">
  <a href="https://github.com/lsvishaal/youtube-agent/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/lsvishaal/youtube-agent/main.yml?branch=main" alt="Build status">
  </a>
  <a href="https://codecov.io/gh/lsvishaal/youtube-agent">
    <img src="https://codecov.io/gh/lsvishaal/youtube-agent/branch/main/graph/badge.svg" alt="codecov">
  </a>
  <a href="https://img.shields.io/github/license/lsvishaal/youtube-agent">
    <img src="https://img.shields.io/github/license/lsvishaal/youtube-agent" alt="License">
  </a>
</p>

---

## 💡 Why This Exists

**Stop endless scrolling.** This AI agent understands what you *actually* want:

**Perfect for:** an AI agent that analyzes YouTube videos and creates structured summaries with accurate timestamps. This agent extracts key insights from video content, making it easy to navigate educational videos, tutorials, and presentations without watching them in full.

---

> **🌐 Join the Internet of Agents**  
> Register your agent at [bindus.directory](https://bindus.directory) to make it discoverable worldwide and enable agent-to-agent collaboration. **It takes 2 minutes and unlocks the full potential of your agent.**

---

## 📚 Quick Links

- 📖 **[Full Documentation](https://lsvishaal.github.io/youtube-agent/)**
- 💻 **[GitHub Repository](https://github.com/lsvishaal/youtube-agent/)**
- 🐛 **[Report Issues](https://github.com/lsvishaal/youtube-agent/issues)**
- 💬 **[Join Discord](https://discord.gg/3w5zuYUuwt)**
- 🌐 **[Agent Directory](https://bindus.directory)**

<br/>

## ⚡ Quick Start - Deploy to bindus.directory in 5 Minutes

This guide will help you deploy your agent to [bindus.directory](https://bindus.directory) where it becomes discoverable worldwide and can collaborate with other agents. **GitHub Actions will automatically build, containerize, and register your agent.**

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (fast Python package installer)
- [GitHub CLI](https://cli.github.com/) (`gh`)
- GitHub account
- Docker Hub account (free)

---

### 1️⃣ Local Setup & Configuration

```bash
# Clone and setup the project
cd youtube-agent
uv venv --python 3.12.9
source .venv/bin/activate
uv sync

# Configure API keys
cp .env.example .env
```

Edit `.env` and add your keys:

| Key | Get It From | Free Tier? |
|-----|-------------|------------|
| `OPENROUTER_API_KEY` | [OpenRouter](https://openrouter.ai/keys) | ✅ Yes |
| `MEM0_API_KEY` | [Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys) | ✅ Yes |

---

### 2️⃣ Setup GitHub Authentication

Authenticate with GitHub CLI:

```bash
# Check if you're already logged in
gh auth status

# If not logged in, authenticate with GitHub
gh auth login
```

Follow the prompts:
1. Select **GitHub.com**
2. Choose **SSH** as your preferred protocol
3. Authenticate via your browser or token

---

### 3️⃣ Create GitHub Repository

# Initialize git repository and commit your code
git init -b main
git add .
git commit -m "Initial commit"

# Create repository on GitHub and push (replace with your GitHub username)
gh repo create lsvishaal/youtube-agent --public --source=. --remote=origin --push
```

**Alternative: Manual creation**
1. Create repository at https://github.com/new
2. Don't initialize with README (you already have one)
3. Then run:
```bash
git remote add origin https://github.com/lsvishaal/youtube-agent.git
git push -u origin main

---

### 4️⃣ Register on bindus.directory

1. **Login** to [bindus.directory](https://bindus.directory)
2. **Grab your API key** from the dashboard
3. **Get Docker Hub token** from [Docker Hub Security Settings](https://hub.docker.com/settings/security)

---

### 5️⃣ Configure GitHub Secrets for Auto-Deployment

Set up secrets so GitHub Actions can automatically deploy your agent:

![GitHub Secrets Setup](../assets/git_secret.png)

```bash
gh secret set BINDU_API_TOKEN --body "<your-bindus-api-key>"
gh secret set DOCKERHUB_TOKEN --body "<your-dockerhub-token>"
```

---

### 6️⃣ Deploy! 🚀

**Push to trigger automatic deployment:**

```bash
git push origin main
```

**What happens automatically:**
1. ✅ GitHub Actions builds your agent
2. ✅ Creates a Docker container
3. ✅ Pushes to Docker Hub
4. ✅ Registers on bindus.directory
5. ✅ Your agent is now live and discoverable!

**That's it!** 🎉 Your agent is now part of the Internet of Agents.

---

## 💡 Usage Examples

Try these queries:

```python
# Natural language search
an AI agent that analyzes YouTube videos and creates structured summaries with accurate timestamps. This agent extracts key insights from video content, making it easy to navigate educational videos, tutorials, and presentations without watching them in full.
```

---

## 🛠️ Development Setup

### Running Tests

```bash
make test              # Run all tests
make test-cov          # With coverage report
```

### Code Quality

```bash
make format            # Format code
make lint              # Run linters
make check             # Format + lint + test
```

### Pre-commit Hooks

Fix formatting issues before committing:

```bash
uv run pre-commit run -a
```

---

## 🐳 Docker Deployment

### Local Docker

```bash
# Build and run
docker-compose up --build

# Production mode
docker-compose -f docker-compose.prod.yml up
```

### Docker Hub Auto-Deploy

Enable automatic Docker image publishing:

1. Go to **Settings → Secrets → Actions**
2. Add secret: `DOCKERHUB_TOKEN` (get from [Docker Hub](https://hub.docker.com/settings/security))
3. Push to `main` → Image auto-builds and publishes 🚀

---

## 🏗️ Project Structure

```
youtube-agent/
├── youtube_agent/    # Main agent code
│   ├── skills/             # Agent capabilities
│   │   └── youtube_agent/ # youtube-agent skill
│   └── __init__.py
├── tests/                  # Test suite
├── docs/                   # Documentation
├── .env.example            # Environment template
├── docker-compose.yml      # Docker setup
└── pyproject.toml          # Dependencies
```


<br/>

## 🌟 Contributing

We love contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

**Built with [Bindu Agent Framework](https://github.com/getbindu/bindu)**

- 🌐 **A2A, AP2, X402 protocols** for Internet of Agents communication
- ⚡ **Zero-config setup** - from idea to production in minutes
- 🛠️ **Production-ready** out of the box

### Want to Build Your Own Agent?

```bash
# Create a new agent in 2 minutes
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong>
</p>

<p align="center">
  <a href="https://github.com/lsvishaal/youtube-agent">⭐ Star this repo</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://docs.getbindu.com">📚 Bindu Docs</a>
</p>

<p align="center">
  <em>From idea to Internet of Agents in minutes. 🌻🚀✨</em>
</p>
