import java.net.*; 
import java.io.*; 
  
public class receiver
{ 
    // initialize socket and input output streams 
    private Socket socket            = null; 
    private BufferedReader  input    = null; 
    private DataOutputStream out     = null;
    private DataInputStream in       =  null;
  
    // constructor to put ip address and port 
    public receiver(String address, int port) 
    { 
        // establish a connection 
        try
        { 
            socket = new Socket(address, port); 
            System.out.println("Connection established"); 
  
            // takes input from terminal 
            input  = new BufferedReader(new InputStreamReader(System.in)); 
  
            // sends output to the socket 
            out    = new DataOutputStream(socket.getOutputStream());

            in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
        } 
        catch(UnknownHostException u) 
        { 
            System.out.println(u); 
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
  
        String line = ""; 
        String size = "";
        String ack = "";
        String win = "";
        int n, w, w2, k, j;
  
        while (true) 
        { 
            try
            { 
                System.out.println("Enter the No. of data items. Enter 't' to terminate.");
                size = input.readLine(); 
                out.writeUTF(size);
                if(size.equals("t"))
                    break;
                n=Integer.parseInt(size);
                System.out.println("window size:");
                win = input.readLine();
                out.writeUTF(win);
                w=Integer.parseInt(win);
                System.out.println("Enter "+n+" data elements:");
                w2=w;
                n=n-w;
                k=1;
                j=1;
                while(w>0)
                {
                    try
                    { 
                        System.out.print("no."+k+"-> ");
                        line = input.readLine();
                        out.writeUTF(line);
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
                        ack = in.readUTF();
                        System.out.println(ack+" "+j+" received");
                        System.out.print("item "+k+": ");
                        line = input.readLine(); 
                        out.writeUTF(line);
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
                    ack = in.readUTF();
                    System.out.println(ack+" "+j+" received");
                    w2--;
                    j++;
                }
            } 
            catch(IOException i) 
            { 
                System.out.println(i); 
            } 
        } 
  
        // close the connection 
        try
        { 
            input.close(); 
            out.close(); 
            socket.close(); 
            in.close();
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
    } 
  
    public static void main(String args[]) 
    { 
        receiver receiver = new receiver("localhost", 4000); 
    } 
} 
