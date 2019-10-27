package com.hakaton.voicenews;

import android.content.Context;
import android.util.Log;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class ReadJSONExample {
    public static Information[] readInformationJSONFile(Context context, int section) throws InterruptedException {
        final Information[][] info = {null};
        Thread t = new Thread(() -> {
        try {
            String host = "http://91.225.131.248:8080/news?type=";
            URL obj = null;
            String jsonText1;
            switch (section) {
                case 0:
                    obj = new URL(host + "sport");
                    break;
                case 2:
                    obj = new URL(host + "business");
                    break;
                case 1:
                    obj = new URL(host + "it");
                    break;
                case 3:
                    obj = new URL(host + "politics");
                    break;
                default:
                    throw new IllegalStateException("Unexpected value: " + 0);
            }
            HttpURLConnection connection = (HttpURLConnection) obj.openConnection();
            Log.i("ParseResult", String.valueOf(obj));
            Log.i("ParseResult", connection.toString());
            connection.setRequestMethod("GET");
            String inputLine;
            StringBuilder response = new StringBuilder();
            InputStream is = connection.getInputStream();
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader in = new BufferedReader(isr);
            while ((inputLine = in.readLine()) != null)
                response.append(inputLine);
            jsonText1 = response.toString();
            Log.i("ParseResult", jsonText1);
            JSONArray mJsonArray = new JSONArray(jsonText1);
            info[0] = new Information[mJsonArray.length()];
            for (int i = 0; i < mJsonArray.length(); i++) {
                info[0][i] = new Information();
                JSONObject mJsonObject = mJsonArray.getJSONObject(i);
                JSONArray mJsonArrayProperty = mJsonObject.getJSONArray("urlNews");
                String url = mJsonObject.getString("url");
                ArticleInformation[] articleInformation = new ArticleInformation[mJsonArrayProperty.length()];
                for (int j = 0; j < mJsonArrayProperty.length(); j++) {
                    articleInformation[j] = new ArticleInformation();
                    JSONObject mJsonObjectProperty = mJsonArrayProperty.getJSONObject(j);
                    String urlAudio = mJsonObjectProperty.getString("urlAudio");
                    String urlTitleAudio = mJsonObjectProperty.getString("urlTitleAudio");
                    String title = mJsonObjectProperty.getString("title");
                    String text = mJsonObjectProperty.getString("Text");
                    String urlActivityInformation = mJsonObjectProperty.getString("url");
                    articleInformation[j].setArticleInformation(urlTitleAudio, urlAudio, text, title, urlActivityInformation);
                }
                info[0][i].setArticleInformation(articleInformation);
            }
        }catch (Exception e){e.printStackTrace();}
    });
        t.start();
        while(info[0] ==null){
            Thread.sleep(100);
        }
        return info[0];
    }



    private static String readText(Context context, int resId) throws IOException {
        InputStream is = context.getResources().openRawResource(resId);
        BufferedReader br= new BufferedReader(new InputStreamReader(is));
        StringBuilder sb= new StringBuilder();
        String s = null;
        while((  s = br.readLine())!=null) {
            sb.append(s);
            sb.append("\n");
        }
        return sb.toString();
    }
}
