# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interpretation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import access_control_pb2 as access__control__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x14interpretation.proto\x12\x05seigr\x1a\x14\x61\x63\x63\x65ss_control.proto"\x89\x05\n\x14InterpretationResult\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.seigr.InterpretationStatus\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x1b\n\x13interpreted_version\x18\x04 \x01(\t\x12H\n\x0f\x61\x64\x64itional_info\x18\x05 \x03(\x0b\x32/.seigr.InterpretationResult.AdditionalInfoEntry\x12\x16\n\x0einterpreter_id\x18\x06 \x01(\t\x12\x1a\n\x12requires_attention\x18\x07 \x01(\x08\x12\x42\n\x0clinked_files\x18\x08 \x03(\x0b\x32,.seigr.InterpretationResult.LinkedFilesEntry\x12\x16\n\x0esource_data_id\x18\t \x01(\t\x12\x16\n\x0epriority_level\x18\n \x01(\x05\x12T\n\x15\x63ontextual_conditions\x18\x0b \x03(\x0b\x32\x35.seigr.InterpretationResult.ContextualConditionsEntry\x12\x13\n\x0b\x65rror_codes\x18\x0c \x03(\t\x1a\x35\n\x13\x41\x64\x64itionalInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10LinkedFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x19\x43ontextualConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xbb\x04\n\tAccessLog\x12\x11\n\thyphen_id\x18\x01 \x01(\t\x12&\n\x0b\x61\x63\x63\x65ss_type\x18\x02 \x01(\x0e\x32\x11.seigr.AccessType\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x18\n\x10metadata_version\x18\x04 \x01(\t\x12\x0f\n\x07success\x18\x05 \x01(\x08\x12\x0f\n\x07\x64\x65tails\x18\x06 \x01(\t\x12\x0f\n\x07user_id\x18\x07 \x01(\t\x12\x30\n\x08metadata\x18\x08 \x03(\x0b\x32\x1e.seigr.AccessLog.MetadataEntry\x12\x17\n\x0f\x61\x63\x63\x65ss_location\x18\t \x01(\t\x12\x41\n\x11\x61\x63\x63\x65ss_conditions\x18\n \x03(\x0b\x32&.seigr.AccessLog.AccessConditionsEntry\x12\x13\n\x0bresult_code\x18\x0b \x01(\x05\x12I\n\x15\x65nvironmental_factors\x18\x0c \x03(\x0b\x32*.seigr.AccessLog.EnvironmentalFactorsEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15\x41\x63\x63\x65ssConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x19\x45nvironmentalFactorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xb9\x03\n\x12\x43ompatibilityCheck\x12\x18\n\x10metadata_version\x18\x01 \x01(\t\x12\x18\n\x10protocol_version\x18\x02 \x01(\t\x12\x1b\n\x13\x63ompatible_versions\x18\x03 \x03(\t\x12\x15\n\ris_compatible\x18\x04 \x01(\x08\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x1a\n\x12recommended_action\x18\x06 \x01(\t\x12\x15\n\rlast_verified\x18\x07 \x01(\t\x12\x18\n\x10\x66\x61llback_version\x18\x08 \x01(\t\x12N\n\x13\x63ompatibility_notes\x18\t \x03(\x0b\x32\x31.seigr.CompatibilityCheck.CompatibilityNotesEntry\x12\x1f\n\x17\x64\x65pendency_requirements\x18\n \x03(\t\x12\x18\n\x10\x66\x61llback_options\x18\x0b \x03(\t\x12\x17\n\x0frequires_update\x18\x0c \x01(\x08\x1a\x39\n\x17\x43ompatibilityNotesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x9a\x05\n\x13\x43\x61pabilityExpansion\x12\x16\n\x0etarget_version\x18\x01 \x01(\t\x12!\n\x19\x61\x64vanced_metadata_enabled\x18\x02 \x01(\x08\x12!\n\x19\x65nhanced_encoding_enabled\x18\x03 \x01(\x08\x12W\n\x17\x61\x64\x64itional_capabilities\x18\x04 \x03(\x0b\x32\x36.seigr.CapabilityExpansion.AdditionalCapabilitiesEntry\x12\x1b\n\x13\x65xpansion_timestamp\x18\x05 \x01(\t\x12\x14\n\x0c\x64\x65pendencies\x18\x06 \x03(\t\x12\x13\n\x0b\x65xpanded_by\x18\x07 \x01(\t\x12K\n\x11\x65xpansion_context\x18\x08 \x03(\x0b\x32\x30.seigr.CapabilityExpansion.ExpansionContextEntry\x12\x17\n\x0fis_experimental\x18\t \x01(\x08\x12\x1a\n\x12\x64\x65precation_notice\x18\n \x01(\t\x12O\n\x13\x66uture_capabilities\x18\x0b \x03(\x0b\x32\x32.seigr.CapabilityExpansion.FutureCapabilitiesEntry\x1a=\n\x1b\x41\x64\x64itionalCapabilitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15\x45xpansionContextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x39\n\x17\x46utureCapabilitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\xbc\x01\n\x14InterpretationStatus\x12#\n\x1fINTERPRETATION_STATUS_UNDEFINED\x10\x00\x12\x1a\n\x16INTERPRETATION_SUCCESS\x10\x01\x12\x1a\n\x16INTERPRETATION_WARNING\x10\x02\x12\x18\n\x14INTERPRETATION_ERROR\x10\x03\x12\x18\n\x14INCOMPATIBLE_VERSION\x10\x04\x12\x13\n\x0fPARTIAL_SUCCESS\x10\x05\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "interpretation_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _INTERPRETATIONRESULT_ADDITIONALINFOENTRY._options = None
    _INTERPRETATIONRESULT_ADDITIONALINFOENTRY._serialized_options = b"8\001"
    _INTERPRETATIONRESULT_LINKEDFILESENTRY._options = None
    _INTERPRETATIONRESULT_LINKEDFILESENTRY._serialized_options = b"8\001"
    _INTERPRETATIONRESULT_CONTEXTUALCONDITIONSENTRY._options = None
    _INTERPRETATIONRESULT_CONTEXTUALCONDITIONSENTRY._serialized_options = b"8\001"
    _ACCESSLOG_METADATAENTRY._options = None
    _ACCESSLOG_METADATAENTRY._serialized_options = b"8\001"
    _ACCESSLOG_ACCESSCONDITIONSENTRY._options = None
    _ACCESSLOG_ACCESSCONDITIONSENTRY._serialized_options = b"8\001"
    _ACCESSLOG_ENVIRONMENTALFACTORSENTRY._options = None
    _ACCESSLOG_ENVIRONMENTALFACTORSENTRY._serialized_options = b"8\001"
    _COMPATIBILITYCHECK_COMPATIBILITYNOTESENTRY._options = None
    _COMPATIBILITYCHECK_COMPATIBILITYNOTESENTRY._serialized_options = b"8\001"
    _CAPABILITYEXPANSION_ADDITIONALCAPABILITIESENTRY._options = None
    _CAPABILITYEXPANSION_ADDITIONALCAPABILITIESENTRY._serialized_options = b"8\001"
    _CAPABILITYEXPANSION_EXPANSIONCONTEXTENTRY._options = None
    _CAPABILITYEXPANSION_EXPANSIONCONTEXTENTRY._serialized_options = b"8\001"
    _CAPABILITYEXPANSION_FUTURECAPABILITIESENTRY._options = None
    _CAPABILITYEXPANSION_FUTURECAPABILITIESENTRY._serialized_options = b"8\001"
    _INTERPRETATIONSTATUS._serialized_start = 2393
    _INTERPRETATIONSTATUS._serialized_end = 2581
    _INTERPRETATIONRESULT._serialized_start = 54
    _INTERPRETATIONRESULT._serialized_end = 703
    _INTERPRETATIONRESULT_ADDITIONALINFOENTRY._serialized_start = 537
    _INTERPRETATIONRESULT_ADDITIONALINFOENTRY._serialized_end = 590
    _INTERPRETATIONRESULT_LINKEDFILESENTRY._serialized_start = 592
    _INTERPRETATIONRESULT_LINKEDFILESENTRY._serialized_end = 642
    _INTERPRETATIONRESULT_CONTEXTUALCONDITIONSENTRY._serialized_start = 644
    _INTERPRETATIONRESULT_CONTEXTUALCONDITIONSENTRY._serialized_end = 703
    _ACCESSLOG._serialized_start = 706
    _ACCESSLOG._serialized_end = 1277
    _ACCESSLOG_METADATAENTRY._serialized_start = 1112
    _ACCESSLOG_METADATAENTRY._serialized_end = 1159
    _ACCESSLOG_ACCESSCONDITIONSENTRY._serialized_start = 1161
    _ACCESSLOG_ACCESSCONDITIONSENTRY._serialized_end = 1216
    _ACCESSLOG_ENVIRONMENTALFACTORSENTRY._serialized_start = 1218
    _ACCESSLOG_ENVIRONMENTALFACTORSENTRY._serialized_end = 1277
    _COMPATIBILITYCHECK._serialized_start = 1280
    _COMPATIBILITYCHECK._serialized_end = 1721
    _COMPATIBILITYCHECK_COMPATIBILITYNOTESENTRY._serialized_start = 1664
    _COMPATIBILITYCHECK_COMPATIBILITYNOTESENTRY._serialized_end = 1721
    _CAPABILITYEXPANSION._serialized_start = 1724
    _CAPABILITYEXPANSION._serialized_end = 2390
    _CAPABILITYEXPANSION_ADDITIONALCAPABILITIESENTRY._serialized_start = 2213
    _CAPABILITYEXPANSION_ADDITIONALCAPABILITIESENTRY._serialized_end = 2274
    _CAPABILITYEXPANSION_EXPANSIONCONTEXTENTRY._serialized_start = 2276
    _CAPABILITYEXPANSION_EXPANSIONCONTEXTENTRY._serialized_end = 2331
    _CAPABILITYEXPANSION_FUTURECAPABILITIESENTRY._serialized_start = 2333
    _CAPABILITYEXPANSION_FUTURECAPABILITIESENTRY._serialized_end = 2390
# @@protoc_insertion_point(module_scope)
