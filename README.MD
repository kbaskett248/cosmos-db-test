# COSMOS-DB-TEST

A simple example of using CosmosDB change feed to trigger a function.

The example consists of two functions. The first is triggered by a timer and writes a new document to the CosmosDB database.
The second reads the changefeed from the database and operates on the data there.

## Local Setup

For this to work locally, follow these steps.

1. Install the [CosmosDB Local Emulator](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator).
2. Create a Database matching the `databaseName` in either `function.json` file. This is TestDB by default. (These should match so the functions deal with the same database.)
3. Create a collection matching the `collectionName` in either `function.json` file. This is MonitoredCollection by default. (These should match so the functions deal with the same database.)
4. Create a `local.settings.json` file in the root of this directory.
``` json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "ConnectionString": ""
  }
}
```
5. Copy the connection string from the CosmosDB Emulator and use it for the `ConnectionString` value.
6. Use F5 in VSCode to launch the two functions.

## Notes

The changefeed includes all updates and creates. It does not include deletes. There is also no way to differentiate between an update and a create. It would be possible to add fields to the document to indicate an update if desired. You could also use a soft-delete flag to indicate deletes if you needed to process those.
