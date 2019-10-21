# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/remove_login_action_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import identity_provider_pb2 as pogoprotos_dot_enums_dot_identity__provider__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/requests/remove_login_action_message.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nIpogoprotos/networking/platform/requests/remove_login_action_message.proto\x12\'pogoprotos.networking.platform.requests\x1a(pogoprotos/enums/identity_provider.proto\"Y\n\x18RemoveLoginActionMessage\x12=\n\x11identity_provider\x18\x01 \x01(\x0e\x32\".pogoprotos.enums.IdentityProviderb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_identity__provider__pb2.DESCRIPTOR,])




_REMOVELOGINACTIONMESSAGE = _descriptor.Descriptor(
  name='RemoveLoginActionMessage',
  full_name='pogoprotos.networking.platform.requests.RemoveLoginActionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity_provider', full_name='pogoprotos.networking.platform.requests.RemoveLoginActionMessage.identity_provider', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=160,
  serialized_end=249,
)

_REMOVELOGINACTIONMESSAGE.fields_by_name['identity_provider'].enum_type = pogoprotos_dot_enums_dot_identity__provider__pb2._IDENTITYPROVIDER
DESCRIPTOR.message_types_by_name['RemoveLoginActionMessage'] = _REMOVELOGINACTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveLoginActionMessage = _reflection.GeneratedProtocolMessageType('RemoveLoginActionMessage', (_message.Message,), dict(
  DESCRIPTOR = _REMOVELOGINACTIONMESSAGE,
  __module__ = 'pogoprotos.networking.platform.requests.remove_login_action_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.RemoveLoginActionMessage)
  ))
_sym_db.RegisterMessage(RemoveLoginActionMessage)


# @@protoc_insertion_point(module_scope)
