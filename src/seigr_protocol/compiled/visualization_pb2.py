# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visualization.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13visualization.proto\x12\x05seigr"\xc3\x02\n\x12InteractiveElement\x12\x12\n\nelement_id\x18\x01 \x01(\t\x12\x11\n\twidget_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x37\n\x07options\x18\x04 \x03(\x0b\x32&.seigr.InteractiveElement.OptionsEntry\x12\x13\n\x0bis_required\x18\x05 \x01(\x08\x12\x44\n\x0e\x62\x65havior_rules\x18\x06 \x03(\x0b\x32,.seigr.InteractiveElement.BehaviorRulesEntry\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x34\n\x12\x42\x65haviorRulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xa3\x04\n\x0cWidgetConfig\x12\x11\n\twidget_id\x18\x01 \x01(\t\x12&\n\x0bwidget_type\x18\x02 \x01(\x0e\x32\x11.seigr.WidgetType\x12\r\n\x05title\x18\x03 \x01(\t\x12$\n\nchart_type\x18\x04 \x01(\x0e\x32\x10.seigr.ChartType\x12\x13\n\x0b\x64\x61ta_source\x18\x05 \x01(\t\x12 \n\x18refresh_interval_seconds\x18\x06 \x01(\x05\x12@\n\x0f\x64isplay_options\x18\x07 \x03(\x0b\x32\'.seigr.WidgetConfig.DisplayOptionsEntry\x12@\n\x0fwidget_metadata\x18\x08 \x03(\x0b\x32\'.seigr.WidgetConfig.WidgetMetadataEntry\x12\x0f\n\x07tooltip\x18\t \x01(\t\x12\x12\n\nfont_style\x18\n \x01(\t\x12\x1c\n\x14\x65nable_interactivity\x18\x0b \x01(\x08\x12\x37\n\x14interactive_elements\x18\x0c \x03(\x0b\x32\x19.seigr.InteractiveElement\x1a\x35\n\x13\x44isplayOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13WidgetMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xc1\x03\n\x0f\x44\x61shboardLayout\x12\x14\n\x0c\x64\x61shboard_id\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x61shboard_name\x18\x02 \x01(\t\x12$\n\x07widgets\x18\x03 \x03(\x0b\x32\x13.seigr.WidgetConfig\x12\x45\n\x10layout_positions\x18\x04 \x03(\x0b\x32+.seigr.DashboardLayout.LayoutPositionsEntry\x12\x12\n\ncreated_by\x18\x05 \x01(\t\x12\x12\n\ncreated_at\x18\x06 \x01(\t\x12I\n\x12\x64\x61shboard_metadata\x18\x07 \x03(\x0b\x32-.seigr.DashboardLayout.DashboardMetadataEntry\x12\x1c\n\x14\x62\x61\x63kground_image_url\x18\x08 \x01(\t\x12\x10\n\x08theme_id\x18\t \x01(\t\x1a\x36\n\x14LayoutPositionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x38\n\x16\x44\x61shboardMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x82\x02\n\x19VisualizationExportConfig\x12\x14\n\x0c\x64\x61shboard_id\x18\x01 \x01(\t\x12#\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x13.seigr.ExportFormat\x12$\n\x1cinclude_interactive_elements\x18\x03 \x01(\x08\x12M\n\x0f\x65xport_metadata\x18\x04 \x03(\x0b\x32\x34.seigr.VisualizationExportConfig.ExportMetadataEntry\x1a\x35\n\x13\x45xportMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xbd\x02\n\rThemeSettings\x12\x10\n\x08theme_id\x18\x01 \x01(\t\x12\x12\n\ntheme_name\x18\x02 \x01(\t\x12\x15\n\rprimary_color\x18\x03 \x01(\t\x12\x17\n\x0fsecondary_color\x18\x04 \x01(\t\x12\x18\n\x10\x62\x61\x63kground_color\x18\x05 \x01(\t\x12\x13\n\x0b\x66ont_family\x18\x06 \x01(\t\x12\x11\n\tfont_size\x18\x07 \x01(\t\x12\x45\n\x11\x61\x64\x64itional_styles\x18\x08 \x03(\x0b\x32*.seigr.ThemeSettings.AdditionalStylesEntry\x12\x14\n\x0cis_dark_mode\x18\t \x01(\x08\x1a\x37\n\x15\x41\x64\x64itionalStylesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xc6\x02\n\x13VisualizationConfig\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x31\n\x11\x64\x65\x66\x61ult_dashboard\x18\x02 \x01(\x0b\x32\x16.seigr.DashboardLayout\x12,\n\x0etheme_settings\x18\x03 \x01(\x0b\x32\x14.seigr.ThemeSettings\x12 \n\x18\x65nable_real_time_updates\x18\x04 \x01(\x08\x12G\n\x0f\x63onfig_metadata\x18\x05 \x03(\x0b\x32..seigr.VisualizationConfig.ConfigMetadataEntry\x12\x1b\n\x13\x66\x61vorite_dashboards\x18\x06 \x03(\t\x1a\x35\n\x13\x43onfigMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x8c\x02\n\x11VisualizationData\x12\x16\n\x0e\x64\x61ta_source_id\x18\x01 \x01(\t\x12\x11\n\twidget_id\x18\x02 \x01(\t\x12%\n\x0b\x64\x61ta_points\x18\x03 \x03(\x0b\x32\x10.seigr.DataPoint\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x41\n\rdata_metadata\x18\x05 \x03(\x0b\x32*.seigr.VisualizationData.DataMetadataEntry\x12\x1a\n\x12is_historical_data\x18\x06 \x01(\x08\x1a\x33\n\x11\x44\x61taMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xaf\x01\n\tDataPoint\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x34\n\nattributes\x18\x03 \x03(\x0b\x32 .seigr.DataPoint.AttributesEntry\x12\r\n\x05\x63olor\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x93\x02\n\x17VisualizationUsageStats\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x61shboard_id\x18\x02 \x01(\t\x12\x11\n\twidget_id\x18\x03 \x01(\t\x12\x12\n\nview_count\x18\x04 \x01(\x05\x12\x15\n\rlast_accessed\x18\x05 \x01(\t\x12\x12\n\nsession_id\x18\x06 \x01(\t\x12I\n\x0eusage_metadata\x18\x07 \x03(\x0b\x32\x31.seigr.VisualizationUsageStats.UsageMetadataEntry\x1a\x34\n\x12UsageMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xfd\x01\n\x15VisualizationErrorLog\x12\x10\n\x08\x65rror_id\x18\x01 \x01(\t\x12\x11\n\twidget_id\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x61ta_source_id\x18\x03 \x01(\t\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\t\x12G\n\x0e\x65rror_metadata\x18\x06 \x03(\x0b\x32/.seigr.VisualizationErrorLog.ErrorMetadataEntry\x1a\x34\n\x12\x45rrorMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\xc7\x01\n\nWidgetType\x12\x19\n\x15WIDGET_TYPE_UNDEFINED\x10\x00\x12\x15\n\x11WIDGET_TYPE_CHART\x10\x01\x12\x15\n\x11WIDGET_TYPE_TABLE\x10\x02\x12\x13\n\x0fWIDGET_TYPE_MAP\x10\x03\x12\x15\n\x11WIDGET_TYPE_GRAPH\x10\x04\x12\x15\n\x11WIDGET_TYPE_GAUGE\x10\x05\x12\x16\n\x12WIDGET_TYPE_METRIC\x10\x06\x12\x15\n\x11WIDGET_TYPE_TREND\x10\x07*\xa7\x01\n\tChartType\x12\x18\n\x14\x43HART_TYPE_UNDEFINED\x10\x00\x12\x13\n\x0f\x43HART_TYPE_LINE\x10\x01\x12\x12\n\x0e\x43HART_TYPE_BAR\x10\x02\x12\x12\n\x0e\x43HART_TYPE_PIE\x10\x03\x12\x16\n\x12\x43HART_TYPE_SCATTER\x10\x04\x12\x16\n\x12\x43HART_TYPE_HEATMAP\x10\x05\x12\x13\n\x0f\x43HART_TYPE_AREA\x10\x06*p\n\x0c\x45xportFormat\x12\x1b\n\x17\x45XPORT_FORMAT_UNDEFINED\x10\x00\x12\x15\n\x11\x45XPORT_FORMAT_PDF\x10\x01\x12\x15\n\x11\x45XPORT_FORMAT_PNG\x10\x02\x12\x15\n\x11\x45XPORT_FORMAT_CSV\x10\x03\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "visualization_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _INTERACTIVEELEMENT_OPTIONSENTRY._options = None
    _INTERACTIVEELEMENT_OPTIONSENTRY._serialized_options = b"8\001"
    _INTERACTIVEELEMENT_BEHAVIORRULESENTRY._options = None
    _INTERACTIVEELEMENT_BEHAVIORRULESENTRY._serialized_options = b"8\001"
    _WIDGETCONFIG_DISPLAYOPTIONSENTRY._options = None
    _WIDGETCONFIG_DISPLAYOPTIONSENTRY._serialized_options = b"8\001"
    _WIDGETCONFIG_WIDGETMETADATAENTRY._options = None
    _WIDGETCONFIG_WIDGETMETADATAENTRY._serialized_options = b"8\001"
    _DASHBOARDLAYOUT_LAYOUTPOSITIONSENTRY._options = None
    _DASHBOARDLAYOUT_LAYOUTPOSITIONSENTRY._serialized_options = b"8\001"
    _DASHBOARDLAYOUT_DASHBOARDMETADATAENTRY._options = None
    _DASHBOARDLAYOUT_DASHBOARDMETADATAENTRY._serialized_options = b"8\001"
    _VISUALIZATIONEXPORTCONFIG_EXPORTMETADATAENTRY._options = None
    _VISUALIZATIONEXPORTCONFIG_EXPORTMETADATAENTRY._serialized_options = b"8\001"
    _THEMESETTINGS_ADDITIONALSTYLESENTRY._options = None
    _THEMESETTINGS_ADDITIONALSTYLESENTRY._serialized_options = b"8\001"
    _VISUALIZATIONCONFIG_CONFIGMETADATAENTRY._options = None
    _VISUALIZATIONCONFIG_CONFIGMETADATAENTRY._serialized_options = b"8\001"
    _VISUALIZATIONDATA_DATAMETADATAENTRY._options = None
    _VISUALIZATIONDATA_DATAMETADATAENTRY._serialized_options = b"8\001"
    _DATAPOINT_ATTRIBUTESENTRY._options = None
    _DATAPOINT_ATTRIBUTESENTRY._serialized_options = b"8\001"
    _VISUALIZATIONUSAGESTATS_USAGEMETADATAENTRY._options = None
    _VISUALIZATIONUSAGESTATS_USAGEMETADATAENTRY._serialized_options = b"8\001"
    _VISUALIZATIONERRORLOG_ERRORMETADATAENTRY._options = None
    _VISUALIZATIONERRORLOG_ERRORMETADATAENTRY._serialized_options = b"8\001"
    _WIDGETTYPE._serialized_start = 3252
    _WIDGETTYPE._serialized_end = 3451
    _CHARTTYPE._serialized_start = 3454
    _CHARTTYPE._serialized_end = 3621
    _EXPORTFORMAT._serialized_start = 3623
    _EXPORTFORMAT._serialized_end = 3735
    _INTERACTIVEELEMENT._serialized_start = 31
    _INTERACTIVEELEMENT._serialized_end = 354
    _INTERACTIVEELEMENT_OPTIONSENTRY._serialized_start = 254
    _INTERACTIVEELEMENT_OPTIONSENTRY._serialized_end = 300
    _INTERACTIVEELEMENT_BEHAVIORRULESENTRY._serialized_start = 302
    _INTERACTIVEELEMENT_BEHAVIORRULESENTRY._serialized_end = 354
    _WIDGETCONFIG._serialized_start = 357
    _WIDGETCONFIG._serialized_end = 904
    _WIDGETCONFIG_DISPLAYOPTIONSENTRY._serialized_start = 796
    _WIDGETCONFIG_DISPLAYOPTIONSENTRY._serialized_end = 849
    _WIDGETCONFIG_WIDGETMETADATAENTRY._serialized_start = 851
    _WIDGETCONFIG_WIDGETMETADATAENTRY._serialized_end = 904
    _DASHBOARDLAYOUT._serialized_start = 907
    _DASHBOARDLAYOUT._serialized_end = 1356
    _DASHBOARDLAYOUT_LAYOUTPOSITIONSENTRY._serialized_start = 1244
    _DASHBOARDLAYOUT_LAYOUTPOSITIONSENTRY._serialized_end = 1298
    _DASHBOARDLAYOUT_DASHBOARDMETADATAENTRY._serialized_start = 1300
    _DASHBOARDLAYOUT_DASHBOARDMETADATAENTRY._serialized_end = 1356
    _VISUALIZATIONEXPORTCONFIG._serialized_start = 1359
    _VISUALIZATIONEXPORTCONFIG._serialized_end = 1617
    _VISUALIZATIONEXPORTCONFIG_EXPORTMETADATAENTRY._serialized_start = 1564
    _VISUALIZATIONEXPORTCONFIG_EXPORTMETADATAENTRY._serialized_end = 1617
    _THEMESETTINGS._serialized_start = 1620
    _THEMESETTINGS._serialized_end = 1937
    _THEMESETTINGS_ADDITIONALSTYLESENTRY._serialized_start = 1882
    _THEMESETTINGS_ADDITIONALSTYLESENTRY._serialized_end = 1937
    _VISUALIZATIONCONFIG._serialized_start = 1940
    _VISUALIZATIONCONFIG._serialized_end = 2266
    _VISUALIZATIONCONFIG_CONFIGMETADATAENTRY._serialized_start = 2213
    _VISUALIZATIONCONFIG_CONFIGMETADATAENTRY._serialized_end = 2266
    _VISUALIZATIONDATA._serialized_start = 2269
    _VISUALIZATIONDATA._serialized_end = 2537
    _VISUALIZATIONDATA_DATAMETADATAENTRY._serialized_start = 2486
    _VISUALIZATIONDATA_DATAMETADATAENTRY._serialized_end = 2537
    _DATAPOINT._serialized_start = 2540
    _DATAPOINT._serialized_end = 2715
    _DATAPOINT_ATTRIBUTESENTRY._serialized_start = 2666
    _DATAPOINT_ATTRIBUTESENTRY._serialized_end = 2715
    _VISUALIZATIONUSAGESTATS._serialized_start = 2718
    _VISUALIZATIONUSAGESTATS._serialized_end = 2993
    _VISUALIZATIONUSAGESTATS_USAGEMETADATAENTRY._serialized_start = 2941
    _VISUALIZATIONUSAGESTATS_USAGEMETADATAENTRY._serialized_end = 2993
    _VISUALIZATIONERRORLOG._serialized_start = 2996
    _VISUALIZATIONERRORLOG._serialized_end = 3249
    _VISUALIZATIONERRORLOG_ERRORMETADATAENTRY._serialized_start = 3197
    _VISUALIZATIONERRORLOG_ERRORMETADATAENTRY._serialized_end = 3249
# @@protoc_insertion_point(module_scope)
