package com.hakaton.voicenews;
import android.content.ActivityNotFoundException;
import android.content.Context;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class ReadJSONExample {
    public static Information[] readInformationJSONFile(Context context, int section) throws IOException, JSONException, ParseException {
        String jsonText1 = readText(context, R.raw.football);
        switch (section) {
            case 0: jsonText1 = readText(context, R.raw.football); break;
            case 1: jsonText1 = readText(context, R.raw.it); break;
        }
        JSONArray mJsonArray = new JSONArray(jsonText1);
        Information[] info = new Information[mJsonArray.length()];
        for (int i = 0; i < mJsonArray.length(); i++) {
            info[i] = new Information();
            JSONObject mJsonObject = mJsonArray.getJSONObject(i);
            JSONArray mJsonArrayProperty = mJsonObject.getJSONArray("urlNews");
            String url = mJsonObject.getString("url");
            ArticleInformation[] articleInformation = new ArticleInformation[mJsonArrayProperty.length()];
            for (int j = 0; j < mJsonArrayProperty.length(); j++) {
                articleInformation[j] = new ArticleInformation();
                JSONObject mJsonObjectProperty = mJsonArrayProperty.getJSONObject(j);
                String title = mJsonObjectProperty.getString("title");
                String text = mJsonObjectProperty.getString("Text");
                String urlActivityInformation = mJsonObjectProperty.getString("url");
                articleInformation[j].setArticleInformation(text, title, urlActivityInformation);
            }
            info[i].setArticleInformation(articleInformation);
        }

        return info;
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
