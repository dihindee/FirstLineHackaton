package com.hakaton.voicenews;

public class Information {

    private String url;
    private ArticleInformation[] articleInformation;

    public Information(String url, ArticleInformation[] articleInformation) {
        this.url = url;
        this.articleInformation = articleInformation;
    }

    public Information() {
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        sb.append("\n url:" + this.url);
        if (this.articleInformation != null) {
            sb.append("\n articleInformation:" + this.articleInformation.toString());
        }
        return sb.toString();
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public ArticleInformation[] getArticleInformation() {
        return articleInformation;
    }

    public void setArticleInformation(ArticleInformation[] articleInformation) {
        this.articleInformation = articleInformation;
    }
}
