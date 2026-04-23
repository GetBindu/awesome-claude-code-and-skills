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

from youtube_agent.__version__ import __version__
from youtube_agent.main import (
    handler,
    initialize_agent,
    main,
)

__all__ = [
    "__version__",
    "handler",
    "initialize_agent",
    "main",
]
