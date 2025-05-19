import os
import sys
import argparse
from github import Github, GithubException
from git import Repo, GitCommandError

def parse_args():
    parser = argparse.ArgumentParser(description="Create and push to GitHub repo.")
    parser.add_argument("--repo-name", required=True, help="Name of GitHub repo to create")
    parser.add_argument("--local-dir", required=True, help="Local directory path")
    parser.add_argument("--commit-message", default="Initial commit", help="Commit message")
    parser.add_argument("--private", action="store_true", help="Create private repo")
    return parser.parse_args()

def create_github_repo(github_token, repo_name, private):
    g = Github(github_token)
    try:
        user = g.get_user()
        print(f"Authenticated as {user.login}")
        repo = user.create_repo(name=repo_name, private=private)
        print(f"Created repository: {repo.clone_url}")
        return repo.clone_url
    except GithubException as e:
        print(f"GitHub error: {e}")
        sys.exit(1)

def init_local_repo(local_dir):
    if not os.path.isdir(local_dir):
        print(f"Directory {local_dir} does not exist. Creating...")
        os.makedirs(local_dir)
    if not os.path.isdir(os.path.join(local_dir, ".git")):
        print(f"Initializing git repository in {local_dir}")
        return Repo.init(local_dir)
    print(f"Using existing git repository at {local_dir}")
    return Repo(local_dir)

def commit_and_push(repo, remote_url, commit_message):
    try:
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        if 'origin' not in [r.name for r in repo.remotes]:
            repo.create_remote('origin', remote_url)
        print("Pushing to remote...")
        repo.remote('origin').push(refspec='HEAD:main')
        print("Push complete.")
    except GitCommandError as e:
        print(f"Git error: {e}")
        sys.exit(1)

def main():
    args = parse_args()
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN env var not set.")
        sys.exit(1)

    remote_url = create_github_repo(token, args.repo_name, args.private)
    repo = init_local_repo(args.local_dir)
    commit_and_push(repo, remote_url, args.commit_message)

if __name__ == "__main__":
    main()