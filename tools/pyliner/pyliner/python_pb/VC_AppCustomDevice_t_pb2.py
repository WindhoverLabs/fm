# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_VC_AppCustomDevice_t.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='_py_VC_AppCustomDevice_t.proto',
  package='',
  serialized_pb=_b('\n\x1e_py_VC_AppCustomDevice_t.proto\"c\n\x15VC_Device_Handle_t_pb\x12\x0e\n\x06\x42uffer\x18\x01 \x02(\t\x12\x0e\n\x06Status\x18\x02 \x02(\r\x12\x0c\n\x04Port\x18\x03 \x02(\r\x12\x0c\n\x04Mode\x18\x04 \x02(\r\x12\x0e\n\x06Socket\x18\x05 \x02(\r\"\xa9\x01\n\x17VC_AppCustomDevice_t_pb\x12\x15\n\rStreamingTask\x18\x01 \x02(\r\x12\x14\n\x0c\x43ontinueFlag\x18\x02 \x02(\x08\x12\x13\n\x0b\x43hildTaskID\x18\x03 \x02(\r\x12\x11\n\tTaskFlags\x18\x04 \x02(\r\x12\x10\n\x08Priority\x18\x05 \x02(\r\x12\'\n\x07\x43hannel\x18\x06 \x03(\x0b\x32\x16.VC_Device_Handle_t_pb')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VC_DEVICE_HANDLE_T_PB = _descriptor.Descriptor(
  name='VC_Device_Handle_t_pb',
  full_name='VC_Device_Handle_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Buffer', full_name='VC_Device_Handle_t_pb.Buffer', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Status', full_name='VC_Device_Handle_t_pb.Status', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Port', full_name='VC_Device_Handle_t_pb.Port', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Mode', full_name='VC_Device_Handle_t_pb.Mode', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Socket', full_name='VC_Device_Handle_t_pb.Socket', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=133,
)


_VC_APPCUSTOMDEVICE_T_PB = _descriptor.Descriptor(
  name='VC_AppCustomDevice_t_pb',
  full_name='VC_AppCustomDevice_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StreamingTask', full_name='VC_AppCustomDevice_t_pb.StreamingTask', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ContinueFlag', full_name='VC_AppCustomDevice_t_pb.ContinueFlag', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChildTaskID', full_name='VC_AppCustomDevice_t_pb.ChildTaskID', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TaskFlags', full_name='VC_AppCustomDevice_t_pb.TaskFlags', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Priority', full_name='VC_AppCustomDevice_t_pb.Priority', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Channel', full_name='VC_AppCustomDevice_t_pb.Channel', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=305,
)

_VC_APPCUSTOMDEVICE_T_PB.fields_by_name['Channel'].message_type = _VC_DEVICE_HANDLE_T_PB
DESCRIPTOR.message_types_by_name['VC_Device_Handle_t_pb'] = _VC_DEVICE_HANDLE_T_PB
DESCRIPTOR.message_types_by_name['VC_AppCustomDevice_t_pb'] = _VC_APPCUSTOMDEVICE_T_PB

VC_Device_Handle_t_pb = _reflection.GeneratedProtocolMessageType('VC_Device_Handle_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _VC_DEVICE_HANDLE_T_PB,
  __module__ = '_py_VC_AppCustomDevice_t_pb2'
  # @@protoc_insertion_point(class_scope:VC_Device_Handle_t_pb)
  ))
_sym_db.RegisterMessage(VC_Device_Handle_t_pb)

VC_AppCustomDevice_t_pb = _reflection.GeneratedProtocolMessageType('VC_AppCustomDevice_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _VC_APPCUSTOMDEVICE_T_PB,
  __module__ = '_py_VC_AppCustomDevice_t_pb2'
  # @@protoc_insertion_point(class_scope:VC_AppCustomDevice_t_pb)
  ))
_sym_db.RegisterMessage(VC_AppCustomDevice_t_pb)


# @@protoc_insertion_point(module_scope)