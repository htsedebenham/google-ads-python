# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/resources/keyword_plan_ad_group.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/resources/keyword_plan_ad_group.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v2.resourcesB\027KeywordPlanAdGroupProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources'),
  serialized_pb=_b('\nCgoogle/ads/googleads_v2/proto/resources/keyword_plan_ad_group.proto\x12!google.ads.googleads.v2.resources\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xf2\x01\n\x12KeywordPlanAdGroup\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12;\n\x15keyword_plan_campaign\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\'\n\x02id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\x0e\x63pc_bid_micros\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x84\x02\n%com.google.ads.googleads.v2.resourcesB\x17KeywordPlanAdGroupProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_KEYWORDPLANADGROUP = _descriptor.Descriptor(
  name='KeywordPlanAdGroup',
  full_name='google.ads.googleads.v2.resources.KeywordPlanAdGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.KeywordPlanAdGroup.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword_plan_campaign', full_name='google.ads.googleads.v2.resources.KeywordPlanAdGroup.keyword_plan_campaign', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v2.resources.KeywordPlanAdGroup.id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v2.resources.KeywordPlanAdGroup.name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_micros', full_name='google.ads.googleads.v2.resources.KeywordPlanAdGroup.cpc_bid_micros', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=411,
)

_KEYWORDPLANADGROUP.fields_by_name['keyword_plan_campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANADGROUP.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANADGROUP.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANADGROUP.fields_by_name['cpc_bid_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['KeywordPlanAdGroup'] = _KEYWORDPLANADGROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanAdGroup = _reflection.GeneratedProtocolMessageType('KeywordPlanAdGroup', (_message.Message,), dict(
  DESCRIPTOR = _KEYWORDPLANADGROUP,
  __module__ = 'google.ads.googleads_v2.proto.resources.keyword_plan_ad_group_pb2'
  ,
  __doc__ = """A Keyword Planner ad group. Max number of keyword plan ad groups per
  plan: 200.
  
  
  Attributes:
      resource_name:
          The resource name of the Keyword Planner ad group.
          KeywordPlanAdGroup resource names have the form:  ``customers/
          {customer_id}/keywordPlanAdGroups/{kp_ad_group_id}``
      keyword_plan_campaign:
          The keyword plan campaign to which this ad group belongs.
      id:
          The ID of the keyword plan ad group.
      name:
          The name of the keyword plan ad group.  This field is required
          and should not be empty when creating keyword plan ad group.
      cpc_bid_micros:
          A default ad group max cpc bid in micros in account currency
          for all biddable keywords under the keyword plan ad group. If
          not set, will inherit from parent campaign.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.KeywordPlanAdGroup)
  ))
_sym_db.RegisterMessage(KeywordPlanAdGroup)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
