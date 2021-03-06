# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/start_gym_battle_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/start_gym_battle_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFpogoprotos/networking/requests/messages/start_gym_battle_message.proto\x12\'pogoprotos.networking.requests.messages\"\x97\x01\n\x15StartGymBattleMessage\x12\x0e\n\x06gym_id\x18\x01 \x01(\t\x12\x1d\n\x15\x61ttacking_pokemon_ids\x18\x02 \x03(\x06\x12\x1c\n\x14\x64\x65\x66\x65nding_pokemon_id\x18\x03 \x01(\x06\x12\x17\n\x0fplayer_latitude\x18\x04 \x01(\x01\x12\x18\n\x10player_longitude\x18\x05 \x01(\x01\x62\x06proto3')
)




_STARTGYMBATTLEMESSAGE = _descriptor.Descriptor(
  name='StartGymBattleMessage',
  full_name='pogoprotos.networking.requests.messages.StartGymBattleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_id', full_name='pogoprotos.networking.requests.messages.StartGymBattleMessage.gym_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attacking_pokemon_ids', full_name='pogoprotos.networking.requests.messages.StartGymBattleMessage.attacking_pokemon_ids', index=1,
      number=2, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defending_pokemon_id', full_name='pogoprotos.networking.requests.messages.StartGymBattleMessage.defending_pokemon_id', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_latitude', full_name='pogoprotos.networking.requests.messages.StartGymBattleMessage.player_latitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_longitude', full_name='pogoprotos.networking.requests.messages.StartGymBattleMessage.player_longitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=116,
  serialized_end=267,
)

DESCRIPTOR.message_types_by_name['StartGymBattleMessage'] = _STARTGYMBATTLEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartGymBattleMessage = _reflection.GeneratedProtocolMessageType('StartGymBattleMessage', (_message.Message,), dict(
  DESCRIPTOR = _STARTGYMBATTLEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.start_gym_battle_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.StartGymBattleMessage)
  ))
_sym_db.RegisterMessage(StartGymBattleMessage)


# @@protoc_insertion_point(module_scope)
