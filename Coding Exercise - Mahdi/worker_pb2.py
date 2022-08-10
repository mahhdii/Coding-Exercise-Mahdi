# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cworker.proto\x12\rworkerPackage\"\x07\n\x05\x65mpty\"\x11\n\x03rid\x12\n\n\x02id\x18\x01 \x01(\x05\"#\n\x06status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"2\n\x08mapInput\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\r\n\x05mapID\x18\x02 \x01(\x05\x12\t\n\x01m\x18\x03 \x01(\x05\"\x1a\n\ndriverPort\x12\x0c\n\x04port\x18\x01 \x01(\x05\x32\xeb\x01\n\x06Worker\x12\x41\n\rsetDriverPort\x12\x19.workerPackage.driverPort\x1a\x15.workerPackage.status\x12\x35\n\x03map\x12\x17.workerPackage.mapInput\x1a\x15.workerPackage.status\x12\x33\n\x06reduce\x12\x12.workerPackage.rid\x1a\x15.workerPackage.status\x12\x32\n\x03\x64ie\x12\x14.workerPackage.empty\x1a\x15.workerPackage.statusb\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['empty']
_RID = DESCRIPTOR.message_types_by_name['rid']
_STATUS = DESCRIPTOR.message_types_by_name['status']
_MAPINPUT = DESCRIPTOR.message_types_by_name['mapInput']
_DRIVERPORT = DESCRIPTOR.message_types_by_name['driverPort']
empty = _reflection.GeneratedProtocolMessageType('empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerPackage.empty)
  })
_sym_db.RegisterMessage(empty)

rid = _reflection.GeneratedProtocolMessageType('rid', (_message.Message,), {
  'DESCRIPTOR' : _RID,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerPackage.rid)
  })
_sym_db.RegisterMessage(rid)

status = _reflection.GeneratedProtocolMessageType('status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerPackage.status)
  })
_sym_db.RegisterMessage(status)

mapInput = _reflection.GeneratedProtocolMessageType('mapInput', (_message.Message,), {
  'DESCRIPTOR' : _MAPINPUT,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerPackage.mapInput)
  })
_sym_db.RegisterMessage(mapInput)

driverPort = _reflection.GeneratedProtocolMessageType('driverPort', (_message.Message,), {
  'DESCRIPTOR' : _DRIVERPORT,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerPackage.driverPort)
  })
_sym_db.RegisterMessage(driverPort)

_WORKER = DESCRIPTOR.services_by_name['Worker']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=31
  _EMPTY._serialized_end=38
  _RID._serialized_start=40
  _RID._serialized_end=57
  _STATUS._serialized_start=59
  _STATUS._serialized_end=94
  _MAPINPUT._serialized_start=96
  _MAPINPUT._serialized_end=146
  _DRIVERPORT._serialized_start=148
  _DRIVERPORT._serialized_end=174
  _WORKER._serialized_start=177
  _WORKER._serialized_end=412
# @@protoc_insertion_point(module_scope)