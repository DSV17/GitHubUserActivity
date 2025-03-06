import argparse
import requests
from datetime import datetime

def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    
    if response.status_code == 200:
        events = response.json()
        for event in events:
            event_type = event['type']
            repo_name = event['repo']['name']
            created_at = event['created_at']
            date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
            
            if event_type == 'PushEvent':
                commits = event['payload']['commits']
                commit_messages = [commit['message'] for commit in commits]
                print(f"{date} - Pushed {len(commits)} commits to {repo_name}")
                for message in commit_messages:
                    print(f"  - {message}")
            
            elif event_type == 'IssuesEvent':
                action = event['payload']['action']
                issue_title = event['payload']['issue']['title']
                print(f"{date} - {action.capitalize()} an issue in {repo_name}: {issue_title}")
            
            elif event_type == 'WatchEvent':
                print(f"{date} - Starred {repo_name}")
            
    else:
        print(f"Failed to fetch data for user {username}. Status code: {response.status_code}")

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub user activity.")
    parser.add_argument('username', type=str, help="GitHub username to fetch activity for")

    args = parser.parse_args()
    get_github_activity(args.username)

if __name__ == "__main__":
    main()