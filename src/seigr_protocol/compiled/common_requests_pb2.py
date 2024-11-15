# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common_requests.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ommon_requests.proto\x12\x05seigr\x1a\x0c\x63ommon.proto\"\xba\x06\n\x12ReplicationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x12\n\nsegment_id\x18\x02 \x01(\t\x12(\n\x0cthreat_level\x18\x03 \x01(\x0e\x32\x12.seigr.ThreatLevel\x12,\n\x08priority\x18\x04 \x01(\x0e\x32\x1a.seigr.ReplicationPriority\x12*\n\x07trigger\x18\x05 \x01(\x0e\x32\x19.seigr.ReplicationTrigger\x12,\n\x08strategy\x18\x06 \x01(\x0e\x32\x1a.seigr.ReplicationStrategy\x12\x1c\n\x14\x63ritical_replication\x18\x07 \x01(\x08\x12\x14\n\x0crequested_by\x18\x08 \x01(\t\x12\x19\n\x11request_timestamp\x18\t \x01(\t\x12=\n\nparameters\x18\n \x03(\x0b\x32).seigr.ReplicationRequest.ParametersEntry\x12\x0e\n\x06reason\x18\x0b \x01(\t\x12\x13\n\x0bmax_retries\x18\x0c \x01(\x05\x12\x1e\n\x16retry_interval_seconds\x18\r \x01(\x05\x12\x14\n\x0ctime_to_live\x18\x0e \x01(\t\x12\x18\n\x10\x63ompliance_level\x18\x0f \x01(\t\x12\x1e\n\x16\x65ncryption_requirement\x18\x10 \x01(\t\x12\x1c\n\x14\x61\x63\x63\x65ss_control_level\x18\x11 \x01(\t\x12\x14\n\x0cgeo_location\x18\x12 \x01(\t\x12\x17\n\x0f\x64ynamic_scaling\x18\x13 \x01(\x08\x12\x1b\n\x13replication_density\x18\x14 \x01(\x01\x12\x1e\n\x16\x65rror_threshold_policy\x18\x15 \x01(\t\x12\x39\n\x08metadata\x18\x16 \x03(\x0b\x32\'.seigr.ReplicationRequest.MetadataEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\x96\x01\n\x13ReplicationPriority\x12\x16\n\x12PRIORITY_UNDEFINED\x10\x00\x12\x10\n\x0cPRIORITY_LOW\x10\x01\x12\x13\n\x0fPRIORITY_MEDIUM\x10\x02\x12\x11\n\rPRIORITY_HIGH\x10\x03\x12\x15\n\x11PRIORITY_CRITICAL\x10\x04\x12\x16\n\x12PRIORITY_EMERGENCY\x10\x05*\xdf\x02\n\x12ReplicationTrigger\x12!\n\x1dREPLICATION_TRIGGER_UNDEFINED\x10\x00\x12&\n\"REPLICATION_TRIGGER_MANUAL_REQUEST\x10\x01\x12$\n REPLICATION_TRIGGER_DEMAND_BASED\x10\x02\x12+\n\'REPLICATION_TRIGGER_IMMUNE_SYSTEM_ALERT\x10\x03\x12&\n\"REPLICATION_TRIGGER_PERIODIC_CHECK\x10\x04\x12)\n%REPLICATION_TRIGGER_NETWORK_EXPANSION\x10\x05\x12-\n)REPLICATION_TRIGGER_REGULATORY_COMPLIANCE\x10\x06\x12)\n%REPLICATION_TRIGGER_DATA_ACCESS_SPIKE\x10\x07*\x9c\x02\n\x13ReplicationStrategy\x12\"\n\x1eREPLICATION_STRATEGY_UNDEFINED\x10\x00\x12%\n!REPLICATION_STRATEGY_DEMAND_BASED\x10\x01\x12!\n\x1dREPLICATION_STRATEGY_PERIODIC\x10\x02\x12\x1d\n\x19REPLICATION_STRATEGY_FULL\x10\x03\x12!\n\x1dREPLICATION_STRATEGY_ADAPTIVE\x10\x04\x12-\n)REPLICATION_STRATEGY_GEOGRAPHICALLY_AWARE\x10\x05\x12&\n\"REPLICATION_STRATEGY_LOAD_BALANCED\x10\x06\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_requests_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REPLICATIONREQUEST_PARAMETERSENTRY._options = None
  _REPLICATIONREQUEST_PARAMETERSENTRY._serialized_options = b'8\001'
  _REPLICATIONREQUEST_METADATAENTRY._options = None
  _REPLICATIONREQUEST_METADATAENTRY._serialized_options = b'8\001'
  _REPLICATIONPRIORITY._serialized_start=876
  _REPLICATIONPRIORITY._serialized_end=1026
  _REPLICATIONTRIGGER._serialized_start=1029
  _REPLICATIONTRIGGER._serialized_end=1380
  _REPLICATIONSTRATEGY._serialized_start=1383
  _REPLICATIONSTRATEGY._serialized_end=1667
  _REPLICATIONREQUEST._serialized_start=47
  _REPLICATIONREQUEST._serialized_end=873
  _REPLICATIONREQUEST_PARAMETERSENTRY._serialized_start=775
  _REPLICATIONREQUEST_PARAMETERSENTRY._serialized_end=824
  _REPLICATIONREQUEST_METADATAENTRY._serialized_start=826
  _REPLICATIONREQUEST_METADATAENTRY._serialized_end=873
# @@protoc_insertion_point(module_scope)
