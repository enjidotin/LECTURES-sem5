// A Java program for a Server 
import java.net.*; 
import java.io.*; 
  
public class sender 
{ 
    //initialize socket and input stream 
    private Socket          socket   = null; 
    private ServerSocket    server   = null; 
    private DataInputStream in       =  null;
    private DataOutputStream out     = null;
  
    // constructor with port 
    public sender(int port) 
    { 
        // starts server and waits for a connection 
        try
        { 
            server = new ServerSocket(port); 
            System.out.println("Server started"); 
  
            System.out.println("Waiting for a client ..."); 
  
            socket = server.accept(); 
            System.out.println("Client accepted"); 
  
            // takes input from the client socket 
            in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
            
            out = new DataOutputStream(socket.getOutputStream());
  
            String line = "";
            String size = "";
            String ack = "Ack";
            String window = "";
            int n, w, w2, k, j;
  
            // reads message from client until "Over" is sent 
            while (true) 
            { 
                try
                { 
                    size = in.readUTF(); 
                    if(size.equals("Over"))
                        break;
                    n=Integer.parseInt(size);
                    window = in.readUTF();
                    w=Integer.parseInt(window);
                    w2=w;
                    n=n-w;
                    k=1;
                    j=1;
                    while(w>0)
                    {
                        try
                        { 
                            line = in.readUTF(); 
                            System.out.println("Received data item "+k+": "+line); 
                        } 
                        catch(IOException i) 
                        { 
                            System.out.println(i); 
                        }
                        w--;
                        k++;
                    }
                    while(n>0)
                    {
                        try
                        { 
                            out.writeUTF(ack);
                            System.out.println(ack+" "+j+" sent");
                            line = in.readUTF(); 
                            System.out.println("Received data item "+k+": "+line); 
                        } 
                        catch(IOException i) 
                        { 
                            System.out.println(i); 
                        }
                        n--;
                        k++;
                        j++;
                    }
                    while(w2>0)
                    {
                        out.writeUTF(ack);
                        System.out.println(ack+" "+j+" sent");
                        w2--;
                        j++;
                    }
                } 
                catch(IOException i) 
                { 
                    System.out.println(i); 
                } 
            } 
            System.out.println("Closing connection"); 
  
            // close connection 
            socket.close(); 
            in.close(); 
            out.close();
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
    } 
  
    public static void main(String args[]) 
    { 
        sender sender = new sender(4000); 
    } 
} 
