package com.hakaton.voicenews;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class article extends AppCompatActivity {
    private TextView sett;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_article);
        RequestParser.articleScreen = this;
        TextView back = (TextView)findViewById(R.id.back);
        back.setOnClickListener(v -> onBackPressed());

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
    @Override
    public void onBackPressed(){
        super.onBackPressed();
        RequestParser.setCurrentActivity("MainActivity");
    }
}
