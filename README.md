# GitHub User Activity CLI
project page:

https://roadmap.sh/projects/github-user-activity

https://roadmap.sh/projects/task-tracker

A simple command-line interface (CLI) tool built with Python and Typer to fetch and neatly display recent public GitHub events of any user.

## Features

- Fetches public events from GitHub's API
- Formats and summarizes various event types like Pushes, Issues, Pull Requests, Stars, and Forks
- Provides a clean and human-readable output
- Easy to use and extend with Typer framework

## Installation
1. Clone this repository or download the script.

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install requests typer
   ```

## Usage
Run the CLI tool with the GitHub username as an argument:

```bash
python script.py <github-username>
```

## Code Overview

- Uses `requests` to call GitHub's public API for user events.
- Processes JSON responses and identifies event types.
- Outputs concise text summaries for events.
- Built using [Typer](https://typer.tiangolo.com/) for easy CLI development.

## Extending
You can add support for more GitHub event types or enhance output formatting by editing the `format_event` function.
