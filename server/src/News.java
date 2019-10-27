
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

@WebServlet("/news")
public class News extends HttpServlet {
    private static final String FILESPORT = "/Users/user/Desktop/server/resource/football.json";
    private static final String FILEBUSINESS = "/Users/user/Desktop/server/resource/business.json";
    private static final String FILEPOLITICS = "/Users/user/Desktop/server/resource/politics.json";
    private static final String FILEIT = "/Users/user/Desktop/server/resource/it.json";
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String param=req.getParameter("type");
        String fileName=null;
        switch (param){
            case ("sport"):
                fileName=FILESPORT;
                break;
            case ("business"):
                fileName=FILEBUSINESS;
                break;
            case ("politics"):
                fileName=FILEPOLITICS;
                break;
            case ("it"):
                fileName=FILEIT;
                break;
        }


    String content = Files.lines(Paths.get(fileName)).reduce("", String::concat);
    BufferedOutputStream bos = new BufferedOutputStream(resp.getOutputStream());
    bos.write(content.getBytes());
    bos.flush();
    bos.close();
    }
}
