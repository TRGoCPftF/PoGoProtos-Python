# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/combat_npc_personality.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/combat_npc_personality.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7pogoprotos/settings/master/combat_npc_personality.proto\x12\x1apogoprotos.settings.master\"\xec\x01\n\x14\x43ombatNpcPersonality\x12\x18\n\x10personality_name\x18\x01 \x01(\t\x12\x1e\n\x16super_effective_chance\x18\x02 \x01(\x02\x12\x16\n\x0especial_chance\x18\x03 \x01(\x02\x12\x1f\n\x17\x64\x65\x66\x65nsive_minimum_score\x18\x04 \x01(\x02\x12\x1f\n\x17\x64\x65\x66\x65nsive_maximum_score\x18\x05 \x01(\x02\x12\x1f\n\x17offensive_minimum_score\x18\x06 \x01(\x02\x12\x1f\n\x17offensive_maximum_score\x18\x07 \x01(\x02\x62\x06proto3')
)




_COMBATNPCPERSONALITY = _descriptor.Descriptor(
  name='CombatNpcPersonality',
  full_name='pogoprotos.settings.master.CombatNpcPersonality',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='personality_name', full_name='pogoprotos.settings.master.CombatNpcPersonality.personality_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='super_effective_chance', full_name='pogoprotos.settings.master.CombatNpcPersonality.super_effective_chance', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='special_chance', full_name='pogoprotos.settings.master.CombatNpcPersonality.special_chance', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defensive_minimum_score', full_name='pogoprotos.settings.master.CombatNpcPersonality.defensive_minimum_score', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defensive_maximum_score', full_name='pogoprotos.settings.master.CombatNpcPersonality.defensive_maximum_score', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offensive_minimum_score', full_name='pogoprotos.settings.master.CombatNpcPersonality.offensive_minimum_score', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offensive_maximum_score', full_name='pogoprotos.settings.master.CombatNpcPersonality.offensive_maximum_score', index=6,
      number=7, type=2, cpp_type=6, label=1,
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
  serialized_start=88,
  serialized_end=324,
)

DESCRIPTOR.message_types_by_name['CombatNpcPersonality'] = _COMBATNPCPERSONALITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatNpcPersonality = _reflection.GeneratedProtocolMessageType('CombatNpcPersonality', (_message.Message,), dict(
  DESCRIPTOR = _COMBATNPCPERSONALITY,
  __module__ = 'pogoprotos.settings.master.combat_npc_personality_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatNpcPersonality)
  ))
_sym_db.RegisterMessage(CombatNpcPersonality)


# @@protoc_insertion_point(module_scope)