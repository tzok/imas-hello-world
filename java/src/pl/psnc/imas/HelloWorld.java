package pl.psnc.imas;

import imasjava.imas;
import imasjava.imas.summary;
import imasjava.UALException;
import imasjava.Vect1DDouble;

public class HelloWorld {
    public static void main(String[] args) throws UALException {
        int pulseCtx = imas.createEnv(1, 1, "imas", "test", "3");

        summary s = new summary();
        s.ids_properties.comment = "Hello World from Java";
        s.ids_properties.homogeneous_time = 1;
        s.time = new Vect1DDouble(new double[] { 0.1 });

        imas.summary.put(pulseCtx, "summary", s);
    }
}
