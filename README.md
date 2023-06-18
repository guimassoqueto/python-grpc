## Python gRPC

A simple server-client service communication using Remote Procedure Call (RPC) with Google’s Protocol Buffers (g)

This project is done with help of [Official Python gRPC Introduction](https://grpc.io/docs/languages/python/quickstart/) and [Youtube -  Python gRPC Tutorial - Create a gRPC Client and Server in Python with Various Types of gRPC Calls ](https://www.youtube.com/watch?v=WB37L7PjI5k)


## Requirements
* [Python 3.10+](https://www.python.org/downloads/)
* [poetry](https://python-poetry.org/)


## Init

1. init pre-commit, to branch protection and linting
```shell
make pc
```

2. Start the virtual enviroment
```shell
poetry shell
```

3. Install virtual enviroment dependencies
```shell
poetry install
```

4. (Be sure to be already whitin the virtual environment) This commands will generate python files based on greet.proto located at protos/greet.proto
```shell
python -m grpc_tools.protoc -I protos --python_out=app --pyi_out=app --grpc_python_out=app protos/greet.proto
```

