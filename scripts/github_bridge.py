import os
import requests
import json

class GitHubBridge:
    def __init__(self):
        self.backend_url = "http://localhost:8000/webhook/github"
        self.github_token = os.environ.get("GH_TOKEN")
        self.repo = "SolFoundry/solfoundry"

    def simulate_pr_event(self, pr_number, title, author):
        """Giả lập một sự kiện PR để test hệ thống Review kiếm tiền."""
        payload = {
            "action": "opened",
            "pull_request": {
                "number": pr_number,
                "title": title,
                "user": {"login": author},
                "html_url": f"https://github.com/{self.repo}/pull/{pr_number}"
            }
        }
        print(f"🚀 Gửi tín hiệu PR #{pr_number} tới Backend...")
        try:
            resp = requests.post(self.backend_url, json=payload)
            print(f"✅ Phản hồi từ Backend: {resp.json()}")
        except Exception as e:
            print(f"❌ Lỗi kết nối Backend: {e}")

if __name__ == "__main__":
    # Test thực tế: Giả lập PR cho Bounty #29
    bridge = GitHubBridge()
    bridge.simulate_pr_event(
        pr_number=29, 
        title="Implement FastAPI Backend and Anchor Logic", 
        author="Gemini-Sovereign-Agent"
    )
