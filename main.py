from praison import Pipeline
from rss_scraper_agent import RSSScraperAgent
from summarization_agent import SummarizationAgent
from script_generation_agent import ScriptGenerationAgent
import os
import json

def load_config():
    try:
        with open('config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print("config.json not found. Please create it based on config.example.json.")
        exit(1)

def main():
    # Load configuration
    config = load_config()

    # Initialize agents
    rss_scraper = RSSScraperAgent(config['rss_feeds'])
    summarizer = SummarizationAgent(os.environ['ANTHROPIC_API_KEY'])
    script_generator = ScriptGenerationAgent(os.environ['ANTHROPIC_API_KEY'])

    # Create pipeline
    pipeline = Pipeline()
    pipeline.add_agent(rss_scraper)
    pipeline.add_agent(summarizer)
    pipeline.add_agent(script_generator)

    # Run pipeline
    results = pipeline.run()

    # Process results
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Script: {result['script']}\n")

if __name__ == "__main__":
    main()
