#!/bin/bash
 
: 'Crear un directorio con un nombre de <yourName>-<currentDate>.

Escribir un script bash en:

Crear veinticinco archivos vacíos (0 KB) (Sugerencia: utilice el comando touch (tocar) ).
Los nombres de archivo deben ser <yourName><number>, <yourName><number+1>, <yourName><number+2> y así sucesivamente.
Diseñe el script de manera que cada vez que lo ejecute, cree el siguiente lote de 25 archivos con números crecientes comenzando por el último número o número máximo que ya existe.
No hard code estos números. Necesita generarlos usando automatización.
Pruebe el script. Muestra una larga lista del directorio y su contenido para validar que el script creó los archivos esperados.

Save the script (Guarde el script) y make a note of its location (absolute path) (anote su ubicación (ruta absoluta)) para referencia futura.
'

nombre="Emanuel"
numfinal=($(ls | grep ^$nombre | grep -oE [0-9]\+))
nummax=0
num=0
 
for ((i=0;i<${#numfinal[@]};i++))
do
        num=${numfinal[i]}
        if ((num > nummax))
        then
                nummax = $num
        fi
done
 
echo "max = $nummax"
 
numsig=$nummax+1
echo $numsig
 
for i in {1..25}
do
        echo "Creando archivo numero $i"
        sigarchivo= "$nombre$numsig"
        echo $sigarchivo
        touch $sigarchivo
        numsig= $numsig + 1
done
echo "DONE!!!"