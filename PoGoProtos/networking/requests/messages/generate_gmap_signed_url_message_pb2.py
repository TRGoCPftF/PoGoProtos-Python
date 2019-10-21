# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/generate_gmap_signed_url_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/generate_gmap_signed_url_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nNpogoprotos/networking/requests/messages/generate_gmap_signed_url_message.proto\x12\'pogoprotos.networking.requests.messages\"\xd7\x01\n\x1cGenerateGmapSignedUrlMessage\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x0c\n\x04zoom\x18\x05 \x01(\x05\x12\x15\n\rlanguage_code\x18\x06 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x07 \x01(\t\x12\x11\n\tmap_style\x18\x08 \x01(\t\x12\x10\n\x08map_type\x18\t \x01(\t\x12\x13\n\x0bicon_params\x18\n \x01(\tb\x06proto3')
)




_GENERATEGMAPSIGNEDURLMESSAGE = _descriptor.Descriptor(
  name='GenerateGmapSignedUrlMessage',
  full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zoom', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.zoom', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.language_code', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.country_code', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_style', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.map_style', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_type', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.map_type', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_params', full_name='pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage.icon_params', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=124,
  serialized_end=339,
)

DESCRIPTOR.message_types_by_name['GenerateGmapSignedUrlMessage'] = _GENERATEGMAPSIGNEDURLMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateGmapSignedUrlMessage = _reflection.GeneratedProtocolMessageType('GenerateGmapSignedUrlMessage', (_message.Message,), dict(
  DESCRIPTOR = _GENERATEGMAPSIGNEDURLMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.generate_gmap_signed_url_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GenerateGmapSignedUrlMessage)
  ))
_sym_db.RegisterMessage(GenerateGmapSignedUrlMessage)


# @@protoc_insertion_point(module_scope)
