# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_asset_digest_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_asset_digest_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?pogoprotos/networking/responses/get_asset_digest_response.proto\x12\x1fpogoprotos.networking.responses\"\x9d\x03\n\x16GetAssetDigestResponse\x12X\n\x06\x64igest\x18\x01 \x03(\x0b\x32H.pogoprotos.networking.responses.GetAssetDigestResponse.AssetDigestEntry\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x04\x12N\n\x06result\x18\x03 \x01(\x0e\x32>.pogoprotos.networking.responses.GetAssetDigestResponse.Result\x12\x13\n\x0bpage_offset\x18\x04 \x01(\x05\x1aw\n\x10\x41ssetDigestEntry\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x13\n\x0b\x62undle_name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\x07\x12\x0c\n\x04size\x18\x05 \x01(\x05\x12\x0b\n\x03key\x18\x06 \x01(\x0c\"5\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x08\n\x04PAGE\x10\x02\x12\t\n\x05RETRY\x10\x03\x62\x06proto3')
)



_GETASSETDIGESTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetAssetDigestResponse.Result',
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
      name='PAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETRY', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=461,
  serialized_end=514,
)
_sym_db.RegisterEnumDescriptor(_GETASSETDIGESTRESPONSE_RESULT)


_GETASSETDIGESTRESPONSE_ASSETDIGESTENTRY = _descriptor.Descriptor(
  name='AssetDigestEntry',
  full_name='pogoprotos.networking.responses.GetAssetDigestResponse.AssetDigestEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.AssetDigestEntry.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bundle_name', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.AssetDigestEntry.bundle_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.AssetDigestEntry.version', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.AssetDigestEntry.checksum', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.AssetDigestEntry.size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.AssetDigestEntry.key', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=340,
  serialized_end=459,
)

_GETASSETDIGESTRESPONSE = _descriptor.Descriptor(
  name='GetAssetDigestResponse',
  full_name='pogoprotos.networking.responses.GetAssetDigestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digest', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.digest', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.timestamp_ms', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.result', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_offset', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.page_offset', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETASSETDIGESTRESPONSE_ASSETDIGESTENTRY, ],
  enum_types=[
    _GETASSETDIGESTRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=514,
)

_GETASSETDIGESTRESPONSE_ASSETDIGESTENTRY.containing_type = _GETASSETDIGESTRESPONSE
_GETASSETDIGESTRESPONSE.fields_by_name['digest'].message_type = _GETASSETDIGESTRESPONSE_ASSETDIGESTENTRY
_GETASSETDIGESTRESPONSE.fields_by_name['result'].enum_type = _GETASSETDIGESTRESPONSE_RESULT
_GETASSETDIGESTRESPONSE_RESULT.containing_type = _GETASSETDIGESTRESPONSE
DESCRIPTOR.message_types_by_name['GetAssetDigestResponse'] = _GETASSETDIGESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAssetDigestResponse = _reflection.GeneratedProtocolMessageType('GetAssetDigestResponse', (_message.Message,), dict(

  AssetDigestEntry = _reflection.GeneratedProtocolMessageType('AssetDigestEntry', (_message.Message,), dict(
    DESCRIPTOR = _GETASSETDIGESTRESPONSE_ASSETDIGESTENTRY,
    __module__ = 'pogoprotos.networking.responses.get_asset_digest_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetAssetDigestResponse.AssetDigestEntry)
    ))
  ,
  DESCRIPTOR = _GETASSETDIGESTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_asset_digest_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetAssetDigestResponse)
  ))
_sym_db.RegisterMessage(GetAssetDigestResponse)
_sym_db.RegisterMessage(GetAssetDigestResponse.AssetDigestEntry)


# @@protoc_insertion_point(module_scope)
