import os
import csv

def saveResponse(content, path, method, headerName):
    os.makedirs("responses", exist_ok=True)
    safePath = path.replace("/", "_")
    filename = f"responses/{safePath}__{method}__{headerName}.txt"
    with open(filename, "wb") as f:
        f.write(content)

def logResult(url, method, header, status, size, outputFile):
    with open(outputFile, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([url, method, header, status, size])
