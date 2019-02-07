from dictionaryutils import dictionary


def test_required_program_property():
    required = "dbgap_accession_number"
    schema = dictionary.schema["program"]
    assert required in schema["required"], (
                "{} is required property for a program node, but not defined "
                "as required".format(required))


def test_required_project_property():
    required = "dbgap_accession_number"
    schema = dictionary.schema["project"]
    assert required in schema["required"], (
                "{} is required property for a project node, but not defined "
                "as required".format(required))


def test_required_properties():
    required = ["submitter_id", "type"]
    for schema in dictionary.schema.values():
        if not schema["id"] in ("program", "project"):
            for property in required:
                assert property in schema["required"], (
                    "{} is required property for a {} node, but not defined "
                    "as required".format(property, schema["id"]))
