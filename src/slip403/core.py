import time
import requests
from termcolor import colored
from urllib.parse import urljoin
from .config import modifiers, headersList, userAgent
from .utils import hashBody, setupBaseline
from .output import logResult, saveResponse


baselineHash = None
baselineSize = None

def printResult(url, status, size, changed):
    color = (
        "green" if status.startswith("2")
        else "yellow" if status.startswith("3")
        else "red"
    )
    flag = colored("✓", "cyan") if changed else " "
    print(f"{colored(status, color)} | {size} bytes | {flag} {url}")

def sendRequest(baseUrl, path, method, header, delay, outputFile, saveResponses, compareBaseline, hashResponses):
    global baselineHash, baselineSize

    fullPath = path if path.startswith("/") else "/" + path
    fullUrl = urljoin(baseUrl, fullPath)
    headers = {"User-Agent": userAgent}
    if header:
        headers.update(header)

    try:
        response = requests.request(method, fullUrl, headers=headers, verify=False, allow_redirects=True)
        statusCode = str(response.status_code)
        bodySize = len(response.content)
        bodyHash = hashBody(response.content) if hashResponses else None

        headerName = next(iter(header), "None") if header else "None"
        changed = True

        if compareBaseline and statusCode == "200":
            changed = (bodySize != baselineSize) or (bodyHash != baselineHash)

        printResult(fullUrl, statusCode, bodySize, changed)

        if saveResponses and statusCode == "200" and changed:
            saveResponse(response.content, path, method, headerName)

        logResult(fullUrl, method, headerName, statusCode, bodySize, outputFile)
        time.sleep(delay)

    except requests.RequestException as error:
        print(colored(f"[!] Error: {error}", "red"))

def runBypassScan(baseUrl, basePath, delay, methods, outputFile, saveResponses, compareBaseline, hashResponses):
    from os import makedirs
    from csv import writer

    with open(outputFile, "w", newline="") as file:
        writer(file).writerow(["URL", "Method", "Header", "Status", "Size"])

    if compareBaseline:
        global baselineHash, baselineSize
        baselineHash, baselineSize = setupBaseline(baseUrl, basePath, hashResponses)

    for modifier in modifiers:
        pathVariant = f"{basePath}{modifier}"
        for method in methods:
            for header in headersList:
                sendRequest(baseUrl, pathVariant, method, header, delay, outputFile, saveResponses, compareBaseline, hashResponses)