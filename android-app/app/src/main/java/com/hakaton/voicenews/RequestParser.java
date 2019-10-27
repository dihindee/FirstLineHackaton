package com.hakaton.voicenews;

import android.content.Context;
import android.content.Intent;
import android.util.Log;
import android.view.View;
import android.widget.Spinner;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import java.util.ArrayList;

public class RequestParser{
    static final String[] settings ={"настройки","открой настройки", "настройка", "settings", "сеттинги"};
    static final String[] categoryRequest ={"покажи новости про","новости о","новости про","открой категорию","категория"};
    static final String[] categories = {"спорт","sport","it","это","айти","business","бизнес","политик"};
    static final String[] readHeaders = {"прочитай заголовки", "прочти заголовки", "читай заголовки"};
    static final String[] openText = {"открой про","новость про", "открой новость про","открой новости", "открой"};
    static final String[] readText = {"прочитай новость", "прочитай", "читай", "прочитай новости", "почитай новости", "почитай новость"};
    static final String[] stopReading = {"стой","подожди","постой","погоди","стоп","останови"};
    static final String[] continueReading = {"продолжай","давай дальше","читай дальше"};
    static final String[] restartReading = {"начни с начала","давай с начала","начни заново","давай заново"};
    static final String[] openSource = {"открой источник","источник новости","откуда новость"};
    static final String[] goBack = {"назад","давай назад","вернись назад"};
    static final String[] exit = {"выход","выключи","вырубай","гаси","заткнись","заткнися"};
    static String currentActivity;
    static MainActivity mainScreen;
    static article articleScreen;
    static settings settingsScreen;
    static void setCurrentActivity(String activity){
        currentActivity = activity;
    }
    static void doAction(ArrayList<String> hyps){
        String hyp = hyps.get(0).toLowerCase();
        for(String str : settings) {
            if(hyp.contains(str)){
                Log.i("ParseResult ", "Settings");
                Intent intent = new Intent(".settings");
                if(currentActivity.equals("MainActivity"))
                    mainScreen.setting_action(null);
                else if(currentActivity.equals("article"))
                        articleScreen.setting_action(null);
                return;
            }
        }
        if(currentActivity.equals("MainActivity")) {
            for (String str : categoryRequest) {
                if (hyp.contains(str)) {
                    hyp = hyp.replaceAll(str, "");
                    Spinner spinner = mainScreen.findViewById(R.id.spinner);
                    if (hyp.contains(categories[0]) || hyp.contains(categories[1])) {
                        Log.i("ParseResult ", "SPORT");
                        spinner.setSelection(0);
                        return;
                    }
                    if (hyp.contains(categories[2]) || hyp.contains(categories[3]) || hyp.contains(categories[4])) {
                        Log.i("ParseResult ", "IT");
                        spinner.setSelection(1);
                        return;
                    }
                    if (hyp.contains(categories[5]) || hyp.contains(categories[6])) {
                        Log.i("ParseResult ", "Business");
                        spinner.setSelection(2);
                        return;
                    }
                    if (hyp.contains(categories[7])) {
                        Log.i("ParseResult ", "POLITICS");
                        spinner.setSelection(3);
                        return;
                    }
                }
            }
            for (String str : readHeaders) {//TODO
                if (hyp.contains(str)) {
                    Log.i("ParseResult ", "read headers");
                    return;
                }
            }
//        if(hyp.matches(openText[0])){
//            hyp = hyp.replaceAll(openText[0].split(" ")[0]," ");
//            hyp = hyp.replaceAll(openText[0].split(" ")[1]," ");
//            Log.i("Parseresult ", "open :"+hyp);
//        }
            for (String str : openText) {//TODO
                if (hyp.contains(str)) {
                    //TODO Text selection
                    hyp = hyp.replaceAll(str, "");
                    Log.i("ParseResult ", "open :" + hyp);
                    return;
                }
            }
        }
        if(currentActivity.equals("article")) {
            for (String str : readText) {//TODO
                if (hyp.contains(str)) {
                    Log.i("ParseResult ", "read text");
                    return;
                }
            }
            for(String str: openSource){//TODO
                if(hyp.contains(str)){
                    Log.i("ParseResult ", "open source");
                    return;
                }
            }
        }
        for(String str: stopReading){//TODO
            if(hyp.contains(str)){
                Log.i("ParseResult ", "stop reading");
                return;
            }
        }
        for(String str: continueReading){//TODO
            if(hyp.contains(str)){
                Log.i("ParseResult ", "continue reading");
                return;
            }
        }
        for(String str: restartReading){//TODO
            if(hyp.contains(str)){
                Log.i("ParseResult ", "restart reading");
                return;
            }
        }

        for(String str: goBack){
            if(hyp.contains(str)){
                Log.i("ParseResult ", "go back");
                if(currentActivity.equals("MainActivity"))
                    mainScreen.onBackPressed();
                else if(currentActivity.equals("article"))
                        articleScreen.onBackPressed();
                else settingsScreen.onBackPressed();
                return;
            }
        }
        for(String str: exit){
            if(hyp.contains(str)){
                Log.i("ParseResult ", "call exit");
                System.exit(0);
            }
        }
    }
}
