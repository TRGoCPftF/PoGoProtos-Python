# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/pokemon_display.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import costume_pb2 as pogoprotos_dot_enums_dot_costume__pb2
from pogoprotos.enums import form_pb2 as pogoprotos_dot_enums_dot_form__pb2
from pogoprotos.enums import gender_pb2 as pogoprotos_dot_enums_dot_gender__pb2
from pogoprotos.enums import weather_condition_pb2 as pogoprotos_dot_enums_dot_weather__condition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/pokemon_display.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%pogoprotos/data/pokemon_display.proto\x12\x0fpogoprotos.data\x1a\x1epogoprotos/enums/costume.proto\x1a\x1bpogoprotos/enums/form.proto\x1a\x1dpogoprotos/enums/gender.proto\x1a(pogoprotos/enums/weather_condition.proto\"\xdc\x02\n\x0ePokemonDisplay\x12*\n\x07\x63ostume\x18\x01 \x01(\x0e\x32\x19.pogoprotos.enums.Costume\x12(\n\x06gender\x18\x02 \x01(\x0e\x32\x18.pogoprotos.enums.Gender\x12\r\n\x05shiny\x18\x03 \x01(\x08\x12$\n\x04\x66orm\x18\x04 \x01(\x0e\x32\x16.pogoprotos.enums.Form\x12\x45\n\x19weather_boosted_condition\x18\x05 \x01(\x0e\x32\".pogoprotos.enums.WeatherCondition\x12<\n\talignment\x18\x06 \x01(\x0e\x32).pogoprotos.data.PokemonDisplay.Alignment\":\n\tAlignment\x12\x13\n\x0f\x41LIGNMENT_UNSET\x10\x00\x12\n\n\x06SHADOW\x10\x01\x12\x0c\n\x08PURIFIED\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_costume__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_form__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_gender__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_weather__condition__pb2.DESCRIPTOR,])



_POKEMONDISPLAY_ALIGNMENT = _descriptor.EnumDescriptor(
  name='Alignment',
  full_name='pogoprotos.data.PokemonDisplay.Alignment',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALIGNMENT_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHADOW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURIFIED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=483,
  serialized_end=541,
)
_sym_db.RegisterEnumDescriptor(_POKEMONDISPLAY_ALIGNMENT)


_POKEMONDISPLAY = _descriptor.Descriptor(
  name='PokemonDisplay',
  full_name='pogoprotos.data.PokemonDisplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='costume', full_name='pogoprotos.data.PokemonDisplay.costume', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='pogoprotos.data.PokemonDisplay.gender', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shiny', full_name='pogoprotos.data.PokemonDisplay.shiny', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='form', full_name='pogoprotos.data.PokemonDisplay.form', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weather_boosted_condition', full_name='pogoprotos.data.PokemonDisplay.weather_boosted_condition', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alignment', full_name='pogoprotos.data.PokemonDisplay.alignment', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POKEMONDISPLAY_ALIGNMENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=541,
)

_POKEMONDISPLAY.fields_by_name['costume'].enum_type = pogoprotos_dot_enums_dot_costume__pb2._COSTUME
_POKEMONDISPLAY.fields_by_name['gender'].enum_type = pogoprotos_dot_enums_dot_gender__pb2._GENDER
_POKEMONDISPLAY.fields_by_name['form'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_POKEMONDISPLAY.fields_by_name['weather_boosted_condition'].enum_type = pogoprotos_dot_enums_dot_weather__condition__pb2._WEATHERCONDITION
_POKEMONDISPLAY.fields_by_name['alignment'].enum_type = _POKEMONDISPLAY_ALIGNMENT
_POKEMONDISPLAY_ALIGNMENT.containing_type = _POKEMONDISPLAY
DESCRIPTOR.message_types_by_name['PokemonDisplay'] = _POKEMONDISPLAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonDisplay = _reflection.GeneratedProtocolMessageType('PokemonDisplay', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONDISPLAY,
  __module__ = 'pogoprotos.data.pokemon_display_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.PokemonDisplay)
  ))
_sym_db.RegisterMessage(PokemonDisplay)


# @@protoc_insertion_point(module_scope)
