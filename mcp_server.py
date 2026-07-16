from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Spotify Music MCP Server")

# Attaches the functions from these tools to the MCP server
from tools import spotify_tools
from tools import history_tools
from resources import spotify_resources
from prompts import spotify_prompts