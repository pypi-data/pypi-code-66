from marshmallow import Schema, fields, post_load


class Bundle:
    def __init__(self, project, stage, platform, bundle_id, version, build_num, release_notes, file_path):
        self.project = project
        self.stage = stage
        self.platform = platform
        self.bundle_id = bundle_id
        self.version = version
        self.build_num = build_num
        self.release_notes = release_notes
        self.file_path = file_path

    def __repr__(self):
        return f'<Bundle: {self.project}:{self.stage}:{self.platform}:{self.version}>'


class BundleSchema(Schema):
    project = fields.Str()
    stage = fields.Str()
    platform = fields.Str()
    bundle_id = fields.Str()
    version = fields.Str()
    build_num = fields.Int()
    release_notes = fields.Str()
    file_path = fields.Str()

    class Meta:
        unknown = 'EXCLUDE'

    @post_load
    def make_bundle(self, data, **kwargs):
        return Bundle(**data)
