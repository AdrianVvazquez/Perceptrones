using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Nodo : MonoBehaviour
{
    public float[,] EntredasYPesos = new float[2,8];
    public float sumatoria;

    
    public Nodo()
    {
    }

    public void LLenarEntrada(int Vx,int Vy){
        int contador = 0;
        for (int x = -1; x <= 1; x++)
        {
            for (int y = -1; y <= 1; y++)
            {
                if (x != 0 || y != 0)
                {
                   
                    EntredasYPesos[0,contador] = GridManager.Grid[Vx + x,Vy + y] ;
                    contador++;               
                }
            }
        }
    }

    public void VerEntradas(){
        for(int x = 0; x < 8; x++)
        {
            Debug.Log(EntredasYPesos[0,x]);
        }
    }

    public void adaptarPesos3(float valor){
        EntredasYPesos[1,0] = valor;
        EntredasYPesos[1,1] = valor;
        EntredasYPesos[1,2] = valor;
        EntredasYPesos[1,3] = valor;
        EntredasYPesos[1,4] = valor;
        EntredasYPesos[1,5] = valor;
        EntredasYPesos[1,6] = valor;
        EntredasYPesos[1,7] = valor;
    }

    public void adaptarPesos(){
        for(int x = 0; x < 8; x++)
        {
            if(EntredasYPesos[1,x] >= 0.9)
            {
                EntredasYPesos[1,x] = 0.0f;
                
            }else{
                EntredasYPesos[1,x] = EntredasYPesos[1,x] + 0.1f;
                break;
            }
        }
    }

    public void adaptarPesos2(float valor){
            
            for(int x = 0; x < 8; x++)
            {
                float number = Random.Range(0.0f, 1.0f);
                double b;
                b = System.Math.Round(number,2);
                
                EntredasYPesos[1,x] = (float)b;
            }   
            

    }




    public void VerPesos(){
        for(int x = 0; x < 8; x++)
        {
            Debug.Log(EntredasYPesos[1,x]);
        }
    }

    public void  Evaluacion(){
        float calculo = 0;
        for(int x = 0; x < 8; x++ )
        {
            calculo = calculo + (EntredasYPesos[0,x] * EntredasYPesos[1,x]); 
        }
        sumatoria = calculo / 8;

    }

    public Vector3 Salida() {
        Vector3 salida = new Vector3(0,0,0);
        if (sumatoria > 0 && sumatoria <= 0.1f) {

            salida = new Vector3(-1,0,1);
        }
        if (sumatoria > 0.1f && sumatoria <= 0.2f)
        {
            salida = new Vector3(0,0,1);
        }
        if (sumatoria > 0.2f && sumatoria <= 0.3f)
        {
            salida = new Vector3(1,0,1);
        }
        if (sumatoria > 0.3f && sumatoria <= 0.4f)
        {
            salida = new Vector3(1,0,0);
        }
        if (sumatoria > 0.4f && sumatoria <= 0.5f)
        {
            salida = new Vector3(1,0,-1);
        }
        if (sumatoria > 0.5f && sumatoria <= 0.6f)
        {
            salida = new Vector3(0,0,-1);
        }
        if (sumatoria > 0.6f && sumatoria <= 0.7f)
        {
            salida = new Vector3(-1,0,-1);
        }
        if (sumatoria > 0.7f && sumatoria <= 0.8f)
        {
            salida = new Vector3(-1,0,0);
        }
        return salida;
    }

}
