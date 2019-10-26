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
import java.net.URLEncoder;
import java.util.ArrayList;


import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public final class ListNews {
    private static final String FILENAMEFOOTBALL = "./resource/football.json";
    private static final String FILENAMEBUSINESS = "./resource/business.json";
    private static final String FILENAMEPOLITICS = "./resource/politics.json";
    private static final String FILENAMEIT = "./resource/it.json";
    private static final String FILEPY = "./src/tts.py";
    private static final String FILEAUDIO = "./web/resource/";
    static private Map<String, ArrayList<String>> adress;

    static private void init() {
        adress=new HashMap<>();
        ArrayList<String> params = new ArrayList<>();
        params.add("card  card--small card--horizontal");
        params.add("all-body js-mediator-article");
        adress.put(FILENAMEBUSINESS, (ArrayList<String>) params.clone());
        params.clear();
        params.add("se19-news-item mr_35");
        params.add("js-swiptable-holder article_text publication blackcolor mt_10 mb_15 js-mediator-article");
        adress.put(FILENAMEFOOTBALL, (ArrayList<String>) params.clone());
        params.clear();
        params.add("post__title");
        params.add("post__body post__body_full");
        adress.put(FILENAMEIT, (ArrayList<String>) params.clone());
        params.clear();
        params.add("list-item__content");
        params.add("article__body js-mediator-article mia-analytics");
        adress.put(FILENAMEPOLITICS, (ArrayList<String>) params.clone());
        params.clear();
    }


    static public void updateJson(String filePath, ArrayList<String> params) throws IOException, ParseException {
        JSONParser parser = new JSONParser();
        JSONArray jsonArray = (JSONArray) parser.parse(new FileReader(filePath));
        jsonArray.forEach(elm -> {
            JSONObject jsonObject = (JSONObject) elm;
            String url = jsonObject.get("url").toString();
            try {
                jsonObject.put("urlNews", parsing(url, params));
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        FileWriter fileWriter = new FileWriter(filePath, false);
        fileWriter.write(jsonArray.toJSONString());
        fileWriter.flush();
        fileWriter.close();

    }

    static public ArrayList<JSONObject> parsing(String mainurl, ArrayList<String> params) throws IOException {
        ArrayList<JSONObject> list = new ArrayList<>();
        Document document = Jsoup.connect(mainurl).get();
        Elements elements = document.getElementsByAttributeValue("class", params.get(0));
        elements.forEach(element -> {
            Element aElement = element.child(0);
            String url = aElement.attr("href");
            Elements elementText = null;
            try {
                Document documentText = Jsoup.connect(url).get();
                elementText = documentText.getElementsByAttributeValue("class", params.get(1));
            } catch (IOException e) {
                e.printStackTrace();
            }

            String title = element.text();
            JSONObject object = new JSONObject();
            object.put("url", url);
            object.put("title", title);
            object.put("Text", elementText.text());
            object.put("urlTitleAudio", "title" + title.hashCode() + ".mp3");
            object.put("urlAudio", title.hashCode() + ".mp3");
            try {
                Process p = Runtime.getRuntime().exec("python3 " + FILEPY + " " + title + " " + FILEAUDIO + "title" + title.hashCode() + ".mp3");
                Process p1 = Runtime.getRuntime().exec("python3 " + FILEPY + " " + elementText.text() + " " + FILEAUDIO + title.hashCode() + ".mp3");
            } catch (Exception e) {
                e.printStackTrace();
            }

            list.add(object);
        });
        return list;
    }

    public static void main(String[] args) throws IOException, ParseException {
       init();
       // updateJson(FILENAMEIT,adress.get(FILENAMEIT));
        adress.forEach((adress,param)->{
            try {
                updateJson(adress,param);
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ParseException e) {
                e.printStackTrace();
            }
        });

//        Document document = Jsoup.connect("https://www.forbes.ru/new").get();
//        Elements elements = document.getElementsByAttributeValue("class","card  card--small card--horizontal");
//        System.out.println(elements);
//        elements.forEach(element -> {
//            Element aElement = element.child(0);
//            String url = aElement.attr("href");
//
//           Elements elementText = null;
//            try {
//                Document documentText = Jsoup.connect(url).get();
//                elementText = documentText.getElementsByAttributeValue("class","all-body js-mediator-article");
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//            System.out.println(url);
//            String title = element.text();
//            System.out.println(element.text());
//            System.out.println(elementText.text());
//
//        });
    }
}