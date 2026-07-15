# Spotify MCP Server

An AI-powered Spotify analytics server built using the Model Context Protocol (MCP). This project allows Claude Desktop to securely interact with Spotify listening history, synchronize data into SQL Server, and answer questions using custom MCP tools.

## Features

- Fetch top Spotify artists
- Retrieve recently played songs
- Synchronize listening history into SQL Server
- Analyze listening history using SQL queries
- Ask Claude questions about your listening habits
- Fully Dockerized deployment

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
| played_at | DATETIME2 |

Unique Constraint

```
(track_id, played_at)
```

Prevents duplicate listening events.

---

## Example Questions for Claude

- Who are my most played artists?
- What have I listened to recently?
- Which artist appears most often in my listening history?
- Sync my latest Spotify listening history.
- Summarize my listening habits.