from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY", api_url="http://10.1.0.150:13002")

# Scrape a website:
scrape_result = app.scrape_url('firecrawl.dev', formats=['markdown'])
print(scrape_result.metadata.get("title"))
