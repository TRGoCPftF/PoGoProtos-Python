# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/download_gm_templates_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/download_gm_templates_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nKpogoprotos/networking/requests/messages/download_gm_templates_message.proto\x12\'pogoprotos.networking.requests.messages\"[\n\x1a\x44ownloadGmTemplatesMessage\x12\x16\n\x0e\x62\x61sis_batch_id\x18\x01 \x01(\x03\x12\x10\n\x08\x62\x61tch_id\x18\x02 \x01(\x03\x12\x13\n\x0bpage_offset\x18\x03 \x01(\x05\x62\x06proto3')
)




_DOWNLOADGMTEMPLATESMESSAGE = _descriptor.Descriptor(
  name='DownloadGmTemplatesMessage',
  full_name='pogoprotos.networking.requests.messages.DownloadGmTemplatesMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basis_batch_id', full_name='pogoprotos.networking.requests.messages.DownloadGmTemplatesMessage.basis_batch_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='pogoprotos.networking.requests.messages.DownloadGmTemplatesMessage.batch_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_offset', full_name='pogoprotos.networking.requests.messages.DownloadGmTemplatesMessage.page_offset', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=120,
  serialized_end=211,
)

DESCRIPTOR.message_types_by_name['DownloadGmTemplatesMessage'] = _DOWNLOADGMTEMPLATESMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownloadGmTemplatesMessage = _reflection.GeneratedProtocolMessageType('DownloadGmTemplatesMessage', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADGMTEMPLATESMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.download_gm_templates_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.DownloadGmTemplatesMessage)
  ))
_sym_db.RegisterMessage(DownloadGmTemplatesMessage)


# @@protoc_insertion_point(module_scope)
