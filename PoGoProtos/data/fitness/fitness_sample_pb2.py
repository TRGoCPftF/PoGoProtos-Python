# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/fitness/fitness_sample.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/fitness/fitness_sample.proto',
  package='pogoprotos.data.fitness',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,pogoprotos/data/fitness/fitness_sample.proto\x12\x17pogoprotos.data.fitness\"\x95\x04\n\rFitnessSample\x12M\n\x0bsample_type\x18\x01 \x01(\x0e\x32\x38.pogoprotos.data.fitness.FitnessSample.FitnessSampleType\x12!\n\x19sample_start_timestamp_ms\x18\x02 \x01(\x03\x12\x1f\n\x17sample_end_timestamp_ms\x18\x03 \x01(\x03\x12\r\n\x05value\x18\x04 \x01(\x01\x12M\n\x0bsource_type\x18\x05 \x01(\x0e\x32\x38.pogoprotos.data.fitness.FitnessSample.FitnessSourceType\"\xb2\x01\n\x11\x46itnessSampleType\x12\x10\n\x0cSAMPLE_UNSET\x10\x00\x12\t\n\x05STEPS\x10\x01\x12\x1b\n\x17WALKING_DISTANCE_METERS\x10\x02\x12\x1e\n\x1aWHEELCHAIR_DISTANCE_METERS\x10\x03\x12\x12\n\x0e\x43\x41LORIES_KCALS\x10\x04\x12\x19\n\x15WHEELCHAIR_PUSH_COUNT\x10\x05\x12\x14\n\x10\x45XERCISE_TIME_MI\x10\x06\"^\n\x11\x46itnessSourceType\x12\x10\n\x0cSOURCE_UNSET\x10\x00\x12\r\n\tHEALTHKIT\x10\x01\x12\x0e\n\nGOOGLE_FIT\x10\x02\x12\x0f\n\x0b\x41PPLE_WATCH\x10\x03\x12\x07\n\x03GPS\x10\x04\x62\x06proto3')
)



_FITNESSSAMPLE_FITNESSSAMPLETYPE = _descriptor.EnumDescriptor(
  name='FitnessSampleType',
  full_name='pogoprotos.data.fitness.FitnessSample.FitnessSampleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SAMPLE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEPS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WALKING_DISTANCE_METERS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WHEELCHAIR_DISTANCE_METERS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALORIES_KCALS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WHEELCHAIR_PUSH_COUNT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXERCISE_TIME_MI', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=333,
  serialized_end=511,
)
_sym_db.RegisterEnumDescriptor(_FITNESSSAMPLE_FITNESSSAMPLETYPE)

_FITNESSSAMPLE_FITNESSSOURCETYPE = _descriptor.EnumDescriptor(
  name='FitnessSourceType',
  full_name='pogoprotos.data.fitness.FitnessSample.FitnessSourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SOURCE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEALTHKIT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_FIT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPLE_WATCH', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPS', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=513,
  serialized_end=607,
)
_sym_db.RegisterEnumDescriptor(_FITNESSSAMPLE_FITNESSSOURCETYPE)


_FITNESSSAMPLE = _descriptor.Descriptor(
  name='FitnessSample',
  full_name='pogoprotos.data.fitness.FitnessSample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_type', full_name='pogoprotos.data.fitness.FitnessSample.sample_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_start_timestamp_ms', full_name='pogoprotos.data.fitness.FitnessSample.sample_start_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_end_timestamp_ms', full_name='pogoprotos.data.fitness.FitnessSample.sample_end_timestamp_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pogoprotos.data.fitness.FitnessSample.value', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_type', full_name='pogoprotos.data.fitness.FitnessSample.source_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FITNESSSAMPLE_FITNESSSAMPLETYPE,
    _FITNESSSAMPLE_FITNESSSOURCETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=607,
)

_FITNESSSAMPLE.fields_by_name['sample_type'].enum_type = _FITNESSSAMPLE_FITNESSSAMPLETYPE
_FITNESSSAMPLE.fields_by_name['source_type'].enum_type = _FITNESSSAMPLE_FITNESSSOURCETYPE
_FITNESSSAMPLE_FITNESSSAMPLETYPE.containing_type = _FITNESSSAMPLE
_FITNESSSAMPLE_FITNESSSOURCETYPE.containing_type = _FITNESSSAMPLE
DESCRIPTOR.message_types_by_name['FitnessSample'] = _FITNESSSAMPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FitnessSample = _reflection.GeneratedProtocolMessageType('FitnessSample', (_message.Message,), dict(
  DESCRIPTOR = _FITNESSSAMPLE,
  __module__ = 'pogoprotos.data.fitness.fitness_sample_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.fitness.FitnessSample)
  ))
_sym_db.RegisterMessage(FitnessSample)


# @@protoc_insertion_point(module_scope)
