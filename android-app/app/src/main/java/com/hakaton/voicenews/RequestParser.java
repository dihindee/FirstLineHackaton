package com.hakaton.voicenews;

import android.util.Log;

import java.util.ArrayList;

public class RequestParser{
    static final String[] settings ={"настройки","открой настройки", "настройка", "settings", "сеттинги"};
    static final String[] categoryRequest ={"покажи новости про","новости о","новости про","открой категорию","категория"};
    static final String[] categories = {"спорт","sport","it","это","айти","business","бизнес","политика"};
    static final String[] readHeaders = {"прочитай заголовки", "прочти заголовки", "читай заголовки"};
    static final String[] openText = {"открой про","новость про", "открой новость про","открой новости", "открой"};
    static final String[] readText = {"прочитай новость", "прочитай", "читай", "прочитай новости", "почитай новости", "почитай новость"};
    static final String[] stopReading = {"стой","подожди","постой","погоди","стоп","останови"};
    static final String[] continueReading = {"продолжай","давай дальше","читай дальше"};
    static final String[] restartReading = {"начни с начала","давай с начала","начни заново","давай заново"};
    static final String[] openSource = {"открой источник","источник новости","откуда новость"};
    static final String[] goBack = {"назад","давай назад","вернись назад"};
    static final String[] exit = {"выход","выключи","вырубай","гаси","заткнись","заткнися"};

    static void doAction(ArrayList<String> hyps){
        String hyp = hyps.get(0).toLowerCase();
        for(String str : settings) {
            if(hyp.contains(str)){
                Log.i("ParseResult ", "Settings");
                return;
            }
        }
        for(String str : categoryRequest){
            if(hyp.contains(str)){
                hyp = hyp.replaceAll(str,"");
                if(hyp.contains(categories[0])||hyp.contains(categories[1])){
                    Log.i("ParseResult ", "SPORT");
                    return;
                }
                if(hyp.contains(categories[2])||hyp.contains(categories[3])||hyp.contains(categories[4])){
                    Log.i("ParseResult ", "IT");
                    return;
                }
                if(hyp.contains(categories[5])||hyp.contains(categories[6])){
                    Log.i("ParseResult ", "Business");
                    return;
                }
                if(hyp.contains(categories[7])){
                    Log.i("ParseResult ", "POLITICS");
                    return;
                }
            }
        }
        for(String str: readHeaders){
            if(hyp.contains(str)){
                Log.i("ParseResult ", "read headers");
                return;
            }
        }
//        if(hyp.matches(openText[0])){
//            hyp = hyp.replaceAll(openText[0].split(" ")[0]," ");
//            hyp = hyp.replaceAll(openText[0].split(" ")[1]," ");
//            Log.i("Parseresult ", "open :"+hyp);
//        }
        for(String str: openText){
            if(hyp.contains(str)){
                //TODO Text selection
                hyp = hyp.replaceAll(str,"");
                Log.i("ParseResult ", "open :"+hyp);
                return;
            }
        }
        for(String str: readText){
            if(hyp.contains(str)){
                Log.i("ParseResult ", "read text");
                return;
            }
        }
        for(String str: stopReading){
            if(hyp.contains(str)){
                Log.i("ParseResult ", "stop reading");
                return;
            }
        }
        for(String str: continueReading){
            if(hyp.contains(str)){
                Log.i("ParseResult ", "continue reading");
                return;
            }
        }
        for(String str: restartReading){
            if(hyp.contains(str)){
                Log.i("ParseResult ", "restart reading");
                return;
            }
        }
        for(String str: openSource){
            if(hyp.contains(str)){
                Log.i("ParseResult ", "open source");
                return;
            }
        }
        for(String str: goBack){
            if(hyp.contains(str)){
                Log.i("ParseResult ", "go back");
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
