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

from competitor_analysis_agent.__version__ import __version__
from competitor_analysis_agent.main import (
    handler,
    initialize_agent,
    initialize_all,
    initialize_mcp_tools,
    main,
)

__all__ = [
    "__version__",
    "handler",
    "initialize_agent",
    "initialize_all",
    "initialize_mcp_tools",
    "main",
]
