from mcp.server.fastmcp import FastMCP
import wikipedia

mcp = FastMCP(
    "Wikipedia",
    dependencies=["wikipedia"],
)

@mcp.tool()
def search(query: str, lang: str = 'en'):
    """
    search corresponding pages in wikipedia, return the relative topics and their summaries

    @param query keyword to be searched

    @param lang specific language to be searched, default is 'en'
    """
    wikipedia.set_lang(lang)
    topics = wikipedia.search(query)
    return [{
        "topic": topic, 
        "summary": wikipedia.page(topic).summary
    } for topic in topics]

@mcp.tool()
def summary(query: str, lang: str = 'en'):
    """
    summary of a topic

    @param query page's topic

    @param lang specific language to be searched, default is 'en'
    """
    wikipedia.set_lang(lang)
    return wikipedia.summary(query)

@mcp.tool()
def page(query: str, lang: str = 'en'):
    """
    full content of a topic

    @param query page's topic

    @param lang specific language to be searched, default is 'en'
    """
    wikipedia.set_lang(lang)
    return wikipedia.page(query).content

@mcp.tool()
def random(lang: str = 'en'):
    """
    return a random page of wikipedia

    @param lang specific language to be searched, default is 'en'
    """
    wikipedia.set_lang(lang)
    return wikipedia.page(wikipedia.random()).content

if __name__ == "__main__":
    mcp.run()