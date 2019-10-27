package com.hakaton.voicenews;

import android.Manifest;
import android.app.ProgressDialog;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import com.icaksama.rapidsphinx.RapidPreparationListener;
import com.icaksama.rapidsphinx.RapidSphinx;

import java.util.ArrayList;

import edu.cmu.pocketsphinx.Config;

public class MainActivity extends AppCompatActivity {
    static RapidSphinx rapidSphinx;
    static private SphinxListener listener;
    static private SpeechRecognize sr;

    private TextView sett;
    ArrayList<String> news = new ArrayList();
    ArrayAdapter<String> adapter;
    ListView newsList;
    private void requestPermission() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.RECORD_AUDIO}, 1);
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        RequestParser.setCurrentActivity("MainActivity");
        RequestParser.mainScreen = this;
        getSupportActionBar().hide();
//        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_main);
        requestPermission();
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
        if(rapidSphinx==null) {
            rapidSphinx = new RapidSphinx(this);

            sr = new SpeechRecognize(this);

            listener = new SphinxListener(rapidSphinx, sr);
            rapidSphinx.addListener(listener);
            ProgressDialog dialog = ProgressDialog.show(MainActivity.this, "",
                    "Preparing data. Please wait...", true);
            rapidSphinx.prepareRapidSphinx(new RapidPreparationListener() {
                @Override
                public void rapidPreExecute(Config config) {
                    rapidSphinx.setSilentToDetect(2000);
                    rapidSphinx.setVadThreshold(1);
                    rapidSphinx.setTimeOutAfterSpeech(10000);
                    config.setBoolean("-backtrace", true);
                }

                @Override
                public void rapidPostExecute(boolean isSuccess) {
                    Toast.makeText(getApplicationContext(), "RapidSphinx ready!", Toast.LENGTH_SHORT).show();
                    rapidSphinx.updateVocabulary("igor", new String[]{}, () -> {
                        dialog.dismiss();
                        rapidSphinx.startRapidSphinx(10000);
                    });
                }
            });
        }
        findViewById(R.id.voice).setOnClickListener(v -> sr.startRecognition());
    }

    public void perform_action(View v)
    {
//        RelativeLayout tv= (RelativeLayout) findViewById(R.id.lot1);
        System.out.println(v);
        Intent intent = new Intent(".article");
        RequestParser.setCurrentActivity("artice");
        startActivity(intent);
    }

    public void setting_action(View v) {
        sett = (TextView)findViewById(R.id.settings);
        Intent intent = new Intent(".settings");
        startActivity(intent);
    }
}
