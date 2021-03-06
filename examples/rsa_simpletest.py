# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Adafruit_CircuitPython_RSA Encryption/Decryption
import ursa

# Create a keypair
print("Generating keypair...")
(public_key, private_key) = ursa.newkeys(512)

# Message to send
message = "hello blinka"

# Encode the string as bytes (Adafruit_RSA only operates on bytes!)
message = message.encode("utf-8")

# Encrypt the message using the public key
print("Encrypting message...")
encrypted_message = ursa.encrypt(message, public_key)

# Decrypt the encrypted message using a private key
print("Decrypting message...")
decrypted_message = ursa.decrypt(encrypted_message, private_key)

# Print out the decrypted message
print("Decrypted Message: ", decrypted_message.decode("utf-8"))
