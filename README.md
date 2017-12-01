# dictionaryutils
python wrapper and metaschema for datadictionary.
It can be used to:
- load a local dictionary to a python object.
- dump schemas to a file that can be uploaded to s3 as an artifact.
- load schema file from an url to a python object that can be used by services

## Use dictionaryutils to load a dictionary
```
from dictionaryutils import DataDictionary

dict_fetch_from_remote = DataDictionary(url=URL_FOR_THE_JSON)

dict_loaded_locally = DataDictionary(root_dir=PATH_TO_SCHEMA_DIR)
```

## Use dictionaryutils to dump a dictionary
```
import json
from dictionaryutils import dump_schemas_from_dir

with open('dump.json', 'w') as f:
    json.dump(dump_schemas_from_dir('../datadictionary/gdcdictionary/schemas/'), f)
```
