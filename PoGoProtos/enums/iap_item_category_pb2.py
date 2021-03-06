# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/iap_item_category.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/iap_item_category.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/enums/iap_item_category.proto\x12\x10pogoprotos.enums*\xb1\x02\n\x13HoloIapItemCategory\x12\x15\n\x11IAP_CATEGORY_NONE\x10\x00\x12\x17\n\x13IAP_CATEGORY_BUNDLE\x10\x01\x12\x16\n\x12IAP_CATEGORY_ITEMS\x10\x02\x12\x19\n\x15IAP_CATEGORY_UPGRADES\x10\x03\x12\x1a\n\x16IAP_CATEGORY_POKECOINS\x10\x04\x12\x17\n\x13IAP_CATEGORY_AVATAR\x10\x05\x12\"\n\x1eIAP_CATEGORY_AVATAR_STORE_LINK\x10\x06\x12\x1c\n\x18IAP_CATEGORY_TEAM_CHANGE\x10\x07\x12$\n IAP_CATEGORY_GLOBAL_EVENT_TICKET\x10\n\x12\x1a\n\x16IAP_CATEGORY_VS_SEEKER\x10\x0b\x62\x06proto3')
)

_HOLOIAPITEMCATEGORY = _descriptor.EnumDescriptor(
  name='HoloIapItemCategory',
  full_name='pogoprotos.enums.HoloIapItemCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_BUNDLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_ITEMS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_UPGRADES', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_POKECOINS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_AVATAR', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_AVATAR_STORE_LINK', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_TEAM_CHANGE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_GLOBAL_EVENT_TICKET', index=8, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_VS_SEEKER', index=9, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=63,
  serialized_end=368,
)
_sym_db.RegisterEnumDescriptor(_HOLOIAPITEMCATEGORY)

HoloIapItemCategory = enum_type_wrapper.EnumTypeWrapper(_HOLOIAPITEMCATEGORY)
IAP_CATEGORY_NONE = 0
IAP_CATEGORY_BUNDLE = 1
IAP_CATEGORY_ITEMS = 2
IAP_CATEGORY_UPGRADES = 3
IAP_CATEGORY_POKECOINS = 4
IAP_CATEGORY_AVATAR = 5
IAP_CATEGORY_AVATAR_STORE_LINK = 6
IAP_CATEGORY_TEAM_CHANGE = 7
IAP_CATEGORY_GLOBAL_EVENT_TICKET = 10
IAP_CATEGORY_VS_SEEKER = 11


DESCRIPTOR.enum_types_by_name['HoloIapItemCategory'] = _HOLOIAPITEMCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
