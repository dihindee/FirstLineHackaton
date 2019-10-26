package com.hakaton.voicenews;

import android.util.Log;

import com.icaksama.rapidsphinx.RapidSphinx;
import com.icaksama.rapidsphinx.RapidSphinxListener;

import java.util.List;

public class SphinxListener implements RapidSphinxListener {
    private RapidSphinx sphinx;
    private SpeechRecognize sr;

    SphinxListener(RapidSphinx sphinx, SpeechRecognize sr) {
        this.sphinx = sphinx;
        this.sr = sr;
    }

    @Override
    public void rapidSphinxDidStop(String reason, int code) {
        if (code == 500) { // 200 code for error
            Log.w("Speech", reason + code);
        } else if (code == 522) { // 200 code for timed out
            Log.w("Speech", reason + code);
        } else if (code == 200) { // 200 code for finish speech
            Log.w("Speech", reason + code);
        }
        sphinx.startRapidSphinx(1000);
    }

    @Override
    public void rapidSphinxFinalResult(String result, List<String> hypArr, List<Double> scores) {
//        if(result.contains("igor")){
//            sr.startRecognition();
//        }
//        else sphinx.startRapidSphinx(10000);
    }

    @Override
    public void rapidSphinxPartialResult(String partialResult) {
        if(partialResult.contains("igor")){
            sphinx.stop();
            sr.startRecognition();
        }
    }

    @Override
    public void rapidSphinxUnsupportedWords(List<String> words) {

    }

    @Override
    public void rapidSphinxDidSpeechDetected() {

    }
}
