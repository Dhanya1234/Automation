# download_sharepoint.py
import os
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential

site_url = os.getenv("SHAREPOINT_SITE_URL")        # e.g. https://yourcompany.sharepoint.com/sites/SiteName
client_id = os.getenv("SHAREPOINT_CLIENT_ID")
client_secret = os.getenv("SHAREPOINT_CLIENT_SECRET")
file_relative_url = os.getenv("SHAREPOINT_FILE_URL")  # e.g. /sites/SiteName/Shared Documents/Folder/MyFile.xlsx
local_path = os.getenv("LOCAL_SAVE_PATH")             # e.g. C:\\Users\\YourName\\Downloads\\MyFile.xlsx

if not all([site_url, client_id, client_secret, file_relative_url, local_path]):
    raise SystemExit("Missing one or more required environment variables (see README).")

ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))
file = ctx.web.get_file_by_server_relative_url(file_relative_url)
with open(local_path, "wb") as f:
    file.download(f).execute_query()

print("File downloaded successfully to:", local_path)
