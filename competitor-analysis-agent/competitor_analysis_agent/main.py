# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""competitor-analysis-agent - An Bindu Agent.

"""

import argparse
import asyncio
import json
import os
from pathlib import Path
from textwrap import dedent
from typing import Any


from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MultiMCPTools
from agno.tools.mem0 import Mem0Tools


from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Global MCP tools instances
mcp_tools: MultiMCPTools | None = None
agent: Agent | None = None
model_name: str | None = None
api_key: str | None = None
mem0_api_key: str | None = None
_initialized = False
_init_lock = asyncio.Lock()


async def initialize_mcp_tools(env: dict[str, str] | None = None) -> None:
    """Initialize and connect to MCP servers.

    Args:
        env: Environment variables dict for MCP servers (e.g., API keys)
    """
    global mcp_tools

    # Initialize MultiMCPTools with all MCP server commands
    # TODO: Add your MCP server commands here
    mcp_tools = MultiMCPTools(
        commands=[
            "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt",
            "npx -y @modelcontextprotocol/server-google-maps",
        ],
        env=env or os.environ,  # Use provided env or fall back to os.environ
        allow_partial_failure=True,  # Don't fail if one server is unavailable
        timeout_seconds=30,
    )

    # Connect to all MCP servers
    await mcp_tools.connect()
    print("✅ Connected to MCP servers")


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Get path to agent_config.json in project root
    config_path = Path(__file__).parent / "agent_config.json"

    with open(config_path, "r") as f:
        return json.load(f)


# Create the agent instance
async def initialize_agent() -> None:
    """Initialize the agent once."""
    global agent, model_name, mcp_tools

    agent = Agent(
        name=f"competitor-analysis-agent Bindu Agent",
        model=OpenRouter(id=model_name),
        tools=[mcp_tools, Mem0Tools(api_key=mem0_api_key)],  # MultiMCPTools instance
        instructions=dedent("""\
            You are a helpful AI assistant with access to multiple capabilities including:
            - Airbnb search for accommodations and listings
            - Google Maps for location information and directions

            Your capabilities:
            - Search for Airbnb listings based on location, dates, and guest requirements
            - Provide detailed information about available properties
            - Access Google Maps data for location information and directions
            - Help users find the best accommodations for their needs

            Always:
            - Be clear and concise in your responses
            - Provide relevant details about listings and locations
            - Ask for clarification if needed
            - Format responses in a user-friendly way
        """),
        add_datetime_to_context=True,
        markdown=True,
    )
    print("✅ Agent initialized")


async def cleanup_mcp_tools()-> None:
    """Close all MCP server connections."""
    global mcp_tools

    if mcp_tools:
        try:
            await mcp_tools.close()
            print("🔌 Disconnected from MCP servers")
        except Exception as e:
            print(f"⚠️  Error closing MCP tools: {e}")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys

    Returns:
        Agent response
    """
    global agent

    # Run the agent and get response
    response = await agent.arun(messages)
    return response




async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys
                  e.g., [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]

    Returns:
        Agent response (ManifestWorker will handle extraction)
    """
    
    # Run agent with messages
    global _initialized

    # Lazy initialization on first call (in bindufy's event loop)
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing MCP tools and agent...")
            # Build environment with API keys
            env = {
                **os.environ,
                #"GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY", ""),
            }
            await initialize_all(env)
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result
    


async def initialize_all(env: dict = None):
    """Initialize MCP tools and agent.

    Args:
        env: Environment variables dict for MCP servers
    """
    await initialize_mcp_tools(env)
    await initialize_agent()


def main():
    """Main entry point for the Airbnb Travel Agent."""
    global model_name, api_key, mem0_api_key

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Bindu Agent with MCP Tools")
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-5-mini"),
        help="Model ID to use (default: openai/gpt-5-mini, env: MODEL_NAME), if you want you can use any free model: https://openrouter.ai/models?q=free",
    )

    parser.add_argument(
        "--api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--mem0-api-key",
        type=str,
        default=os.getenv("MEM0_API_KEY"),
        help="Mem0 API key (env: MEM0_API_KEY)",
    )
    args = parser.parse_args()

    # Set global model name and API keys
    model_name = args.model
    api_key = args.api_key
    mem0_api_key = args.mem0_api_key

    if not api_key:
        print("⚠️  OPENROUTER_API_KEY not set. LLM functionality will be disabled until you provide it.")
    if not mem0_api_key:
        print("ℹ️  MEM0_API_KEY not set. Mem0 memory will be disabled.")

    print(f"🤖 Using model: {model_name}")
    print("🧠 Mem0 memory enabled")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        # Note: MCP tools and agent will be initialized lazily on first request
        print("🚀 Starting Bindu agent server...")
        bindufy(config, handler)
    finally:
        # Cleanup on exit
        print("\n🧹 Cleaning up...")
        asyncio.run(cleanup_mcp_tools())


# Bindufy and start the agent server
if __name__ == "__main__":
    main()
