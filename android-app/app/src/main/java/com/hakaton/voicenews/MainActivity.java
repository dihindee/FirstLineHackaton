package com.hakaton.voicenews;

import android.Manifest;
import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import com.icaksama.rapidsphinx.RapidPreparationListener;
import com.icaksama.rapidsphinx.RapidSphinx;

import org.json.JSONException;
import org.json.simple.parser.ParseException;

import java.io.IOException;
import java.util.ArrayList;

import edu.cmu.pocketsphinx.Config;

public class MainActivity extends AppCompatActivity {
    static RapidSphinx rapidSphinx;
    static private SphinxListener listener;
    static SpeechRecognize sr;

    private TextView sett;
    int currentSection = 1;
    boolean fl;
    ArrayList<String> news = new ArrayList();
    String[] mas;
    int index;
    ArrayAdapter<String> adapter1;
    ListView newsList;
    Spinner spinner;

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
        spinner = findViewById(R.id.spinner);
        ArrayAdapter adapter = ArrayAdapter.createFromResource(this, R.array.categories, R.layout.main_spinner);
        adapter.setDropDownViewResource(R.layout.spinner_dropout);
        spinner.setAdapter(adapter);

        newsList = findViewById(R.id.newsList);
        adapter = new ArrayAdapter<>(this, R.layout.news_list_articles, news);
        newsList.setAdapter(adapter);

        if (rapidSphinx == null) {
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
        updateTitles();
//        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
//            @Override
//            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
//                currentSection = position;
//                try {
//                    Information[] information;
//                    information = ReadJSONExample.readInformationJSONFile(getApplicationContext(), currentSection);
//                    mas = new String[information[0].getArticleInformation().length];
//                    news.clear();
////                    System.out.println(fl);
//                    for (int i = 0; i < information[0].getArticleInformation().length; i++) {
//                        System.out.println(1);
//                        news.add(information[0].getArticleInformation()[i].getTitle());
//                        System.out.println(information[0].getArticleInformation()[i].getTitle());
//                        mas[i] = information[0].getArticleInformation()[i].getTitle();
//
//                    }
//                } catch (Exception e) {
//                    e.printStackTrace();
//                }
//                adapter1 = new ArrayAdapter<>(getApplicationContext(), R.layout.news_list_articles, news);
////                System.out.println(newsList);
//                newsList.setAdapter(adapter1);
//                for(int i = 0; i< newsList.getChildCount(); i++)
//                    newsList.getChildAt(i).setOnClickListener(new View.OnClickListener() {
//                        @Override
//                        public void onClick(View v) {
//                            perform_action(v);
//                        }
//                    });
//            }
//
//            @Override
//            public void onNothingSelected(AdapterView<?> parent) {
//
//            }
//        });
        spinner.setSelection(1);
        findViewById(R.id.voice).setOnClickListener(v -> {
            sr.startRecognition();
            if (RequestParser.player!=null && RequestParser.player.isPlaying()) RequestParser.player.pause();
        });
    }

    public void updateTitles() {
        try {
            Information[] information;
            information = ReadJSONExample.readInformationJSONFile(getApplicationContext(),1);
            mas = new String[information[0].getArticleInformation().length];
            for (int i = 0; i < information[0].getArticleInformation().length; i++) {
                news.add(information[0].getArticleInformation()[i].getTitle());
                mas[i] = information[0].getArticleInformation()[i].getTitle();

            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void perform_action(View v) {
//        Log.i("ParseResult", v.getClass().toString() + "   " + v.toString());
        try {
            TextView t = (TextView) v;
            Information[] information;
            information = ReadJSONExample.readInformationJSONFile(this, 1);
            System.out.println(information[0].getArticleInformation()[0].getTitle());
            for (int i = 0; i < news.size(); i++) {
                if (mas[i] == t.getText()) {
                    index = i;
                }
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        Intent intent = new Intent(MainActivity.this, article.class);
        intent.putExtra("id", String.valueOf(index));
        startActivityForResult(intent, 0);
    }

    public void setting_action(View v) {
        sett = findViewById(R.id.settings);
        Intent intent = new Intent(".settings");
        startActivity(intent);
    }
}