import socket, click , os
from app.file_service import file_prompt
 
def Main():

    host = '127.0.0.1'
    port = 2048
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        s.connect((host,port))

        while True:
            
            if not os.path.isfile(".env"): 

                file_prompt()

            client = input(" Dîtes quelque chose (q : quitter , m : modifier api_key ) > ")

            if client == "q":
                
                
                break
            
            elif client == "m":
                
                file_prompt()
                break

            s.send(client.encode('ascii'))
            data = s.recv(1024)
            resp = str(data.decode('ascii'))

            click.echo("----------------------------------------------------------")
            click.echo(f"<< 🤖 >> {resp}")
            click.echo("\n")
            click.echo("----------------------------------------------------------")
   
    except BrokenPipeError:
        print("Connection lost")

    finally:
        # close the connection
        s.close()
 
if __name__ == '__main__':
    Main()