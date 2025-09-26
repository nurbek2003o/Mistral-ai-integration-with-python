import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ChatView(APIView):
    def get(self, request):
        q = request.GET.get("q", "")
        try:
            resp = requests.post(
                "http://ollama:11434/api/generate",
                json={"model": "mistral", "prompt": q},
                stream=True  # stream yoqildi
            )

            if resp.status_code != 200:
                return Response(
                    {"error": "Ollama xato qaytardi", "status": resp.status_code},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            # Streamdan response yig'amiz
            full_text = ""
            for line in resp.iter_lines():
                if not line:
                    continue
                try:
                    data = line.decode("utf-8")
                    import json
                    parsed = json.loads(data)
                    if "response" in parsed:
                        full_text += parsed["response"]
                except Exception as e:
                    continue

            return Response({"response": full_text})

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
