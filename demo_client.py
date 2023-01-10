
import grpc

import demo_pb2
import demo_pb2_grpc

channel = grpc.insecure_channel('127.0.0.1:50051')

stub = demo_pb2_grpc.BranchServiceStub(channel)

branch = demo_pb2.Request(index=3)

response = stub.getBranch(branch)

print(response.branchName)