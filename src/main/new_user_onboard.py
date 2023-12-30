import json
import os

from requests.auth import HTTPBasicAuth

from src.main import issue


# invite user
def get_absolute_directory_path(folder_name):
    current_dir = os.path.abspath(__file__)
    while not os.path.exists(os.path.join(current_dir, folder_name)):
        current_dir = os.path.dirname(current_dir)
    return os.path.join(current_dir, folder_name)


def load_json_data_from_fp(fp: str) -> list:
    return json.load(open(fp))


def get_all_objects_in_dir(fp: str) -> list:
    file_paths = []
    for root, _, files in os.walk(fp):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


def get_all_json_file_data() -> list:
    # the absolute path to the JIRA issue JSON templates
    all_json_fps = get_all_objects_in_dir(
        f"{get_absolute_directory_path('AutoJIRA')}/src/templates"
    )
    # get json files
    return [load_json_data_from_fp(fp) for fp in all_json_fps if os.path.getsize(fp) > 0]


def get_auth():
    return HTTPBasicAuth(
        json.load(
            open(f'{get_absolute_directory_path("AutoJIRA")}/resources/jira-credentials.json')
        )['jira_auth_email'],
        json.load(
            open(f'{get_absolute_directory_path("AutoJIRA")}/resources/jira-credentials.json')
        )['jira_api_key']
    )


def get_url():
    return json.load(
        open(f'{get_absolute_directory_path("AutoJIRA")}/resources/jira-credentials.json')
    )['jira_url']


if __name__ == "__main__":
    # create team for a cohort
    # when user accepts invitation to a team - load issues - S1E1, S1E2(closing bugs, subtasks), S1E3()
    issues = get_all_json_file_data()

    [
        issue.create_issue(
            get_url(),
            {"Content-Type": "application/json"},
            get_auth(),
            story
        )
        for story in issues
    ]

    # for each issue create GitHub actions test to test issue completed correctly
    # 1.) JIRA updated correctly
    # 2.) Test pass in GitHub actions (expect test with name 'my/test/pattern' created)
    # 3.) Passes in GitHub branch protection
    # 4.) Reopen story with JIRA comment attached if fails

