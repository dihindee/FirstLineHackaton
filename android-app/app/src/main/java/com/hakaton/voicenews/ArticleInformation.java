package com.hakaton.voicenews;

public class ArticleInformation {
    private String text;
    private String title;
    private String url;

    public ArticleInformation() {

    }

    public ArticleInformation(String text, String title, String url) {
        this.text = text;
        this.title = title;
        this.url = url;
    }

    public void setArticleInformation(String text, String title, String url) {
        this.text = text;
        this.title = title;
        this.url = url;
    }

    public String getText() {
        return text;
    }

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
