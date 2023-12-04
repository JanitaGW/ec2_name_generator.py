import random
import string

def generate_ec2_names():
    valid_departments = ['marketing', 'accounting', 'finops']

    department = input("Enter your department: ").lower()
    if department not in valid_departments:
        print("Your department should not use this Name Generator.")
        return

    num_instances = int(input("Enter the number of EC2 instances: "))

    for _ in range(num_instances):
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        print(f"{department}_{random_str}")

generate_ec2_names()
