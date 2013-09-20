/**
 * 
 */
package uk.bl.dpt.bbc;

import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.RandomAccessFile;

/**
 * 
 * Using BACKUP, form here http://mdfs.net/Apps/DiskTools/
 * 
 * We find retrieved images that do not make emulators happy. So, looking here
 * 
 *  - http://www.8bs.com/filecon.htm#dit
 *  - http://mdfs.net/Docs/Books/HADFSMan/Chap5.htm
 *  
 * Implies that raw images from BACKUP are not interlaced, but DSD files are expected to be.
 * 
 * Therefore, we re-interlace them, like this...
 * 
 * @author AnJackson
 *
 */
public class DiskImageInterlacer {

    /**
     * @param args
     * @throws IOException 
     */
    public static void main(String[] args) throws IOException {
        interlaceImage("input/DISK01_DSD", "output/DISK01.DSD" );
        interlaceImage("input/DISK02_DSD", "output/DISK02.DSD" );
        interlaceImage("input/DISK03_DSD", "output/DISK03.DSD" );
        interlaceImage("input/DISK04_DSD", "output/DISK04.DSD" );
        interlaceImage("input/DISK05_DSD", "output/DISK05.DSD" );
//        interlaceImage("input/DISK06_DSD", "output/DISK06.DSD" );
        interlaceImage("input/DISK07_DSD", "output/DISK07.DSD" );
        interlaceImage("input/DISK08_DSD", "output/DISK08.DSD" );
        interlaceImage("input/DISK09_DSD", "output/DISK09.DSD" );
        interlaceImage("input/DISK10_DSD", "output/DISK10.DSD" );
        interlaceImage("input/DISK11_DSD", "output/DISK11.DSD" );
        interlaceImage("input/DISK12_DSD", "output/DISK12.DSD" );
        interlaceImage("input/DISK13_DSD", "output/DISK13.DSD" );
        interlaceImage("input/DISK14_DSD", "output/DISK14.DSD" );
        interlaceImage("input/DISK15_DSD", "output/DISK15.DSD" );
        interlaceImage("input/ELITE_DSD", "output/ELITE.DSD" );
    }
    
    /**
     * @param inputImage
     * @param outputImage
     * @throws IOException
     */
    public static void interlaceImage( String inputImage, String outputImage ) throws IOException {
        System.out.println("Converting "+inputImage+" to "+outputImage);
        RandomAccessFile in = new RandomAccessFile( inputImage, "r");
        int sectorSize = 256*10;
        int sideSize = sectorSize*80;
        int diskSize = sideSize*2;
        if( (int)in.length() != diskSize ) {
            System.out.println("Wrong size.");
            return;
        }
        byte[] tempId = new byte[diskSize];
        in.read(tempId, 0, diskSize);
        in.close();

        DataOutputStream out = new DataOutputStream(new FileOutputStream( outputImage ));
        for( int t = 0; t < 80; t++ ) {
            for( int s = 0; s < 2; s++ ) {
                out.write(tempId, s*sideSize + sectorSize*t, sectorSize);
            }
        }
        out.close();
    }

}
