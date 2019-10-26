package com.hakaton.voicenews;

import android.content.Context;
import android.os.Bundle;
import android.speech.RecognitionListener;
import android.speech.SpeechRecognizer;
import android.util.Log;
import android.widget.Toast;

import com.icaksama.rapidsphinx.RapidSphinx;

import java.util.Objects;

public class MyRecognitionListener implements RecognitionListener {
    private Context context;
    private RapidSphinx sphinx;

    MyRecognitionListener(Context context){
        this.context = context;
        sphinx = ((MainActivity)context).rapidSphinx;
    }

    @Override
    public void onReadyForSpeech(Bundle params) {
        Log.d("Speech", "onReadyForSpeech");
    }

    @Override
    public void onBeginningOfSpeech() {
        Toast.makeText(context, "Speech started", Toast.LENGTH_LONG).show();
    }

    @Override
    public void onRmsChanged(float rmsdB) {
//        Log.d("Speech", "onRmsChanged");
    }

    @Override
    public void onBufferReceived(byte[] buffer) {
        Log.d("Speech", "onBufferReceived");
    }

    @Override
    public void onEndOfSpeech() {
        Toast.makeText(context, "Speech finished", Toast.LENGTH_LONG).show();
    }

    @Override
    public void onError(int error) {
//        Toast.makeText(context, "sorry error occurred: "+error, Toast.LENGTH_LONG).show();
        Log.i("ERROR", String.valueOf(error));
        sphinx.startRapidSphinx(1000);
    }

    @Override
    public void onResults(Bundle results) {
        Log.d("ParseResult", "onResults "+ results.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION));
        RequestParser.doAction(Objects.requireNonNull(results.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)));
        sphinx.startRapidSphinx(1000);
    }

    @Override
    public void onPartialResults(Bundle partialResults) {
        Log.d("Speech", String.valueOf(partialResults.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)));
    }

    @Override
    public void onEvent(int eventType, Bundle params) {
        Log.d("Speech", "onEvent");
    }
}
