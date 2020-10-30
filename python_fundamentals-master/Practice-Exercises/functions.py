

def job_Applications(success_rate):

    num_applications = 1 / success_rate

    return num_applications


print(f"The number of applications you need to submit in order to be success is {job_Applications(0.01)}")
