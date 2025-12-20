from unittest.mock import Mock
import json
json = Mock()



json.dumps({'a':1})
json.dumps({'a':1})
json.dumps({'a':1})
json.loads({"a":2})

print(dir(json))



print(json.dumps.call_args)
print(json.dumps.call_count)
print(json.method_calls)

