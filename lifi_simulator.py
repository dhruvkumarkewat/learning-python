import time

# Step 1: Convert text to binary
def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

# Step 2: Convert binary back to text
def binary_to_text(binary):
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        text += chr(int(byte, 2))
    return text

# Step 3: Simulate Li-Fi transmission
def transmit_data(binary_data):
    print("\n🔄 Transmitting Data using Light (Li-Fi Simulation)...\n")
    for bit in binary_data:
        if bit == '1':
            print("💡 Light ON (1)")
        else:
            print("💡 Light OFF (0)")
        time.sleep(0.1)  # Delay to simulate transmission speed
    print("\n✅ Transmission Complete!")
    return binary_data

# Step 4: Simulate receiver
def receive_data(binary_data):
    print("\n📥 Receiving Data...\n")
    received_text = binary_to_text(binary_data)
    return received_text

# Main program
def lifi_simulator():
    print("========== 💡 Li-Fi Simulator (Python Project) ==========\n")
    user_message = input("Enter a message to transmit: ")

    # Encoding
    binary_message = text_to_binary(user_message)
    print(f"\n📦 Binary Encoded Message: {binary_message}")

    # Transmission (simulation)
    transmitted_binary = transmit_data(binary_message)

    # Reception
    decoded_message = receive_data(transmitted_binary)
    print(f"\n📨 Decoded Message at Receiver: {decoded_message}")

    # Final result
    if user_message == decoded_message:
        print("\n✅ Transmission Successful! No errors.")
    else:
        print("\n❌ Transmission Failed. Message corrupted.")

# Run the program
if __name__ == "_main_":
    lifi_simulator()