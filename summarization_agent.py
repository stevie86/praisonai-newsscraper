from agent import Agent
import anthropic

class SummarizationAgent(Agent):
    def __init__(self, api_key):
        super().__init__()
        self.client = anthropic.Client(api_key)

    def run(self, articles):
        summaries = []
        for article in articles:
            prompt = f"""Summarize the following article in 3-4 concise sentences. Focus on the key points, main insights, and any notable data or statistics. Ensure the summary is informative and engaging:

Title: {article['title']}

Content: {article['summary']}

Your summary should:
1. Capture the essence of the article
2. Highlight the most important information
3. Be clear and easy to understand
4. Maintain a neutral tone"""

            response = self.client.completion(
                prompt=prompt,
                model="claude-2",
                max_tokens_to_sample=200,
                temperature=0.7
            )
            summaries.append({
                'title': article['title'],
                'summary': response.completion.strip()
            })
        return summaries
