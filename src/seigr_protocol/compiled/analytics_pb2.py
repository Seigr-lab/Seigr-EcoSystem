# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61nalytics.proto\x12\x05seigr\"\xb4\x02\n\x06Metric\x12\x11\n\tmetric_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x01\x12\x0c\n\x04unit\x18\x04 \x01(\t\x12\'\n\x08\x63\x61tegory\x18\x05 \x01(\x0e\x32\x15.seigr.MetricCategory\x12\x13\n\x0brecorded_at\x18\x06 \x01(\t\x12-\n\x08metadata\x18\x07 \x03(\x0b\x32\x1b.seigr.Metric.MetadataEntry\x12\x34\n\x12\x61ggregation_method\x18\x08 \x01(\x0e\x32\x18.seigr.AggregationMethod\x12\x18\n\x10source_component\x18\t \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbf\x03\n\tMetricLog\x12\x1e\n\x07metrics\x18\x01 \x03(\x0b\x32\r.seigr.Metric\x12\x18\n\x10log_period_start\x18\x02 \x01(\t\x12\x16\n\x0elog_period_end\x18\x03 \x01(\t\x12\x39\n\rmetric_counts\x18\x04 \x03(\x0b\x32\".seigr.MetricLog.MetricCountsEntry\x12=\n\x0f\x63\x61tegory_totals\x18\x05 \x03(\x0b\x32$.seigr.MetricLog.CategoryTotalsEntry\x12\x41\n\x11\x63\x61tegory_averages\x18\x06 \x03(\x0b\x32&.seigr.MetricLog.CategoryAveragesEntry\x1a\x33\n\x11MetricCountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x35\n\x13\x43\x61tegoryTotalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x37\n\x15\x43\x61tegoryAveragesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\xaa\x02\n\x0fMetricThreshold\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t\x12\'\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x15.seigr.MetricCategory\x12\x17\n\x0fthreshold_value\x18\x03 \x01(\x01\x12\x1b\n\x13threshold_condition\x18\x04 \x01(\t\x12\x15\n\ralert_message\x18\x05 \x01(\t\x12O\n\x15notification_metadata\x18\x06 \x03(\x0b\x32\x30.seigr.MetricThreshold.NotificationMetadataEntry\x1a;\n\x19NotificationMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf3\x01\n\x0f\x41nalyticsConfig\x12$\n\x1c\x61ggregation_interval_seconds\x18\x01 \x01(\x05\x12\x1d\n\x15retention_period_days\x18\x02 \x01(\x05\x12\x1f\n\x17\x65nable_real_time_alerts\x18\x03 \x01(\x08\x12\x43\n\x0f\x63onfig_metadata\x18\x04 \x03(\x0b\x32*.seigr.AnalyticsConfig.ConfigMetadataEntry\x1a\x35\n\x13\x43onfigMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xba\x02\n\rMetricSummary\x12\x12\n\nsummary_id\x18\x01 \x01(\t\x12\'\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x15.seigr.MetricCategory\x12\x15\n\raverage_value\x18\x03 \x01(\x01\x12\x11\n\tmax_value\x18\x04 \x01(\x01\x12\x11\n\tmin_value\x18\x05 \x01(\x01\x12\x1a\n\x12standard_deviation\x18\x06 \x01(\x01\x12\x16\n\x0esummary_period\x18\x07 \x01(\t\x12\x43\n\x10summary_metadata\x18\x08 \x03(\x0b\x32).seigr.MetricSummary.SummaryMetadataEntry\x1a\x36\n\x14SummaryMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\xd6\x01\n\x0eMetricCategory\x12\x1d\n\x19METRIC_CATEGORY_UNDEFINED\x10\x00\x12\x1f\n\x1bMETRIC_CATEGORY_PERFORMANCE\x10\x01\x12\x19\n\x15METRIC_CATEGORY_USAGE\x10\x02\x12\x1c\n\x18METRIC_CATEGORY_SECURITY\x10\x03\x12!\n\x1dMETRIC_CATEGORY_SYSTEM_HEALTH\x10\x04\x12(\n$METRIC_CATEGORY_RESOURCE_CONSUMPTION\x10\x05*e\n\x11\x41ggregationMethod\x12\x14\n\x10METHOD_UNDEFINED\x10\x00\x12\x07\n\x03SUM\x10\x01\x12\x0b\n\x07\x41VERAGE\x10\x02\x12\x0b\n\x07MINIMUM\x10\x03\x12\x0b\n\x07MAXIMUM\x10\x04\x12\n\n\x06MEDIAN\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analytics_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _METRIC_METADATAENTRY._options = None
  _METRIC_METADATAENTRY._serialized_options = b'8\001'
  _METRICLOG_METRICCOUNTSENTRY._options = None
  _METRICLOG_METRICCOUNTSENTRY._serialized_options = b'8\001'
  _METRICLOG_CATEGORYTOTALSENTRY._options = None
  _METRICLOG_CATEGORYTOTALSENTRY._serialized_options = b'8\001'
  _METRICLOG_CATEGORYAVERAGESENTRY._options = None
  _METRICLOG_CATEGORYAVERAGESENTRY._serialized_options = b'8\001'
  _METRICTHRESHOLD_NOTIFICATIONMETADATAENTRY._options = None
  _METRICTHRESHOLD_NOTIFICATIONMETADATAENTRY._serialized_options = b'8\001'
  _ANALYTICSCONFIG_CONFIGMETADATAENTRY._options = None
  _ANALYTICSCONFIG_CONFIGMETADATAENTRY._serialized_options = b'8\001'
  _METRICSUMMARY_SUMMARYMETADATAENTRY._options = None
  _METRICSUMMARY_SUMMARYMETADATAENTRY._serialized_options = b'8\001'
  _METRICCATEGORY._serialized_start=1652
  _METRICCATEGORY._serialized_end=1866
  _AGGREGATIONMETHOD._serialized_start=1868
  _AGGREGATIONMETHOD._serialized_end=1969
  _METRIC._serialized_start=27
  _METRIC._serialized_end=335
  _METRIC_METADATAENTRY._serialized_start=288
  _METRIC_METADATAENTRY._serialized_end=335
  _METRICLOG._serialized_start=338
  _METRICLOG._serialized_end=785
  _METRICLOG_METRICCOUNTSENTRY._serialized_start=622
  _METRICLOG_METRICCOUNTSENTRY._serialized_end=673
  _METRICLOG_CATEGORYTOTALSENTRY._serialized_start=675
  _METRICLOG_CATEGORYTOTALSENTRY._serialized_end=728
  _METRICLOG_CATEGORYAVERAGESENTRY._serialized_start=730
  _METRICLOG_CATEGORYAVERAGESENTRY._serialized_end=785
  _METRICTHRESHOLD._serialized_start=788
  _METRICTHRESHOLD._serialized_end=1086
  _METRICTHRESHOLD_NOTIFICATIONMETADATAENTRY._serialized_start=1027
  _METRICTHRESHOLD_NOTIFICATIONMETADATAENTRY._serialized_end=1086
  _ANALYTICSCONFIG._serialized_start=1089
  _ANALYTICSCONFIG._serialized_end=1332
  _ANALYTICSCONFIG_CONFIGMETADATAENTRY._serialized_start=1279
  _ANALYTICSCONFIG_CONFIGMETADATAENTRY._serialized_end=1332
  _METRICSUMMARY._serialized_start=1335
  _METRICSUMMARY._serialized_end=1649
  _METRICSUMMARY_SUMMARYMETADATAENTRY._serialized_start=1595
  _METRICSUMMARY_SUMMARYMETADATAENTRY._serialized_end=1649
# @@protoc_insertion_point(module_scope)
