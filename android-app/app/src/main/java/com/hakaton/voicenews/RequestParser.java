package com.hakaton.voicenews;

import android.content.Intent;
import android.media.MediaPlayer;
import android.util.Log;
import android.widget.Spinner;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;

public class RequestParser {
    static final String[] settings = {"настройки", "открой настройки", "настройка", "settings", "сеттинги"};
    static final String[] categoryRequest = {"покажи новости про", "открой категорию", "категория"};
    static final String[] categories = {"спорт", "sport", "it", "это", "айти", "business", "бизнес", "политик"};
    static final String[] readHeaders = {"прочитай заголовки", "прочти заголовки", "читай заголовки"};
    static final String[] openText = {"открой про", "новость про", "новости про", "открой новость про", "открой новости", "открой"};
    static final String[] openTextByIndex = {"открой", "новость", "открой", "новости"};
    static final String[] readText = {"прочитай новость", "прочитай", "читай", "прочитай новости", "почитай новости", "почитай новость"};
    static final String[] stopReading = {"стой", "подожди", "постой", "погоди", "стоп", "останови"};
    static final String[] continueReading = {"продолжай", "давай дальше", "читай дальше"};
    static final String[] restartReading = {"начни с начала", "давай с начала", "начни заново", "давай заново"};
    static final String[] openSource = {"открой источник", "источник новости", "откуда новость"};
    static final String[] goBack = {"назад", "давай назад", "вернись назад"};
    static final String[] exit = {"выход", "выключи", "вырубай", "выключись", "заткнись", "выключайся"};
    static String currentActivity;
    static MainActivity mainScreen;
    static article articleScreen;
    static settings settingsScreen;
    static MediaPlayer player;

    static void setCurrentActivity(String activity) {
        currentActivity = activity;
    }

    static void doAction(ArrayList<String> hyps) {
        String hyp = hyps.get(0).toLowerCase();
        for (String str : settings) {
            if (hyp.contains(str)) {
                Log.i("ParseResult ", "Settings");
                Intent intent = new Intent(".settings");
                if (currentActivity.equals("MainActivity"))
                    mainScreen.setting_action(null);
                else if (currentActivity.equals("article"))
                    articleScreen.setting_action(null);
                return;
            }
        }
        if (currentActivity.equals("MainActivity")) {
            for (String str : categoryRequest) {
                if (hyp.contains(str)) {
                    hyp = hyp.replaceAll(str, "");
                    Spinner spinner = mainScreen.spinner;
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
//                    mainScreen.spinner.setSelection();
                }
            }
            for (String str : readHeaders) {
                if (hyp.contains(str)) {
                    Log.i("ParseResult ", "read headers");
                    return;
                }
            }for (String str : openText) {
                if (hyp.contains(str)) {
                    hyp = hyp.replaceAll(str, "");
                    String[] req_items = hyp.split(" ");
                    for (int i = 0; i < req_items.length; i++) {
                        if (req_items[i].isEmpty())
                            req_items[i] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa";
                    }
//                    Log.i("ParseResult","req items: "+Arrays.toString(req_items));
                    String[][] header_items = new String[mainScreen.news.size()][];
                    int[] match_count = new int[header_items.length];
//                    Log.i("ParseResult",Arrays.toString(mainScreen.news.toArray()));
                    for (int i = 0; i < mainScreen.news.size(); i++) {
                        header_items[i] = Objects.requireNonNull(mainScreen.news.get(i)).toLowerCase().split(" ");
                        for (int j = 0; j < header_items[i].length; j++) {
                            if (header_items[i][j].length() < 3)
                                header_items[i][j] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa";
                        }
//                        Log.i("ParseResult","Header items: "+Arrays.toString(header_items[i]));
                        for (String req : req_items) {
                            for (String header : header_items[i]) {
                                if (header.contains(req.substring(0, Math.max(0, req.length() - 2))))
                                    match_count[i]++;
                            }
                        }
                    }
                    int max = 0, maxIndex = 0;
                    for (int i = 0; i < match_count.length; i++) {
                        if (match_count[i] > max) {
                            max = match_count[i];
                            maxIndex = i;
                        }
                    }
                    Log.i("ParseResult", "matches: " + Arrays.toString(match_count));
                    Log.i("ParseResult ", "open :" + hyp);
                    Log.i("ParseResult ", "best match: " + mainScreen.news.get(maxIndex));
                    mainScreen.perform_action(mainScreen.newsList.getChildAt(maxIndex));
                    return;
                }
            }
            for (int i = 0; i < 4; i += 2) {
                if (hyp.contains(openTextByIndex[i]) && hyp.contains(openTextByIndex[i + 1])) {
                    hyp = hyp.replaceAll(openTextByIndex[i], "");
                    hyp = hyp.replaceAll(openTextByIndex[i + 1], "");
//                    Log.i("Parseresult ", "open :"+hyp);
                    final String[] numeric = {"перв", "втор", "треть", "четверт", "пят", "шес", "се", "вос", "девят", "десят", "одиннадцат", "двенадцат"};
                    final String[] numericDigital = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"};
                    for (int j = 0; j < numeric.length; j++) {
                        if (hyp.contains(numeric[j]) || hyp.contains(numericDigital[j])) {
//                            Log.i("ParseResult ", "best match: " + mainScreen.news.get(j));
                            mainScreen.perform_action(mainScreen.newsList.getChildAt(j));
                            return;
                        }
                    }
                }
            }
        }

//        if (currentActivity.equals("article")) {
        for (String str : readText) {
            //TODO
            if (hyp.contains(str)) {
                Log.i("ParseResult ", "read text");
                if (!player.isPlaying())
                    player.start();
                return;
            }

        }
//        }
        for (String str : openSource) {//TODO
            if (hyp.contains(str)) {
                Log.i("ParseResult ", "open source");
                return;
            }
        }
        for (String str : stopReading) {//TODO
            if (hyp.contains(str)) {
                if (player != null && player.isPlaying())
                    player.pause();
                Log.i("ParseResult ", "stop reading");
                return;
            }
        }

        for (String str : continueReading) {//TODO
            if (hyp.contains(str)) {
                if (player != null && !player.isPlaying())
                    player.start();
                Log.i("ParseResult ", "continue reading");
                return;
            }
        }
        for (String str : restartReading) {//TODO
            if (hyp.contains(str)) {
                if (player != null) {
                    player.seekTo(0);
                    player.start();
                }
                Log.i("ParseResult ", "restart reading");
                return;
            }
        }

        for (String str : goBack) {
            if (hyp.contains(str)) {
                Log.i("ParseResult ", "go back");
                if (currentActivity.equals("MainActivity"))
                    mainScreen.onBackPressed();
                else if (currentActivity.equals("article"))
                    articleScreen.onBackPressed();
                else settingsScreen.onBackPressed();
                return;
            }
        }
        for (String str : exit) {
            if (hyp.contains(str)) {
                Log.i("ParseResult ", "call exit");
                System.exit(0);
            }
        }
    }
}
