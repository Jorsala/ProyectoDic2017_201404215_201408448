package spotify;


 import java.io.File;
import java.io.IOException;
import java.util.List;
import org.jdom2.Document;
import org.jdom2.Element;
import org.jdom2.JDOMException;
import org.jdom2.input.SAXBuilder;




/**
 *
 * @author Jorge Salazar
 */
public class LeerXML {
  
    public void recorrerXml(String path) throws IOException{
        SAXBuilder builder = new SAXBuilder();
        File xmlFile = new File(path);

        try {
            
            Document document = (Document) builder.build(xmlFile);
            Element rootNode = document.getRootElement();
            List listUs = rootNode.getChildren("usuarios");
            List listAr = rootNode.getChildren("artistas");

            for (int i = 0; i < listUs.size(); i++) {
                Element node = (Element) listUs.get(i);
                List listUs2 = node.getChildren("usuario");
                
                for (int j = 0; j < listUs2.size(); j++) {
                    Element node2 = (Element) listUs2.get(j);
                    System.out.println("Usuario : " + node2.getChildText("nombre")+","+"Pass : " + node2.getChildText("pass"));
                }
            }
            
            for (int i = 0; i < listAr.size(); i++) {
                Element node = (Element) listAr.get(i);
                List listAr2 = node.getChildren("artista");
                
                for (int j = 0; j < listAr2.size(); j++) {
                    Element node2 = (Element) listAr2.get(j);
                    System.out.println("ARTISTA: " + node2.getChildText("nombre"));
                    
                    List listAl = node2.getChildren("albumes");
                    for (int k = 0; k < listAl.size(); k++) {
                        Element node3 = (Element) listAl.get(k);
                        List listAl2 = node3.getChildren("album");
                        
                        for (int l = 0; l < listAl2.size(); l++) {
                            Element node4 = (Element) listAl2.get(l);
                            System.out.println("ALBUM: " + node4.getChildText("nombre")+","+"GENERO: " + node4.getChildText("genero")+","+"AÑO: " + node4.getChildText("año"));
                            
                            List listCa = node4.getChildren("canciones");
                            for (int m = 0; m < listCa.size(); m++) {
                                Element node5 = (Element) listCa.get(m);
                                List listCa2 = node5.getChildren("cancion");

                                for (int n = 0; n < listCa2.size(); n++) {
                                    Element node6 = (Element) listCa2.get(n);
                                    System.out.println("CANCION: " + node6.getChildText("nombre")+","+"PATH: " + node6.getChildText("path"));
                                }
                            }
                        }
                    }
                }
            }
        } catch (JDOMException jdomex) {
        System.out.println(jdomex.getMessage());
        }
    }
}
