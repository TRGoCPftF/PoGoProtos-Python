# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/get_fitness_report_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.fitness import fitness_report_pb2 as pogoprotos_dot_data_dot_fitness_dot_fitness__report__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/responses/get_fitness_report_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nJpogoprotos/networking/platform/responses/get_fitness_report_response.proto\x12(pogoprotos.networking.platform.responses\x1a,pogoprotos/data/fitness/fitness_report.proto\"\xfd\x02\n\x18GetFitnessReportResponse\x12Y\n\x06status\x18\x01 \x01(\x0e\x32I.pogoprotos.networking.platform.responses.GetFitnessReportResponse.Status\x12=\n\rdaily_reports\x18\x02 \x03(\x0b\x32&.pogoprotos.data.fitness.FitnessReport\x12>\n\x0eweekly_reports\x18\x03 \x03(\x0b\x32&.pogoprotos.data.fitness.FitnessReport\"\x86\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x45RROR_PLAYER_NOT_FOUND\x10\x02\x12\x1b\n\x17\x45RROR_RECORDS_NOT_FOUND\x10\x03\x12\x18\n\x14\x45RROR_INVALID_WINDOW\x10\x04\x12\x11\n\rERROR_UNKNOWN\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_fitness_dot_fitness__report__pb2.DESCRIPTOR,])



_GETFITNESSREPORTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.platform.responses.GetFitnessReportResponse.Status',
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
      name='ERROR_PLAYER_NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RECORDS_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_WINDOW', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=414,
  serialized_end=548,
)
_sym_db.RegisterEnumDescriptor(_GETFITNESSREPORTRESPONSE_STATUS)


_GETFITNESSREPORTRESPONSE = _descriptor.Descriptor(
  name='GetFitnessReportResponse',
  full_name='pogoprotos.networking.platform.responses.GetFitnessReportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.platform.responses.GetFitnessReportResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='daily_reports', full_name='pogoprotos.networking.platform.responses.GetFitnessReportResponse.daily_reports', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weekly_reports', full_name='pogoprotos.networking.platform.responses.GetFitnessReportResponse.weekly_reports', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETFITNESSREPORTRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=548,
)

_GETFITNESSREPORTRESPONSE.fields_by_name['status'].enum_type = _GETFITNESSREPORTRESPONSE_STATUS
_GETFITNESSREPORTRESPONSE.fields_by_name['daily_reports'].message_type = pogoprotos_dot_data_dot_fitness_dot_fitness__report__pb2._FITNESSREPORT
_GETFITNESSREPORTRESPONSE.fields_by_name['weekly_reports'].message_type = pogoprotos_dot_data_dot_fitness_dot_fitness__report__pb2._FITNESSREPORT
_GETFITNESSREPORTRESPONSE_STATUS.containing_type = _GETFITNESSREPORTRESPONSE
DESCRIPTOR.message_types_by_name['GetFitnessReportResponse'] = _GETFITNESSREPORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFitnessReportResponse = _reflection.GeneratedProtocolMessageType('GetFitnessReportResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFITNESSREPORTRESPONSE,
  __module__ = 'pogoprotos.networking.platform.responses.get_fitness_report_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.GetFitnessReportResponse)
  ))
_sym_db.RegisterMessage(GetFitnessReportResponse)


# @@protoc_insertion_point(module_scope)
