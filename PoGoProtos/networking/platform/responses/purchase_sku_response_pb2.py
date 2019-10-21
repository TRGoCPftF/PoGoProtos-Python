# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/purchase_sku_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.store import currency_update_pb2 as pogoprotos_dot_data_dot_store_dot_currency__update__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/responses/purchase_sku_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDpogoprotos/networking/platform/responses/purchase_sku_response.proto\x12(pogoprotos.networking.platform.responses\x1a+pogoprotos/data/store/currency_update.proto\"\xbe\x02\n\x13PurchaseSkuResponse\x12T\n\x06result\x18\x01 \x01(\x0e\x32\x44.pogoprotos.networking.platform.responses.PurchaseSkuResponse.Status\x12\x1c\n\x14\x61\x64\x64\x65\x64_inventory_item\x18\x02 \x03(\x0c\x12>\n\x0f\x63urrency_update\x18\x03 \x03(\x0b\x32%.pogoprotos.data.store.CurrencyUpdate\"s\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x12\x13\n\x0f\x42\x41LANCE_TOO_LOW\x10\x03\x12\x15\n\x11SKU_NOT_AVAILABLE\x10\x04\x12\x18\n\x14OVER_INVENTORY_LIMIT\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_store_dot_currency__update__pb2.DESCRIPTOR,])



_PURCHASESKURESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.platform.responses.PurchaseSkuResponse.Status',
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
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALANCE_TOO_LOW', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKU_NOT_AVAILABLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVER_INVENTORY_LIMIT', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=363,
  serialized_end=478,
)
_sym_db.RegisterEnumDescriptor(_PURCHASESKURESPONSE_STATUS)


_PURCHASESKURESPONSE = _descriptor.Descriptor(
  name='PurchaseSkuResponse',
  full_name='pogoprotos.networking.platform.responses.PurchaseSkuResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.platform.responses.PurchaseSkuResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='added_inventory_item', full_name='pogoprotos.networking.platform.responses.PurchaseSkuResponse.added_inventory_item', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_update', full_name='pogoprotos.networking.platform.responses.PurchaseSkuResponse.currency_update', index=2,
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
    _PURCHASESKURESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=478,
)

_PURCHASESKURESPONSE.fields_by_name['result'].enum_type = _PURCHASESKURESPONSE_STATUS
_PURCHASESKURESPONSE.fields_by_name['currency_update'].message_type = pogoprotos_dot_data_dot_store_dot_currency__update__pb2._CURRENCYUPDATE
_PURCHASESKURESPONSE_STATUS.containing_type = _PURCHASESKURESPONSE
DESCRIPTOR.message_types_by_name['PurchaseSkuResponse'] = _PURCHASESKURESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PurchaseSkuResponse = _reflection.GeneratedProtocolMessageType('PurchaseSkuResponse', (_message.Message,), dict(
  DESCRIPTOR = _PURCHASESKURESPONSE,
  __module__ = 'pogoprotos.networking.platform.responses.purchase_sku_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.PurchaseSkuResponse)
  ))
_sym_db.RegisterMessage(PurchaseSkuResponse)


# @@protoc_insertion_point(module_scope)
