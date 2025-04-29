from mcp.server.fastmcp import FastMCP
import wikipedia

mcp = FastMCP(
    "Wikipedia",
    dependencies=["wikipedia"],
)

@mcp.tool()
def search(query: str):
    """
    search corresponding pages in wikipedia, results is a list of page topics

    the proper way to use wikipedia is to:
    
    0. call set_lang(lang) to set language (e.g. zh or en) (default is en)
    1. call search(keyword), get some reletive topics
    2. choose a topic, call page(topic) to get full content; or call summary(topic) to get a summary

    @param query keyword to be searched
    """
    return wikipedia.search(query)

@mcp.tool()
def summary(query: str):
    """
    summary of a topic

    @param query page's topic
    """
    return wikipedia.summary(query)

@mcp.tool()
def page(query: str):
    """
    full content of a topic

    @param query page's topic
    """
    return wikipedia.page(query).content

@mcp.tool()
def random():
    """
    return a random page of wikipedia
    """
    return wikipedia.page(wikipedia.random()).content

@mcp.tool()
def set_lang(lang: str):
    """
    set wikipedia language to be searched

    @param lang language
    """
    wikipedia.set_lang(lang)
    return f"Language set to {lang}"

if __name__ == "__main__":
    mcp.run()