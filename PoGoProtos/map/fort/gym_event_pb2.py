# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/fort/gym_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/fort/gym_event.proto',
  package='pogoprotos.map.fort',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#pogoprotos/map/fort/gym_event.proto\x12\x13pogoprotos.map.fort\"\xb9\x02\n\x08GymEvent\x12\x0f\n\x07trainer\x18\x01 \x01(\t\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x03\x12\x32\n\x05\x65vent\x18\x03 \x01(\x0e\x32#.pogoprotos.map.fort.GymEvent.Event\x12\x12\n\npokedex_id\x18\x04 \x01(\x05\x12\x12\n\npokemon_id\x18\x05 \x01(\x06\"\xa9\x01\n\x05\x45vent\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bPOKEMON_FED\x10\x01\x12\x14\n\x10POKEMON_DEPLOYED\x10\x02\x12\x14\n\x10POKEMON_RETURNED\x10\x03\x12\x0e\n\nBATTLE_WON\x10\x04\x12\x0f\n\x0b\x42\x41TTLE_LOSS\x10\x05\x12\x10\n\x0cRAID_STARTED\x10\x06\x12\x0e\n\nRAID_ENDED\x10\x07\x12\x13\n\x0fGYM_NEUTRALIZED\x10\x08\x62\x06proto3')
)



_GYMEVENT_EVENT = _descriptor.EnumDescriptor(
  name='Event',
  full_name='pogoprotos.map.fort.GymEvent.Event',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_FED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_DEPLOYED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_RETURNED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTLE_WON', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTLE_LOSS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAID_STARTED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAID_ENDED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_NEUTRALIZED', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=205,
  serialized_end=374,
)
_sym_db.RegisterEnumDescriptor(_GYMEVENT_EVENT)


_GYMEVENT = _descriptor.Descriptor(
  name='GymEvent',
  full_name='pogoprotos.map.fort.GymEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trainer', full_name='pogoprotos.map.fort.GymEvent.trainer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.map.fort.GymEvent.timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='pogoprotos.map.fort.GymEvent.event', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokedex_id', full_name='pogoprotos.map.fort.GymEvent.pokedex_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.map.fort.GymEvent.pokemon_id', index=4,
      number=5, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GYMEVENT_EVENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=374,
)

_GYMEVENT.fields_by_name['event'].enum_type = _GYMEVENT_EVENT
_GYMEVENT_EVENT.containing_type = _GYMEVENT
DESCRIPTOR.message_types_by_name['GymEvent'] = _GYMEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymEvent = _reflection.GeneratedProtocolMessageType('GymEvent', (_message.Message,), dict(
  DESCRIPTOR = _GYMEVENT,
  __module__ = 'pogoprotos.map.fort.gym_event_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.fort.GymEvent)
  ))
_sym_db.RegisterMessage(GymEvent)


# @@protoc_insertion_point(module_scope)
