# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/complete_quest_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/complete_quest_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDpogoprotos/networking/requests/messages/complete_quest_message.proto\x12\'pogoprotos.networking.requests.messages\">\n\x14\x43ompleteQuestMessage\x12\x10\n\x08quest_id\x18\x01 \x01(\t\x12\x14\n\x0csub_quest_id\x18\x02 \x01(\tb\x06proto3')
)




_COMPLETEQUESTMESSAGE = _descriptor.Descriptor(
  name='CompleteQuestMessage',
  full_name='pogoprotos.networking.requests.messages.CompleteQuestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quest_id', full_name='pogoprotos.networking.requests.messages.CompleteQuestMessage.quest_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_quest_id', full_name='pogoprotos.networking.requests.messages.CompleteQuestMessage.sub_quest_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=113,
  serialized_end=175,
)

DESCRIPTOR.message_types_by_name['CompleteQuestMessage'] = _COMPLETEQUESTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CompleteQuestMessage = _reflection.GeneratedProtocolMessageType('CompleteQuestMessage', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETEQUESTMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.complete_quest_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.CompleteQuestMessage)
  ))
_sym_db.RegisterMessage(CompleteQuestMessage)


# @@protoc_insertion_point(module_scope)
