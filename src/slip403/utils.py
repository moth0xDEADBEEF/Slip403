import hashlib
import requests
from .config import userAgent

def hashBody(content):
    return hashlib.sha256(content).hexdigest()

def setupBaseline(baseUrl, basePath, hashResponses):
    url = baseUrl.rstrip("/") + "/" + basePath.lstrip("/")
    headers = {"User-Agent": userAgent}
    try:
        response = requests.get(url, headers=headers, verify=False, allow_redirects=True)
        content = response.content
        baselineSize = len(content)
        baselineHash = hashBody(content) if hashResponses else None
        print(f"Baseline status: {response.status_code} | {baselineSize} bytes")
        return baselineHash, baselineSize
    except requests.RequestException as e:
        print(f"[!] Failed to fetch baseline: {e}")
        return None, None