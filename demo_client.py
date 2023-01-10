
import grpc

import demo_pb2
import demo_pb2_grpc

channel = grpc.insecure_channel('127.0.0.1:50051')

stub = demo_pb2_grpc.BranchServiceStub(channel)

# FOR UNARY

branch = demo_pb2.Request(index=3)
branchResponse = stub.getBranch(branch)
print(branchResponse.branchName)

# FOR SERVER STREAMING

branches = demo_pb2.emptyReq()
branchesResponse = stub.getAllBranches(branches)
for branch in branchesResponse:
    print(branch)