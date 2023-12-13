from OpenSSL import SSL
import socket

def connect_to_stunnel(host, port, psk, psk_identity):
    # Create an SSL context
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.set_cipher_list(b'PSK')

    # Set the PSK and identity
    context.set_psk_identity_hint(psk_identity)
    context.set_psk_server_callback(lambda _, hint: psk)

    # Create an SSL connection
    connection = SSL.Connection(context, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    connection.set_connect_state()

    try:
        # Connect to the Stunnel server
        connection.connect((host, port))

        # Send a test message
        connection.sendall(b"Hello from the client!")

        # Receive the response
        response = connection.recv(1024)
        print("Server response:", response.decode())

    except Exception as e:
        print("Error:", str(e))

    finally:
        # Close the connection
        connection.close()

if __name__ == "__main__":
    stunnel_host = "0.0.0.0"
    stunnel_port = 9999  # Replace with your Stunnel server port
    psk_secret = b'Cisco1234Cisco1234'  # Replace with your PSK secret
    psk_identity = b'CiascoACiscoB'  # Replace with your PSK identity

    connect_to_stunnel(stunnel_host, stunnel_port, psk_secret, psk_identity)
