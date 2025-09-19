import requests
import typer

app = typer.Typer()

def format_event(event):
    event_type = event.get('type', '')
    repo_name = event.get('repo', {}).get('name', 'unknown repo')
    payload = event.get('payload', {})

    if event_type == 'PushEvent':
        commit_count = len(payload.get('commits', []))
        return f"- Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {repo_name}"

    elif event_type == 'IssuesEvent':
        action = payload.get('action', 'performed action on')
        issue = payload.get('issue', {})
        title = issue.get('title', 'an issue')
        return f"- {action.capitalize()} an issue \"{title}\" in {repo_name}"

    elif event_type == 'PullRequestEvent':
        action = payload.get('action', 'performed action on')
        pr = payload.get('pull_request', {})
        title = pr.get('title', 'a pull request')
        return f"- {action.capitalize()} a pull request \"{title}\" in {repo_name}"

    elif event_type == 'WatchEvent':
        action = payload.get('action', 'starred')
        return f"- {action.capitalize()} {repo_name}"

    elif event_type == 'ForkEvent':
        forkee = payload.get('forkee', {})
        forked_repo = forkee.get('full_name', '')
        return f"- Forked {repo_name} to {forked_repo}"

    else:
        return f"- {event_type} in {repo_name}"


@app.command()
def get_events(username: str):
    """
    Fetch and display recent GitHub events for the specified username.
    """
    url = f'https://api.github.com/users/{username}/events'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            events = response.json()
            for event in events:
                typer.echo(format_event(event))
        else:
            typer.echo(f"Error fetching events: {response.status_code}")
    except requests.exceptions.RequestException as e:
        typer.echo(f"Request failed: {e}")

if __name__ == "__main__":
    app()
