import os
from elasticsearch import Elasticsearch

host = os.environ.get('ELASTICSEARCH_HOST')
port = os.environ.get('ELASTICSEARCH_PORT')

es = Elasticsearch([{'host': host, 'port': port}])

question_index_map = {
    "properties": {
        "title": {"type": "text"},
        "difficulty": {"type": "keyword"},
        "body": {"type": "text"},
        "explanation": {"type": "text"}
    }
}

es.indices.create(index="question_index", body=question_index_map)

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
