# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/redeem/redeemed_avatar_item.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/redeem/redeemed_avatar_item.proto',
  package='pogoprotos.data.redeem',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1pogoprotos/data/redeem/redeemed_avatar_item.proto\x12\x16pogoprotos.data.redeem\"D\n\x12RedeemedAvatarItem\x12\x1a\n\x12\x61vatar_template_id\x18\x01 \x01(\t\x12\x12\n\nitem_count\x18\x02 \x01(\x05\x62\x06proto3')
)




_REDEEMEDAVATARITEM = _descriptor.Descriptor(
  name='RedeemedAvatarItem',
  full_name='pogoprotos.data.redeem.RedeemedAvatarItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatar_template_id', full_name='pogoprotos.data.redeem.RedeemedAvatarItem.avatar_template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_count', full_name='pogoprotos.data.redeem.RedeemedAvatarItem.item_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=77,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['RedeemedAvatarItem'] = _REDEEMEDAVATARITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedeemedAvatarItem = _reflection.GeneratedProtocolMessageType('RedeemedAvatarItem', (_message.Message,), dict(
  DESCRIPTOR = _REDEEMEDAVATARITEM,
  __module__ = 'pogoprotos.data.redeem.redeemed_avatar_item_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.redeem.RedeemedAvatarItem)
  ))
_sym_db.RegisterMessage(RedeemedAvatarItem)


# @@protoc_insertion_point(module_scope)
