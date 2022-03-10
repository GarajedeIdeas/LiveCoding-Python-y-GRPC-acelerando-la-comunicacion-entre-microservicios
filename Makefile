.PHONY = pb2

SHELL := /bin/bash

pb2:
	python3 -m venv make_env
	source make_env/bin/activate
	pip3 install grpcio grpcio-tools
	python3 -m grpc_tools.protoc -I protobufs --python_out=srv_persistor/ --grpc_python_out=srv_persistor/ protobufs/sales_record.proto

	cp -R srv_persistor/sales_record_pb2.py srv_reader
	cp -R srv_persistor/sales_record_pb2_grpc.py srv_reader

	rm -r make_env