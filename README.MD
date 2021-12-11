# cosmos-cf-fxn

A simple example of using CosmosDB change feed to trigger a function.

This example calls an endpoint, defined in the `ENDPOINT` environment variable, whenever a document is changed.

## Setup

Deploy the app to Azure. Then [configure the following settings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal).

* `AzureWebJobsStorage`: A connection string for the Azure Storage account to use with this Function.
* `ConnectionString`: The CosmosDB connection string for the database you want to monitor.
* `ENDPOINT`: An endpoint to make a request to when a document is updated. A POST request will be made to this endpoint.

## Local Setup

For this to work locally, follow these steps.

1. In VSCode, install the following extensions:
   * [Azure Account](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account)
   * [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
   * [Azure Resources](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureresourcegroups)
   * [Azurite](https://marketplace.visualstudio.com/items?itemName=Azurite.azurite)
2. Install [azure-function-core-tools](https://github.com/Azure/azure-functions-core-tools).
3. You may need to install [.Net](https://dotnet.microsoft.com/en-us/download/dotnet-framework).
4. If you want to emulate CosmosDB locally:
   1. Install the [CosmosDB Local Emulator](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator).
   2. Create a Database matching the `databaseName` in the `function.json` file. This is `data-pipeline-metadata` by default.
   3. Create a collection matching the `collectionName` in the `function.json` file. This is `container1` by default.
5. Create a `local.settings.json` file in the root of this directory.
``` json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "ConnectionString": "",
    "ENDPOINT": ""
  }
}
```
5. Copy the connection string from CosmosDB (or the CosmosDB Emulator) and use it for the `ConnectionString` value.
6. Enter the endpoint which the function should make a request to for the `ENDPOINT` value.
7. Use F5 in VSCode to launch the function.
8. Add a new document, or update an existing document in CosmosDB (or the emulator). This should trigger the function to run and log information to the console in VSCode. It should also make a POST request to the endpoint you specified.

## Notes

The changefeed includes all updates and creates. It does not include deletes. There is also no way to differentiate between an update and a create. It would be possible to add fields to the document to indicate an update if desired. You could also use a soft-delete flag to indicate deletes if you needed to process those.
