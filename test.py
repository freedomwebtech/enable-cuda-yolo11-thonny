import torch
print(torch.cuda.is_available())  # Returns True if CUDA is available
print(torch.cuda.current_device())  # Displays the current CUDA device index
print(torch.cuda.get_device_name(torch.cuda.current_device()))  