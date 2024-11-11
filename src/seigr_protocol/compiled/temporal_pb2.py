# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import file_metadata_pb2 as file__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etemporal.proto\x12\x05seigr\x1a\x13\x66ile_metadata.proto\"\xff\x01\n\x0fTemporalHistory\x12\x12\n\nhistory_id\x18\x01 \x01(\t\x12-\n\x0ftemporal_layers\x18\x02 \x03(\x0b\x32\x14.seigr.TemporalLayer\x12\x12\n\ncreated_by\x18\x03 \x01(\t\x12\x12\n\ncreated_at\x18\x04 \x01(\t\x12\x18\n\x10last_modified_at\x18\x05 \x01(\t\x12\x36\n\x08metadata\x18\x06 \x03(\x0b\x32$.seigr.TemporalHistory.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf3\x01\n\x0fLineageTracking\x12\x12\n\nlineage_id\x18\x01 \x01(\t\x12\x17\n\x0f\x61ncestor_hashes\x18\x02 \x03(\t\x12\x19\n\x11\x64\x65scendant_hashes\x18\x03 \x03(\t\x12\x19\n\x11original_creation\x18\x04 \x01(\t\x12\x45\n\x10lineage_metadata\x18\x05 \x03(\x0b\x32+.seigr.LineageTracking.LineageMetadataEntry\x1a\x36\n\x14LineageMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf7\x01\n\x17TemporalSnapshotRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x12\n\nsegment_id\x18\x02 \x01(\t\x12\x18\n\x10target_timestamp\x18\x03 \x01(\t\x12\x13\n\x0b\x65xact_match\x18\x04 \x01(\x08\x12M\n\x10request_metadata\x18\x05 \x03(\x0b\x32\x33.seigr.TemporalSnapshotRequest.RequestMetadataEntry\x1a\x36\n\x14RequestMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8f\x02\n\x18TemporalSnapshotResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12,\n\x0esnapshot_layer\x18\x02 \x01(\x0b\x32\x14.seigr.TemporalLayer\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12P\n\x11response_metadata\x18\x05 \x03(\x0b\x32\x35.seigr.TemporalSnapshotResponse.ResponseMetadataEntry\x1a\x37\n\x15ResponseMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'temporal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TEMPORALHISTORY_METADATAENTRY._options = None
  _TEMPORALHISTORY_METADATAENTRY._serialized_options = b'8\001'
  _LINEAGETRACKING_LINEAGEMETADATAENTRY._options = None
  _LINEAGETRACKING_LINEAGEMETADATAENTRY._serialized_options = b'8\001'
  _TEMPORALSNAPSHOTREQUEST_REQUESTMETADATAENTRY._options = None
  _TEMPORALSNAPSHOTREQUEST_REQUESTMETADATAENTRY._serialized_options = b'8\001'
  _TEMPORALSNAPSHOTRESPONSE_RESPONSEMETADATAENTRY._options = None
  _TEMPORALSNAPSHOTRESPONSE_RESPONSEMETADATAENTRY._serialized_options = b'8\001'
  _TEMPORALHISTORY._serialized_start=47
  _TEMPORALHISTORY._serialized_end=302
  _TEMPORALHISTORY_METADATAENTRY._serialized_start=255
  _TEMPORALHISTORY_METADATAENTRY._serialized_end=302
  _LINEAGETRACKING._serialized_start=305
  _LINEAGETRACKING._serialized_end=548
  _LINEAGETRACKING_LINEAGEMETADATAENTRY._serialized_start=494
  _LINEAGETRACKING_LINEAGEMETADATAENTRY._serialized_end=548
  _TEMPORALSNAPSHOTREQUEST._serialized_start=551
  _TEMPORALSNAPSHOTREQUEST._serialized_end=798
  _TEMPORALSNAPSHOTREQUEST_REQUESTMETADATAENTRY._serialized_start=744
  _TEMPORALSNAPSHOTREQUEST_REQUESTMETADATAENTRY._serialized_end=798
  _TEMPORALSNAPSHOTRESPONSE._serialized_start=801
  _TEMPORALSNAPSHOTRESPONSE._serialized_end=1072
  _TEMPORALSNAPSHOTRESPONSE_RESPONSEMETADATAENTRY._serialized_start=1017
  _TEMPORALSNAPSHOTRESPONSE_RESPONSEMETADATAENTRY._serialized_end=1072
# @@protoc_insertion_point(module_scope)
