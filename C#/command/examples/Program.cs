using System;

namespace examples
{
    class Program
    {
        static void Main(string[] args)
        {
            
            float[][] jaggedArray= new float[8][];
            float[] arrayAux = new float[50];
            for (int i = 0; i < jaggedArray.Length; i++)
            {
                ;
                int cont = 0;
                bool bandera = false;
                do
                {
                    Console.WriteLine("---Inserte los valores del jaggedArray fila numero {0}---", i);
                    string valor = Console.ReadLine();
                    if (float.TryParse(valor, out float valorF))
                    {
                        arrayAux[cont] = valorF;
                        Console.WriteLine("¡¡¡Valor insertado en la fila {0} columna {1} !!!", i, cont);
                        int opc;
                        do
                        {
                            Console.WriteLine("¡¡¡Desea insertar un valor más? SI(1) / NO(0) !!!");
                            _ = Console.ReadLine();
                            if (int.TryParse(valor, out opc))
                            {
                                if (opc == 1)
                                {
                                    Console.WriteLine("---------");
                                }
                                else if (opc == 0)
                                {
                                    bandera = true;
                                    arrayAux = new float[50];
                                }
                                else
                                {
                                    Console.WriteLine("Input invalido");
                                }
                            }
                            else
                            {
                                Console.WriteLine("Input invalido");
                            }
                        } while (opc != 0);
                    }
                    else
                    {
                        Console.WriteLine("Input invalido");
                    }

                } while (bandera != true);
            }

            Console.WriteLine(jaggedArray);

        }
    }
}
