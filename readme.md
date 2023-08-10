# Aula 01 - Warm-up

## Atividade de Teatro

Alunos, bem vindos à mais um semestre letivo. 

Preciso que criem essa atividade em Python, para que possamos iniciar nossos trabalhos.

Boa diversão.



Crie um algoritmo que desenvolva o controle de uma sessão de teatro, contendo os seguintes quesitos:

O teatro deverá ter, no máximo, 300 linhas por 300 colunas (completando um total de 90.000 cadeiras).

O usuário, ao iniciar o sistema deverá escolher o tamanho da sala (informando linha e coluna, respectivamente e o valor de ingresso total.)

Deverá ser desenhado um menu, com as seguintes opções:


	
* [1] - Iniciar o teatro: essa opção o usuário informa quantas linhas e colunas serão ocupadas, não podendo superar o total de linhas e colunas determinadas para o tamanho do teatro e, também não poderá ser feito se outro espetáculo estiver aberto.
	
* [2] - Reservar lugar, informando linha e coluna. Se este lugar estiver livre, poderá ser reservado e colocado uma informação que está reservado (para que futuramente não possa ser reservado novamente). Para reserva, deverá pagar 30% do valor total. Se estiver reservado, informar ao usuário e pedir novo conjunto de linha e coluna.
	
* [3] - Comprar lugar. Verificar se lugar está livre, se tiver, cobrar valor cheio, se estiver reservado, cobrar valor de 70% do valor cheio, já que para reservar, precisou pagar 30%.
	
* [4] - Liberar lugar. Caso lugar esteja reservado ou comprado, trocar status para Livre e subtrair do sistema o valor pago anteriormente (se reservado, subtrair 30% do valor cheio, se estiver vendido, subtrair 100% do valor cheio).
	
* [5] - Listar poltronas (assim o usuário poderá saber, quantos e quais locais estão livres, quais e quantos reservados e quais e quantos vendidos).
	
* [6] - Encerrar o espetáculo (essa opção só poderá ser utilizada se tivermos 60% + 1, da ocupação total do teatro - posições vendidas. Neste momento, reservas não contam). Quando o espetáculo for encerrado, deverá ser exibido o total de cadeiras vendidas (e o valor das vendas), o total de reserva (e o valor das reservas), o total de cadeiras livres (e o valor que não foi recebido). Deverá também exibir ao final, a totalização do espetáculo.


	Total Geral de Cadeiras: XXX
	Total de Cadeiras Vazias: XXX
	Total de Cadeiras Reservadas: XXX
	Total de Cadeiras Vendidas: XXX
	Total do Espetáculo em R$: 000.00
	Total não recebido em R$: 000.00
	Total em reservas R$: 000.00
	Total em Reservas Liberadas R$: 000.00

* [7] - Reiniciar o espetáculo (todas as variáveis deverão ser reiniciadas e as cadeiras do espetáculo, liberadas).
