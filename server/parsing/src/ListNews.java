import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.*;
import java.net.URLEncoder;
import java.util.ArrayList;


import java.util.HashMap;
import java.util.Map;

public final class ListNews {
    private static final String FILENAMEFOOTBALL = "/Users/user/Desktop/server/resource/football.json";
    private static final String FILENAMEBUSINESS = "/Users/user/Desktop/server/resource/business.json";
    private static final String FILENAMEPOLITICS = "/Users/user/Desktop/server/resource//politics.json";
    private static final String FILENAMEIT = "/Users/user/Desktop/server/resource/it.json";
    private static final String FILEPY = "./src/tts.py";
    private static final String FILEAUDIO = "./web/resource/";
    static private Map<String, ArrayList<String>> adress;

    private static void deleteAllFilesFolder(String path,ArrayList<JSONObject> deleteFile) {
        for (File myFile : new File(path).listFiles()){
             if (myFile.isFile()) {
                deleteFile.forEach(del->{
                    if(del.get("urlAudio").toString().equals(myFile.getName()) || del.get("urlTitleAudio").toString().equals(myFile.getName()))
                        myFile.delete();
                });

             }
        }

    }

    static private void init() {
        adress = new HashMap<>();
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
                jsonObject.put("urlNews", parsing(url, params, (JSONArray) jsonObject.get("urlNews")));
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        FileWriter fileWriter = new FileWriter(filePath, false);
        fileWriter.write(jsonArray.toJSONString());
        fileWriter.flush();
        fileWriter.close();

    }

    static public ArrayList<JSONObject> parsing(String mainurl, ArrayList<String> params, JSONArray jsonArray) throws IOException {
        ArrayList<JSONObject> list = new ArrayList<>();
        ArrayList<JSONObject> deleteFile = new ArrayList<>(jsonArray);
        Document document = Jsoup.connect(mainurl).get();
        Elements elements = document.getElementsByAttributeValue("class", params.get(0));

        elements.forEach(element -> {
            int fl = 0;
            JSONObject object = new JSONObject();
            Element aElement = element.child(0);
            String url = aElement.attr("href");
            for (Object obj : jsonArray) {
                if (((JSONObject) obj).get("url").toString().equals(url)) {
                    object = (JSONObject) obj;
                    deleteFile.remove(obj);
                    fl = 1;
                }
            }
            ;
            if (fl == 0) {
                Elements elementText = null;
                try {
                    Document documentText = Jsoup.connect(url).get();
                    elementText = documentText.getElementsByAttributeValue("class", params.get(1));
                } catch (IOException e) {
                    e.printStackTrace();
                }

                String title = element.text();

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
            }
            list.add(object);
        });
        deleteAllFilesFolder(FILEAUDIO,deleteFile);
        return list;
    }

    public static void UpdateResourse() {
        init();
        adress.forEach((adress, param) -> {
            try {
                updateJson(adress, param);
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ParseException e) {
                e.printStackTrace();
            }
        });

    }
}