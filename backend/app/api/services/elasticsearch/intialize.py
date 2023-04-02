import os
from elasticsearch import Elasticsearch

host = os.environ.get('ELASTICSEARCH_HOST')
port = int(os.environ.get('ELASTICSEARCH_PORT'))


es = Elasticsearch([{'host': host, 'port': port, "scheme": "https"}])

question_index_map = {
    "mappings": {
        "properties": {
            "title": {"type": "text"},
            "body": {"type": "text"},
            "explanation": {"type": "text"}
        }
    }
}

es.indices.create(index="question_index", body=question_index_map)
