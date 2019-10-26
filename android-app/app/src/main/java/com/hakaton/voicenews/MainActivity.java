package com.hakaton.voicenews;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.RelativeLayout;
import android.widget.Spinner;
import android.widget.TextView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private TextView sett;
    ArrayList<String> news = new ArrayList();
    ArrayAdapter<String> adapter;
    ListView newsList;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().hide();
//        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_main);

        Spinner spinner = (Spinner) findViewById(R.id.spinner);
        ArrayAdapter adapter = ArrayAdapter.createFromResource(this, R.array.categories, R.layout.main_spinner);
        adapter.setDropDownViewResource(R.layout.spinner_dropout);
        spinner.setAdapter(adapter);

        news.add("iPhone 7");
        news.add("Samsung Galaxy S7");
        news.add("Google Pixel");
        news.add("Huawei P10");
        news.add("HP Elite z3");
        news.add("iPhone 7");
        news.add("Samsung Galaxy S7");
        news.add("Google Pixel");
        news.add("Huawei P10");
        news.add("HP Elite z3");

        newsList = (ListView) findViewById(R.id.newsList);
        adapter = new ArrayAdapter<String>(this, R.layout.news_list_articles, news);
        newsList.setAdapter(adapter);
    }

    public void perform_action(View v)
    {
//        RelativeLayout tv= (RelativeLayout) findViewById(R.id.lot1);
        System.out.println(v);
        Intent intent = new Intent(".article");
        startActivity(intent);
    }

    public void setting_action(View v) {
        sett = (TextView)findViewById(R.id.settings);
        Intent intent = new Intent(".settings");
        startActivity(intent);
    }
}
