# PraisonAI NewsScraper

This project is a PraisonAI-powered pipeline that scrapes RSS feeds, summarizes articles, and generates scripts for YouTube Shorts.

## Components

1. **RSS Scraper Agent**: Extracts data from specified RSS feeds.
2. **Summarization Agent**: Uses Claude AI to condense the content of scraped articles.
3. **Script Generation Agent**: Creates YouTube Shorts scripts based on the summarized content.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/praisonai-newsscraper.git
   cd praisonai-newsscraper
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Anthropic API key as an environment variable:
   
   For Linux/macOS:
   ```
   export ANTHROPIC_API_KEY='your_api_key_here'
   ```
   
   For Windows (Command Prompt):
   ```
   set ANTHROPIC_API_KEY=your_api_key_here
   ```
   
   For Windows (PowerShell):
   ```
   $env:ANTHROPIC_API_KEY = 'your_api_key_here'
   ```

4. Create a `config.json` file based on the `config.example.json` template:
   ```
   cp config.example.json config.json
   ```
   Then edit `config.json` to include your desired RSS feed URLs.

## Usage

Run the main script to start the pipeline:

```
python main.py
```

This will scrape the specified RSS feeds, summarize the articles, and generate YouTube Shorts scripts based on the summaries.

## Customization

- Modify the `RSSScraperAgent` in `rss_scraper_agent.py` to change how RSS feeds are processed.
- Adjust the prompts in `summarization_agent.py` and `script_generation_agent.py` to alter the style of summaries and scripts.
- Extend the pipeline in `main.py` to add more processing steps or output formats.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
