# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_available_skus_and_balances_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/get_available_skus_and_balances_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nUpogoprotos/networking/requests/messages/get_available_skus_and_balances_message.proto\x12\'pogoprotos.networking.requests.messages\"$\n\"GetAvailableSkusAndBalancesMessageb\x06proto3')
)




_GETAVAILABLESKUSANDBALANCESMESSAGE = _descriptor.Descriptor(
  name='GetAvailableSkusAndBalancesMessage',
  full_name='pogoprotos.networking.requests.messages.GetAvailableSkusAndBalancesMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=130,
  serialized_end=166,
)

DESCRIPTOR.message_types_by_name['GetAvailableSkusAndBalancesMessage'] = _GETAVAILABLESKUSANDBALANCESMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAvailableSkusAndBalancesMessage = _reflection.GeneratedProtocolMessageType('GetAvailableSkusAndBalancesMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETAVAILABLESKUSANDBALANCESMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.get_available_skus_and_balances_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetAvailableSkusAndBalancesMessage)
  ))
_sym_db.RegisterMessage(GetAvailableSkusAndBalancesMessage)


# @@protoc_insertion_point(module_scope)
