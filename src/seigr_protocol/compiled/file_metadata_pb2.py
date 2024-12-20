# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import segment_metadata_pb2 as segment__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13\x66ile_metadata.proto\x12\x05seigr\x1a\x16segment_metadata.proto"\xea\x01\n\x0cOperationLog\x12\x16\n\x0eoperation_type\x18\x01 \x01(\t\x12\x14\n\x0cperformed_by\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x05 \x01(\t\x12\x33\n\x08metadata\x18\x06 \x03(\x0b\x32!.seigr.OperationLog.MetadataEntry\x12\x12\n\nerror_code\x18\x07 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xa6\x03\n\rTemporalLayer\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12(\n\x08segments\x18\x02 \x03(\x0b\x32\x16.seigr.SegmentMetadata\x12\x12\n\nlayer_hash\x18\x03 \x01(\t\x12=\n\rdata_snapshot\x18\x04 \x03(\x0b\x32&.seigr.TemporalLayer.DataSnapshotEntry\x12\x1b\n\x13previous_layer_hash\x18\x05 \x01(\t\x12\x18\n\x10rollback_allowed\x18\x06 \x01(\x08\x12\x34\n\x08metadata\x18\x07 \x03(\x0b\x32".seigr.TemporalLayer.MetadataEntry\x12\x19\n\x11\x63hecksum_segments\x18\x08 \x03(\t\x12\x17\n\x0f\x62\x61\x63kup_location\x18\t \x01(\t\x1a\x33\n\x11\x44\x61taSnapshotEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xd9\x01\n\nAccessRule\x12\x0f\n\x07rule_id\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x03(\t\x12\x12\n\nexpiration\x18\x04 \x01(\t\x12\x12\n\nconditions\x18\x05 \x01(\t\x12:\n\rrule_metadata\x18\x06 \x03(\x0b\x32#.seigr.AccessRule.RuleMetadataEntry\x1a\x33\n\x11RuleMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x9a\x08\n\x0c\x46ileMetadata\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x12\n\ncreator_id\x18\x02 \x01(\t\x12"\n\tfile_type\x18\x03 \x01(\x0e\x32\x0f.seigr.FileType\x12&\n\x0b\x66ile_status\x18\x04 \x01(\x0e\x32\x11.seigr.FileStatus\x12\x19\n\x11original_filename\x18\x05 \x01(\t\x12\x1a\n\x12original_extension\x18\x06 \x01(\t\x12\x1a\n\x12\x63reation_timestamp\x18\x07 \x01(\t\x12\x11\n\tfile_hash\x18\x08 \x01(\t\x12(\n\x08segments\x18\t \x03(\x0b\x32\x16.seigr.SegmentMetadata\x12-\n\x0ftemporal_layers\x18\n \x03(\x0b\x32\x14.seigr.TemporalLayer\x12+\n\x0eoperation_logs\x18\x0b \x03(\x0b\x32\x13.seigr.OperationLog\x12\x44\n\x11\x63ustom_attributes\x18\x0c \x03(\x0b\x32).seigr.FileMetadata.CustomAttributesEntry\x12\x18\n\x10\x61\x63\x63\x65ss_policy_id\x18\r \x01(\t\x12\x1b\n\x13\x65ncryption_protocol\x18\x0e \x01(\t\x12\x18\n\x10network_protocol\x18\x0f \x01(\t\x12#\n\x1bintegrity_verification_hash\x18\x10 \x01(\t\x12\x18\n\x10redundancy_level\x18\x11 \x01(\x05\x12\x18\n\x10\x61uthorized_users\x18\x12 \x03(\t\x12H\n\x13protocol_attributes\x18\x13 \x03(\x0b\x32+.seigr.FileMetadata.ProtocolAttributesEntry\x12\x1b\n\x13\x61\x63\x63\x65ss_control_list\x18\x14 \x03(\t\x12\'\n\x0c\x61\x63\x63\x65ss_rules\x18\x15 \x03(\x0b\x32\x11.seigr.AccessRule\x12\x1e\n\x16\x63ompliance_requirement\x18\x16 \x01(\t\x12\x18\n\x10retention_period\x18\x17 \x01(\t\x12\x1a\n\x12origin_data_source\x18\x18 \x01(\t\x12\x1f\n\x17last_modified_timestamp\x18\x19 \x01(\t\x12!\n\x19\x66ormat_conversion_history\x18\x1a \x03(\t\x12\x1f\n\x17primary_backup_location\x18\x1b \x01(\t\x1a\x37\n\x15\x43ustomAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x39\n\x17ProtocolAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\x8f\x01\n\x08\x46ileType\x12\x12\n\x0e\x46ILE_UNDEFINED\x10\x00\x12\n\n\x06\x42INARY\x10\x01\x12\n\n\x06SENARY\x10\x02\x12\x11\n\rCUSTOM_FORMAT\x10\x03\x12\x08\n\x04TEXT\x10\x04\x12\t\n\x05IMAGE\x10\x05\x12\t\n\x05VIDEO\x10\x06\x12\t\n\x05\x41UDIO\x10\x07\x12\x0b\n\x07\x41RCHIVE\x10\x08\x12\x0c\n\x08\x44\x41TABASE\x10\t*\x95\x01\n\nFileStatus\x12\x19\n\x15\x46ILE_STATUS_UNDEFINED\x10\x00\x12\x16\n\x12\x46ILE_STATUS_ACTIVE\x10\x01\x12\x18\n\x14\x46ILE_STATUS_ARCHIVED\x10\x02\x12\x1e\n\x1a\x46ILE_STATUS_PENDING_REVIEW\x10\x03\x12\x1a\n\x16\x46ILE_STATUS_RESTRICTED\x10\x04\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "file_metadata_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _OPERATIONLOG_METADATAENTRY._options = None
    _OPERATIONLOG_METADATAENTRY._serialized_options = b"8\001"
    _TEMPORALLAYER_DATASNAPSHOTENTRY._options = None
    _TEMPORALLAYER_DATASNAPSHOTENTRY._serialized_options = b"8\001"
    _TEMPORALLAYER_METADATAENTRY._options = None
    _TEMPORALLAYER_METADATAENTRY._serialized_options = b"8\001"
    _ACCESSRULE_RULEMETADATAENTRY._options = None
    _ACCESSRULE_RULEMETADATAENTRY._serialized_options = b"8\001"
    _FILEMETADATA_CUSTOMATTRIBUTESENTRY._options = None
    _FILEMETADATA_CUSTOMATTRIBUTESENTRY._serialized_options = b"8\001"
    _FILEMETADATA_PROTOCOLATTRIBUTESENTRY._options = None
    _FILEMETADATA_PROTOCOLATTRIBUTESENTRY._serialized_options = b"8\001"
    _FILETYPE._serialized_start = 1990
    _FILETYPE._serialized_end = 2133
    _FILESTATUS._serialized_start = 2136
    _FILESTATUS._serialized_end = 2285
    _OPERATIONLOG._serialized_start = 55
    _OPERATIONLOG._serialized_end = 289
    _OPERATIONLOG_METADATAENTRY._serialized_start = 242
    _OPERATIONLOG_METADATAENTRY._serialized_end = 289
    _TEMPORALLAYER._serialized_start = 292
    _TEMPORALLAYER._serialized_end = 714
    _TEMPORALLAYER_DATASNAPSHOTENTRY._serialized_start = 614
    _TEMPORALLAYER_DATASNAPSHOTENTRY._serialized_end = 665
    _TEMPORALLAYER_METADATAENTRY._serialized_start = 242
    _TEMPORALLAYER_METADATAENTRY._serialized_end = 289
    _ACCESSRULE._serialized_start = 717
    _ACCESSRULE._serialized_end = 934
    _ACCESSRULE_RULEMETADATAENTRY._serialized_start = 883
    _ACCESSRULE_RULEMETADATAENTRY._serialized_end = 934
    _FILEMETADATA._serialized_start = 937
    _FILEMETADATA._serialized_end = 1987
    _FILEMETADATA_CUSTOMATTRIBUTESENTRY._serialized_start = 1873
    _FILEMETADATA_CUSTOMATTRIBUTESENTRY._serialized_end = 1928
    _FILEMETADATA_PROTOCOLATTRIBUTESENTRY._serialized_start = 1930
    _FILEMETADATA_PROTOCOLATTRIBUTESENTRY._serialized_end = 1987
# @@protoc_insertion_point(module_scope)
