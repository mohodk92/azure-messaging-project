// service bus project 

1. fork repo https://github.com/atulkamble/azure-messaging-project
2. create resource group 

// follow steps from repo 

3. update string format in 

local.settings.json

and 

send_message.py

4. copy and update Connection string to code 

Service Bus | Shared access policies | RootManageSharedAccessKey >> Primary Conenction String

syntax: 

```

Endpoint=sb://cloudnautic-messaging-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=DOT0qI/T5xWRd+I//vnFy1ZizKhcnpGnT+ASbPm670A=

```
