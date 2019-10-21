# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/attack_raid_battle_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_action_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/attack_raid_battle_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nHpogoprotos/networking/requests/messages/attack_raid_battle_message.proto\x12\'pogoprotos.networking.requests.messages\x1a*pogoprotos/data/battle/battle_action.proto\"\xd7\x01\n\x17\x41ttackRaidBattleMessage\x12\x0e\n\x06gym_id\x18\x01 \x01(\t\x12\x11\n\tbattle_id\x18\x02 \x01(\t\x12>\n\x10\x61ttacker_actions\x18\x03 \x03(\x0b\x32$.pogoprotos.data.battle.BattleAction\x12\x43\n\x15last_retrieved_action\x18\x04 \x01(\x0b\x32$.pogoprotos.data.battle.BattleAction\x12\x14\n\x0ctimestamp_ms\x18\x05 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__action__pb2.DESCRIPTOR,])




_ATTACKRAIDBATTLEMESSAGE = _descriptor.Descriptor(
  name='AttackRaidBattleMessage',
  full_name='pogoprotos.networking.requests.messages.AttackRaidBattleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_id', full_name='pogoprotos.networking.requests.messages.AttackRaidBattleMessage.gym_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battle_id', full_name='pogoprotos.networking.requests.messages.AttackRaidBattleMessage.battle_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attacker_actions', full_name='pogoprotos.networking.requests.messages.AttackRaidBattleMessage.attacker_actions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_retrieved_action', full_name='pogoprotos.networking.requests.messages.AttackRaidBattleMessage.last_retrieved_action', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.networking.requests.messages.AttackRaidBattleMessage.timestamp_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=162,
  serialized_end=377,
)

_ATTACKRAIDBATTLEMESSAGE.fields_by_name['attacker_actions'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__action__pb2._BATTLEACTION
_ATTACKRAIDBATTLEMESSAGE.fields_by_name['last_retrieved_action'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__action__pb2._BATTLEACTION
DESCRIPTOR.message_types_by_name['AttackRaidBattleMessage'] = _ATTACKRAIDBATTLEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttackRaidBattleMessage = _reflection.GeneratedProtocolMessageType('AttackRaidBattleMessage', (_message.Message,), dict(
  DESCRIPTOR = _ATTACKRAIDBATTLEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.attack_raid_battle_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.AttackRaidBattleMessage)
  ))
_sym_db.RegisterMessage(AttackRaidBattleMessage)


# @@protoc_insertion_point(module_scope)
