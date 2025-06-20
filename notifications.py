import requests
from pathlib import Path
from typing import Dict

class TelegramReporter:
    def __init__(self, bot_token: str, chat_id: str):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    def _collect_stats(self, results_dir: str) -> Dict[str, int]:
        stats = {'passed': 0, 'failed': 0}
        for result_file in Path(results_dir).glob('*.json'):
            content = result_file.read_text(encoding='utf-8')
            if '"status": "passed"' in content:
                stats['passed'] += 1
            elif '"status": "failed"' in content:
                stats['failed'] += 1
        return stats

    def send_report(self, results_dir: str) -> None:
        stats = self._collect_stats(results_dir)
        message = (
            "📊 Test Results:\n"
            f"✅ Passed: {stats['passed']}\n"
            f"❌ Failed: {stats['failed']}\n"
            "🔗 Report: http://ci-server/allure-report/"
        )

        try:
            response = requests.post(
                self.api_url,
                json={
                    'chat_id': self.chat_id,
                    'text': message,
                    'parse_mode': 'Markdown'
                },
                verify=False,
                timeout=10
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to send Telegram notification: {e}")
