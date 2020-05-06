### 這是使用pip install elasticsearch的範例 #############
# 實現了建立Index以及查詢Index，查詢也需要用正則，
# 若查詢的match為空白相當於沒有過濾、全部輸出
# 他的量產版本是pip install elasticsearch-dsl
#########################################################


#resp = es.get(index="logstash-2020.05.05-000001", id="1")
# ignore 400 cause by IndexAlreadyExistsException when creating an index
#es.indices.create(index='test-index', ignore=400)

# ignore 404 and 400
#es.indices.delete(index='test-index', ignore=[400, 404])

# You can add to the client to apply to all requests
#client = Elasticsearch(opaque_id="app17@dc06.eu_user1234")

# Or you can apply per-request for more granularity.
#resp = client.get(index="logstash-2020.05.05-000001", id="1", opaque_id="app17@dc06.eu_user1234")


#es = Elasticsearch(
#    [
#        'http://192.168.105.134:9200/',
#    ],
#    verify_certs=False
#)

#es.indices.create(index="test-index", ignore=400)
#es.get(index="test-index", id="1")

from datetime import datetime
from elasticsearch import Elasticsearch

# create an instance
es = Elasticsearch([
        'http://192.168.105.134:9200/',
    ],
    verify_certs=True    
)

### data,dict, to be wrote
#doc = {
#    'author': 'kimchy',
#    'text': 'Elasticsearch: awesome, bosina awesome',
#    'timestamp': datetime.now(),
#}

### insert index with body ( json message )
#res = es.index(index="test-index", id=3, body=doc)
#print(res['result'])

### get index 
#res = es.get(index="test-index", id=3)
#print(res['_source'])

### refresh
#es.indices.refresh(index="test-index")

### query data with index, body
#res = es.search(index="test-index", body={"query": {"match_all": {}}})

### print the response
#print("Got %d Hits:" % res['hits']['total']['value'])
#for hit in res['hits']['hits']:
#    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

