from dictionaryutils import dictionary

def test_require_core_metadata_collections():
    for schema in dictionary.schema.values():
        if schema["category"].endswith("_file"):
            assert (
                "core_metadata_collections" in schema["properties"],
                "core_metadata_collections is required for data node {}"
                .format(schema["id"])
            )
