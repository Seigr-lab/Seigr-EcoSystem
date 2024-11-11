# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import access_control_pb2 as access__control__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eidentity.proto\x12\x05seigr\x1a\x14\x61\x63\x63\x65ss_control.proto\"\xf8\x02\n\rAliasIdentity\x12\x10\n\x08\x61lias_id\x18\x01 \x01(\t\x12%\n\x06status\x18\x02 \x01(\x0e\x32\x15.seigr.IdentityStatus\x12*\n\rprivacy_level\x18\x03 \x01(\x0e\x32\x13.seigr.PrivacyLevel\x12*\n\ridentity_type\x18\x04 \x01(\x0e\x32\x13.seigr.IdentityType\x12\x12\n\nalias_name\x18\x05 \x01(\t\x12\x17\n\x0f\x61lias_signature\x18\x06 \x01(\t\x12\x32\n\x15\x61lias_access_policies\x18\x07 \x03(\x0b\x32\x13.seigr.AccessPolicy\x12?\n\x0e\x61lias_metadata\x18\x08 \x03(\x0b\x32\'.seigr.AliasIdentity.AliasMetadataEntry\x1a\x34\n\x12\x41liasMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd6\x01\n\x10IdentityAuditLog\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x14\n\x0cperformed_by\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x05 \x01(\t\x12\x37\n\x08metadata\x18\x06 \x03(\x0b\x32%.seigr.IdentityAuditLog.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa4\x07\n\x11SeigrIdentityData\x12\x1a\n\x12\x63reation_timestamp\x18\x01 \x01(\x03\x12*\n\ridentity_type\x18\x02 \x01(\x0e\x32\x13.seigr.IdentityType\x12%\n\x06status\x18\x03 \x01(\x0e\x32\x15.seigr.IdentityStatus\x12\x11\n\tsenary_id\x18\x04 \x01(\x0c\x12\x18\n\x10owner_public_key\x18\x05 \x01(\x0c\x12\x1d\n\x15\x65ncrypted_private_key\x18\x06 \x01(\x0c\x12\x17\n\x0fowner_signature\x18\x07 \x01(\x0c\x12\x0f\n\x07revoked\x18\x08 \x01(\x08\x12\x19\n\x11revocation_reason\x18\t \x01(\t\x12\x1a\n\x12verification_level\x18\n \x01(\t\x12,\n\x0f\x61\x63\x63\x65ss_policies\x18\x0b \x03(\x0b\x32\x13.seigr.AccessPolicy\x12+\n\naudit_logs\x18\x0c \x03(\x0b\x32\x17.seigr.IdentityAuditLog\x12Q\n\x15verification_metadata\x18\r \x03(\x0b\x32\x32.seigr.SeigrIdentityData.VerificationMetadataEntry\x12\x0f\n\x07version\x18\x0e \x01(\t\x12\x38\n\x08metadata\x18\x0f \x03(\x0b\x32&.seigr.SeigrIdentityData.MetadataEntry\x12\x16\n\x0e\x65ncryption_key\x18\x10 \x01(\x0c\x12\x10\n\x08usb_path\x18\x11 \x01(\t\x12\x14\n\x0cusb_required\x18\x12 \x01(\x08\x12\x1b\n\x13last_used_timestamp\x18\x13 \x01(\t\x12M\n\x13security_parameters\x18\x14 \x03(\x0b\x32\x30.seigr.SeigrIdentityData.SecurityParametersEntry\x12%\n\x07\x61liases\x18\x15 \x03(\x0b\x32\x14.seigr.AliasIdentity\x1a;\n\x19VerificationMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x39\n\x17SecurityParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*q\n\x0eIdentityStatus\x12\x1d\n\x19IDENTITY_STATUS_UNDEFINED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\r\n\tSUSPENDED\x10\x02\x12\x0b\n\x07REVOKED\x10\x03\x12\x18\n\x14PENDING_VERIFICATION\x10\x04*^\n\x0cIdentityType\x12\x1b\n\x17IDENTITY_TYPE_UNDEFINED\x10\x00\x12\x08\n\x04USER\x10\x01\x12\n\n\x06SENSOR\x10\x02\x12\n\n\x06SERVER\x10\x03\x12\x0f\n\x0b\x41PPLICATION\x10\x04*U\n\x0cPrivacyLevel\x12\n\n\x06PUBLIC\x10\x00\x12\x11\n\rPARTIAL_TRACE\x10\x01\x12\x12\n\x0eSEMI_ANONYMOUS\x10\x02\x12\x12\n\x0e\x46ULL_ANONYMOUS\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'identity_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ALIASIDENTITY_ALIASMETADATAENTRY._options = None
  _ALIASIDENTITY_ALIASMETADATAENTRY._serialized_options = b'8\001'
  _IDENTITYAUDITLOG_METADATAENTRY._options = None
  _IDENTITYAUDITLOG_METADATAENTRY._serialized_options = b'8\001'
  _SEIGRIDENTITYDATA_VERIFICATIONMETADATAENTRY._options = None
  _SEIGRIDENTITYDATA_VERIFICATIONMETADATAENTRY._serialized_options = b'8\001'
  _SEIGRIDENTITYDATA_METADATAENTRY._options = None
  _SEIGRIDENTITYDATA_METADATAENTRY._serialized_options = b'8\001'
  _SEIGRIDENTITYDATA_SECURITYPARAMETERSENTRY._options = None
  _SEIGRIDENTITYDATA_SECURITYPARAMETERSENTRY._serialized_options = b'8\001'
  _IDENTITYSTATUS._serialized_start=1578
  _IDENTITYSTATUS._serialized_end=1691
  _IDENTITYTYPE._serialized_start=1693
  _IDENTITYTYPE._serialized_end=1787
  _PRIVACYLEVEL._serialized_start=1789
  _PRIVACYLEVEL._serialized_end=1874
  _ALIASIDENTITY._serialized_start=48
  _ALIASIDENTITY._serialized_end=424
  _ALIASIDENTITY_ALIASMETADATAENTRY._serialized_start=372
  _ALIASIDENTITY_ALIASMETADATAENTRY._serialized_end=424
  _IDENTITYAUDITLOG._serialized_start=427
  _IDENTITYAUDITLOG._serialized_end=641
  _IDENTITYAUDITLOG_METADATAENTRY._serialized_start=594
  _IDENTITYAUDITLOG_METADATAENTRY._serialized_end=641
  _SEIGRIDENTITYDATA._serialized_start=644
  _SEIGRIDENTITYDATA._serialized_end=1576
  _SEIGRIDENTITYDATA_VERIFICATIONMETADATAENTRY._serialized_start=1409
  _SEIGRIDENTITYDATA_VERIFICATIONMETADATAENTRY._serialized_end=1468
  _SEIGRIDENTITYDATA_METADATAENTRY._serialized_start=594
  _SEIGRIDENTITYDATA_METADATAENTRY._serialized_end=641
  _SEIGRIDENTITYDATA_SECURITYPARAMETERSENTRY._serialized_start=1519
  _SEIGRIDENTITYDATA_SECURITYPARAMETERSENTRY._serialized_end=1576
# @@protoc_insertion_point(module_scope)