 using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Agente : MonoBehaviour
{
    public TextMeshProUGUI texto;
    private Nodo nodo;
    private Memoria memoria;
    public int contador = 0;
    public int contadorDeJuegos = 0;
    private bool llego;
    public float valor;
    public float[] pesosGanadores;

    // Start is called before the first frame update
    void Start()
    {
        nodo = new Nodo();
        pesosGanadores = new float[8];
        llego = false;    
        texto = FindObjectOfType<TextMeshProUGUI>();
        valor = 0f;
    }

    // Update is called once per frame
    void Update()
    {   

        Agente_RandomAcotacion();
    }

    
   /*
    void AgenteRandomFinal(){
        Debug.Log("*******************");

                nodo.adaptarPesos2(valor);//Pesos Random
                //nodo.VerPesos();//Vemos pesos
                for(int x = 0; x < 20; x++)
                {
                     //Avanzamos 20 con mismos Pesos
                     nodo.LLenarEntrada((int)transform.position.x,(int)transform.position.z);//LLenamos Entradas
                     nodo.Evaluacion();//Sumatoria
                     //nodo.VerEntradas();
                     Vector3 movimiento = nodo.Salida();
                     if(GridManager.Grid[(int)transform.position.x + (int)movimiento.x,(int)transform.position.z + (int)movimiento.z] != 0)
                     {
                            transform.position += movimiento;//Movimeinto sin Obstaculo
                            nodo2.LlenarEntradas((int)transform.position.x,(int)transform.position.z);
                            Vector3 comprobacion = nodo2.Comprobar();
                            if(comprobacion != new Vector3(0,0,0))
                            {
                                //Si estas en un a linea amarrilla
                                while(GridManager.Grid[(int)transform.position.x + (int)comprobacion.x,(int)transform.position.z + (int)comprobacion.z] != 0){
                                    //Seguir avanzando hasta tocar obstaculo
                                    transform.position += comprobacion;
                                    if(GridManager.Grid[(int)transform.position.x,(int)transform.position.z] == 2)
                                    {
                                        Debug.Log("Llegaste a la meta");
                                        break;
                                    }
                                }
                            }
                     }  
                }
                texto.text = $"Contador: {contador} ";
                Debug.Log($"Iteracion {contador}");
                contador++;
                transform.position = new Vector3(3,0,5);

        Debug.Log("*******************");
    }
   */
    void Agente_RandomAcotacion(){
        if(llego == false)
        {
                Debug.Log("**********************");
            nodo.LLenarEntrada((int)transform.position.x,(int)transform.position.z);
            nodo.adaptarPesos2(valor);
            //nodo.VerPesos();
            //nodo.VerEntradas();
            nodo.Evaluacion();
            Vector3 movimiento = nodo.Salida();
            if(GridManager.Grid[(int)transform.position.x + (int)movimiento.x,(int)transform.position.z + (int)movimiento.z] != 0)
                {
                     transform.position += movimiento;
                }
            if(GridManager.Grid[(int)transform.position.x,(int)transform.position.z] == 2){            
                GameObject casilla = GameObject.Find("Meta");
                casilla.GetComponent<Renderer>().material.color = Color.blue;
                transform.position = new Vector3(2,0,6);
                llego = true;   

            }   
            texto.text = $"Contador: {contador}";
            contador++; 
            valor = valor + .1f;
            if(valor >= 1.0f)
            {
                valor = .05f;
                transform.position = new Vector3(2,0,6);
            }

            
            Debug.Log("**********************");
        }
        
    }
  
    void Agente_Arbol(){
    
            if(llego == false)
            {
                nodo.adaptarPesos();
                nodo.VerPesos();
            for(int x = 0; x < 10; x++)
            {
                nodo.LLenarEntrada((int)transform.position.x,(int)transform.position.z);
                nodo.Evaluacion();
                nodo.VerEntradas();
                Vector3 movimiento = nodo.Salida();
                if(GridManager.Grid[(int)transform.position.x + (int)movimiento.x,(int)transform.position.z + (int)movimiento.z] != 0)
                {
                     transform.position += movimiento;
                }       
                if(GridManager.Grid[(int)transform.position.x,(int)transform.position.z] == 2){
                    Debug.Log($"LLegue a la meta en {contador}");
                    GameObject casilla = GameObject.Find("Meta");
                    casilla.GetComponent<Renderer>().material.color = Color.blue;
                    transform.position = new Vector3(2,0,6);
                    for(int y = 0; y < 10; y++)
                    {
                         nodo.LLenarEntrada((int)transform.position.x,(int)transform.position.z);
                         nodo.Evaluacion();
                         Vector3 mov = nodo.Salida();
                         if(GridManager.Grid[(int)transform.position.x + (int)movimiento.x,(int)transform.position.z + (int)movimiento.z] != 0)
                         {
                            
                            transform.position += mov;
                            GameObject cas = GameObject.Find($"{transform.position.x},{transform.position.z}");
                            cas.GetComponent<Renderer>().material.color = Color.blue;
                         }
                    }
                    llego = true;
                    break;
                    }
            }
            texto.text = $"Contador: {contador} ";
            Debug.Log($"Iteracion {contador}");
            contador++;
            transform.position = new Vector3(2,0,6);
            }
    }
    
   
}
