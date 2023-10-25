import psutil
import time


def print_process_info():
    """Prints information about all running processes with active TCP connections."""

    processes = psutil.process_iter()

    print("| Process Name | PID | Connection Type | Local Address | Remote Address | Local Port | Remote Port |")
    print("|---|---|---|---|---|---|---|")

    for process in processes:
        process_name = process.name()
        process_pid = process.pid

        connections = process.connections()
        filtered_connections = list(filter(lambda connection: connection.status == psutil.CONN_ESTABLISHED, connections))
        for connection in filtered_connections:
            connection_type = "TCP"
            local_address, local_port = connection.laddr
            remote_address, remote_port = connection.raddr

            print(
                f"| {process_name} | {process_pid} | {connection_type} | {local_address} | {remote_address} | {local_port} | {remote_port} |"
            )


def main():
    while True:
        print_process_info()
        time.sleep(5)


if __name__ == "__main__":
    main()
