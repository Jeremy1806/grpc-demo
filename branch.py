
branch_list = ["Delhi_0","Gurgaon_1","Jhansi_2","Jabalpur_3"]


def branch_request(x):
    if x>=len(branch_list):
        return f"Branch Does Not Exist at index:{x}"    
    return f"Branch Name : {branch_list[x]}"