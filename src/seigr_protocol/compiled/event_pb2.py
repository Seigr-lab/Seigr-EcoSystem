# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65vent.proto\x12\x05seigr\x1a\x0c\x63ommon.proto\"\x81\x03\n\x05\x45vent\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x1e\n\x04type\x18\x02 \x01(\x0e\x32\x10.seigr.EventType\x12&\n\x08priority\x18\x03 \x01(\x0e\x32\x14.seigr.PriorityLevel\x12\x30\n\x10\x65scalation_level\x18\x04 \x01(\x0e\x32\x16.seigr.EscalationLevel\x12\x0e\n\x06origin\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12,\n\x08metadata\x18\x08 \x03(\x0b\x32\x1a.seigr.Event.MetadataEntry\x12\x1a\n\x12target_subscribers\x18\t \x03(\t\x12\x1f\n\x17requires_acknowledgment\x18\n \x01(\x08\x12\x18\n\x10\x61llow_forwarding\x18\x0b \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd4\x03\n\x11\x45ventSubscription\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\t\x12\x15\n\rsubscriber_id\x18\x02 \x01(\t\x12%\n\x0b\x65vent_types\x18\x03 \x03(\x0e\x32\x10.seigr.EventType\x12\x36\n\x07\x66ilters\x18\x04 \x03(\x0b\x32%.seigr.EventSubscription.FiltersEntry\x12\x14\n\x0c\x63\x61llback_url\x18\x05 \x01(\t\x12Q\n\x15subscription_metadata\x18\x06 \x03(\x0b\x32\x32.seigr.EventSubscription.SubscriptionMetadataEntry\x12\x14\n\x0clast_updated\x18\x07 \x01(\t\x12\x34\n\x14min_escalation_level\x18\x08 \x01(\x0e\x32\x16.seigr.EscalationLevel\x12\x0e\n\x06\x61\x63tive\x18\t \x01(\x08\x1a.\n\x0c\x46iltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x19SubscriptionMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xfa\x02\n\rEventResponse\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\x12\x14\n\x0cresponder_id\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x63tion_taken\x18\x04 \x01(\t\x12\x1a\n\x12response_timestamp\x18\x05 \x01(\t\x12\x45\n\x11response_metadata\x18\x06 \x03(\x0b\x32*.seigr.EventResponse.ResponseMetadataEntry\x12\x1a\n\x12requires_follow_up\x18\x07 \x01(\x08\x12\x1b\n\x13\x66ollow_up_action_id\x18\x08 \x01(\t\x12/\n\x0f\x65scalation_path\x18\t \x01(\x0e\x32\x16.seigr.EscalationLevel\x12\x10\n\x08resolved\x18\n \x01(\x08\x1a\x37\n\x15ResponseMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa0\x02\n\x10\x45scalationConfig\x12%\n\x05level\x18\x01 \x01(\x0e\x32\x16.seigr.EscalationLevel\x12\x1a\n\x12\x65scalation_path_id\x18\x02 \x01(\t\x12;\n\nconditions\x18\x03 \x03(\x0b\x32\'.seigr.EscalationConfig.ConditionsEntry\x12\x18\n\x10\x61lert_recipients\x18\x04 \x03(\t\x12\x1b\n\x13\x65scalation_strategy\x18\x05 \x01(\t\x12\"\n\x1a\x65nable_automatic_responses\x18\x06 \x01(\x08\x1a\x31\n\x0f\x43onditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa1\x02\n\x08\x45ventLog\x12\x0e\n\x06log_id\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\x12\x11\n\tlogged_at\x18\x03 \x01(\t\x12\x11\n\tlogger_id\x18\x04 \x01(\t\x12\x13\n\x0blog_message\x18\x05 \x01(\t\x12\x36\n\x0clog_metadata\x18\x06 \x03(\x0b\x32 .seigr.EventLog.LogMetadataEntry\x12\x37\n\x17logged_escalation_level\x18\x07 \x01(\x0e\x32\x16.seigr.EscalationLevel\x12\x13\n\x0bis_resolved\x18\x08 \x01(\x08\x1a\x32\n\x10LogMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"L\n\x0fSubscriptionAck\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\"_\n\x12\x41\x63knowledgeRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x15\n\rsubscriber_id\x18\x02 \x01(\t\x12 \n\x18\x61\x63knowledgment_timestamp\x18\x03 \x01(\t\"7\n\x13\x41\x63knowledgeResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"f\n\x0f\x45ventLogRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x18\n\x10time_range_start\x18\x02 \x01(\t\x12\x16\n\x0etime_range_end\x18\x03 \x01(\t\x12\x0f\n\x07\x66ilters\x18\x04 \x03(\t\"R\n\x10\x45ventLogResponse\x12\x1d\n\x04logs\x18\x01 \x03(\x0b\x32\x0f.seigr.EventLog\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t*\x85\x02\n\tEventType\x12\x18\n\x14\x45VENT_TYPE_UNDEFINED\x10\x00\x12\x14\n\x10\x45VENT_TYPE_ERROR\x10\x01\x12\x14\n\x10\x45VENT_TYPE_ALERT\x10\x02\x12\x1a\n\x16\x45VENT_TYPE_USER_ACTION\x10\x03\x12)\n%EVENT_TYPE_RESOURCE_THRESHOLD_REACHED\x10\x04\x12\x1c\n\x18\x45VENT_TYPE_SYSTEM_UPDATE\x10\x05\x12\x19\n\x15\x45VENT_TYPE_MONITORING\x10\x06\x12\x1b\n\x17\x45VENT_TYPE_SELF_HEALING\x10\x07\x12\x15\n\x11\x45VENT_TYPE_CUSTOM\x10\x08*\x9d\x01\n\x0f\x45scalationLevel\x12\x19\n\x15\x45SCALATION_LEVEL_NONE\x10\x00\x12\x18\n\x14\x45SCALATION_LEVEL_LOW\x10\x01\x12\x1b\n\x17\x45SCALATION_LEVEL_MEDIUM\x10\x02\x12\x19\n\x15\x45SCALATION_LEVEL_HIGH\x10\x03\x12\x1d\n\x19\x45SCALATION_LEVEL_CRITICAL\x10\x04\x32\x99\x02\n\x0c\x45ventService\x12\x32\n\x0cPublishEvent\x12\x0c.seigr.Event\x1a\x14.seigr.EventResponse\x12\x45\n\x11SubscribeToEvents\x12\x18.seigr.EventSubscription\x1a\x16.seigr.SubscriptionAck\x12I\n\x10\x41\x63knowledgeEvent\x12\x19.seigr.AcknowledgeRequest\x1a\x1a.seigr.AcknowledgeResponse\x12\x43\n\x10RetrieveEventLog\x12\x16.seigr.EventLogRequest\x1a\x17.seigr.EventLogResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENT_METADATAENTRY._options = None
  _EVENT_METADATAENTRY._serialized_options = b'8\001'
  _EVENTSUBSCRIPTION_FILTERSENTRY._options = None
  _EVENTSUBSCRIPTION_FILTERSENTRY._serialized_options = b'8\001'
  _EVENTSUBSCRIPTION_SUBSCRIPTIONMETADATAENTRY._options = None
  _EVENTSUBSCRIPTION_SUBSCRIPTIONMETADATAENTRY._serialized_options = b'8\001'
  _EVENTRESPONSE_RESPONSEMETADATAENTRY._options = None
  _EVENTRESPONSE_RESPONSEMETADATAENTRY._serialized_options = b'8\001'
  _ESCALATIONCONFIG_CONDITIONSENTRY._options = None
  _ESCALATIONCONFIG_CONDITIONSENTRY._serialized_options = b'8\001'
  _EVENTLOG_LOGMETADATAENTRY._options = None
  _EVENTLOG_LOGMETADATAENTRY._serialized_options = b'8\001'
  _EVENTTYPE._serialized_start=2280
  _EVENTTYPE._serialized_end=2541
  _ESCALATIONLEVEL._serialized_start=2544
  _ESCALATIONLEVEL._serialized_end=2701
  _EVENT._serialized_start=37
  _EVENT._serialized_end=422
  _EVENT_METADATAENTRY._serialized_start=375
  _EVENT_METADATAENTRY._serialized_end=422
  _EVENTSUBSCRIPTION._serialized_start=425
  _EVENTSUBSCRIPTION._serialized_end=893
  _EVENTSUBSCRIPTION_FILTERSENTRY._serialized_start=786
  _EVENTSUBSCRIPTION_FILTERSENTRY._serialized_end=832
  _EVENTSUBSCRIPTION_SUBSCRIPTIONMETADATAENTRY._serialized_start=834
  _EVENTSUBSCRIPTION_SUBSCRIPTIONMETADATAENTRY._serialized_end=893
  _EVENTRESPONSE._serialized_start=896
  _EVENTRESPONSE._serialized_end=1274
  _EVENTRESPONSE_RESPONSEMETADATAENTRY._serialized_start=1219
  _EVENTRESPONSE_RESPONSEMETADATAENTRY._serialized_end=1274
  _ESCALATIONCONFIG._serialized_start=1277
  _ESCALATIONCONFIG._serialized_end=1565
  _ESCALATIONCONFIG_CONDITIONSENTRY._serialized_start=1516
  _ESCALATIONCONFIG_CONDITIONSENTRY._serialized_end=1565
  _EVENTLOG._serialized_start=1568
  _EVENTLOG._serialized_end=1857
  _EVENTLOG_LOGMETADATAENTRY._serialized_start=1807
  _EVENTLOG_LOGMETADATAENTRY._serialized_end=1857
  _SUBSCRIPTIONACK._serialized_start=1859
  _SUBSCRIPTIONACK._serialized_end=1935
  _ACKNOWLEDGEREQUEST._serialized_start=1937
  _ACKNOWLEDGEREQUEST._serialized_end=2032
  _ACKNOWLEDGERESPONSE._serialized_start=2034
  _ACKNOWLEDGERESPONSE._serialized_end=2089
  _EVENTLOGREQUEST._serialized_start=2091
  _EVENTLOGREQUEST._serialized_end=2193
  _EVENTLOGRESPONSE._serialized_start=2195
  _EVENTLOGRESPONSE._serialized_end=2277
  _EVENTSERVICE._serialized_start=2704
  _EVENTSERVICE._serialized_end=2985
# @@protoc_insertion_point(module_scope)