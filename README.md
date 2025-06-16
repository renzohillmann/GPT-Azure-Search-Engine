# Azure CSV Chatbot

This repo demonstrates a minimal chatbot that answers questions from `data/all-states-history.csv` using Azure OpenAI. The bot runs as a Microsoft Teams bot. The Azure deployment templates remain the same as the original accelerator and provision Azure OpenAI, Cosmos DB and related resources.

## Quick start

1. Fork this repository.
2. Deploy the infrastructure with the button below or `azuredeploy.json`.
3. Populate `credentials.env` with the outputs from the deployment.
4. Deploy the backend bot (see `apps/backend/botservice/README.md`) or run it locally.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fpablomarin%2FGPT-Azure-Search-Engine%2Fmain%2Fazuredeploy.json)
