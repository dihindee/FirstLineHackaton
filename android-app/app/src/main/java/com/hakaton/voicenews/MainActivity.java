package com.hakaton.voicenews;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView sett;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().hide();
//        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_main);
    }

    public void perform_action(View v)
    {
        RelativeLayout tv= (RelativeLayout) findViewById(R.id.lot1);
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
