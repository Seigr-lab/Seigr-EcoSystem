# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: encryption.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from src.seigr_protocol.compiled import hashing_pb2 as hashing__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x65ncryption.proto\x12\x05seigr\x1a\rhashing.proto\"\xea\x02\n\x0cSymmetricKey\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0c\n\x04salt\x18\x03 \x01(\x0c\x12\x11\n\talgorithm\x18\x04 \x01(\t\x12\x1a\n\x12\x63reation_timestamp\x18\x05 \x01(\t\x12\x1c\n\x14\x65xpiration_timestamp\x18\x06 \x01(\t\x12\x18\n\x10lifecycle_status\x18\x07 \x01(\t\x12\x1a\n\x12rotation_frequency\x18\x08 \x01(\t\x12\x12\n\nkey_source\x18\t \x01(\t\x12\x11\n\tcustodian\x18\n \x01(\t\x12\x33\n\x08metadata\x18\x0b \x03(\x0b\x32!.seigr.SymmetricKey.MetadataEntry\x12\x1f\n\x17\x63ompliance_requirements\x18\x0c \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xdd\x02\n\x11\x41symmetricKeyPair\x12\x13\n\x0bkey_pair_id\x18\x01 \x01(\t\x12\x12\n\npublic_key\x18\x02 \x01(\x0c\x12\x13\n\x0bprivate_key\x18\x03 \x01(\x0c\x12\x11\n\talgorithm\x18\x04 \x01(\t\x12\x1a\n\x12\x63reation_timestamp\x18\x05 \x01(\t\x12\x1c\n\x14\x65xpiration_timestamp\x18\x06 \x01(\t\x12\x18\n\x10lifecycle_status\x18\x07 \x01(\t\x12\x17\n\x0frotation_policy\x18\x08 \x01(\t\x12\x38\n\x08metadata\x18\t \x03(\x0b\x32&.seigr.AsymmetricKeyPair.MetadataEntry\x12\x1f\n\x17\x63ompliance_requirements\x18\n \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xae\x02\n\x13HybridEncryptionKey\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12*\n\rsymmetric_key\x18\x02 \x01(\x0b\x32\x13.seigr.SymmetricKey\x12\x31\n\x0f\x61symmetric_keys\x18\x03 \x01(\x0b\x32\x18.seigr.AsymmetricKeyPair\x12\x1a\n\x12\x63reation_timestamp\x18\x04 \x01(\t\x12:\n\x08metadata\x18\x05 \x03(\x0b\x32(.seigr.HybridEncryptionKey.MetadataEntry\x12\x1f\n\x17\x63ompliance_requirements\x18\x06 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x92\x02\n\rEncryptedData\x12\x12\n\nciphertext\x18\x01 \x01(\x0c\x12\n\n\x02iv\x18\x02 \x01(\x0c\x12.\n\x0f\x65ncryption_type\x18\x03 \x01(\x0e\x32\x15.seigr.EncryptionType\x12\x0e\n\x06key_id\x18\x04 \x01(\t\x12\x34\n\x08metadata\x18\x05 \x03(\x0b\x32\".seigr.EncryptedData.MetadataEntry\x12\x1c\n\x14\x65ncryption_timestamp\x18\x06 \x01(\t\x12\x1c\n\x14\x65ncryption_policy_id\x18\x07 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa3\x02\n\x0cSignatureLog\x12\x0e\n\x06log_id\x18\x01 \x01(\t\x12\x11\n\tsigner_id\x18\x02 \x01(\t\x12\x11\n\tsignature\x18\x03 \x01(\x0c\x12\x19\n\x11signing_algorithm\x18\x04 \x01(\t\x12\x18\n\x10signed_data_hash\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\t\x12\x16\n\x0ekey_provenance\x18\x07 \x01(\t\x12\x33\n\x08metadata\x18\x08 \x03(\x0b\x32!.seigr.SignatureLog.MetadataEntry\x12\x17\n\x0f\x63ompliance_note\x18\t \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa6\x03\n\x18IntegrityVerificationLog\x12\x17\n\x0fverification_id\x18\x01 \x01(\t\x12\x12\n\nsegment_id\x18\x02 \x01(\t\x12,\n\x0ehash_algorithm\x18\x03 \x01(\x0e\x32\x14.seigr.HashAlgorithm\x12\x32\n\x0fverified_status\x18\x04 \x01(\x0e\x32\x19.seigr.VerificationStatus\x12\x1e\n\x16verification_timestamp\x18\x05 \x01(\t\x12\x1a\n\x12verification_depth\x18\x06 \x01(\t\x12\x15\n\rerror_message\x18\x07 \x01(\t\x12\x1e\n\x16parent_verification_id\x18\x08 \x01(\t\x12\x16\n\x0eretry_attempts\x18\t \x01(\x05\x12?\n\x08metadata\x18\n \x03(\x0b\x32-.seigr.IntegrityVerificationLog.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb8\x03\n\x16\x43ryptographicOperation\x12\x14\n\x0coperation_id\x18\x01 \x01(\t\x12.\n\x0f\x65ncryption_type\x18\x02 \x01(\x0e\x32\x15.seigr.EncryptionType\x12\x39\n\x0eoperation_type\x18\x03 \x01(\x0e\x32!.seigr.CryptographicOperationType\x12\x12\n\ninput_data\x18\x04 \x01(\x0c\x12\x13\n\x0bresult_data\x18\x05 \x01(\x0c\x12\x0e\n\x06key_id\x18\x06 \x01(\t\x12\x1b\n\x13operation_timestamp\x18\x07 \x01(\t\x12\x1f\n\x17operation_result_status\x18\x08 \x01(\t\x12\x12\n\nerror_code\x18\t \x01(\t\x12\"\n\x1aoperation_duration_seconds\x18\n \x01(\x01\x12=\n\x08metadata\x18\x0b \x03(\x0b\x32+.seigr.CryptographicOperation.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf1\x01\n\x11\x45ncryptedHashData\x12\"\n\thash_info\x18\x01 \x01(\x0b\x32\x0f.seigr.HashData\x12.\n\x0f\x65ncryption_type\x18\x02 \x01(\x0e\x32\x15.seigr.EncryptionType\x12M\n\x13\x61\x64\x64itional_metadata\x18\x03 \x03(\x0b\x32\x30.seigr.EncryptedHashData.AdditionalMetadataEntry\x1a\x39\n\x17\x41\x64\x64itionalMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\x8a\x01\n\x0e\x45ncryptionType\x12\x1d\n\x19\x45NCRYPTION_TYPE_UNDEFINED\x10\x00\x12\x1d\n\x19\x45NCRYPTION_TYPE_SYMMETRIC\x10\x01\x12\x1e\n\x1a\x45NCRYPTION_TYPE_ASYMMETRIC\x10\x02\x12\x1a\n\x16\x45NCRYPTION_TYPE_HYBRID\x10\x03*\xd6\x01\n\x1a\x43ryptographicOperationType\x12\x1c\n\x18OPERATION_TYPE_UNDEFINED\x10\x00\x12\x1d\n\x19OPERATION_TYPE_ENCRYPTION\x10\x01\x12\x1d\n\x19OPERATION_TYPE_DECRYPTION\x10\x02\x12\x1a\n\x16OPERATION_TYPE_SIGNING\x10\x03\x12\x1f\n\x1bOPERATION_TYPE_VERIFICATION\x10\x04\x12\x1f\n\x1bOPERATION_TYPE_KEY_ROTATION\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'encryption_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYMMETRICKEY_METADATAENTRY._options = None
  _SYMMETRICKEY_METADATAENTRY._serialized_options = b'8\001'
  _ASYMMETRICKEYPAIR_METADATAENTRY._options = None
  _ASYMMETRICKEYPAIR_METADATAENTRY._serialized_options = b'8\001'
  _HYBRIDENCRYPTIONKEY_METADATAENTRY._options = None
  _HYBRIDENCRYPTIONKEY_METADATAENTRY._serialized_options = b'8\001'
  _ENCRYPTEDDATA_METADATAENTRY._options = None
  _ENCRYPTEDDATA_METADATAENTRY._serialized_options = b'8\001'
  _SIGNATURELOG_METADATAENTRY._options = None
  _SIGNATURELOG_METADATAENTRY._serialized_options = b'8\001'
  _INTEGRITYVERIFICATIONLOG_METADATAENTRY._options = None
  _INTEGRITYVERIFICATIONLOG_METADATAENTRY._serialized_options = b'8\001'
  _CRYPTOGRAPHICOPERATION_METADATAENTRY._options = None
  _CRYPTOGRAPHICOPERATION_METADATAENTRY._serialized_options = b'8\001'
  _ENCRYPTEDHASHDATA_ADDITIONALMETADATAENTRY._options = None
  _ENCRYPTEDHASHDATA_ADDITIONALMETADATAENTRY._serialized_options = b'8\001'
  _ENCRYPTIONTYPE._serialized_start=2748
  _ENCRYPTIONTYPE._serialized_end=2886
  _CRYPTOGRAPHICOPERATIONTYPE._serialized_start=2889
  _CRYPTOGRAPHICOPERATIONTYPE._serialized_end=3103
  _SYMMETRICKEY._serialized_start=43
  _SYMMETRICKEY._serialized_end=405
  _SYMMETRICKEY_METADATAENTRY._serialized_start=358
  _SYMMETRICKEY_METADATAENTRY._serialized_end=405
  _ASYMMETRICKEYPAIR._serialized_start=408
  _ASYMMETRICKEYPAIR._serialized_end=757
  _ASYMMETRICKEYPAIR_METADATAENTRY._serialized_start=358
  _ASYMMETRICKEYPAIR_METADATAENTRY._serialized_end=405
  _HYBRIDENCRYPTIONKEY._serialized_start=760
  _HYBRIDENCRYPTIONKEY._serialized_end=1062
  _HYBRIDENCRYPTIONKEY_METADATAENTRY._serialized_start=358
  _HYBRIDENCRYPTIONKEY_METADATAENTRY._serialized_end=405
  _ENCRYPTEDDATA._serialized_start=1065
  _ENCRYPTEDDATA._serialized_end=1339
  _ENCRYPTEDDATA_METADATAENTRY._serialized_start=358
  _ENCRYPTEDDATA_METADATAENTRY._serialized_end=405
  _SIGNATURELOG._serialized_start=1342
  _SIGNATURELOG._serialized_end=1633
  _SIGNATURELOG_METADATAENTRY._serialized_start=358
  _SIGNATURELOG_METADATAENTRY._serialized_end=405
  _INTEGRITYVERIFICATIONLOG._serialized_start=1636
  _INTEGRITYVERIFICATIONLOG._serialized_end=2058
  _INTEGRITYVERIFICATIONLOG_METADATAENTRY._serialized_start=358
  _INTEGRITYVERIFICATIONLOG_METADATAENTRY._serialized_end=405
  _CRYPTOGRAPHICOPERATION._serialized_start=2061
  _CRYPTOGRAPHICOPERATION._serialized_end=2501
  _CRYPTOGRAPHICOPERATION_METADATAENTRY._serialized_start=358
  _CRYPTOGRAPHICOPERATION_METADATAENTRY._serialized_end=405
  _ENCRYPTEDHASHDATA._serialized_start=2504
  _ENCRYPTEDHASHDATA._serialized_end=2745
  _ENCRYPTEDHASHDATA_ADDITIONALMETADATAENTRY._serialized_start=2688
  _ENCRYPTEDHASHDATA_ADDITIONALMETADATAENTRY._serialized_end=2745
# @@protoc_insertion_point(module_scope)
