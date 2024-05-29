import os

api_folders = [x[0] for x in os.walk("./api")]
client_folders = [x[0] for x in os.walk("./client")]


files = {}

for folder in [*api_folders, *client_folders]:
    if "migrations" in folder:
        continue
    if "templates" in folder:
        continue
    if "git" in folder:
        continue
    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        if "__init__" in file or os.path.isdir(filepath):
            continue
        if "sqlite" in file:
            continue
        if "git" in file:
            continue

        with open(filepath, "r") as f:
            files[filepath] = f.read()

report = """"""

for i, filepath in enumerate(files):
    report += f"\n{i}. {filepath}\n\n{files[filepath]}\n"

with open("report.txt", "w+") as f:
    f.write(report)