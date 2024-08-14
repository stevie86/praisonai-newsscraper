from praison import Agent
import anthropic

class ScriptGenerationAgent(Agent):
    def __init__(self, api_key):
        super().__init__()
        self.client = anthropic.Client(api_key)

    def run(self, summaries):
        scripts = []
        for summary in summaries:
            prompt = f"""Create an engaging script for a 60-second YouTube Short based on this summary:

Title: {summary['title']}

Summary: {summary['summary']}

Guidelines for the script:
1. Start with a hook to grab the viewer's attention
2. Present the main points in a clear and concise manner
3. Use conversational language suitable for a younger audience
4. Include a call-to-action at the end
5. Ensure the script is paced well for a 60-second video
6. Add suggestions for visual elements or on-screen text where appropriate

Format the script with clear sections for INTRO, MAIN CONTENT, and OUTRO."""

            response = self.client.completion(
                prompt=prompt,
                model="claude-2",
                max_tokens_to_sample=400,
                temperature=0.8
            )
            scripts.append({
                'title': summary['title'],
                'script': response.completion.strip()
            })
        return scripts
