import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USER_NAME")
repo_name = os.getenv("REPO_NAME")
api_token = os.getenv("API_TOKEN")


def create_repository():
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    data = {
        "name": f"{repo_name}"
    }
    requests.post(url, headers=headers, json=data)


def get_repositories():
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    return response.json()


def delete_repository():
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {
        "Authorization": f"Bearer {api_token}",
    }
    requests.delete(url, headers=headers)


def check_if_repo_exists(repos):
    repo_names = []
    for repo in repos:
        repo_names.append(repo["name"])

    if repo_name not in repo_names:
        pytest.fail(f"\"{repo_name}\" repository has not been created.")


def test_run():
    create_repository()
    repos = get_repositories()
    check_if_repo_exists(repos)
    delete_repository()
