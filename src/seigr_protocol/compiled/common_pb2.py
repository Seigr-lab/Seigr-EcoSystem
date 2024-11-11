# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\x12\x05seigr\"+\n\rBasicMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"H\n\tTimestamp\x12\x12\n\ncreated_at\x18\x01 \x01(\t\x12\x12\n\nupdated_at\x18\x02 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssed_at\x18\x03 \x01(\t\"\xb7\x01\n\x10StandardResponse\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.seigr.OperationalStatus\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x37\n\x08metadata\x18\x03 \x03(\x0b\x32%.seigr.StandardResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf9\x01\n\x12ThreatDetectionLog\x12(\n\x0cthreat_level\x18\x01 \x01(\x0e\x32\x12.seigr.ThreatLevel\x12\x0e\n\x06origin\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12(\n\x0e\x64\x65tection_time\x18\x04 \x01(\x0b\x32\x10.seigr.Timestamp\x12\x39\n\x08metadata\x18\x05 \x03(\x0b\x32\'.seigr.ThreatDetectionLog.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xce\x01\n\x12ResourceIdentifier\x12\x13\n\x0bresource_id\x18\x01 \x01(\t\x12\"\n\tdata_type\x18\x02 \x01(\x0e\x32\x0f.seigr.DataType\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x39\n\x08metadata\x18\x04 \x03(\x0b\x32\'.seigr.ResourceIdentifier.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\x8c\x01\n\x0bThreatLevel\x12\x1a\n\x16THREAT_LEVEL_UNDEFINED\x10\x00\x12\x14\n\x10THREAT_LEVEL_LOW\x10\x01\x12\x19\n\x15THREAT_LEVEL_MODERATE\x10\x02\x12\x15\n\x11THREAT_LEVEL_HIGH\x10\x03\x12\x19\n\x15THREAT_LEVEL_CRITICAL\x10\x04*\xd3\x01\n\x11OperationalStatus\x12 \n\x1cOPERATIONAL_STATUS_UNDEFINED\x10\x00\x12\x19\n\x15OPERATIONAL_STATUS_OK\x10\x01\x12\x1e\n\x1aOPERATIONAL_STATUS_WARNING\x10\x02\x12\x1c\n\x18OPERATIONAL_STATUS_ERROR\x10\x03\x12\"\n\x1eOPERATIONAL_STATUS_MAINTENANCE\x10\x04\x12\x1f\n\x1bOPERATIONAL_STATUS_DEGRADED\x10\x05*\x94\x01\n\rPriorityLevel\x12\x1c\n\x18PRIORITY_LEVEL_UNDEFINED\x10\x00\x12\x16\n\x12PRIORITY_LEVEL_LOW\x10\x01\x12\x19\n\x15PRIORITY_LEVEL_MEDIUM\x10\x02\x12\x17\n\x13PRIORITY_LEVEL_HIGH\x10\x03\x12\x19\n\x15PRIORITY_LEVEL_URGENT\x10\x04*\xa6\x01\n\x08\x44\x61taType\x12\x17\n\x13\x44\x41TA_TYPE_UNDEFINED\x10\x00\x12\x12\n\x0e\x44\x41TA_TYPE_TEXT\x10\x01\x12\x13\n\x0f\x44\x41TA_TYPE_IMAGE\x10\x02\x12\x13\n\x0f\x44\x41TA_TYPE_VIDEO\x10\x03\x12\x13\n\x0f\x44\x41TA_TYPE_AUDIO\x10\x04\x12\x16\n\x12\x44\x41TA_TYPE_DOCUMENT\x10\x05\x12\x16\n\x12\x44\x41TA_TYPE_METADATA\x10\x06\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STANDARDRESPONSE_METADATAENTRY._options = None
  _STANDARDRESPONSE_METADATAENTRY._serialized_options = b'8\001'
  _THREATDETECTIONLOG_METADATAENTRY._options = None
  _THREATDETECTIONLOG_METADATAENTRY._serialized_options = b'8\001'
  _RESOURCEIDENTIFIER_METADATAENTRY._options = None
  _RESOURCEIDENTIFIER_METADATAENTRY._serialized_options = b'8\001'
  _THREATLEVEL._serialized_start=790
  _THREATLEVEL._serialized_end=930
  _OPERATIONALSTATUS._serialized_start=933
  _OPERATIONALSTATUS._serialized_end=1144
  _PRIORITYLEVEL._serialized_start=1147
  _PRIORITYLEVEL._serialized_end=1295
  _DATATYPE._serialized_start=1298
  _DATATYPE._serialized_end=1464
  _BASICMETADATA._serialized_start=23
  _BASICMETADATA._serialized_end=66
  _TIMESTAMP._serialized_start=68
  _TIMESTAMP._serialized_end=140
  _STANDARDRESPONSE._serialized_start=143
  _STANDARDRESPONSE._serialized_end=326
  _STANDARDRESPONSE_METADATAENTRY._serialized_start=279
  _STANDARDRESPONSE_METADATAENTRY._serialized_end=326
  _THREATDETECTIONLOG._serialized_start=329
  _THREATDETECTIONLOG._serialized_end=578
  _THREATDETECTIONLOG_METADATAENTRY._serialized_start=279
  _THREATDETECTIONLOG_METADATAENTRY._serialized_end=326
  _RESOURCEIDENTIFIER._serialized_start=581
  _RESOURCEIDENTIFIER._serialized_end=787
  _RESOURCEIDENTIFIER_METADATAENTRY._serialized_start=279
  _RESOURCEIDENTIFIER_METADATAENTRY._serialized_end=326
# @@protoc_insertion_point(module_scope)