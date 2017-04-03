package morse;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Morse extends JApplet implements ActionListener
{
	private static final long serialVersionUID = 1L;

	char[] normal=new char[]{'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',' '};
	
	String[] morse=new String[]{"._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._",
			"._..","__","_.","__.__","___",".__.","__._","._.","...","_",".._","..._",".__","_.._",
			"_.__","__.."," "};
	
	
	JTextField txtNorm = new JTextField(53);
	JLabel lblNorm = new JLabel("Normal");
	JTextField txtMorse = new JTextField(53);
	JLabel lblMorse = new JLabel("Morse ");
	JButton btnConvMorse;
	JButton btnConvNorm;
	Container contenedor = new Container();
	Font font = new Font(Font.MONOSPACED, Font.ITALIC + Font.BOLD, 20 );
	
	
	public void init()
	{
		this.setSize(700, 125);
		
		iniciarComponentes();
		
		this.setFont(font);
		
	}
	public void iniciarComponentes()
	{
		contenedor = this.getContentPane();
		contenedor.setLayout(new FlowLayout());
		contenedor.add(lblNorm);
		
		txtNorm.setFont(font);
		contenedor.add(txtNorm);
		
		contenedor.add(lblMorse);
		
		txtMorse.setFont(font);
		contenedor.add(txtMorse);
		
		btnConvNorm=new JButton("Normal a Morse");
		btnConvNorm.addActionListener( this);
		contenedor.add(btnConvNorm);
		
		btnConvMorse=new JButton("Morse a Normal");
		btnConvMorse.addActionListener(this);
		contenedor.add(btnConvMorse);
	}
	public void actionPerformed(ActionEvent e)
	{
		JButton btn = (JButton)e.getSource();
		if (btn.getText()=="Normal a Morse")
		{
			String cadena=txtNorm.getText().toUpperCase();
			txtMorse.setText(convertirMorse(cadena));
		}
		else if (btn.getText()=="Morse a Normal")
		{
			String cadena=txtMorse.getText();
			txtNorm.setText(convertirNormal(cadena));
		}
	}
	public String convertirMorse(String cadenaNormal)
	{
		char[] arregloNormal=cadenaNormal.toCharArray();
		String salida="";
		
		for (int cont=0;cont<arregloNormal.length;cont++)
		{
			for (int cont2=0;cont2<normal.length;cont2++)
			{
				if(arregloNormal[cont]==normal[cont2])
					{
						salida += morse[cont2] + " ";
					}
			}
		}
		
		
		return salida;
	}
	public String convertirNormal(String cadenaMorse)
	{
		cadenaMorse=cadenaMorse.replace("   ", " * ");
		String[] arregloMorse = cadenaMorse.split(" ");
		String salida="";
		for (int cont=0;cont<arregloMorse.length;cont++)
		{
			for (int cont2=0;cont2<morse.length;cont2++)
			{
				if(arregloMorse[cont].equalsIgnoreCase(morse[cont2]))
				{
						salida += normal[cont2];
						break;
				}
				else if(arregloMorse[cont].equalsIgnoreCase("*"))
				{
					salida+=" ";
					break;
				}
						
			}
		}
		return salida;
	}
	

}
