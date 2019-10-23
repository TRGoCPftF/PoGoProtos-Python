# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/invasion_availability_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/invasion_availability_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?pogoprotos/settings/master/invasion_availability_settings.proto\x12\x1apogoprotos.settings.master\"\xe4\x03\n\x1cInvasionAvailabilitySettings\x12!\n\x19\x61vailability_start_minute\x18\x01 \x01(\x03\x12\x1f\n\x17\x61vailability_end_minute\x18\x02 \x01(\x03\"\xff\x02\n\x1eInvasionAvailabilitySettingsId\x12(\n$INVASION_AVAILABILITY_SETTINGS_UNSET\x10\x00\x12)\n%INVASION_AVAILABILITY_SETTINGS_MONDAY\x10\x01\x12*\n&INVASION_AVAILABILITY_SETTINGS_TUESDAY\x10\x02\x12,\n(INVASION_AVAILABILITY_SETTINGS_WEDNESDAY\x10\x03\x12+\n\'INVASION_AVAILABILITY_SETTINGS_THURSDAY\x10\x04\x12)\n%INVASION_AVAILABILITY_SETTINGS_FRIDAY\x10\x05\x12+\n\'INVASION_AVAILABILITY_SETTINGS_SATURDAY\x10\x06\x12)\n%INVASION_AVAILABILITY_SETTINGS_SUNDAY\x10\x07\x62\x06proto3')
)



_INVASIONAVAILABILITYSETTINGS_INVASIONAVAILABILITYSETTINGSID = _descriptor.EnumDescriptor(
  name='InvasionAvailabilitySettingsId',
  full_name='pogoprotos.settings.master.InvasionAvailabilitySettings.InvasionAvailabilitySettingsId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVASION_AVAILABILITY_SETTINGS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_AVAILABILITY_SETTINGS_MONDAY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_AVAILABILITY_SETTINGS_TUESDAY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_AVAILABILITY_SETTINGS_WEDNESDAY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_AVAILABILITY_SETTINGS_THURSDAY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_AVAILABILITY_SETTINGS_FRIDAY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_AVAILABILITY_SETTINGS_SATURDAY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_AVAILABILITY_SETTINGS_SUNDAY', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=197,
  serialized_end=580,
)
_sym_db.RegisterEnumDescriptor(_INVASIONAVAILABILITYSETTINGS_INVASIONAVAILABILITYSETTINGSID)


_INVASIONAVAILABILITYSETTINGS = _descriptor.Descriptor(
  name='InvasionAvailabilitySettings',
  full_name='pogoprotos.settings.master.InvasionAvailabilitySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='availability_start_minute', full_name='pogoprotos.settings.master.InvasionAvailabilitySettings.availability_start_minute', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='availability_end_minute', full_name='pogoprotos.settings.master.InvasionAvailabilitySettings.availability_end_minute', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INVASIONAVAILABILITYSETTINGS_INVASIONAVAILABILITYSETTINGSID,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=580,
)

_INVASIONAVAILABILITYSETTINGS_INVASIONAVAILABILITYSETTINGSID.containing_type = _INVASIONAVAILABILITYSETTINGS
DESCRIPTOR.message_types_by_name['InvasionAvailabilitySettings'] = _INVASIONAVAILABILITYSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InvasionAvailabilitySettings = _reflection.GeneratedProtocolMessageType('InvasionAvailabilitySettings', (_message.Message,), dict(
  DESCRIPTOR = _INVASIONAVAILABILITYSETTINGS,
  __module__ = 'pogoprotos.settings.master.invasion_availability_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.InvasionAvailabilitySettings)
  ))
_sym_db.RegisterMessage(InvasionAvailabilitySettings)


# @@protoc_insertion_point(module_scope)
