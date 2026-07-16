# Spotify MCP Server

An AI-powered Spotify analytics server built with the Model Context Protocol (MCP).

This project allows Claude Desktop to interact with personal Spotify listening data through custom MCP tools. 

It automatically synchronizes listening history into SQL Server, enables querying and analysis of listening patterns, and provides natural language insights through Claude.

## Features

- Fetch Spotify top artists
- Retrieve recently played tracks
- Automatically synchronize listening history into SQL Server
- Prevent duplicate listening events
- Query listening history through MCP tools
- Analyze listening patterns using SQL queries
- Ask Claude natural language questions about listening habits
- Fully containerized with Docker

---

## Tech Stack

- Python
- FastMCP
- Spotify Web API
- SQL Server
- pyodbc
- Docker
- Claude Desktop
- Model Context Protocol (MCP)

---

## Architecture

```
                Claude Desktop
                       │
             MCP (stdio protocol)
                       │
                       ▼
          Spotify MCP Server (Docker)
                       │
                 Spotify API
                       │
                       ▼
                 SQL Server (Docker)
                       │
                       ▼
              ListeningHistory Table
```

### Data Flow

1. Claude sends a request through MCP.
2. The Spotify MCP Server executes the requested tool.
3. Spotify data is retrieved or queried from SQL Server.
4. Results are returned to Claude for analysis.

A background scheduler periodically synchronizes recently played tracks from Spotify into the database.

---


## MCP Tools

### fetch_top_artists_from_spotify()

Retrieves a user's top Spotify artists.

---

### fetch_recently_played_from_spotify()

Retrieves recently played songs directly from Spotify.

---

### sync_recently_played()

Synchronizes Spotify listening history into SQL Server while preventing duplicate listening events.

---

### get_listening_history()

Returns historical listening events stored locally.

---

### get_most_played_artists()

Aggregates listening history and returns the user's most played artists.

---

## Database Schema

ListeningHistory

| Column | Type |
|---------|------|
| id | INT |
| track_id | NVARCHAR |
| track_name | NVARCHAR |
| album_name | NVARCHAR |
| artist_id | NVARCHAR |
| artist_name | NVARCHAR |
| played_at | DATETIMEOFFSET |

Unique Constraint

```
(track_id, played_at)
```

Prevents duplicate listening events.

---

## Background Scheduler

The project includes a long-running worker that periodically synchronizes Spotify listening history.

Example workflow:
```
                    Scheduler
                        |
                        ▼
              sync_recently_played()
                        |
                        ▼
                    Spotify API
                        |
                        ▼
                    SQL Server
```
The scheduler runs as a Docker service and automatically restarts if stopped.

## Running Locally

Build and start services: `docker compose up --build`

### Services

spotify-sync-scheduler
spotify-sqlserver

The MCP server can then be connected to Claude Desktop through the MCP configuration.

---

## Example Questions for Claude

- Who are my most played artists?
- What have I listened to recently?
- Which artist appears most often in my listening history?
- Sync my latest Spotify listening history.
- Summarize my listening habits.