# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: access_policies.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import access_control_pb2 as access__control__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15\x61\x63\x63\x65ss_policies.proto\x12\x05seigr\x1a\x14\x61\x63\x63\x65ss_control.proto"\xca\x02\n\x0f\x41\x63\x63\x65ssPolicySet\x12\x0e\n\x06set_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x08policies\x18\x03 \x03(\x0b\x32\x13.seigr.AccessPolicy\x12\x19\n\x11inherited_set_ids\x18\x04 \x03(\t\x12\x1d\n\x15max_inheritance_depth\x18\x05 \x01(\x05\x12\x0f\n\x07version\x18\x06 \x01(\t\x12\x15\n\rlast_reviewed\x18\x07 \x01(\t\x12\x36\n\x08metadata\x18\x08 \x03(\x0b\x32$.seigr.AccessPolicySet.MetadataEntry\x12\'\n\x1f\x63onditional_inheritance_enabled\x18\t \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x8c\x03\n\x12PolicyCheckRequest\x12\x14\n\x0crequester_id\x18\x01 \x01(\t\x12\x11\n\tpolicy_id\x18\x02 \x01(\t\x12!\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32\x11.seigr.ActionType\x12\x13\n\x0bresource_id\x18\x04 \x01(\t\x12\x37\n\x07\x63ontext\x18\x05 \x03(\x0b\x32&.seigr.PolicyCheckRequest.ContextEntry\x12,\n\x11requested_actions\x18\x06 \x03(\x0e\x32\x11.seigr.ActionType\x12\x12\n\nip_address\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65vice_info\x18\x08 \x01(\t\x12\x19\n\x11request_timestamp\x18\t \x01(\t\x12\x19\n\x11network_condition\x18\n \x01(\t\x12\x1f\n\x17\x65mergency_override_flag\x18\x0b \x01(\x08\x1a.\n\x0c\x43ontextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xbb\x03\n\x13PolicyCheckResponse\x12\x19\n\x11is_action_allowed\x18\x01 \x01(\x08\x12\x11\n\tpolicy_id\x18\x02 \x01(\t\x12*\n\rpolicy_status\x18\x03 \x01(\x0e\x32\x13.seigr.PolicyStatus\x12\x15\n\rdenial_reason\x18\x04 \x01(\t\x12,\n\x11permitted_actions\x18\x05 \x03(\x0e\x32\x11.seigr.ActionType\x12\x45\n\x0e\x61udit_metadata\x18\x06 \x03(\x0b\x32-.seigr.PolicyCheckResponse.AuditMetadataEntry\x12\x18\n\x10\x63ompliance_score\x18\x07 \x01(\x01\x12\x12\n\nrisk_score\x18\x08 \x01(\x01\x12\x1d\n\x15\x65scalation_suggestion\x18\t \x01(\t\x12\x1a\n\x12\x64\x65\x63ision_timestamp\x18\n \x01(\t\x12\x1f\n\x17\x65mergency_override_used\x18\x0b \x01(\x08\x1a\x34\n\x12\x41uditMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\xaf\x02\n\nActionType\x12\x19\n\x15\x41\x43TION_TYPE_UNDEFINED\x10\x00\x12\x14\n\x10\x41\x43TION_TYPE_READ\x10\x01\x12\x15\n\x11\x41\x43TION_TYPE_WRITE\x10\x02\x12\x17\n\x13\x41\x43TION_TYPE_EXECUTE\x10\x03\x12\x16\n\x12\x41\x43TION_TYPE_DELETE\x10\x04\x12\x15\n\x11\x41\x43TION_TYPE_SHARE\x10\x05\x12\x18\n\x14\x41\x43TION_TYPE_ROLLBACK\x10\x06\x12\x1d\n\x19\x41\x43TION_TYPE_MODIFY_POLICY\x10\x07\x12\x15\n\x11\x41\x43TION_TYPE_AUDIT\x10\x08\x12\x1f\n\x1b\x41\x43TION_TYPE_OVERRIDE_POLICY\x10\t\x12 \n\x1c\x41\x43TION_TYPE_EMERGENCY_ACCESS\x10\nb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "access_policies_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ACCESSPOLICYSET_METADATAENTRY._options = None
    _ACCESSPOLICYSET_METADATAENTRY._serialized_options = b"8\001"
    _POLICYCHECKREQUEST_CONTEXTENTRY._options = None
    _POLICYCHECKREQUEST_CONTEXTENTRY._serialized_options = b"8\001"
    _POLICYCHECKRESPONSE_AUDITMETADATAENTRY._options = None
    _POLICYCHECKRESPONSE_AUDITMETADATAENTRY._serialized_options = b"8\001"
    _ACTIONTYPE._serialized_start = 1233
    _ACTIONTYPE._serialized_end = 1536
    _ACCESSPOLICYSET._serialized_start = 55
    _ACCESSPOLICYSET._serialized_end = 385
    _ACCESSPOLICYSET_METADATAENTRY._serialized_start = 338
    _ACCESSPOLICYSET_METADATAENTRY._serialized_end = 385
    _POLICYCHECKREQUEST._serialized_start = 388
    _POLICYCHECKREQUEST._serialized_end = 784
    _POLICYCHECKREQUEST_CONTEXTENTRY._serialized_start = 738
    _POLICYCHECKREQUEST_CONTEXTENTRY._serialized_end = 784
    _POLICYCHECKRESPONSE._serialized_start = 787
    _POLICYCHECKRESPONSE._serialized_end = 1230
    _POLICYCHECKRESPONSE_AUDITMETADATAENTRY._serialized_start = 1178
    _POLICYCHECKRESPONSE_AUDITMETADATAENTRY._serialized_end = 1230
# @@protoc_insertion_point(module_scope)
