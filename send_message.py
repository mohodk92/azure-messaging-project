rom azure.servicebus import ServiceBusClient, ServiceBusMessage

conn_str = "cloudnautic-messaging-func-dcfbdrcffcbhggf2.canadacentral-01.azurewebsites.net"
queue_name = "orders-queue"

with ServiceBusClient.from_connection_string(conn_str) as client:
    sender = client.get_queue_sender(queue_name)
    with sender:
        msg = ServiceBusMessage("Hello from Cloudnautic Project!>
        sender.send_messages(msg)
        print("Message sent successfully!")

