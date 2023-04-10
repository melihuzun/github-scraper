import requests
import time
from dotenv import load_dotenv
import os
load_dotenv()

token = os.environ.get("GITHUB_TOKEN")

username=input("username:")
repo_name=input("reponame:")
keyword=input("keyword:")

github_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
Headers = { "Authorization" :"Bearer "+ token}

data = requests.get(github_url, headers=Headers)

for i in data.json():
    commit_url=i["url"]
    commit=requests.get(commit_url,headers=Headers)
    commit_data=commit.json()
    for j in commit_data["files"]:
        try:
            if keyword in j["patch"]:
                print(j["patch"]) 
            else:
                pass
        except KeyError:
            pass
    print("------------------------------")
    time.sleep(0.5)