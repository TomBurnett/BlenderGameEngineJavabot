# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BlenderData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
#from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

#_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BlenderData.proto',
  package='',
  serialized_pb=_b('\n\x11\x42lenderData.proto\"\xf3\x01\n\x07\x43ommand\x12\x13\n\x0b\x63ommandType\x18\x01 \x02(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12\x18\n\x10uniqueObjectName\x18\x03 \x01(\t\x12\x0c\n\x04posX\x18\x04 \x01(\x02\x12\x0c\n\x04posY\x18\x05 \x01(\x02\x12\x0c\n\x04velX\x18\x06 \x01(\x02\x12\x0c\n\x04velY\x18\x07 \x01(\x02\x12\r\n\x05state\x18\x08 \x01(\x02\x12\x0e\n\x06target\x18\t \x01(\t\x12\x0e\n\x06scaleX\x18\n \x01(\x02\x12\x0e\n\x06scaleY\x18\x0b \x01(\x02\x12\x10\n\x08\x64inoType\x18\x0c \x01(\x05\x12\x0f\n\x07targetX\x18\r \x01(\x02\x12\x0f\n\x07targetY\x18\x0e \x01(\x02\"<\n\x06Header\x12\x13\n\x0bsequenceNum\x18\x01 \x02(\x05\x12\x0b\n\x03\x61\x63k\x18\x02 \x02(\x05\x12\x10\n\x08\x62itField\x18\x03 \x02(\x05\"A\n\x0b\x42lenderData\x12\x19\n\x07\x63ommand\x18\x01 \x03(\x0b\x32\x08.Command\x12\x17\n\x06header\x18\x02 \x01(\x0b\x32\x07.HeaderB\x13\x42\x11\x42lenderDataProtos')
)
#_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commandType', full_name='Command.commandType', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object', full_name='Command.object', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uniqueObjectName', full_name='Command.uniqueObjectName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posX', full_name='Command.posX', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posY', full_name='Command.posY', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velX', full_name='Command.velX', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velY', full_name='Command.velY', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='Command.state', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='Command.target', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scaleX', full_name='Command.scaleX', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scaleY', full_name='Command.scaleY', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dinoType', full_name='Command.dinoType', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='targetX', full_name='Command.targetX', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='targetY', full_name='Command.targetY', index=13,
      number=14, type=2, cpp_type=6, label=1,
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
  #oneofs=[
  #],
  serialized_start=22,
  serialized_end=265,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequenceNum', full_name='Header.sequenceNum', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ack', full_name='Header.ack', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bitField', full_name='Header.bitField', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  #oneofs=[
  #],
  serialized_start=267,
  serialized_end=327,
)


_BLENDERDATA = _descriptor.Descriptor(
  name='BlenderData',
  full_name='BlenderData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='BlenderData.command', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='BlenderData.header', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  #oneofs=[
  #],
  serialized_start=329,
  serialized_end=394,
)

_BLENDERDATA.fields_by_name['command'].message_type = _COMMAND
_BLENDERDATA.fields_by_name['header'].message_type = _HEADER
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['BlenderData'] = _BLENDERDATA

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'BlenderData_pb2'
  # @@protoc_insertion_point(class_scope:Command)
  ))
#_sym_db.RegisterMessage(Command)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'BlenderData_pb2'
  # @@protoc_insertion_point(class_scope:Header)
  ))
#_sym_db.RegisterMessage(Header)

BlenderData = _reflection.GeneratedProtocolMessageType('BlenderData', (_message.Message,), dict(
  DESCRIPTOR = _BLENDERDATA,
  __module__ = 'BlenderData_pb2'
  # @@protoc_insertion_point(class_scope:BlenderData)
  ))
#_sym_db.RegisterMessage(BlenderData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\021BlenderDataProtos'))
# @@protoc_insertion_point(module_scope)
