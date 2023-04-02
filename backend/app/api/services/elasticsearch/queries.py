import os
from elasticsearch import Elasticsearch

host = os.environ.get('ELASTICSEARCH_HOST')
port = int(os.environ.get('ELASTICSEARCH_PORT'))

es = Elasticsearch([{'host': host, 'port': port, "scheme": "https"}])

def search_questions(query):
    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "body", "explanation"]
            }
        }
    }

    response = es.search(index="question_index", body=body)

    hits = response['hits']['hits']
    results = []

    for hit in hits:
        result = hit['_source']
        result['id'] = hit['_id']
        results.append(result)

    return results
