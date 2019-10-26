import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

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
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        String param=req.getParameter("type");
//        switch (param){
////            case ("football"):
////                ////////
////                break;
////            case ("business"):
////                break;
////        }
//

    String fileName = "/Users/user/Desktop/server/resource/football.json";
    String content = Files.lines(Paths.get(fileName)).reduce("", String::concat);
    BufferedOutputStream bos = new BufferedOutputStream(resp.getOutputStream());
    bos.write(content.getBytes());
    bos.flush();
    bos.close();




        //PrintWriter printWriter=resp.getWriter();
//        printWriter.write(param);
    }
}
