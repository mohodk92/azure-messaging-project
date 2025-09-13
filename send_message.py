rom azure.servicebus import ServiceBusClient, ServiceBusMessage

conn_str = "Endpoint=sb://cloudnautic-messaging-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=DOT0qI/T5xWRd+I//vnFy1ZizKhcnpGnT+ASbPm670A="
queue_name = "orders-queue"

with ServiceBusClient.from_connection_string(conn_str) as client:
    sender = client.get_queue_sender(queue_name)
    with sender:
        msg = ServiceBusMessage("Hello from Cloudnautic Project!>")
        sender.send_messages(msg)
        print("Message sent successfully!")

