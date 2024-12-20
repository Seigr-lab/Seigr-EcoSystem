# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_management.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import access_control_pb2 as access__control__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15user_management.proto\x12\x05seigr\x1a\x14\x61\x63\x63\x65ss_control.proto"\xbb\x04\n\x0bUserProfile\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x1e\n\x05roles\x18\x04 \x03(\x0e\x32\x0f.seigr.RoleType\x12,\n\x0e\x61\x63\x63ount_status\x18\x05 \x01(\x0e\x32\x14.seigr.AccountStatus\x12\x30\n\x0b\x61uth_method\x18\x06 \x01(\x0e\x32\x1b.seigr.AuthenticationMethod\x12\x12\n\ncreated_at\x18\x07 \x01(\t\x12\x12\n\nlast_login\x18\x08 \x01(\t\x12\x41\n\x10profile_metadata\x18\t \x03(\x0b\x32\'.seigr.UserProfile.ProfileMetadataEntry\x12;\n\rsecurity_keys\x18\n \x03(\x0b\x32$.seigr.UserProfile.SecurityKeysEntry\x12\x1e\n\x16\x61\x63\x63ount_recovery_email\x18\x0b \x01(\t\x12\x14\n\x0cphone_number\x18\x0c \x01(\t\x12\x19\n\x11profile_image_url\x18\r \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x0e \x01(\t\x1a\x36\n\x14ProfileMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x33\n\x11SecurityKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01"\x9f\x03\n\x0fUserPermissions\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12*\n\x0bpermissions\x18\x02 \x03(\x0e\x32\x15.seigr.PermissionType\x12\x34\n\x07\x63ontext\x18\x03 \x03(\x0b\x32#.seigr.UserPermissions.ContextEntry\x12\x0e\n\x06\x65xpiry\x18\x04 \x01(\t\x12\x19\n\x11is_admin_override\x18\x05 \x01(\x08\x12O\n\x15resource_restrictions\x18\x06 \x03(\x0b\x32\x30.seigr.UserPermissions.ResourceRestrictionsEntry\x12\x1a\n\x12\x61uthorized_devices\x18\x07 \x03(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_zones\x18\x08 \x03(\t\x1a.\n\x0c\x43ontextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x19ResourceRestrictionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01"\x9f\x02\n\rUserAccessLog\x12\x0e\n\x06log_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x13\n\x0bresource_id\x18\x05 \x01(\t\x12\x0f\n\x07success\x18\x06 \x01(\x08\x12\x34\n\x08metadata\x18\x07 \x03(\x0b\x32".seigr.UserAccessLog.MetadataEntry\x12\x11\n\tdevice_id\x18\x08 \x01(\t\x12\x12\n\nsession_id\x18\t \x01(\t\x12\x16\n\x0e\x66\x61ilure_reason\x18\n \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x8d\x04\n\x0fUserPreferences\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x31\n\x0c\x61uth_methods\x18\x02 \x03(\x0e\x32\x1b.seigr.AuthenticationMethod\x12\x1a\n\x12two_factor_enabled\x18\x03 \x01(\x08\x12\x1a\n\x12preferred_language\x18\x04 \x01(\t\x12\x1d\n\x15receive_notifications\x18\x05 \x01(\x08\x12U\n\x18permission_notifications\x18\x06 \x03(\x0b\x32\x33.seigr.UserPreferences.PermissionNotificationsEntry\x12G\n\x11ui_customizations\x18\x07 \x03(\x0b\x32,.seigr.UserPreferences.UiCustomizationsEntry\x12\x10\n\x08timezone\x18\x08 \x01(\t\x12\x19\n\x11\x64\x61rk_mode_enabled\x18\t \x01(\x08\x12\x19\n\x11\x66\x61vorite_features\x18\n \x03(\t\x1a>\n\x1cPermissionNotificationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x37\n\x15UiCustomizationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xd8\x02\n\x0eUserManagement\x12$\n\x08profiles\x18\x01 \x03(\x0b\x32\x12.seigr.UserProfile\x12+\n\x0bpermissions\x18\x02 \x03(\x0b\x32\x16.seigr.UserPermissions\x12+\n\x0bpreferences\x18\x03 \x03(\x0b\x32\x16.seigr.UserPreferences\x12)\n\x0b\x61\x63\x63\x65ss_logs\x18\x04 \x03(\x0b\x32\x14.seigr.UserAccessLog\x12\x14\n\x0clast_updated\x18\x05 \x01(\t\x12J\n\x13management_metadata\x18\x06 \x03(\x0b\x32-.seigr.UserManagement.ManagementMetadataEntry\x1a\x39\n\x17ManagementMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\xa7\x01\n\rAccountStatus\x12\x1c\n\x18\x41\x43\x43OUNT_STATUS_UNDEFINED\x10\x00\x12\x12\n\x0e\x41\x43\x43OUNT_ACTIVE\x10\x01\x12\x15\n\x11\x41\x43\x43OUNT_SUSPENDED\x10\x02\x12\x17\n\x13\x41\x43\x43OUNT_DEACTIVATED\x10\x03\x12 \n\x1c\x41\x43\x43OUNT_PENDING_VERIFICATION\x10\x04\x12\x12\n\x0e\x41\x43\x43OUNT_LOCKED\x10\x05*\x93\x01\n\x14\x41uthenticationMethod\x12\x12\n\x0e\x41UTH_UNDEFINED\x10\x00\x12\x11\n\rAUTH_PASSWORD\x10\x01\x12\x12\n\x0e\x41UTH_BIOMETRIC\x10\x02\x12\x0c\n\x08\x41UTH_OTP\x10\x03\x12\x0e\n\nAUTH_TOKEN\x10\x04\x12\x14\n\x10\x41UTH_CERTIFICATE\x10\x05\x12\x0c\n\x08\x41UTH_SSO\x10\x06\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "user_management_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _USERPROFILE_PROFILEMETADATAENTRY._options = None
    _USERPROFILE_PROFILEMETADATAENTRY._serialized_options = b"8\001"
    _USERPROFILE_SECURITYKEYSENTRY._options = None
    _USERPROFILE_SECURITYKEYSENTRY._serialized_options = b"8\001"
    _USERPERMISSIONS_CONTEXTENTRY._options = None
    _USERPERMISSIONS_CONTEXTENTRY._serialized_options = b"8\001"
    _USERPERMISSIONS_RESOURCERESTRICTIONSENTRY._options = None
    _USERPERMISSIONS_RESOURCERESTRICTIONSENTRY._serialized_options = b"8\001"
    _USERACCESSLOG_METADATAENTRY._options = None
    _USERACCESSLOG_METADATAENTRY._serialized_options = b"8\001"
    _USERPREFERENCES_PERMISSIONNOTIFICATIONSENTRY._options = None
    _USERPREFERENCES_PERMISSIONNOTIFICATIONSENTRY._serialized_options = b"8\001"
    _USERPREFERENCES_UICUSTOMIZATIONSENTRY._options = None
    _USERPREFERENCES_UICUSTOMIZATIONSENTRY._serialized_options = b"8\001"
    _USERMANAGEMENT_MANAGEMENTMETADATAENTRY._options = None
    _USERMANAGEMENT_MANAGEMENTMETADATAENTRY._serialized_options = b"8\001"
    _ACCOUNTSTATUS._serialized_start = 2212
    _ACCOUNTSTATUS._serialized_end = 2379
    _AUTHENTICATIONMETHOD._serialized_start = 2382
    _AUTHENTICATIONMETHOD._serialized_end = 2529
    _USERPROFILE._serialized_start = 55
    _USERPROFILE._serialized_end = 626
    _USERPROFILE_PROFILEMETADATAENTRY._serialized_start = 519
    _USERPROFILE_PROFILEMETADATAENTRY._serialized_end = 573
    _USERPROFILE_SECURITYKEYSENTRY._serialized_start = 575
    _USERPROFILE_SECURITYKEYSENTRY._serialized_end = 626
    _USERPERMISSIONS._serialized_start = 629
    _USERPERMISSIONS._serialized_end = 1044
    _USERPERMISSIONS_CONTEXTENTRY._serialized_start = 937
    _USERPERMISSIONS_CONTEXTENTRY._serialized_end = 983
    _USERPERMISSIONS_RESOURCERESTRICTIONSENTRY._serialized_start = 985
    _USERPERMISSIONS_RESOURCERESTRICTIONSENTRY._serialized_end = 1044
    _USERACCESSLOG._serialized_start = 1047
    _USERACCESSLOG._serialized_end = 1334
    _USERACCESSLOG_METADATAENTRY._serialized_start = 1287
    _USERACCESSLOG_METADATAENTRY._serialized_end = 1334
    _USERPREFERENCES._serialized_start = 1337
    _USERPREFERENCES._serialized_end = 1862
    _USERPREFERENCES_PERMISSIONNOTIFICATIONSENTRY._serialized_start = 1743
    _USERPREFERENCES_PERMISSIONNOTIFICATIONSENTRY._serialized_end = 1805
    _USERPREFERENCES_UICUSTOMIZATIONSENTRY._serialized_start = 1807
    _USERPREFERENCES_UICUSTOMIZATIONSENTRY._serialized_end = 1862
    _USERMANAGEMENT._serialized_start = 1865
    _USERMANAGEMENT._serialized_end = 2209
    _USERMANAGEMENT_MANAGEMENTMETADATAENTRY._serialized_start = 2152
    _USERMANAGEMENT_MANAGEMENTMETADATAENTRY._serialized_end = 2209
# @@protoc_insertion_point(module_scope)
