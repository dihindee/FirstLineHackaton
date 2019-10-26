import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.util.ArrayList;


import java.io.FileReader;
import java.io.IOException;

public final class ListNews {
    private static final String FILENAMEFOTBALL = "./resource/football.json";
    private static final String FILENAMEBUSINESS = "./resource/business.json";
    private static final String FILEPY = "./src/tts.py";
    private static final String FILEAUDIO = "./web/resource/";

   static public void updateJson() throws IOException, ParseException {
        JSONParser parser = new JSONParser();
        JSONArray jsonArray = (JSONArray) parser.parse(new FileReader(FILENAMEFOTBALL));
        jsonArray.forEach(elm -> {
            JSONObject jsonObject = (JSONObject) elm;
            String url = jsonObject.get("url").toString();
            try {
                jsonObject.put("urlNews",parsing(url));
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        FileWriter fileWriter=new FileWriter(FILENAMEFOTBALL,false);
        fileWriter.write(jsonArray.toJSONString());
        fileWriter.flush();
        fileWriter.close();

    }
    static public ArrayList<JSONObject> parsing(String mainurl) throws IOException  {
        ArrayList<JSONObject> list=new ArrayList<>();
        Document document=Jsoup.connect(mainurl).get();
        Elements elements=document.getElementsByAttributeValue("class","se19-news-item mr_35");
        elements.forEach(element -> {
            Element aElement=element.child(0);
            String url=aElement.attr("href");
            Elements elementText = null;
            try {
                Document documentText = Jsoup.connect(url).get();
                elementText=documentText.getElementsByAttributeValue("class", "js-swiptable-holder article_text publication blackcolor mt_10 mb_15 js-mediator-article");
            } catch (IOException e) {
                e.printStackTrace();
            }

            String title=element.text();
            JSONObject object=new JSONObject();
            object.put("url",url);
            object.put("title",title);
            object.put("Text",elementText.text());
            object.put("urlTitleAudio","title"+title.hashCode()+".mp3");
            object.put("urlAudio",title.hashCode()+".mp3");
            try {
                Process p = Runtime.getRuntime().exec("python3 "+FILEPY+" "+title+" "+FILEAUDIO+"title"+title.hashCode()+".mp3");
                Process p1 = Runtime.getRuntime().exec("python3 "+FILEPY+" "+elementText.text()+" "+FILEAUDIO+title.hashCode()+".mp3");
            } catch (Exception e) {
                e.printStackTrace();
            }

            list.add(object);
         });
        return list;
    }

    public static void main(String[] args) throws IOException, ParseException {
        updateJson();
    }
}
