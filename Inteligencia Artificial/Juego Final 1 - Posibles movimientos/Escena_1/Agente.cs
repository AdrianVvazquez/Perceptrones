 using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Agente : MonoBehaviour
{
    public TextMeshProUGUI texto;
    private Nodo nodo;
    public int contador = 0;
    public int contadorDeJuegos = 0;
    private bool llego;
    public float valor;

    // Start is called before the first frame update
    void Start()
    {
        nodo = new Nodo();
        llego = false;    
        texto = FindObjectOfType<TextMeshProUGUI>();
        valor = 0f;
    }

    // Update is called once per frame
    void Update()
    {       
            Agente_Arbol();
    }

    void Agente_RandomAcotacion(){
        Debug.Log("**********************");
            nodo.LLenarEntrada((int)transform.position.x,(int)transform.position.z);
            nodo.adaptarPesos2(valor);
            nodo.VerPesos();
            nodo.VerEntradas();
            nodo.Evaluacion();
            Vector3 movimiento = nodo.Salida();
            if(GridManager.Grid[(int)transform.position.x + (int)movimiento.x,(int)transform.position.z + (int)movimiento.z] != 0)
                {
                     transform.position += movimiento;
                }
            if(GridManager.Grid[(int)transform.position.x,(int)transform.position.z] == 2){
                contadorDeJuegos++;
                valor = valor + .1f;
                transform.position = new Vector3(2,0,2);

            }
            float rangoRandom = 1.0f - valor;   
            texto.text = $"Contador: {contador} cuantas veces a llegado a la meta {contadorDeJuegos} random rango 0-{rangoRandom} ";
            contador++;  
            Debug.Log("**********************");
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
                    transform.position = new Vector3(2,0,2);
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
                         }else{

                         }
                    }
                    llego = true;
                    break;
                    }
            }
            texto.text = $"Contador: {contador} ";
            Debug.Log($"Iteracion {contador}");
            contador++;
            transform.position = new Vector3(2,0,2);
            }
    }

}
