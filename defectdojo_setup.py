
import requests
import os

DD_URL = os.environ["DEFECTDOJO_URL"]
DD_TOKEN = os.environ["DEFECTDOJO_TOKEN"]
PRODUCT_NAME = os.environ["PRODUCT_NAME"]
ENGAGEMENT_NAME = os.environ["ENGAGEMENT_NAME"]

headers = {"Authorization": f"Token {DD_TOKEN}"}

# --------------- PRODUCT ----------------
product_search = requests.get(
    f"{DD_URL}/api/v2/products/?name={PRODUCT_NAME}",
    headers=headers
).json()

if product_search["count"] > 0:
    product_id = product_search["results"][0]["id"]
else:
    create = requests.post(
        f"{DD_URL}/api/v2/products/",
        headers=headers,
        json={"name": PRODUCT_NAME, "description": "Auto CI/CD Product"}
    ).json()
    product_id = create["id"]

# --------------- ENGAGEMENT ----------------
engagement_search = requests.get(
    f"{DD_URL}/api/v2/engagements/?name={ENGAGEMENT_NAME}&product={product_id}",
    headers=headers
).json()

if engagement_search["count"] > 0:
    engagement_id = engagement_search["results"][0]["id"]
else:
    create = requests.post(
        f"{DD_URL}/api/v2/engagements/",
        headers=headers,
        json={
            "name": ENGAGEMENT_NAME,
            "product": product_id,
            "status": "In Progress",
            "engagement_type": "CI/CD"
        }
    ).json()
    engagement_id = create["id"]

print(f"export PRODUCT_ID={product_id}")
print(f"export ENGAGEMENT_ID={engagement_id}")
