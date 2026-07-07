import requests

class SearchEngine:

    def __init__(self):
        self.timeout = 15

    def search(self, url, params=None, headers=None):
        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=self.timeout
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
