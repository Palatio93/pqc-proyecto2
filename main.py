import oqs
import time
from pprint import pprint

def ml_kem():
    #Gets the time of the start of the execution
    start_time = time.time()

    # Create client and server with sample KEM mechanisms
    kemalg = "Kyber512"
    #secures symmetric key for transmission using the key encapsulation mechanism Kyber512
    with oqs.KeyEncapsulation(kemalg) as client:
        with oqs.KeyEncapsulation(kemalg) as server:
            #Info in the client is printed
            print("\nDetalles de la llave de encapsulacion:")
            pprint(client.details)

            # Client generates its keypair
            public_key_client = client.generate_keypair()

            # The server encapsulates its secret using the client's public key
            ciphertext, shared_secret_server = server.encap_secret(public_key_client)

            # The client decapsulates the server's ciphertext to obtain the shared secret
            shared_secret_client = client.decap_secret(ciphertext)

            #If the secrets are the same or not it is printed
            print("\n¿Los secretos compartidos coinciden? --> ", shared_secret_client == shared_secret_server)

    #Gets the time of when the execution ended
    end_time = time.time()
    #Calculate the time of total execution substracting the end and start time of the execution
    return end_time - start_time

def ml_dsa():
    #Gets the time of the start of the execution
    start_time = time.time()
    #Get the message to sign, and encodes it using UTF-8
    message = "El mensaje a firmar es este".encode()

    # Create signer and verifier with sample signature mechanisms
    sigalg = "Dilithium3"
    #secures symmetric key for transmission using the key encapsulation mechanism Dilithium3
    with oqs.Signature(sigalg) as signer:
        with oqs.Signature(sigalg) as verifier:
            #Prints the info of the signer
            print("\nDetalles de la firma:")
            pprint(signer.details)

            # Signer generates its keypair
            signer_public_key = signer.generate_keypair()

            # Signer signs the message
            signature = signer.sign(message)

            # Verifier verifies the signature
            is_valid = verifier.verify(message, signature, signer_public_key)

            #Prints if the signature is valid or not
            print("\n¿Firma valida?", is_valid)

    #Gets the time of when the execution ended
    end_time = time.time()
    #Calculate the time of total execution substracting the end and start time of the execution
    return end_time - start_time

def slh_dsa():
    #Gets the time of the start of the execution
    start_time = time.time()
    #Get the message to sign, and encodes it using UTF-8
    message = "El mensaje a firmar es este".encode()

    # Create signer and verifier with sample signature mechanisms
    sigalg = "SPHINCS+-SHA2-256s-simple"
    #secures symmetric key for transmission using the key encapsulation mechanism SPHINCS+-SHA2-256s-simple
    with oqs.Signature(sigalg) as signer:
        with oqs.Signature(sigalg) as verifier:
            #Prints the info of the signer
            print("\nSignature details:")
            pprint(signer.details)

            # Signer generates its keypair
            signer_public_key = signer.generate_keypair()

            # Signer signs the message
            signature = signer.sign(message)

            # Verifier verifies the signature
            is_valid = verifier.verify(message, signature, signer_public_key)

            #Prints if the signature is valid or not
            print("\n¿Firma valida?", is_valid)


    #Gets the time of when the execution ended
    end_time = time.time()
    #Calculate the time of total execution substracting the end and start time of the execution
    return end_time - start_time

#Prints the execution of each algorithm and then its time.
if __name__ == "__main__":
    print("Corriendo un programa")
    print("\n--------------------- Ejecutando ML-KEM ---------------------")
    tiempo1 = ml_kem()
    print("\n--------------------- Ejecutando ML-DSA ---------------------")
    tiempo2 = ml_dsa()
    print("\n--------------------- Ejecutando SLH-DSA ---------------------")
    tiempo3 = slh_dsa()

#Prints the times for the execution for each algorithm
    print("---------------------------------------------------------------")
    print(f"\nML-KEM se tardó {tiempo1:1.4f} segundos\nML-DSA se tardó {tiempo2:1.4f} segundos\nSLH-DSA se tardó {tiempo3:1.4f} segundos")
