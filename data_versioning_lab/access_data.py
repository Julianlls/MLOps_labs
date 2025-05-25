# Get url from DVC
import pandas as pd
import dvc.api
import git

path='data_versioning_lab/wine_original.csv'
repo='/Users/julianlilas/desktop/mlops/mlops_labs/'

repo_git = git.Repo(repo)∂
tags = [tag.name for tag in repo_git.tags]

print("Available versions:")
for tag in tags:
    print(tags)

version = input("Version wanted:")

data_url = dvc.api.get_url(
  path=path,
  repo=repo,
  rev = version
  )

data = pd.read_csv(data_url, sep=";")
print(data)
