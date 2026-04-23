# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""youtube-agent - An Bindu Agent that analyzes YouTube videos.

"""

import argparse
import asyncio
import json
import os
from pathlib import Path
from textwrap import dedent
from typing import Any

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.openrouter import OpenRouter
from agno.tools.youtube import YouTubeTools

from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Global agent instance
agent: Agent | None = None
openai_api_key: str | None = None
openrouter_api_key: str | None = None
_initialized = False
_init_lock = asyncio.Lock()


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Get path to agent_config.json in project root
    config_path = Path(__file__).parent / "agent_config.json"

    with open(config_path, "r") as f:
        return json.load(f)


def initialize_agent() -> None:
    """Initialize the agent."""
    global agent, openai_api_key, openrouter_api_key

    # Determine which model to use based on available keys
    if openai_api_key:
        model = OpenAIChat(id="gpt-4o")
        model_info = "OpenAI GPT-4o"
    elif openrouter_api_key:
        model = OpenRouter(id="openai/gpt-4o")
        model_info = "OpenRouter (OpenAI GPT-4o)"
    else:
        # Boot without error, but agent will fail when tools are actually used
        model = OpenAIChat(id="gpt-4o")
        model_info = "OpenAI GPT-4o (key required at runtime)"

    agent = Agent(
        name="YouTube Agent",
        model=model,
        tools=[YouTubeTools()],
        instructions=dedent("""\
            You are an expert YouTube content analyst with a keen eye for detail! 🎓
            Follow these steps for comprehensive video analysis:
            1. Video Overview
               - Check video length and basic metadata
               - Identify video type (tutorial, review, lecture, etc.)
               - Note the content structure
            2. Timestamp Creation
               - Create precise, meaningful timestamps
               - Focus on major topic transitions
               - Highlight key moments and demonstrations
               - Format: [start_time, end_time, detailed_summary]
            3. Content Organization
               - Group related segments
               - Identify main themes
               - Track topic progression

            Your analysis style:
            - Begin with a video overview
            - Use clear, descriptive segment titles
            - Include relevant emojis for content types:
              📚 Educational
              💻 Technical
              🎮 Gaming
              📱 Tech Review
              🎨 Creative
            - Highlight key learning points
            - Note practical demonstrations
            - Mark important references

            Quality Guidelines:
            - Verify timestamp accuracy
            - Avoid timestamp hallucination
            - Ensure comprehensive coverage
            - Maintain consistent detail level
            - Focus on valuable content markers
        """),
        add_datetime_to_context=True,
        markdown=True,
    )
    print(f"✅ Agent initialized (model: {model_info})")


async def run_agent(message: str) -> Any:
    """Run the agent with the given message.

    Args:
        message: User message to process

    Returns:
        Agent response
    """
    global agent

    # Run the agent and get response
    response = agent.run(message, stream=True)
    return response


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys
                  e.g., [{"role": "user", "content": "..."}]

    Returns:
        Agent response (ManifestWorker will handle extraction)
    """
    global _initialized

    # Lazy initialization on first call (in bindufy's event loop)
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing YouTube Agent...")
            initialize_agent()
            _initialized = True

    # Extract user message from messages list
    user_message = next(
        (msg["content"] for msg in messages if msg.get("role") == "user"),
        "Analyze this YouTube video",
    )

    # Run the agent
    result = await run_agent(user_message)
    return result


def main():
    """Main entry point for the YouTube Agent."""
    global openai_api_key, openrouter_api_key

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="YouTube Agent")
    parser.add_argument(
        "--openai-key",
        type=str,
        default=os.getenv("OPENAI_API_KEY"),
        help="OpenAI API key (env: OPENAI_API_KEY)",
    )
    parser.add_argument(
        "--openrouter-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    args = parser.parse_args()

    # Set global API keys
    openai_api_key = args.openai_key
    openrouter_api_key = args.openrouter_key

    # Log which keys are available (but don't require them)
    if openai_api_key:
        print("🤖 OPENAI_API_KEY loaded")
    if openrouter_api_key:
        print("🤖 OPENROUTER_API_KEY loaded")
    if not openai_api_key and not openrouter_api_key:
        print("⚠️  No API keys provided. Agent will boot but require keys at runtime.")
        print("   Provide via: docker run -e OPENAI_API_KEY=xxx ... or -e OPENROUTER_API_KEY=xxx ...")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        # Note: Agent will be initialized lazily on first request
        print("🚀 Starting YouTube Agent server...")
        bindufy(config, handler)
    except KeyboardInterrupt:
        print("\n🧹 Shutting down...")


# Entry point
if __name__ == "__main__":
    main()
