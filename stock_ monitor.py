import os
import json
import urllib.request
from datetime import datetime, timezone

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")

def send_discord(message):
    if not WEBHOOK_URL:
        raise RuntimeError("DISCORD_WEBHOOK_URL is not configured")

    data = json.dumps({
        "content": message
    }).encode("utf-8")

    request = urllib.request.Request(
        WEBHOOK_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        return response.status


def main():
    now = datetime.now(timezone.utc).strftime(
        "%Y-%m-%d %H:%M UTC"
    )

    message = (
        "📱 iPhone Duo 在庫監視システム\n"
        f"動作確認: {now}\n"
        "対象: スターホワイト\n"
        "優先: 256GB / 512GB\n"
        "代替: 1TB\n"
        "価格条件: Apple公式定価以下\n"
        "状態: 通知テスト（在庫未確認）"
    )

    status = send_discord(message)
    print(f"Discord notification: {status}")


if __name__ == "__main__":
    main()
