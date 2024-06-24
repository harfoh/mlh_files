import boto3

# Create a boto3 EC2 client
ec2 = boto3.client('ec2')

# Function to release unused Elastic IPs
def release_unused_elastic_ips():
    released_count = 0  # to count the released Elastic IPs
    no_instance_id_count = 0  # to count the addresses without InstanceId
    total_count = 0  # to count d total number of Elastic IPs

# Try to describe addresses
    try:
        response = ec2.describe_addresses()
        for address in response['Addresses']:
            total_count += 1  # Increment the counter for each Elastic IP address
            if 'InstanceId' not in address:
                no_instance_id_count += 1  # Increment the counter for each address without InstanceId
                allocation_id = address["AllocationId"]
                print(f"Releasing Elastic IP: {address['PublicIp']} with AllocationId: {allocation_id}")
                # Try to release the Elastic IP
                try:
                    ec2.release_address(AllocationId=allocation_id)
                    released_count += 1  # Increment the counter for each released IP
                # this shows errors in releasing the ELastic IP addresses if it doesn't work
                except Exception as e:
                    print(f"Error releasing Elastic IP {allocation_id}: {e}")
    # this will handle errors in describing addresses
    except Exception as e:
        print(f"Error describing addresses: {e}")

    print(f"Total number of Elastic IPs: {total_count}")
    print(f"Total number of Elastic IPs released: {released_count}")
    print(f"Total number of Elastic IPs without InstanceId: {no_instance_id_count}")

#the function to release unused Elastic IPs
release_unused_elastic_ips()
