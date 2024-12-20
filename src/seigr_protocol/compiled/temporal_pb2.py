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


from . import file_metadata_pb2 as file__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0etemporal.proto\x12\x05seigr\x1a\x13\x66ile_metadata.proto"\xa9\x02\n\x0fTemporalHistory\x12\x12\n\nhistory_id\x18\x01 \x01(\t\x12-\n\x0ftemporal_layers\x18\x02 \x03(\x0b\x32\x14.seigr.TemporalLayer\x12\x12\n\ncreated_by\x18\x03 \x01(\t\x12\x12\n\ncreated_at\x18\x04 \x01(\t\x12\x18\n\x10last_modified_at\x18\x05 \x01(\t\x12\x36\n\x08metadata\x18\x06 \x03(\x0b\x32$.seigr.TemporalHistory.MetadataEntry\x12\x15\n\rversion_count\x18\x07 \x01(\x05\x12\x11\n\tis_active\x18\x08 \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xcd\x02\n\x0fLineageTracking\x12\x12\n\nlineage_id\x18\x01 \x01(\t\x12\x17\n\x0f\x61ncestor_hashes\x18\x02 \x03(\t\x12\x19\n\x11\x64\x65scendant_hashes\x18\x03 \x03(\t\x12\x19\n\x11original_creation\x18\x04 \x01(\t\x12\x45\n\x10lineage_metadata\x18\x05 \x03(\x0b\x32+.seigr.LineageTracking.LineageMetadataEntry\x12\x17\n\x0fintegrity_check\x18\x06 \x01(\t\x12\x10\n\x08\x61rchived\x18\x07 \x01(\x08\x12\x17\n\x0f\x65volution_depth\x18\x08 \x01(\x05\x12\x14\n\x0clineage_type\x18\t \x01(\t\x1a\x36\n\x14LineageMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xa6\x02\n\x17TemporalSnapshotRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x12\n\nsegment_id\x18\x02 \x01(\t\x12\x18\n\x10target_timestamp\x18\x03 \x01(\t\x12\x13\n\x0b\x65xact_match\x18\x04 \x01(\x08\x12\x14\n\x0crequested_by\x18\x05 \x01(\t\x12M\n\x10request_metadata\x18\x06 \x03(\x0b\x32\x33.seigr.TemporalSnapshotRequest.RequestMetadataEntry\x12\x17\n\x0frequest_purpose\x18\x07 \x01(\t\x1a\x36\n\x14RequestMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xe4\x02\n\x18TemporalSnapshotResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12,\n\x0esnapshot_layer\x18\x02 \x01(\x0b\x32\x14.seigr.TemporalLayer\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12P\n\x11response_metadata\x18\x05 \x03(\x0b\x32\x35.seigr.TemporalSnapshotResponse.ResponseMetadataEntry\x12\x1b\n\x13retrieved_timestamp\x18\x06 \x01(\t\x12\x1d\n\x15retrieval_duration_ms\x18\x07 \x01(\x03\x12\x17\n\x0fsnapshot_source\x18\x08 \x01(\t\x1a\x37\n\x15ResponseMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x90\x02\n\x14TemporalMergeRequest\x12\x10\n\x08merge_id\x18\x01 \x01(\t\x12\x11\n\tlayer_ids\x18\x02 \x03(\t\x12\x11\n\ttarget_id\x18\x03 \x01(\t\x12\x14\n\x0cinitiated_by\x18\x04 \x01(\t\x12\x12\n\nmerge_type\x18\x05 \x01(\t\x12\x46\n\x0emerge_metadata\x18\x06 \x03(\x0b\x32..seigr.TemporalMergeRequest.MergeMetadataEntry\x12\x18\n\x10retain_originals\x18\x07 \x01(\x08\x1a\x34\n\x12MergeMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x8d\x02\n\x15TemporalMergeResponse\x12\x10\n\x08merge_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x17\n\x0fmerged_layer_id\x18\x03 \x01(\t\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12M\n\x11response_metadata\x18\x05 \x03(\x0b\x32\x32.seigr.TemporalMergeResponse.ResponseMetadataEntry\x12\x19\n\x11merge_duration_ms\x18\x06 \x01(\x03\x1a\x37\n\x15ResponseMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xf9\x02\n\x0eTemporalPolicy\x12\x11\n\tpolicy_id\x18\x01 \x01(\t\x12\x13\n\x0bpolicy_name\x18\x02 \x01(\t\x12\x1f\n\x17retention_duration_days\x18\x03 \x01(\x05\x12 \n\x18\x65nable_automatic_merging\x18\x04 \x01(\x08\x12\x1c\n\x14merge_frequency_days\x18\x05 \x01(\x05\x12 \n\x18\x65nable_snapshot_deletion\x18\x06 \x01(\x08\x12\x19\n\x11\x64\x65letion_criteria\x18\x07 \x01(\t\x12\x42\n\x0fpolicy_metadata\x18\x08 \x03(\x0b\x32).seigr.TemporalPolicy.PolicyMetadataEntry\x12\x12\n\ncreated_by\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\n \x01(\t\x1a\x35\n\x13PolicyMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "temporal_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _TEMPORALHISTORY_METADATAENTRY._options = None
    _TEMPORALHISTORY_METADATAENTRY._serialized_options = b"8\001"
    _LINEAGETRACKING_LINEAGEMETADATAENTRY._options = None
    _LINEAGETRACKING_LINEAGEMETADATAENTRY._serialized_options = b"8\001"
    _TEMPORALSNAPSHOTREQUEST_REQUESTMETADATAENTRY._options = None
    _TEMPORALSNAPSHOTREQUEST_REQUESTMETADATAENTRY._serialized_options = b"8\001"
    _TEMPORALSNAPSHOTRESPONSE_RESPONSEMETADATAENTRY._options = None
    _TEMPORALSNAPSHOTRESPONSE_RESPONSEMETADATAENTRY._serialized_options = b"8\001"
    _TEMPORALMERGEREQUEST_MERGEMETADATAENTRY._options = None
    _TEMPORALMERGEREQUEST_MERGEMETADATAENTRY._serialized_options = b"8\001"
    _TEMPORALMERGERESPONSE_RESPONSEMETADATAENTRY._options = None
    _TEMPORALMERGERESPONSE_RESPONSEMETADATAENTRY._serialized_options = b"8\001"
    _TEMPORALPOLICY_POLICYMETADATAENTRY._options = None
    _TEMPORALPOLICY_POLICYMETADATAENTRY._serialized_options = b"8\001"
    _TEMPORALHISTORY._serialized_start = 47
    _TEMPORALHISTORY._serialized_end = 344
    _TEMPORALHISTORY_METADATAENTRY._serialized_start = 297
    _TEMPORALHISTORY_METADATAENTRY._serialized_end = 344
    _LINEAGETRACKING._serialized_start = 347
    _LINEAGETRACKING._serialized_end = 680
    _LINEAGETRACKING_LINEAGEMETADATAENTRY._serialized_start = 626
    _LINEAGETRACKING_LINEAGEMETADATAENTRY._serialized_end = 680
    _TEMPORALSNAPSHOTREQUEST._serialized_start = 683
    _TEMPORALSNAPSHOTREQUEST._serialized_end = 977
    _TEMPORALSNAPSHOTREQUEST_REQUESTMETADATAENTRY._serialized_start = 923
    _TEMPORALSNAPSHOTREQUEST_REQUESTMETADATAENTRY._serialized_end = 977
    _TEMPORALSNAPSHOTRESPONSE._serialized_start = 980
    _TEMPORALSNAPSHOTRESPONSE._serialized_end = 1336
    _TEMPORALSNAPSHOTRESPONSE_RESPONSEMETADATAENTRY._serialized_start = 1281
    _TEMPORALSNAPSHOTRESPONSE_RESPONSEMETADATAENTRY._serialized_end = 1336
    _TEMPORALMERGEREQUEST._serialized_start = 1339
    _TEMPORALMERGEREQUEST._serialized_end = 1611
    _TEMPORALMERGEREQUEST_MERGEMETADATAENTRY._serialized_start = 1559
    _TEMPORALMERGEREQUEST_MERGEMETADATAENTRY._serialized_end = 1611
    _TEMPORALMERGERESPONSE._serialized_start = 1614
    _TEMPORALMERGERESPONSE._serialized_end = 1883
    _TEMPORALMERGERESPONSE_RESPONSEMETADATAENTRY._serialized_start = 1281
    _TEMPORALMERGERESPONSE_RESPONSEMETADATAENTRY._serialized_end = 1336
    _TEMPORALPOLICY._serialized_start = 1886
    _TEMPORALPOLICY._serialized_end = 2263
    _TEMPORALPOLICY_POLICYMETADATAENTRY._serialized_start = 2210
    _TEMPORALPOLICY_POLICYMETADATAENTRY._serialized_end = 2263
# @@protoc_insertion_point(module_scope)
