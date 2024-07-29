from elasticsearch import Elasticsearch

es = Elasticsearch(
    hosts=["localhost"],
    scheme="http",
    port=9200,
)
