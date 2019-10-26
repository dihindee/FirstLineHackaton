package com.hakaton.voicenews;

import android.content.Context;
import android.content.Intent;
import android.speech.RecognizerIntent;
import android.speech.SpeechRecognizer;
import android.view.View;

public class SpeechRecognize {
    SpeechRecognizer sr;

    public SpeechRecognize(Context context){
        sr = SpeechRecognizer.createSpeechRecognizer(context);
        sr.setRecognitionListener(new MyRecognitionListener(context));
    }

    void startRecognition(){
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "ru-RU");
        sr.startListening(intent);
    }
}
