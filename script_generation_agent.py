from praison import Agent
import anthropic

class ScriptGenerationAgent(Agent):
    def __init__(self, api_key):
        super().__init__()
        self.client = anthropic.Client(api_key)

    def run(self, summaries):
        scripts = []
        for summary in summaries:
            prompt = f"Create a script for a 60-second YouTube Short based on this summary:\n\nTitle: {summary['title']}\n\nSummary: {summary['summary']}\n\nThe script should be engaging, concise, and suitable for a vertical video format."
            response = self.client.completion(
                prompt=prompt,
                model="claude-2",
                max_tokens_to_sample=300
            )
            scripts.append({
                'title': summary['title'],
                'script': response.completion
            })
        return scripts
