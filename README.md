# vue-django-template

## Overview

Welcome to **LLM Spire**, your go-to solution for spinning up your own Large Language Models (LLMs) or leveraging GPT if you don't want to host the models! Built on a powerful combination of **Vue** and **Django**, LLM Spire empowers developers and data enthusiasts to harness the capabilities of advanced language models with ease.

## Features

- **Spin Up Your Own LLMs**: Quickly deploy custom LLMs tailored to your specific needs.
- **GPT Integration**: Seamlessly integrate with OpenAI's GPT for versatile applications.
- **User-Friendly Interface**: A sleek, intuitive front-end powered by Vue for a smooth user experience.
- **Robust Backend**: Leverage Django's capabilities for secure and efficient data handling.
- **Flexible Machine Learning Support**: Ideal for projects ranging from chatbots to content generation.

This project follows an **orchestrator pattern** with Vue for the frontend, Django as a gateway/orchestrator, and microservices using FastAPI 


## Getting Started

### Prerequisites

- Python 3.x
- Node.js
- Preferably cuda+cudnn if you want to run the models on a GPU
  
Then for the frontend run `pnpm install`

and `pip install -r requirements.txt` for each of the backend projects (just read up on how to add your keys for the online-gpt)



## Todos
- [ ] Expand the project's UI to be a bit more user friendly
- [ ] Live updates for GPU utilization
- [ ] More LLMs (hopefully some from Ollama that do not need CUDA + cuDNN to utilize the GPU)
- [ ] More customized prompts and integration with selection
- [ ] Lookups for old questions to LLMs
- [ ] User sign-in
- [ ] User preference persistence 
- [ ] Finish the project's Docker Compose
