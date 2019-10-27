import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import java.io.IOException;

public class MyAppServletContextListener implements ServletContextListener{
    @Override
    public void contextDestroyed(ServletContextEvent arg0) {
        System.out.println("SERVER DISCONECT");
    }
    //Run this before web application is started
    @Override
    public void contextInitialized(ServletContextEvent arg0) {
         while (true) {
            System.out.println("UPDATE");
            //ListNews.UpdateResourse();
            try {
                Thread.sleep(30000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}