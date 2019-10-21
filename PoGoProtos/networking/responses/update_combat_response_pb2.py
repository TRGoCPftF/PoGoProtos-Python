# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/update_combat_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.combat import combat_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/update_combat_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n<pogoprotos/networking/responses/update_combat_response.proto\x12\x1fpogoprotos.networking.responses\x1a#pogoprotos/data/combat/combat.proto\"\xf3\x04\n\x14UpdateCombatResponse\x12L\n\x06result\x18\x01 \x01(\x0e\x32<.pogoprotos.networking.responses.UpdateCombatResponse.Result\x12.\n\x06\x63ombat\x18\x02 \x01(\x0b\x32\x1e.pogoprotos.data.combat.Combat\"\xdc\x03\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1e\n\x1a\x45RROR_INVALID_COMBAT_STATE\x10\x02\x12\x1a\n\x16\x45RROR_COMBAT_NOT_FOUND\x10\x03\x12\x1e\n\x1a\x45RROR_PLAYER_NOT_IN_COMBAT\x10\x04\x12\x18\n\x14\x45RROR_ILLEGAL_ACTION\x10\x05\x12\x1d\n\x19\x45RROR_INVALID_SUBMIT_TIME\x10\x06\x12\x1c\n\x18\x45RROR_PLAYER_IN_MINIGAME\x10\x07\x12 \n\x1c\x45RROR_EXISTING_QUEUED_ATTACK\x10\x08\x12 \n\x1c\x45RROR_INVALID_CHANGE_POKEMON\x10\t\x12\x1d\n\x19\x45RROR_INSUFFICIENT_ENERGY\x10\n\x12\x16\n\x12\x45RROR_INVALID_MOVE\x10\x0b\x12 \n\x1c\x45RROR_INVALID_DURATION_TURNS\x10\x0c\x12 \n\x1c\x45RROR_INVALID_MINIGAME_STATE\x10\r\x12$\n ERROR_INVALID_QUICK_SWAP_POKEMON\x10\x0e\x12\"\n\x1e\x45RROR_QUICK_SWAP_NOT_AVAILABLE\x10\x0f\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_combat_dot_combat__pb2.DESCRIPTOR,])



_UPDATECOMBATRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.UpdateCombatResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_COMBAT_STATE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_COMBAT_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_IN_COMBAT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ILLEGAL_ACTION', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_SUBMIT_TIME', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_IN_MINIGAME', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_EXISTING_QUEUED_ATTACK', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_CHANGE_POKEMON', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INSUFFICIENT_ENERGY', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_MOVE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_DURATION_TURNS', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_MINIGAME_STATE', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_QUICK_SWAP_POKEMON', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_QUICK_SWAP_NOT_AVAILABLE', index=15, number=15,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=286,
  serialized_end=762,
)
_sym_db.RegisterEnumDescriptor(_UPDATECOMBATRESPONSE_RESULT)


_UPDATECOMBATRESPONSE = _descriptor.Descriptor(
  name='UpdateCombatResponse',
  full_name='pogoprotos.networking.responses.UpdateCombatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.UpdateCombatResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat', full_name='pogoprotos.networking.responses.UpdateCombatResponse.combat', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPDATECOMBATRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=762,
)

_UPDATECOMBATRESPONSE.fields_by_name['result'].enum_type = _UPDATECOMBATRESPONSE_RESULT
_UPDATECOMBATRESPONSE.fields_by_name['combat'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__pb2._COMBAT
_UPDATECOMBATRESPONSE_RESULT.containing_type = _UPDATECOMBATRESPONSE
DESCRIPTOR.message_types_by_name['UpdateCombatResponse'] = _UPDATECOMBATRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateCombatResponse = _reflection.GeneratedProtocolMessageType('UpdateCombatResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECOMBATRESPONSE,
  __module__ = 'pogoprotos.networking.responses.update_combat_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.UpdateCombatResponse)
  ))
_sym_db.RegisterMessage(UpdateCombatResponse)


# @@protoc_insertion_point(module_scope)
