# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/create_combat_challenge_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/create_combat_challenge_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nMpogoprotos/networking/requests/messages/create_combat_challenge_message.proto\x12\'pogoprotos.networking.requests.messages\"4\n\x1c\x43reateCombatChallengeMessage\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\tb\x06proto3')
)




_CREATECOMBATCHALLENGEMESSAGE = _descriptor.Descriptor(
  name='CreateCombatChallengeMessage',
  full_name='pogoprotos.networking.requests.messages.CreateCombatChallengeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge_id', full_name='pogoprotos.networking.requests.messages.CreateCombatChallengeMessage.challenge_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=122,
  serialized_end=174,
)

DESCRIPTOR.message_types_by_name['CreateCombatChallengeMessage'] = _CREATECOMBATCHALLENGEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateCombatChallengeMessage = _reflection.GeneratedProtocolMessageType('CreateCombatChallengeMessage', (_message.Message,), dict(
  DESCRIPTOR = _CREATECOMBATCHALLENGEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.create_combat_challenge_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.CreateCombatChallengeMessage)
  ))
_sym_db.RegisterMessage(CreateCombatChallengeMessage)


# @@protoc_insertion_point(module_scope)
