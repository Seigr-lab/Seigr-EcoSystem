# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cross_chain_operations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1c\x63ross_chain_operations.proto\x12\x05seigr"\xe0\x02\n\x0f\x43rossChainToken\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x18\n\x10wrapped_token_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\x12\'\n\x06status\x18\x04 \x01(\x0e\x32\x17.seigr.CrossChainStatus\x12\x19\n\x11originating_chain\x18\x05 \x01(\t\x12\x19\n\x11\x64\x65stination_chain\x18\x06 \x01(\t\x12\x18\n\x10\x63ompliance_level\x18\x07 \x01(\t\x12\x1d\n\x15\x64\x65stination_wallet_id\x18\x08 \x01(\t\x12\x41\n\x0etoken_metadata\x18\t \x03(\x0b\x32).seigr.CrossChainToken.TokenMetadataEntry\x1a\x34\n\x12TokenMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xe7\x01\n\x10WrapTokenRequest\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12\x19\n\x11\x64\x65stination_chain\x18\x03 \x01(\t\x12\x1d\n\x15\x64\x65stination_wallet_id\x18\x04 \x01(\t\x12@\n\rwrap_metadata\x18\x05 \x03(\x0b\x32).seigr.WrapTokenRequest.WrapMetadataEntry\x1a\x33\n\x11WrapMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"a\n\x11WrapTokenResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x0etransaction_id\x18\x03 \x01(\t\x12\x12\n\nerror_code\x18\x04 \x01(\t"\xf1\x01\n\x12UnwrapTokenRequest\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12\x19\n\x11\x64\x65stination_chain\x18\x03 \x01(\t\x12\x1d\n\x15\x64\x65stination_wallet_id\x18\x04 \x01(\t\x12\x46\n\x0funwrap_metadata\x18\x05 \x03(\x0b\x32-.seigr.UnwrapTokenRequest.UnwrapMetadataEntry\x1a\x35\n\x13UnwrapMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"c\n\x13UnwrapTokenResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x0etransaction_id\x18\x03 \x01(\t\x12\x12\n\nerror_code\x18\x04 \x01(\t"\xa7\x01\n\x15SyncGovernanceRequest\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x45\n\rsync_metadata\x18\x02 \x03(\x0b\x32..seigr.SyncGovernanceRequest.SyncMetadataEntry\x1a\x33\n\x11SyncMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"f\n\x16SyncGovernanceResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x0etransaction_id\x18\x03 \x01(\t\x12\x12\n\nerror_code\x18\x04 \x01(\t"\xab\x01\n&GetCrossChainTransactionHistoryRequest\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\r\x12,\n\x0c\x66ilter_types\x18\x03 \x03(\x0e\x32\x16.seigr.TransactionType\x12\x18\n\x10\x64\x61te_range_start\x18\x04 \x01(\t\x12\x16\n\x0e\x64\x61te_range_end\x18\x05 \x01(\t"q\n\'GetCrossChainTransactionHistoryResponse\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x32\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x1c.seigr.CrossChainTransaction"\x80\x02\n\x15\x43rossChainTransaction\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x12\n\nfrom_chain\x18\x02 \x01(\t\x12\x10\n\x08to_chain\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x11\n\ttimestamp\x18\x05 \x01(\t\x12$\n\x04type\x18\x06 \x01(\x0e\x32\x16.seigr.TransactionType\x12\'\n\x06status\x18\x07 \x01(\x0e\x32\x17.seigr.CrossChainStatus\x12\x0b\n\x03\x66\x65\x65\x18\x08 \x01(\t\x12\x11\n\twallet_id\x18\t \x01(\t\x12\x17\n\x0f\x63ompliance_note\x18\n \x01(\t"\x96\x02\n\x1dUpdateCrossChainStatusRequest\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12+\n\nnew_status\x18\x02 \x01(\x0e\x32\x17.seigr.CrossChainStatus\x12\x15\n\rstatus_reason\x18\x03 \x01(\t\x12\x13\n\x0bretry_count\x18\x04 \x01(\x05\x12Q\n\x0fupdate_metadata\x18\x05 \x03(\x0b\x32\x38.seigr.UpdateCrossChainStatusRequest.UpdateMetadataEntry\x1a\x35\n\x13UpdateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"V\n\x1eUpdateCrossChainStatusResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nerror_code\x18\x03 \x01(\t*\xb2\x01\n\x10\x43rossChainStatus\x12\x16\n\x12\x43ROSS_CHAIN_ACTIVE\x10\x00\x12\x16\n\x12\x43ROSS_CHAIN_SYNCED\x10\x01\x12\x18\n\x14\x43ROSS_CHAIN_INACTIVE\x10\x02\x12\x1c\n\x18\x43ROSS_CHAIN_PENDING_WRAP\x10\x03\x12\x1e\n\x1a\x43ROSS_CHAIN_PENDING_UNWRAP\x10\x04\x12\x16\n\x12\x43ROSS_CHAIN_FAILED\x10\x05*O\n\x0fTransactionType\x12\x08\n\x04WRAP\x10\x00\x12\n\n\x06UNWRAP\x10\x01\x12\x13\n\x0fGOVERNANCE_SYNC\x10\x02\x12\x11\n\rSTATUS_UPDATE\x10\x03\x32\xd2\x03\n\x11\x43rossChainService\x12>\n\tWrapToken\x12\x17.seigr.WrapTokenRequest\x1a\x18.seigr.WrapTokenResponse\x12\x44\n\x0bUnwrapToken\x12\x19.seigr.UnwrapTokenRequest\x1a\x1a.seigr.UnwrapTokenResponse\x12M\n\x0eSyncGovernance\x12\x1c.seigr.SyncGovernanceRequest\x1a\x1d.seigr.SyncGovernanceResponse\x12\x80\x01\n\x1fGetCrossChainTransactionHistory\x12-.seigr.GetCrossChainTransactionHistoryRequest\x1a..seigr.GetCrossChainTransactionHistoryResponse\x12\x65\n\x16UpdateCrossChainStatus\x12$.seigr.UpdateCrossChainStatusRequest\x1a%.seigr.UpdateCrossChainStatusResponseb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "cross_chain_operations_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CROSSCHAINTOKEN_TOKENMETADATAENTRY._options = None
    _CROSSCHAINTOKEN_TOKENMETADATAENTRY._serialized_options = b"8\001"
    _WRAPTOKENREQUEST_WRAPMETADATAENTRY._options = None
    _WRAPTOKENREQUEST_WRAPMETADATAENTRY._serialized_options = b"8\001"
    _UNWRAPTOKENREQUEST_UNWRAPMETADATAENTRY._options = None
    _UNWRAPTOKENREQUEST_UNWRAPMETADATAENTRY._serialized_options = b"8\001"
    _SYNCGOVERNANCEREQUEST_SYNCMETADATAENTRY._options = None
    _SYNCGOVERNANCEREQUEST_SYNCMETADATAENTRY._serialized_options = b"8\001"
    _UPDATECROSSCHAINSTATUSREQUEST_UPDATEMETADATAENTRY._options = None
    _UPDATECROSSCHAINSTATUSREQUEST_UPDATEMETADATAENTRY._serialized_options = b"8\001"
    _CROSSCHAINSTATUS._serialized_start = 2264
    _CROSSCHAINSTATUS._serialized_end = 2442
    _TRANSACTIONTYPE._serialized_start = 2444
    _TRANSACTIONTYPE._serialized_end = 2523
    _CROSSCHAINTOKEN._serialized_start = 40
    _CROSSCHAINTOKEN._serialized_end = 392
    _CROSSCHAINTOKEN_TOKENMETADATAENTRY._serialized_start = 340
    _CROSSCHAINTOKEN_TOKENMETADATAENTRY._serialized_end = 392
    _WRAPTOKENREQUEST._serialized_start = 395
    _WRAPTOKENREQUEST._serialized_end = 626
    _WRAPTOKENREQUEST_WRAPMETADATAENTRY._serialized_start = 575
    _WRAPTOKENREQUEST_WRAPMETADATAENTRY._serialized_end = 626
    _WRAPTOKENRESPONSE._serialized_start = 628
    _WRAPTOKENRESPONSE._serialized_end = 725
    _UNWRAPTOKENREQUEST._serialized_start = 728
    _UNWRAPTOKENREQUEST._serialized_end = 969
    _UNWRAPTOKENREQUEST_UNWRAPMETADATAENTRY._serialized_start = 916
    _UNWRAPTOKENREQUEST_UNWRAPMETADATAENTRY._serialized_end = 969
    _UNWRAPTOKENRESPONSE._serialized_start = 971
    _UNWRAPTOKENRESPONSE._serialized_end = 1070
    _SYNCGOVERNANCEREQUEST._serialized_start = 1073
    _SYNCGOVERNANCEREQUEST._serialized_end = 1240
    _SYNCGOVERNANCEREQUEST_SYNCMETADATAENTRY._serialized_start = 1189
    _SYNCGOVERNANCEREQUEST_SYNCMETADATAENTRY._serialized_end = 1240
    _SYNCGOVERNANCERESPONSE._serialized_start = 1242
    _SYNCGOVERNANCERESPONSE._serialized_end = 1344
    _GETCROSSCHAINTRANSACTIONHISTORYREQUEST._serialized_start = 1347
    _GETCROSSCHAINTRANSACTIONHISTORYREQUEST._serialized_end = 1518
    _GETCROSSCHAINTRANSACTIONHISTORYRESPONSE._serialized_start = 1520
    _GETCROSSCHAINTRANSACTIONHISTORYRESPONSE._serialized_end = 1633
    _CROSSCHAINTRANSACTION._serialized_start = 1636
    _CROSSCHAINTRANSACTION._serialized_end = 1892
    _UPDATECROSSCHAINSTATUSREQUEST._serialized_start = 1895
    _UPDATECROSSCHAINSTATUSREQUEST._serialized_end = 2173
    _UPDATECROSSCHAINSTATUSREQUEST_UPDATEMETADATAENTRY._serialized_start = 2120
    _UPDATECROSSCHAINSTATUSREQUEST_UPDATEMETADATAENTRY._serialized_end = 2173
    _UPDATECROSSCHAINSTATUSRESPONSE._serialized_start = 2175
    _UPDATECROSSCHAINSTATUSRESPONSE._serialized_end = 2261
    _CROSSCHAINSERVICE._serialized_start = 2526
    _CROSSCHAINSERVICE._serialized_end = 2992
# @@protoc_insertion_point(module_scope)
