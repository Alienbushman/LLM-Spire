from transformers import pipeline
import torch

generator_map = {}



def get_llm(model: str):
    llmMap = {}

    llmMap['gpt2'] = 'gpt2'
    # behind licenses
    # llmMap['gemma_it'] = 'mlx-community/gemma-2-2b-it'
    # llmMap['gemma'] = 'ZeroWw/gemma-2-2b-it-abliterated-SILLY'
    llmMap['t5-small'] = 'google-t5/t5-small'
    llmMap['mia'] = 'S1mp1eXXX/Mia-2b-2'
    # llmMap['experimental'] = 'meta-llama/Llama-3.2-3B'
    llmMap['gpt-j-6b'] = 'EleutherAI/gpt-j-6b'
    llmMap['gpt-neo-2.7B'] = 'EleutherAI/gpt-neo-2.7B'
    llmMap['experimental'] = 'EleutherAI/gpt-j-6b'
    return llmMap[model]


def llm_output(prompt, model='gpt2'):
    device = 0 if torch.cuda.is_available() else -1  # 0 for first GPU, -1 for CPU
    if model not in generator_map:
        model_id = get_llm(model)
        # Load and store the generator in the dictionary
        # generator_map[model] = pipeline('text-generation', model=model_id, device=device)
        generator_map[model] = pipeline('text-generation', model=model_id, device=device,
                                        torch_dtype=torch.float16 if device >= 0 else torch.float32
                                        )
        running_on_device = generator_map[model].model.device
        print(f"Running on device {running_on_device} (0 means GPU). Model '{model}' loaded.")
    else:
        running_on_device = generator_map[model].model.device
        print(f"Using cached model '{model}' on device {running_on_device} (0 means GPU).")

    generator = generator_map[model]
    with torch.no_grad():
        generated_text = generator(prompt, max_length=500, num_return_sequences=1)

    return generated_text


def running_on_device():
    device = 0 if torch.cuda.is_available() else -1  # 0 for first GPU, -1 for CPU
    # google-t5-small is chosen since it is small and easiest
    generator = pipeline('text-generation', model="google-t5/t5-small", device=device)
    device = generator.model.device
    return device


def gpu_details():
    message = {}
    num_gpus = torch.cuda.device_count()

    print(f"Number of CUDA devices available: {num_gpus}")
    message["gpu_num"] = num_gpus

    # Print details about each GPU
    for i in range(num_gpus):
        message[f"device_{i}_name"] = torch.cuda.get_device_name(i)
        message[f"device_{i}_mem_allocated"] = f"Memory Allocated: {torch.cuda.memory_allocated(i) / 1024 ** 3:.2f} GB"
        message[f"device_{i}_mem_cached"] = f"Memory Cached: {torch.cuda.memory_reserved(i) / 1024 ** 3:.2f} GB"
    return message


def gpu_available():
    return torch.cuda.is_available()
