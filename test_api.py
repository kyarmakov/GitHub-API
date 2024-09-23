import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USER_NAME")
repo_name = os.getenv("REPO_NAME")
api_token = os.getenv("API_TOKEN")


def create_repository(repo, token):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "name": f"{repo}"
    }
    requests.post(url, headers=headers, json=data)


def get_repositories(user):
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    return response.json()


def delete_repository(user, repo, token):
    url = f"https://api.github.com/repos/{user}/{repo}"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    requests.delete(url, headers=headers)


def check_if_repo_exists(repos):
    repo_names = []
    for repo in repos:
        repo_names.append(repo["name"])

    if repo_name not in repo_names:
        pytest.fail(f"\"{repo_name}\" repository has not been created.")


def test_run():
    create_repository(repo=repo_name, token=api_token)
    repos = get_repositories(username)
    check_if_repo_exists(repos)
    delete_repository(user=username, repo=repo_name, token=api_token)
