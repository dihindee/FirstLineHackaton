package com.hakaton.voicenews;

import android.Manifest;
import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.view.View;
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
    static private SpeechRecognize sr;

    private TextView sett;
    ArrayList<String> news = new ArrayList();
    String[] mas;
    int index;
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

        try {
            Information[] information;
            information = ReadJSONExample.readInformationJSONFile(this);
            mas = new String[information[0].getArticleInformation().length];
            for (int i = 0; i < information[0].getArticleInformation().length; i++) {
                news.add(information[0].getArticleInformation()[i].getTitle());
                mas[i] = information[0].getArticleInformation()[i].getTitle();

            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (JSONException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }

        newsList = (ListView) findViewById(R.id.newsList);
        adapter = new ArrayAdapter<String>(this, R.layout.news_list_articles, news);
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
        findViewById(R.id.voice).setOnClickListener(v -> sr.startRecognition());
    }

    public void perform_action(View v) {
//        RelativeLayout tv= (RelativeLayout) findViewById(R.id.lot1);
        try {
            TextView t = (TextView) v;
            Information[] information;
            information = ReadJSONExample.readInformationJSONFile(this);
            System.out.println(information[0].getArticleInformation()[0].getTitle());
            for (int i = 0; i < news.size(); i++) {
                if (mas[i] == t.getText()) {
                    index = i;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (JSONException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }
        Intent intent = new Intent(MainActivity.this, article.class);
        intent.putExtra("id", String.valueOf(index));
        startActivityForResult(intent, 0);
    }

    public void setting_action(View v) {
        sett = (TextView) findViewById(R.id.settings);
        Intent intent = new Intent(".settings");
        startActivity(intent);
    }
}