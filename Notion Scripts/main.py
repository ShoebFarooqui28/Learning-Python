from notion_client import Client
from datetime import datetime

# Initialize Notion client
notion = Client(auth="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")

# Database ID
dateBaseID = "14bb212b193c8093992fd53d23cd347c"

# Get today's date in the format YYYY-MM-DD
today = datetime.now().strftime("%Y-%m-%d")

# Query the database to fetch all pages
response = notion.databases.query(database_id=dateBaseID)

# Check if a page exists for today's date based on the title
today_page_found = False
for page in response["results"]:
    title = page["properties"]["Name"]["title"][0]["plain_text"]
    
    # Compare the title with today's date
    if title == today:
        today_page_found = True
        page_id = page["id"]
        print(f"Today's Page Found! Page ID: {page_id}")
        break

if not today_page_found:
    print("No Page Found for Today")
    

page_url = f"https://www.notion.so/{page_id}"
print(f"Open today's page here: {page_url}")

