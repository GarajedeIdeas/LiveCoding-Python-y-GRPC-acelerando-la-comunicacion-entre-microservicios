### Generate pb2 files from proto
```python -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. protobufs/managers.proto```