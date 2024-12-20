# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rnetwork.proto\x12\x05seigr\x1a\x0c\x63ommon.proto"\xbe\x03\n\rNetworkHyphen\x12\x11\n\thyphen_id\x18\x01 \x01(\t\x12\x12\n\nip_address\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x30\n\x10primary_protocol\x18\x04 \x01(\x0e\x32\x16.seigr.NetworkProtocol\x12#\n\x06status\x18\x05 \x01(\x0e\x32\x13.seigr.HyphenStatus\x12\x33\n\x13supported_protocols\x18\x06 \x03(\x0e\x32\x16.seigr.NetworkProtocol\x12\x34\n\x08metadata\x18\x07 \x03(\x0b\x32".seigr.NetworkHyphen.MetadataEntry\x12\x11\n\tlast_seen\x18\x08 \x01(\t\x12\x17\n\x0fload_percentage\x18\t \x01(\x05\x12\x16\n\x0e\x61vg_latency_ms\x18\n \x01(\x05\x12 \n\x18\x61vailable_bandwidth_mbps\x18\x0b \x01(\x05\x12\x1f\n\x17\x61\x64\x61ptive_scaling_status\x18\x0c \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xb2\x03\n\x0ePeerConnection\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x18\n\x10source_hyphen_id\x18\x02 \x01(\t\x12\x18\n\x10target_hyphen_id\x18\x03 \x01(\t\x12(\n\x08protocol\x18\x04 \x01(\x0e\x32\x16.seigr.NetworkProtocol\x12\x12\n\nlatency_ms\x18\x05 \x01(\x05\x12"\n\tqos_level\x18\x06 \x01(\x0e\x32\x0f.seigr.QoSLevel\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x12\n\ncreated_at\x18\x08 \x01(\t\x12\x14\n\x0clast_updated\x18\t \x01(\t\x12\x35\n\x08metadata\x18\n \x03(\x0b\x32#.seigr.PeerConnection.MetadataEntry\x12\x1e\n\x16\x64\x61ta_transferred_bytes\x18\x0b \x01(\x03\x12\x17\n\x0f\x61uto_scaled_qos\x18\x0c \x01(\x08\x12\x18\n\x10\x63ongestion_level\x18\r \x01(\x02\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x83\x04\n\x0eNetworkCluster\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12%\n\x07hyphens\x18\x02 \x03(\x0b\x32\x14.seigr.NetworkHyphen\x12K\n\x14hyphen_status_counts\x18\x03 \x03(\x0b\x32-.seigr.NetworkCluster.HyphenStatusCountsEntry\x12*\n\x11\x64\x65\x66\x61ult_qos_level\x18\x04 \x01(\x0e\x32\x0f.seigr.QoSLevel\x12\x19\n\x11last_health_check\x18\x05 \x01(\t\x12\x15\n\rhealth_status\x18\x06 \x01(\t\x12\x44\n\x10\x63luster_metadata\x18\x07 \x03(\x0b\x32*.seigr.NetworkCluster.ClusterMetadataEntry\x12\x33\n\x0ehealth_summary\x18\x08 \x01(\x0b\x32\x1b.seigr.NetworkHealthSummary\x12\x1d\n\x15load_balancing_factor\x18\t \x01(\x02\x1a\x39\n\x17HyphenStatusCountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x36\n\x14\x43lusterMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xa6\x03\n\rNetworkConfig\x12\x17\n\x0fmax_connections\x18\x01 \x01(\x05\x12\x13\n\x0bretry_limit\x18\x02 \x01(\x05\x12\x17\n\x0ftimeout_seconds\x18\x03 \x01(\x05\x12\x19\n\x11\x65nable_encryption\x18\x04 \x01(\x08\x12$\n\x0b\x64\x65\x66\x61ult_qos\x18\x05 \x01(\x0e\x32\x0f.seigr.QoSLevel\x12\x31\n\x11\x61llowed_protocols\x18\x06 \x03(\x0e\x32\x16.seigr.NetworkProtocol\x12\x41\n\x0f\x63onfig_metadata\x18\x07 \x03(\x0b\x32(.seigr.NetworkConfig.ConfigMetadataEntry\x12!\n\x19max_packet_loss_threshold\x18\x08 \x01(\x05\x12"\n\x1a\x65nable_dynamic_qos_scaling\x18\t \x01(\x08\x12\x19\n\x11\x66\x61llback_protocol\x18\n \x01(\t\x1a\x35\n\x13\x43onfigMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xf2\x03\n\x11NetworkStatistics\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rtotal_hyphens\x18\x02 \x01(\x05\x12\x1a\n\x12\x61\x63tive_connections\x18\x03 \x01(\x05\x12!\n\x19total_data_transferred_mb\x18\x04 \x01(\x05\x12G\n\x10latency_averages\x18\x05 \x03(\x0b\x32-.seigr.NetworkStatistics.LatencyAveragesEntry\x12G\n\x10qos_distribution\x18\x06 \x03(\x0b\x32-.seigr.NetworkStatistics.QosDistributionEntry\x12\x14\n\x0clast_updated\x18\x07 \x01(\t\x12=\n\x13performance_summary\x18\x08 \x01(\x0b\x32 .seigr.NetworkPerformanceSummary\x12\x1c\n\x14\x61vg_congestion_level\x18\t \x01(\x02\x1a\x36\n\x14LatencyAveragesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x36\n\x14QosDistributionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01"\xb4\x03\n\x15NetworkSecurityPolicy\x12\x11\n\tpolicy_id\x18\x01 \x01(\t\x12\x19\n\x11\x61llowed_ip_ranges\x18\x02 \x03(\t\x12\x19\n\x11\x62locked_ip_ranges\x18\x03 \x03(\t\x12\x1a\n\x12\x65nforce_strict_tls\x18\x04 \x01(\x08\x12\x31\n\x11\x61llowed_protocols\x18\x05 \x03(\x0e\x32\x16.seigr.NetworkProtocol\x12\x1d\n\x15\x61\x64\x61ptive_blacklisting\x18\x06 \x01(\x08\x12I\n\x0fpolicy_metadata\x18\x07 \x03(\x0b\x32\x30.seigr.NetworkSecurityPolicy.PolicyMetadataEntry\x12\x1c\n\x14\x61uto_response_action\x18\x08 \x01(\t\x12"\n\x1a\x65nable_intrusion_detection\x18\t \x01(\x08\x12 \n\x18security_update_schedule\x18\n \x01(\t\x1a\x35\n\x13PolicyMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xb7\x03\n\x11NetworkErrorEvent\x12\x10\n\x08\x65rror_id\x18\x01 \x01(\t\x12\x18\n\x10source_hyphen_id\x18\x02 \x01(\t\x12\x18\n\x10target_hyphen_id\x18\x03 \x01(\t\x12(\n\x08protocol\x18\x04 \x01(\x0e\x32\x16.seigr.NetworkProtocol\x12\x12\n\nerror_code\x18\x05 \x01(\t\x12\x15\n\rerror_message\x18\x06 \x01(\t\x12\x11\n\ttimestamp\x18\x07 \x01(\t\x12\x38\n\x08metadata\x18\x08 \x03(\x0b\x32&.seigr.NetworkErrorEvent.MetadataEntry\x12\x15\n\rauto_resolved\x18\t \x01(\x08\x12\x16\n\x0eretry_attempts\x18\n \x01(\x05\x12\x1b\n\x13\x65scalation_strategy\x18\x0b \x01(\t\x12#\n\x1brecommended_followup_action\x18\x0c \x01(\t\x12\x18\n\x10\x61lert_recipients\x18\r \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\xda\x01\n\x0fNetworkProtocol\x12\x16\n\x12PROTOCOL_UNDEFINED\x10\x00\x12\x10\n\x0cPROTOCOL_TCP\x10\x01\x12\x10\n\x0cPROTOCOL_UDP\x10\x02\x12\x11\n\rPROTOCOL_IPFS\x10\x03\x12\x13\n\x0fPROTOCOL_HYPHEN\x10\x04\x12\x11\n\rPROTOCOL_HTTP\x10\x05\x12\x10\n\x0cPROTOCOL_P2P\x10\x06\x12\x1d\n\x19PROTOCOL_ADAPTIVE_LAYERED\x10\x07\x12\x1f\n\x1bPROTOCOL_SENARY_COMPRESSION\x10\x08*\xd5\x01\n\x0cHyphenStatus\x12\x1b\n\x17HYPHEN_STATUS_UNDEFINED\x10\x00\x12\x11\n\rHYPHEN_ONLINE\x10\x01\x12\x12\n\x0eHYPHEN_OFFLINE\x10\x02\x12\x16\n\x12HYPHEN_MAINTENANCE\x10\x03\x12\x13\n\x0fHYPHEN_DEGRADED\x10\x04\x12\x16\n\x12HYPHEN_UNREACHABLE\x10\x05\x12\x1e\n\x1aHYPHEN_ADAPTIVE_SCALE_DOWN\x10\x06\x12\x1c\n\x18HYPHEN_ADAPTIVE_SCALE_UP\x10\x07\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "network_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _NETWORKHYPHEN_METADATAENTRY._options = None
    _NETWORKHYPHEN_METADATAENTRY._serialized_options = b"8\001"
    _PEERCONNECTION_METADATAENTRY._options = None
    _PEERCONNECTION_METADATAENTRY._serialized_options = b"8\001"
    _NETWORKCLUSTER_HYPHENSTATUSCOUNTSENTRY._options = None
    _NETWORKCLUSTER_HYPHENSTATUSCOUNTSENTRY._serialized_options = b"8\001"
    _NETWORKCLUSTER_CLUSTERMETADATAENTRY._options = None
    _NETWORKCLUSTER_CLUSTERMETADATAENTRY._serialized_options = b"8\001"
    _NETWORKCONFIG_CONFIGMETADATAENTRY._options = None
    _NETWORKCONFIG_CONFIGMETADATAENTRY._serialized_options = b"8\001"
    _NETWORKSTATISTICS_LATENCYAVERAGESENTRY._options = None
    _NETWORKSTATISTICS_LATENCYAVERAGESENTRY._serialized_options = b"8\001"
    _NETWORKSTATISTICS_QOSDISTRIBUTIONENTRY._options = None
    _NETWORKSTATISTICS_QOSDISTRIBUTIONENTRY._serialized_options = b"8\001"
    _NETWORKSECURITYPOLICY_POLICYMETADATAENTRY._options = None
    _NETWORKSECURITYPOLICY_POLICYMETADATAENTRY._serialized_options = b"8\001"
    _NETWORKERROREVENT_METADATAENTRY._options = None
    _NETWORKERROREVENT_METADATAENTRY._serialized_options = b"8\001"
    _NETWORKPROTOCOL._serialized_start = 3250
    _NETWORKPROTOCOL._serialized_end = 3468
    _HYPHENSTATUS._serialized_start = 3471
    _HYPHENSTATUS._serialized_end = 3684
    _NETWORKHYPHEN._serialized_start = 39
    _NETWORKHYPHEN._serialized_end = 485
    _NETWORKHYPHEN_METADATAENTRY._serialized_start = 438
    _NETWORKHYPHEN_METADATAENTRY._serialized_end = 485
    _PEERCONNECTION._serialized_start = 488
    _PEERCONNECTION._serialized_end = 922
    _PEERCONNECTION_METADATAENTRY._serialized_start = 438
    _PEERCONNECTION_METADATAENTRY._serialized_end = 485
    _NETWORKCLUSTER._serialized_start = 925
    _NETWORKCLUSTER._serialized_end = 1440
    _NETWORKCLUSTER_HYPHENSTATUSCOUNTSENTRY._serialized_start = 1327
    _NETWORKCLUSTER_HYPHENSTATUSCOUNTSENTRY._serialized_end = 1384
    _NETWORKCLUSTER_CLUSTERMETADATAENTRY._serialized_start = 1386
    _NETWORKCLUSTER_CLUSTERMETADATAENTRY._serialized_end = 1440
    _NETWORKCONFIG._serialized_start = 1443
    _NETWORKCONFIG._serialized_end = 1865
    _NETWORKCONFIG_CONFIGMETADATAENTRY._serialized_start = 1812
    _NETWORKCONFIG_CONFIGMETADATAENTRY._serialized_end = 1865
    _NETWORKSTATISTICS._serialized_start = 1868
    _NETWORKSTATISTICS._serialized_end = 2366
    _NETWORKSTATISTICS_LATENCYAVERAGESENTRY._serialized_start = 2256
    _NETWORKSTATISTICS_LATENCYAVERAGESENTRY._serialized_end = 2310
    _NETWORKSTATISTICS_QOSDISTRIBUTIONENTRY._serialized_start = 2312
    _NETWORKSTATISTICS_QOSDISTRIBUTIONENTRY._serialized_end = 2366
    _NETWORKSECURITYPOLICY._serialized_start = 2369
    _NETWORKSECURITYPOLICY._serialized_end = 2805
    _NETWORKSECURITYPOLICY_POLICYMETADATAENTRY._serialized_start = 2752
    _NETWORKSECURITYPOLICY_POLICYMETADATAENTRY._serialized_end = 2805
    _NETWORKERROREVENT._serialized_start = 2808
    _NETWORKERROREVENT._serialized_end = 3247
    _NETWORKERROREVENT_METADATAENTRY._serialized_start = 438
    _NETWORKERROREVENT_METADATAENTRY._serialized_end = 485
# @@protoc_insertion_point(module_scope)
