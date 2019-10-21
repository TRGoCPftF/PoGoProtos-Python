# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/fitness/fitness_metrics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/fitness/fitness_metrics.proto',
  package='pogoprotos.data.fitness',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-pogoprotos/data/fitness/fitness_metrics.proto\x12\x17pogoprotos.data.fitness\"\xc4\x01\n\x0e\x46itnessMetrics\x12\x1e\n\x16\x64istance_walked_meters\x18\x01 \x01(\x01\x12\x12\n\nstep_count\x18\x02 \x01(\x05\x12\x1d\n\x15\x63\x61lories_burned_kcals\x18\x03 \x01(\x01\x12\x1c\n\x14\x65xercise_duration_mi\x18\x04 \x01(\x03\x12\"\n\x1awheelchair_distance_meters\x18\x05 \x01(\x01\x12\x1d\n\x15wheelchair_push_count\x18\x06 \x01(\x01\x62\x06proto3')
)




_FITNESSMETRICS = _descriptor.Descriptor(
  name='FitnessMetrics',
  full_name='pogoprotos.data.fitness.FitnessMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='distance_walked_meters', full_name='pogoprotos.data.fitness.FitnessMetrics.distance_walked_meters', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step_count', full_name='pogoprotos.data.fitness.FitnessMetrics.step_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calories_burned_kcals', full_name='pogoprotos.data.fitness.FitnessMetrics.calories_burned_kcals', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exercise_duration_mi', full_name='pogoprotos.data.fitness.FitnessMetrics.exercise_duration_mi', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wheelchair_distance_meters', full_name='pogoprotos.data.fitness.FitnessMetrics.wheelchair_distance_meters', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wheelchair_push_count', full_name='pogoprotos.data.fitness.FitnessMetrics.wheelchair_push_count', index=5,
      number=6, type=1, cpp_type=5, label=1,
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
  serialized_start=75,
  serialized_end=271,
)

DESCRIPTOR.message_types_by_name['FitnessMetrics'] = _FITNESSMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FitnessMetrics = _reflection.GeneratedProtocolMessageType('FitnessMetrics', (_message.Message,), dict(
  DESCRIPTOR = _FITNESSMETRICS,
  __module__ = 'pogoprotos.data.fitness.fitness_metrics_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.fitness.FitnessMetrics)
  ))
_sym_db.RegisterMessage(FitnessMetrics)


# @@protoc_insertion_point(module_scope)
