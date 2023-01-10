import grpc
from concurrent import futures
import time

import demo_pb2
import demo_pb2_grpc

branch_list = ["Delhi_0","Gurgaon_1","Jhansi_2","Jabalpur_3"]


def branch_request(x):
    if x>=len(branch_list):
        return f"Branch Does Not Exist at index:{x}"    
    return f"Branch Name : {branch_list[x]}"
     

class BranchRequestService(demo_pb2_grpc.BranchServiceServicer):
    def getBranch(self, request, context):
        # return super().getBranch(request, context)
        # resp = demo_pb2

        resp = branch_request(request.index)
        return demo_pb2.Response(branchName = resp)

    def getAllBranches(self, request, context):

        idx=0
        
        for branch in branch_list:
            idx=idx+1
            resp = demo_pb2.AllBranchResponse()
            resp.branchName = f"Branch {idx} : {branch}"
            
            yield resp

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