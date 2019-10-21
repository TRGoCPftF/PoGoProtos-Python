# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/view_point_of_interest_image_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.map.fort import fort_type_pb2 as pogoprotos_dot_map_dot_fort_dot_fort__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/view_point_of_interest_image_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFpogoprotos/data/telemetry/view_point_of_interest_image_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a#pogoprotos/map/fort/fort_type.proto\"\xb6\x01\n!ViewPointOfInterestImageTelemetry\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x0f\n\x07\x66ort_id\x18\x02 \x01(\t\x12\x30\n\tfort_type\x18\x03 \x01(\x0e\x32\x1d.pogoprotos.map.fort.FortType\x12\x10\n\x08in_range\x18\x04 \x01(\x08\x12\x18\n\x10was_gym_interior\x18\x05 \x01(\x08\x12\x12\n\npartner_id\x18\x06 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_map_dot_fort_dot_fort__type__pb2.DESCRIPTOR,])




_VIEWPOINTOFINTERESTIMAGETELEMETRY = _descriptor.Descriptor(
  name='ViewPointOfInterestImageTelemetry',
  full_name='pogoprotos.data.telemetry.ViewPointOfInterestImageTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.telemetry.ViewPointOfInterestImageTelemetry.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.data.telemetry.ViewPointOfInterestImageTelemetry.fort_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_type', full_name='pogoprotos.data.telemetry.ViewPointOfInterestImageTelemetry.fort_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in_range', full_name='pogoprotos.data.telemetry.ViewPointOfInterestImageTelemetry.in_range', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='was_gym_interior', full_name='pogoprotos.data.telemetry.ViewPointOfInterestImageTelemetry.was_gym_interior', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='pogoprotos.data.telemetry.ViewPointOfInterestImageTelemetry.partner_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=139,
  serialized_end=321,
)

_VIEWPOINTOFINTERESTIMAGETELEMETRY.fields_by_name['fort_type'].enum_type = pogoprotos_dot_map_dot_fort_dot_fort__type__pb2._FORTTYPE
DESCRIPTOR.message_types_by_name['ViewPointOfInterestImageTelemetry'] = _VIEWPOINTOFINTERESTIMAGETELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ViewPointOfInterestImageTelemetry = _reflection.GeneratedProtocolMessageType('ViewPointOfInterestImageTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _VIEWPOINTOFINTERESTIMAGETELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.view_point_of_interest_image_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ViewPointOfInterestImageTelemetry)
  ))
_sym_db.RegisterMessage(ViewPointOfInterestImageTelemetry)


# @@protoc_insertion_point(module_scope)
