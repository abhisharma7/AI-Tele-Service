package hackdfw.com.hackdfw;


import com.microsoft.azure.storage.CloudStorageAccount;
import com.microsoft.azure.storage.blob.CloudBlobClient;
import com.microsoft.azure.storage.blob.CloudBlobContainer;
import com.microsoft.azure.storage.blob.CloudBlockBlob;
import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.io.File;
import java.io.FileInputStream;
import java.net.Socket;


/**
 * Created by rohin on 16-04-2016.
 */
public class RestThread extends AsyncTask<String,Void,String>{

    @Override
    protected String doInBackground(String...params){
        try {
           URL url = new URL("https://ec2-54-186-94-164.us-west-2.compute.amazonaws.com:7000/request");

            String valueurl = "https://something.com";
            URLConnection con = url.openConnection();
            String valuephone = "6823138508";
            String data  = URLEncoder.encode("URL","UTF-8") +
                    "=" + URLEncoder.encode(valueurl,"UTF-8");
            data += "&" + URLEncoder.encode("phone_number","UTF-8") +
                    "=" +URLEncoder.encode(valuephone,"UTF-8");
            con.setDoOutput(true);
            OutputStreamWriter writer = new OutputStreamWriter(con.getOutputStream());
            writer.write(" ");
            writer.flush();
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
        return "Nothing";
    }
}
