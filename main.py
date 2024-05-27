import oqs
import time
from pprint import pprint

def ml_kem():
    start_time = time.time()
    
    # print("liboqs version:", oqs.oqs_version())
    # print("liboqs-python version:", oqs.oqs_python_version())
    # print("Enabled KEM mechanisms:")
    # kems = oqs.get_enabled_kem_mechanisms()
    # pprint(kems, compact=True)

    # Create client and server with sample KEM mechanisms
    kemalg = "Kyber512"
    with oqs.KeyEncapsulation(kemalg) as client:
        with oqs.KeyEncapsulation(kemalg) as server:
            print("\nDetalles de la llave de encapsulacion:")
            pprint(client.details)

            # Client generates its keypair
            public_key_client = client.generate_keypair()
            # Optionally, the secret key can be obtained by calling export_secret_key()
            # and the client can later be re-instantiated with the key pair:
            # secret_key_client = client.export_secret_key()

            # Store key pair, wait... (session resumption):
            # client = oqs.KeyEncapsulation(kemalg, secret_key_client)

            # The server encapsulates its secret using the client's public key
            ciphertext, shared_secret_server = server.encap_secret(public_key_client)

            # The client decapsulates the server's ciphertext to obtain the shared secret
            shared_secret_client = client.decap_secret(ciphertext)

            print("\n¿Los secretos compartidos coinciden? --> ", shared_secret_client == shared_secret_server)
    
    end_time = time.time()
    #print(f"ml_kem execution time: {end_time - start_time} seconds")
    return end_time - start_time

def ml_dsa():
    start_time = time.time()

    # print("liboqs version:", oqs.oqs_version())
    # print("liboqs-python version:", oqs.oqs_python_version())
    # print("Enabled signature mechanisms:")
    # sigs = oqs.get_enabled_sig_mechanisms()
    # pprint(sigs, compact=True)

    message = "El mensaje a firmar es este".encode()

    # Create signer and verifier with sample signature mechanisms
    sigalg = "Dilithium3"
    with oqs.Signature(sigalg) as signer:
        with oqs.Signature(sigalg) as verifier:
            print("\nDetalles de la firma:")
            pprint(signer.details)

            # Signer generates its keypair
            signer_public_key = signer.generate_keypair()
            # Optionally, the secret key can be obtained by calling export_secret_key()
            # and the signer can later be re-instantiated with the key pair:
            # secret_key = signer.export_secret_key()

            # Store key pair, wait... (session resumption):
            # signer = oqs.Signature(sigalg, secret_key)

            # Signer signs the message
            signature = signer.sign(message)

            # Verifier verifies the signature
            is_valid = verifier.verify(message, signature, signer_public_key)

            print("\n¿Firma valida?", is_valid)
    
    end_time = time.time()
    # print(f"ml_dsa execution time: {end_time - start_time} seconds")
    return end_time - start_time

def slh_dsa():
    start_time = time.time()

    # print("liboqs version:", oqs.oqs_version())
    # print("liboqs-python version:", oqs.oqs_python_version())
    # print("Enabled signature mechanisms:")
    # sigs = oqs.get_enabled_sig_mechanisms()
    # pprint(sigs, compact=True)

    message = "El mensaje a firmar es este".encode()

    # Create signer and verifier with sample signature mechanisms
    sigalg = "SPHINCS+-SHA2-256s-simple"
    with oqs.Signature(sigalg) as signer:
        with oqs.Signature(sigalg) as verifier:
            print("\nSignature details:")
            pprint(signer.details)

            # Signer generates its keypair
            signer_public_key = signer.generate_keypair()
            # Optionally, the secret key can be obtained by calling export_secret_key()
            # and the signer can later be re-instantiated with the key pair:
            # secret_key = signer.export_secret_key()

            # Store key pair, wait... (session resumption):
            # signer = oqs.Signature(sigalg, secret_key)

            # Signer signs the message
            signature = signer.sign(message)

            # Verifier verifies the signature
            is_valid = verifier.verify(message, signature, signer_public_key)

            print("\n¿Firma valida?", is_valid)
    
    end_time = time.time()
    #print(f"slh_dsa execution time: {end_time - start_time} seconds")
    return end_time - start_time

if __name__ == "__main__":
    print("Corriendo un programa")
    print("\n--------------------- Ejecutando ML-KEM ---------------------")
    tiempo1 = ml_kem()
    print("\n--------------------- Ejecutando ML-DSA ---------------------")
    tiempo2 = ml_dsa()
    print("\n--------------------- Ejecutando SLH-DSA ---------------------")
    tiempo3 = slh_dsa()

    print("---------------------------------------------------------------")
    print(f"\nML-KEM se tardó {tiempo1:1.4f} segundos\nML-DSA se tardó {tiempo2:1.4f} segundos\nSLH-DSA se tardó {tiempo3:1.4f} segundos")
