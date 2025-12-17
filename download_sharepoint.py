# download_sharepoint.py (NO Azure App)
import os
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

site_url = os.getenv("SHAREPOINT_SITE_URL")
username = os.getenv("SHAREPOINT_USERNAME")
password = os.getenv("SHAREPOINT_PASSWORD")
file_relative_url = os.getenv("SHAREPOINT_FILE_URL")
local_path = os.getenv("LOCAL_SAVE_PATH")

if not all([site_url, username, password, file_relative_url, local_path]):
    raise SystemExit("Missing required environment variables")

ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
file = ctx.web.get_file_by_server_relative_url(file_relative_url)

with open(local_path, "wb") as f:
    file.download(f).execute_query()

print("File downloaded successfully to:", local_path)
