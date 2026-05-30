import os

webhook_url = os.getenv("hT0B72ANNZAA/B0B7YS098SC/Jw2CpfaN1CjQS7DIS0rna41y")

message = {
    "text": "⚠ Server Health Alert"
}

requests.post(webhook_url, json=message)