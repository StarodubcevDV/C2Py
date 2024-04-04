
from c2py.jumbf_boxes.super_box import SuperBox
from c2py.utils.content_types import c2pa_content_types


class ManifestStore(SuperBox):

    manifests = []

    def __init__(self, manifests=[]):
        self.manifests = manifests
        super().__init__(content_type=c2pa_content_types['manifest_store'], label='c2pa', content_boxes=manifests)

