from openai import AsyncOpenAI


class ChatDeepseekService:
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    async def ask_deepseek(self, user_text_deepseek: str, role_text_deepseek: str):
        response = await self.client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=[
                {"role": "system", "content": role_text_deepseek},
                {"role": "user", "content": user_text_deepseek},
            ],
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}}
        )
        answer = response.choices[0].message.content

        return answer
