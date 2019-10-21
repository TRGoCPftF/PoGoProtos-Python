# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/permissions_flow_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/permissions_flow_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:pogoprotos/data/telemetry/permissions_flow_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"\xb7\x02\n\x18PermissionsFlowTelemetry\x12Y\n permission_context_telemetry_ids\x18\x01 \x01(\x0e\x32/.pogoprotos.enums.PermissionContextTelemetryIds\x12Q\n\x1c\x64\x65vice_service_telemetry_ids\x18\x02 \x01(\x0e\x32+.pogoprotos.enums.DeviceServiceTelemetryIds\x12\\\n\"permission_flow_step_telemetry_ids\x18\x03 \x01(\x0e\x32\x30.pogoprotos.enums.PermissionFlowStepTelemetryIds\x12\x0f\n\x07success\x18\x04 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_PERMISSIONSFLOWTELEMETRY = _descriptor.Descriptor(
  name='PermissionsFlowTelemetry',
  full_name='pogoprotos.data.telemetry.PermissionsFlowTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='permission_context_telemetry_ids', full_name='pogoprotos.data.telemetry.PermissionsFlowTelemetry.permission_context_telemetry_ids', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_service_telemetry_ids', full_name='pogoprotos.data.telemetry.PermissionsFlowTelemetry.device_service_telemetry_ids', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission_flow_step_telemetry_ids', full_name='pogoprotos.data.telemetry.PermissionsFlowTelemetry.permission_flow_step_telemetry_ids', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.data.telemetry.PermissionsFlowTelemetry.success', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=128,
  serialized_end=439,
)

_PERMISSIONSFLOWTELEMETRY.fields_by_name['permission_context_telemetry_ids'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._PERMISSIONCONTEXTTELEMETRYIDS
_PERMISSIONSFLOWTELEMETRY.fields_by_name['device_service_telemetry_ids'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._DEVICESERVICETELEMETRYIDS
_PERMISSIONSFLOWTELEMETRY.fields_by_name['permission_flow_step_telemetry_ids'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._PERMISSIONFLOWSTEPTELEMETRYIDS
DESCRIPTOR.message_types_by_name['PermissionsFlowTelemetry'] = _PERMISSIONSFLOWTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PermissionsFlowTelemetry = _reflection.GeneratedProtocolMessageType('PermissionsFlowTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _PERMISSIONSFLOWTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.permissions_flow_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.PermissionsFlowTelemetry)
  ))
_sym_db.RegisterMessage(PermissionsFlowTelemetry)


# @@protoc_insertion_point(module_scope)
