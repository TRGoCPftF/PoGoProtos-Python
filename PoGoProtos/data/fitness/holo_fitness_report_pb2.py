# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/fitness/holo_fitness_report.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/fitness/holo_fitness_report.proto',
  package='pogoprotos.data.fitness',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1pogoprotos/data/fitness/holo_fitness_report.proto\x12\x17pogoprotos.data.fitness\"~\n\x11HoloFitnessReport\x12\x18\n\x10num_eggs_hatched\x18\x01 \x01(\x05\x12\x1e\n\x16num_buddy_candy_earned\x18\x02 \x01(\x05\x12\x1a\n\x12\x64istance_walked_km\x18\x03 \x01(\x01\x12\x13\n\x0bweek_bucket\x18\x04 \x01(\x03\x62\x06proto3')
)




_HOLOFITNESSREPORT = _descriptor.Descriptor(
  name='HoloFitnessReport',
  full_name='pogoprotos.data.fitness.HoloFitnessReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_eggs_hatched', full_name='pogoprotos.data.fitness.HoloFitnessReport.num_eggs_hatched', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_buddy_candy_earned', full_name='pogoprotos.data.fitness.HoloFitnessReport.num_buddy_candy_earned', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance_walked_km', full_name='pogoprotos.data.fitness.HoloFitnessReport.distance_walked_km', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='week_bucket', full_name='pogoprotos.data.fitness.HoloFitnessReport.week_bucket', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=78,
  serialized_end=204,
)

DESCRIPTOR.message_types_by_name['HoloFitnessReport'] = _HOLOFITNESSREPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HoloFitnessReport = _reflection.GeneratedProtocolMessageType('HoloFitnessReport', (_message.Message,), dict(
  DESCRIPTOR = _HOLOFITNESSREPORT,
  __module__ = 'pogoprotos.data.fitness.holo_fitness_report_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.fitness.HoloFitnessReport)
  ))
_sym_db.RegisterMessage(HoloFitnessReport)


# @@protoc_insertion_point(module_scope)
