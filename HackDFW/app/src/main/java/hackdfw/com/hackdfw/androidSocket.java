package hackdfw.com.hackdfw;

import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.io.File;
import java.io.FileInputStream;
import java.net.Socket;

/**
 * Created by rohin on 17-04-2016.
 */
public class androidSocket extends AsyncTask<String,Void,String>{
    private static final String HOST = "ec2-54-186-94-164.us-west-2.compute.amazonaws.com";
    private  static final int PORT = 7000;

    @Override
    protected String doInBackground(String...params){
        String retValue= null;
        try{
            Socket socket = new Socket(HOST,PORT);
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            String url_website = "https://hackdfwstorage.blob.core.windows.net/mycontainer/myimage.jpg";
            String phone_number = "16822414439";
            String data = url_website + "," + phone_number;
            writer.write(data);
            writer.flush();
            writer.close();
            retValue = "Success";
        }
        catch (IOException e){
            e.printStackTrace();
            retValue = "Failure";
        }
        return retValue;
    }


}
