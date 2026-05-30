import psutil
import docker

cpu = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory().percent

disk = psutil.disk_usage('/').percent

print(f"CPU: {cpu}%")
print(f"Memory: {memory}%")
print(f"Disk: {disk}%")

client = docker.from_env()

containers = client.containers.list()

print(f"Docker Containers: {len(containers)} Running")