#!/usr/bin/env python3
import os
import json
import requests
import google.generativeai as genai
from datetime import datetime

def get_diff():
    # Giả lập hoặc đọc diff từ môi trường CI
    diff_path = "/tmp/pr_diff.txt"
    if os.path.exists(diff_path):
        with open(diff_path, "r") as f:
            diff = f.read()
    else:
        diff = "No diff available for local test."
    
    if len(diff) > 30000:
        diff = diff[:30000] + "\n\n... [diff truncated]"
    return diff

def run_review(diff: str, pr_title: str, pr_body: str) -> dict:
    # Cấu hình Gemini (Miễn phí) theo Mandate
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""You are a senior code reviewer for SolFoundry, an AI software factory on Solana.
Review this pull request diff. Respond in EXACT JSON format.

PR Title: {pr_title}
PR Description: {pr_body}

Evaluate: Code Quality, Correctness, Security, Completeness, Tests (all 1-10).
Verdict: APPROVE, REQUEST_CHANGES, or REJECT.

DIFF:
{diff}

JSON Response Format:
{{
  "quality_score": 7,
  "quality_note": "...",
  "correctness_score": 8,
  "correctness_note": "...",
  "security_score": 9,
  "security_note": "...",
  "completeness_score": 6,
  "completeness_note": "...",
  "tests_score": 3,
  "tests_note": "...",
  "overall_score": 6.6,
  "verdict": "REQUEST_CHANGES",
  "summary": "...",
  "issues": [],
  "suggestions": []
}}"""

    response = model.generate_content(prompt, generation_config={"response_mime_type": "application/json"})
    return json.loads(response.text)

def send_telegram(review: dict):
    bot_token = "8578781014:AAF_QVtny3nAXDVOYpBEw4bGBKC20-BGKGM"
    chat_id = "6021048216"
    
    verdict_emoji = {"APPROVE": "✅", "REQUEST_CHANGES": "⚠️", "REJECT": "❌"}
    emoji = verdict_emoji.get(review["verdict"], "❓")

    msg = f"""<b>🤖 CƠ CẤU HOẠT ĐỘNG - AI REVIEW BOT</b>
<b>Kết quả:</b> {emoji} {review['verdict']}
<b>Điểm tổng:</b> {review['overall_score']}/10

<b>Tình trạng "Tay chân":</b>
- Code Quality: {review['quality_score']}
- Security: {review['security_score']}
- Tests: {review['tests_score']}

<b>Tóm lược:</b> {review['summary']}
"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": msg, "parse_mode": "HTML"})

if __name__ == "__main__":
    # Test chạy nội bộ để báo cáo cơ cấu
    review_data = {
        "verdict": "APPROVE",
        "overall_score": 9.5,
        "quality_score": 10,
        "security_score": 10,
        "tests_score": 8,
        "summary": "Hệ thống 'Tay chân' đang phối hợp cực tốt. Đã chuyển đổi sang Gemini 2.0 Flash để tiết kiệm 100% chi phí API."
    }
    send_telegram(review_data)
    print("✅ Đã gửi báo cáo cơ cấu hoạt động sang Telegram.")
