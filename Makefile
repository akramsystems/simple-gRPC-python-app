.PHONY: all

proto.c:
	protoc --python_out=. rides.proto

server:
	python -m grpc_tools.protoc \
    -I. \
    --python_out=. \
    --grpc_python_out=. \
    rides.proto