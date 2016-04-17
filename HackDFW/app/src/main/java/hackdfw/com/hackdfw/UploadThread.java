package hackdfw.com.hackdfw;

import com.microsoft.azure.storage.CloudStorageAccount;
import com.microsoft.azure.storage.blob.CloudBlobClient;
import com.microsoft.azure.storage.blob.CloudBlobContainer;
import com.microsoft.azure.storage.blob.CloudBlockBlob;
import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;
import java.io.File;
import java.io.FileInputStream;

/**
 * Created by rohin on 16-04-2016.
 */
public class UploadThread extends AsyncTask<File,Void,String>{

    // Define the connection-string with your values
    public static final String storageConnectionString =
            "DefaultEndpointsProtocol=http;" +
                    "AccountName=hackdfwstorage;" +
                    "AccountKey=Jo3SJ5zxgi0ZxaYEe2tecmau+CzzHtdA2Nsf4zSX6/NJSieiF0r3TTZ2OI1sUHDgW+EcPOjqyDOWXBhQOB+5Ag==";

    @Override
    protected String doInBackground(File... uploadFile){
        saveData(uploadFile[0]);
        return "Success";
    }

    public void saveData(File photofile){
        try
        {
            // Retrieve storage account from connection-string.
            CloudStorageAccount storageAccount = CloudStorageAccount.parse(storageConnectionString);

            // Create the blob client.
            CloudBlobClient blobClient = storageAccount.createCloudBlobClient();

            // Retrieve reference to a previously created container.
            CloudBlobContainer container = blobClient.getContainerReference("mycontainer");

            // Create or overwrite the "myimage.jpg" blob with contents from a local file.
            CloudBlockBlob blob = container.getBlockBlobReference("myimage.jpg");
            blob.upload(new FileInputStream(photofile), photofile.length());
        }
        catch (Exception e)
        {
            // Output the stack trace.
            e.printStackTrace();
        }
    }

    protected void onPostExecute(String result){
        //RestThread restapi = new RestThread();
        //restapi.execute(" ");
        androidSocket sock = new androidSocket();
        sock.execute("hello");
    }
}
