from elasticsearch import Elasticsearch


es = Elasticsearch(["HOST:PORT"])

es.indices.create(index="test_index")

es.search(index='INDEX_NAME', body={'query': {'match': {'field': 'QUERY'}}})
