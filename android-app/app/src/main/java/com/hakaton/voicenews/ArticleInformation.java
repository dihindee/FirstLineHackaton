package com.hakaton.voicenews;

public class ArticleInformation {
    private String text;
    private String title;
    private String url;
    private String urlTitleAudio;
    private String urlAudio;

    public ArticleInformation() {

    }

    public ArticleInformation(String urlTitleAudio, String urlAudio, String text, String title, String url) {
        this.text = text;
        this.title = title;
        this.url = url;
        this.urlTitleAudio = urlTitleAudio;
        this.urlAudio = urlAudio;

    }

    public void setArticleInformation(String urlTitleAudio, String urlAudio, String text, String title, String url) {
        this.text = text;
        this.title = title;
        this.url = url;
        this.urlTitleAudio = urlTitleAudio;
        this.urlAudio = urlAudio;
    }

    public String getText() {
        return text;
    }

    public String getUrlTitleAudio() {return urlTitleAudio; }

    public void setUrlTitleAudio(String urlTitleAudio) { this.urlTitleAudio = urlTitleAudio; }

    public String getUrlAudio() {return urlAudio; }

    public void setUrlAudio(String urlAudio) { this.urlAudio = urlAudio; }

    public void setText(String text) {
        this.text = text;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String text) {
        this.title = title;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String text) {
        this.url = url;
    }

    @Override
    public String toString() {
        return title + ", " + text + ", " + url;
    }
}
