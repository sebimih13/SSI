import hashlib
import requests
import json


def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def check_virustotal(api_key, file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {
        "x-apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        result = response.json()

        if "data" in result and "attributes" in result["data"]:
            attributes = result["data"]["attributes"]
            if "last_analysis_stats" in attributes:
                stats = attributes["last_analysis_stats"]
                return stats.get("malicious", 0) + stats.get("suspicious", 0)

        print("No detection information found in the VirusTotal response.")
        return 0

    except requests.exceptions.RequestException as e:
        print(f"VirusTotal API Request Error: {e}")
        return None


file_path = "SSI L8 - Introducere in inginerie inversa.pdf"
api_key = "fbca19394046bdc5f09b40b637dff2cbe56090812df7febddd95e4becb7fa931"

file_hash = calculate_sha256(file_path)
print(f"File SHA256: {file_hash}")

detection_count = check_virustotal(api_key, file_hash)
if detection_count is not None:
    print(f"The number of antivirus engines that detect the file: {detection_count}")

