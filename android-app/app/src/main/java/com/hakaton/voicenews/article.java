package com.hakaton.voicenews;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.text.Html;
import android.text.Spannable;
import android.text.SpannableStringBuilder;
import android.text.method.LinkMovementMethod;
import android.text.style.ClickableSpan;
import android.text.style.URLSpan;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONException;
import org.json.simple.parser.ParseException;

import java.io.IOException;

public class article extends Activity {
    private TextView sett;
    private TextView outputText;
    private TextView outputText1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_article);
        int index = Integer.parseInt(getIntent().getStringExtra("id"));
        int currentSection = Integer.parseInt(getIntent().getStringExtra("section"));
        RequestParser.articleScreen = this;

        TextView back = (TextView)findViewById(R.id.back);
        back.setOnClickListener(v -> onBackPressed());
        outputText = (TextView)findViewById(R.id.textView3);
        outputText1 = (TextView)findViewById(R.id.textView4);
        try {

            Information[] information;
            information = ReadJSONExample.readInformationJSONFile(this, currentSection);
            outputText.setText(information[0].getArticleInformation()[index].getTitle());
            outputText1.setText(Html.fromHtml(information[0].getArticleInformation()[index].getText()+ "\n"+"Источник: "+"<a href="+"\""+information[0].getArticleInformation()[index].getUrl()+"\""+">Здесь</a>"));
            outputText1.setMovementMethod(LinkMovementMethod.getInstance());

        } catch (IOException e) {
            e.printStackTrace();
        } catch (JSONException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }

    }

    public void perform_action(View v)
    {
//        RelativeLayout tv= (RelativeLayout) findViewById(R.id.lot1);
        //System.out.println(v);
        Intent intent = new Intent(".article");
        startActivity(intent);
    }

    public void setting_action(View v) {
        sett = (TextView)findViewById(R.id.settings);
        Intent intent = new Intent(".settings");
        startActivity(intent);
    }
    @Override
    public void onBackPressed(){
        super.onBackPressed();
        RequestParser.setCurrentActivity("MainActivity");
    }
}
