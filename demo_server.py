import grpc
from concurrent import futures
import time

import demo_pb2
import demo_pb2_grpc

import branch

class BranchRequestService(demo_pb2_grpc.BranchServiceServicer):
    def getBranch(self, request, context):
        # return super().getBranch(request, context)
        # resp = demo_pb2

        resp = branch.branch_request(request.index)
        return demo_pb2.Response(branchName = resp)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

demo_pb2_grpc.add_BranchServiceServicer_to_server(BranchRequestService(),server)

print('Listening on port 50051')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)