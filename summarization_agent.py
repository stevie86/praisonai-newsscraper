from praison import Agent
import anthropic

class SummarizationAgent(Agent):
    def __init__(self, api_key):
        super().__init__()
        self.client = anthropic.Client(api_key)

    def run(self, articles):
        summaries = []
        for article in articles:
            prompt = f"Summarize the following article in 2-3 sentences:\n\nTitle: {article['title']}\n\nContent: {article['summary']}"
            response = self.client.completion(
                prompt=prompt,
                model="claude-2",
                max_tokens_to_sample=150
            )
            summaries.append({
                'title': article['title'],
                'summary': response.completion
            })
        return summaries
