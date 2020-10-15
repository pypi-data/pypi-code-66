"""Abstraction around cwltool and related libraries for loading a CWL artifact."""
import os
from collections import namedtuple

from .cwltool_deps import (
    default_loader,
    ensure_cwltool_available,
    load_tool,
    LoadingContext,
    resolve_and_validate_document,
)

RawProcessReference = namedtuple("RawProcessReference", ["loading_context", "process_object", "uri"])
ResolvedProcessDefinition = namedtuple("ResolvedProcessDefinition", ["loading_context", "uri", "raw_process_reference"])
REWRITE_EXPRESSIONS = False


class SchemaLoader:

    def __init__(self, strict=True, validate=True):
        self._strict = strict
        self._validate = validate

    @property
    def raw_document_loader(self):
        ensure_cwltool_available()
        return default_loader(None)

    def loading_context(self):
        loading_context = LoadingContext()
        loading_context.strict = self._strict
        loading_context.do_validate = self._validate
        loading_context.loader = self.raw_document_loader
        loading_context.do_update = True
        return loading_context

    def raw_process_reference(self, path, loading_context=None):
        path = os.path.abspath(path)
        uri = "file://" + path
        loading_context = loading_context or self.loading_context()
        if REWRITE_EXPRESSIONS and not uri.endswith(".galaxy"):
            galaxy_path = os.path.abspath(path) + ".galaxy"
            from cwl_utils import etools_to_clt
            etools_to_clt.main([path, galaxy_path])
            galaxy_uri = "file://" + galaxy_path
            uri = galaxy_uri
        loading_context, process_object, uri = load_tool.fetch_document(uri, loadingContext=loading_context)
        return RawProcessReference(loading_context, process_object, uri)

    def raw_process_reference_for_object(self, process_object, uri=None, loading_context=None):
        if uri is None:
            uri = "galaxy://"
        loading_context = loading_context or self.loading_context()
        process_object["id"] = uri
        loading_context, process_object, uri = load_tool.fetch_document(process_object, loadingContext=loading_context)
        return RawProcessReference(loading_context, process_object, uri)

    def process_definition(self, raw_process_reference):
        assert raw_process_reference.loading_context is not None, "No loading context found for raw_process_reference"
        loading_context, uri = resolve_and_validate_document(
            raw_process_reference.loading_context,
            raw_process_reference.process_object,
            raw_process_reference.uri,
        )
        process_def = ResolvedProcessDefinition(
            loading_context,
            uri,
            raw_process_reference,
        )
        return process_def

    def tool(self, **kwds):
        process_definition = kwds.get("process_definition", None)
        if process_definition is None:
            raw_process_reference = kwds.get("raw_process_reference", None)
            if raw_process_reference is None:
                raw_process_reference = self.raw_process_reference(kwds["path"])
            process_definition = self.process_definition(raw_process_reference)

        tool = load_tool.make_tool(
            process_definition.uri,
            process_definition.loading_context,
        )
        return tool


schema_loader = SchemaLoader()
non_strict_non_validating_schema_loader = SchemaLoader(strict=False, validate=False)
