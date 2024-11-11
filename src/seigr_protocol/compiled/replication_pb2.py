# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: replication.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_requests_pb2 as common__requests__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11replication.proto\x12\x05seigr\x1a\x15\x63ommon_requests.proto\"\xce\x02\n\x11ReplicationConfig\x12\x1a\n\x12replication_factor\x18\x01 \x01(\x05\x12\x1e\n\x16min_replication_factor\x18\x02 \x01(\x05\x12\x1e\n\x16max_replication_factor\x18\x03 \x01(\x05\x12$\n\x1c\x61\x64\x61ptive_replication_enabled\x18\x04 \x01(\x08\x12\x34\n\x10\x64\x65\x66\x61ult_strategy\x18\x05 \x01(\x0e\x32\x1a.seigr.ReplicationStrategy\x12\x16\n\x0e\x63onfig_version\x18\x06 \x01(\t\x12\x38\n\x08metadata\x18\x07 \x03(\x0b\x32&.seigr.ReplicationConfig.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd6\x02\n\x11ReplicationStatus\x12\x12\n\nsegment_id\x18\x01 \x01(\t\x12!\n\x19\x63urrent_replication_count\x18\x02 \x01(\x05\x12 \n\x18target_replication_count\x18\x03 \x01(\x05\x12\x1a\n\x12replica_hyphen_ids\x18\x04 \x03(\t\x12\x1d\n\x15replication_completed\x18\x05 \x01(\x08\x12,\n\x08priority\x18\x06 \x01(\x0e\x32\x1a.seigr.ReplicationPriority\x12\x14\n\x0clast_checked\x18\x07 \x01(\t\x12\x38\n\x08metadata\x18\x08 \x03(\x0b\x32&.seigr.ReplicationStatus.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xee\x01\n\x13ReplicationEventLog\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x12\n\nsegment_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\x14\n\x0cinitiated_by\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x38\n\x07\x64\x65tails\x18\x07 \x03(\x0b\x32\'.seigr.ReplicationEventLog.DetailsEntry\x1a.\n\x0c\x44\x65tailsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb1\x03\n\x11RedundancyManager\x12\x1c\n\x14min_redundancy_level\x18\x01 \x01(\x05\x12\x1c\n\x14max_redundancy_level\x18\x02 \x01(\x05\x12G\n\x10segment_priority\x18\x03 \x03(\x0b\x32-.seigr.RedundancyManager.SegmentPriorityEntry\x12\x1e\n\x16high_priority_segments\x18\x04 \x03(\t\x12\x19\n\x11\x63ritical_segments\x18\x05 \x03(\t\x12M\n\x13redundancy_metadata\x18\x06 \x03(\x0b\x32\x30.seigr.RedundancyManager.RedundancyMetadataEntry\x1aR\n\x14SegmentPriorityEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0e\x32\x1a.seigr.ReplicationPriority:\x02\x38\x01\x1a\x39\n\x17RedundancyMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc8\x02\n\x15ReplicationEscalation\x12\x15\n\rescalation_id\x18\x01 \x01(\t\x12\x12\n\nsegment_id\x18\x02 \x01(\t\x12,\n\x08priority\x18\x03 \x01(\x0e\x32\x1a.seigr.ReplicationPriority\x12\x14\n\x0c\x65scalated_at\x18\x04 \x01(\t\x12\x0e\n\x06reason\x18\x05 \x01(\t\x12\x18\n\x10\x61lert_recipients\x18\x06 \x03(\t\x12\'\n\x1fimmediate_replication_triggered\x18\x07 \x01(\x08\x12<\n\x08metadata\x18\x08 \x03(\x0b\x32*.seigr.ReplicationEscalation.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xde\x03\n\x12ReplicationSummary\x12\x12\n\nsummary_id\x18\x01 \x01(\t\x12!\n\x19total_segments_replicated\x18\x02 \x01(\x05\x12\"\n\x1ahigh_priority_replications\x18\x03 \x01(\x05\x12\x1b\n\x13\x66\x61iled_replications\x18\x04 \x01(\x05\x12\x1c\n\x14ongoing_replications\x18\x05 \x01(\x05\x12\x14\n\x0cgenerated_at\x18\x06 \x01(\t\x12H\n\x10segment_statuses\x18\x07 \x03(\x0b\x32..seigr.ReplicationSummary.SegmentStatusesEntry\x12H\n\x10summary_metadata\x18\x08 \x03(\x0b\x32..seigr.ReplicationSummary.SummaryMetadataEntry\x1aP\n\x14SegmentStatusesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.seigr.ReplicationStatus:\x02\x38\x01\x1a\x36\n\x14SummaryMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'replication_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REPLICATIONCONFIG_METADATAENTRY._options = None
  _REPLICATIONCONFIG_METADATAENTRY._serialized_options = b'8\001'
  _REPLICATIONSTATUS_METADATAENTRY._options = None
  _REPLICATIONSTATUS_METADATAENTRY._serialized_options = b'8\001'
  _REPLICATIONEVENTLOG_DETAILSENTRY._options = None
  _REPLICATIONEVENTLOG_DETAILSENTRY._serialized_options = b'8\001'
  _REDUNDANCYMANAGER_SEGMENTPRIORITYENTRY._options = None
  _REDUNDANCYMANAGER_SEGMENTPRIORITYENTRY._serialized_options = b'8\001'
  _REDUNDANCYMANAGER_REDUNDANCYMETADATAENTRY._options = None
  _REDUNDANCYMANAGER_REDUNDANCYMETADATAENTRY._serialized_options = b'8\001'
  _REPLICATIONESCALATION_METADATAENTRY._options = None
  _REPLICATIONESCALATION_METADATAENTRY._serialized_options = b'8\001'
  _REPLICATIONSUMMARY_SEGMENTSTATUSESENTRY._options = None
  _REPLICATIONSUMMARY_SEGMENTSTATUSESENTRY._serialized_options = b'8\001'
  _REPLICATIONSUMMARY_SUMMARYMETADATAENTRY._options = None
  _REPLICATIONSUMMARY_SUMMARYMETADATAENTRY._serialized_options = b'8\001'
  _REPLICATIONCONFIG._serialized_start=52
  _REPLICATIONCONFIG._serialized_end=386
  _REPLICATIONCONFIG_METADATAENTRY._serialized_start=339
  _REPLICATIONCONFIG_METADATAENTRY._serialized_end=386
  _REPLICATIONSTATUS._serialized_start=389
  _REPLICATIONSTATUS._serialized_end=731
  _REPLICATIONSTATUS_METADATAENTRY._serialized_start=339
  _REPLICATIONSTATUS_METADATAENTRY._serialized_end=386
  _REPLICATIONEVENTLOG._serialized_start=734
  _REPLICATIONEVENTLOG._serialized_end=972
  _REPLICATIONEVENTLOG_DETAILSENTRY._serialized_start=926
  _REPLICATIONEVENTLOG_DETAILSENTRY._serialized_end=972
  _REDUNDANCYMANAGER._serialized_start=975
  _REDUNDANCYMANAGER._serialized_end=1408
  _REDUNDANCYMANAGER_SEGMENTPRIORITYENTRY._serialized_start=1267
  _REDUNDANCYMANAGER_SEGMENTPRIORITYENTRY._serialized_end=1349
  _REDUNDANCYMANAGER_REDUNDANCYMETADATAENTRY._serialized_start=1351
  _REDUNDANCYMANAGER_REDUNDANCYMETADATAENTRY._serialized_end=1408
  _REPLICATIONESCALATION._serialized_start=1411
  _REPLICATIONESCALATION._serialized_end=1739
  _REPLICATIONESCALATION_METADATAENTRY._serialized_start=339
  _REPLICATIONESCALATION_METADATAENTRY._serialized_end=386
  _REPLICATIONSUMMARY._serialized_start=1742
  _REPLICATIONSUMMARY._serialized_end=2220
  _REPLICATIONSUMMARY_SEGMENTSTATUSESENTRY._serialized_start=2084
  _REPLICATIONSUMMARY_SEGMENTSTATUSESENTRY._serialized_end=2164
  _REPLICATIONSUMMARY_SUMMARYMETADATAENTRY._serialized_start=2166
  _REPLICATIONSUMMARY_SUMMARYMETADATAENTRY._serialized_end=2220
# @@protoc_insertion_point(module_scope)