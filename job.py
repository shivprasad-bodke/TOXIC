# job scheduling

# Define a function to perform job scheduling using the Greedy algorithm
def job_scheduling(jobs):
    # Sort the jobs in decreasing order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Initialize the list of scheduled jobs and the list of time slots
    scheduled_jobs = []
    time_slots = [False] * (max(jobs, key=lambda x: x[1])[1] + 1)
    
    # Iterate through the sorted jobs and schedule them if possible
    max_profit = 0
    for job in jobs:
        for i in range(job[1], 0, -1):
            if not time_slots[i]:
                scheduled_jobs.append(job)
                time_slots[i] = True
                max_profit += job[2]
                break
    
    
    return scheduled_jobs, max_profit

# Example usage
if __name__ == '__main__':
    # Get user input for the jobs
    jobs = []
    num_jobs = int(input("Enter the number of jobs: "))
    for i in range(num_jobs):
        name = input(f"Enter the name of job {i + 1}: ")
        deadline = int(input(f"Enter the deadline of job {name}: "))
        profit = int(input(f"Enter the profit of job {name}: "))
        jobs.append((name, deadline, profit))
    
    # Perform job scheduling using the Greedy algorithm
    scheduled_jobs, max_profit = job_scheduling(jobs)
    
    # Print the scheduled jobs and the maximum profit
    print("Scheduled Jobs:")
    for job in scheduled_jobs:
        print(f"Name: {job[0]}, Deadline: {job[1]}, Profit: {job[2]}")
    print(f"Maximum Profit: {max_profit}")