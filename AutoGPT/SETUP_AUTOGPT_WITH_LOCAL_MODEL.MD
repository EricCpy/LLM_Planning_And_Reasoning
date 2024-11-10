# How to Set Up AutoGPT with a Local Model 
**ONLY TESTED WITH 68158de126a0574fba9f0e824f5d89963b7dc8da OF AutoGPT MAIN BRANCH**

This tutorial, will guide you through the process of setting up AutoGPT using GPT4ALL. While we will focus on GPT4ALL, you can use other compatible tools that allow local model hosting.

## Step 1: Download AutoGPT

1. Clone the AutoGPT repository:
   ```bash
   git clone https://github.com/Significant-Gravitas/AutoGPT
   ```
2. Navigate to the AutoGPT directory:
   ```bash
   cd AutoGPT
   ```

## Step 2: Download GPT4ALL

1. Visit the GPT4ALL website: [GPT4ALL](https://www.nomic.ai/gpt4all) and download the latest version.
2. Launch the GPT4ALL application and go to **Settings** and enable the **Local API Server**.
3. Download a model. For this tutorial, I used the **Llama 3.2 3B Instruct** model.
4. Restart the GPT4ALL application to apply the changes.

### Step 2.1: Test Your Setup

To ensure your setup is working, use the following command to test the API:

```bash
curl -X POST http://localhost:4891/v1/chat/completions -d '{
  "model": "Llama 3.2 3B Instruct",
  "messages": [{"role": "user", "content": "Who is Lionel Messi?"}],
  "max_tokens": 50,
  "temperature": 0.28
}'
```

If everything is set up correctly, you should receive a valid response.

## Step 3: Configure AutoGPT to Use the Local Model

1. Navigate to the AutoGPT backend directory:
   ```bash
   cd autogpt_platform/backend/backend/
   ```
2. Replace the `llm.py` file with the modified version provided in this tutorial. This version is specifically tailored for the **Llama 3.2 3B Instruct** model.
   - Note: If you want to use other models, you’ll need to modify the `LlmModel` class, `Model_Metadata` constant, and the `llm_call` functions accordingly.
3. For automation, you can use the following endpoint provided by GPT4ALL: **/v1/models**. I didn't do this.

## Step 4: Follow AutoGPT Setup Instructions

Refer to the README file located in the `autogpt_platform` directory for instructions on configuring and running AutoGPT.

## Troubleshooting: Docker Container Issues

If you've already built a Docker container and are experiencing issues, try the following commands:

1. Build the executor service:
   ```bash
   docker compose build executor
   ```
2. Start the Docker services:
   ```bash
   docker compose up -d
   ```

### Step 4.1: Rebuilding Containers

If the above steps do not resolve the issue, remove existing containers and images, then rebuild.