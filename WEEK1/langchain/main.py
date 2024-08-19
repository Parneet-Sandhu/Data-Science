from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import Html2TextTransformer

url="https://indianexpress.com/"
loader=AsyncChromiumLoader([url])
docs=loader.load()
print(docs[0].page_content)