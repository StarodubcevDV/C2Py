
import datetime
import pytz

import cbor2
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from c2py.jumbf_boxes.super_box import SuperBox
from c2py.jumbf_boxes.content_box import ContentBox
from c2py.utils.content_types import c2pa_content_types


class ClaimSignature(SuperBox):

    def __init__(self, claim, private_key, certificate):

        self.claim = claim
        self.private_key = private_key
        self.certificate = certificate

        content_boxes = []
        if self.claim != None and self.private_key != None and self.certificate != None:
            content_box = ContentBox(box_type='cbor'.encode('utf-8').hex(), payload=self.create_signature())
            content_boxes.append(content_box)

        super().__init__(content_type=c2pa_content_types['claim_signature'], label='c2pa.signature', content_boxes=content_boxes)


    # Sign by ps256 algo
    def create_signature(self):

        # -37 stands for PS256 (RSASSA-PSS using SHA-256 and MGF1 with SHA-256)
        phdr = cbor2.dumps({1: -37})

        cert = x509.load_pem_x509_certificate(self.certificate, default_backend())
        certificates_info = {
            'x5chain': cert.public_bytes(Encoding.DER),
            'temp_signing_time': str(datetime.datetime.now(pytz.utc)),
        }

        private_key = serialization.load_pem_private_key(self.private_key, password=None)
        sig_structure_data = cbor2.dumps(['Signature1', phdr, b'' b'', self.claim.serialize()])
        sig_structure_data = b'\x84' + sig_structure_data[1:]
        signature = private_key.sign(
            sig_structure_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=32
            ),
            hashes.SHA256()
        )

        payload = None
        message = [phdr, certificates_info, payload, signature]
        tag = cbor2.CBORTag(18, message)
        cose_tag = cbor2.dumps(tag)

        pad = b'\x00' * (4096 - len(cose_tag))
        payload = cose_tag + pad
        return payload
        
