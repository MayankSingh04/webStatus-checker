import requests
import time
import os

# List of websites to monitor from an environment variable, or a default list
websites_to_check = os.environ.get("WEBSITES", "https://google.com,https://github.com").split(',')

def check_websites():
    html_output = "<html><head><title>Website Status</title><meta http-equiv='refresh' content='60'></head><body><h1>Website Status</h1>"

    for url in websites_to_check:
        try:
            response = requests.get(url.strip(), timeout=5)
            if 200 <= response.status_code < 300:
                html_output += f"<p>{url.strip()} is <b><font color='green'>UP</font></b></p>"
            else:
                html_output += f"<p>{url.strip()} is <b><font color='red'>DOWN</font></b> (Status Code: {response.status_code})</p>"
        except requests.ConnectionError:
            html_output += f"<p>{url.strip()} is <b><font color='red'>DOWN</font></b> (Connection Error)</p>"

    html_output += f"<hr>Last checked: {time.ctime()}</body></html>"

    with open("/app/html/index.html", "w") as file:
        file.write(html_output)

if __name__ == "__main__":
    # Create the directory for the html file if it doesn't exist
    os.makedirs("/app/html", exist_ok=True)
    while True:
        check_websites()
        time.sleep(60)