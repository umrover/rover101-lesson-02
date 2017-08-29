"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class Simple(object):
    __slots__ = ["elapsed_time_s", "latitude_deg", "longitude_deg"]

    def __init__(self):
        self.elapsed_time_s = 0
        self.latitude_deg = 0.0
        self.longitude_deg = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(Simple._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">idd", self.elapsed_time_s, self.latitude_deg, self.longitude_deg))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != Simple._get_packed_fingerprint():
            raise ValueError("Decode error")
        return Simple._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = Simple()
        self.elapsed_time_s, self.latitude_deg, self.longitude_deg = struct.unpack(">idd", buf.read(20))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if Simple in parents: return 0
        tmphash = (0xb7ffdd0f07096099) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if Simple._packed_fingerprint is None:
            Simple._packed_fingerprint = struct.pack(">Q", Simple._get_hash_recursive([]))
        return Simple._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

