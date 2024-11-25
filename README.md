# SEL0337_1528

<h1> 
Prática 5: SystemD e personalização de serviços de inicialização em Linux embarcado
</h1> 
<body>
<p> O projeto escolhido para ser implementado foi o LED PWM, realizado durante a prática 3, que possui a montagem utilizando um led e um resistor, idêntica a montagem realizada na prática 3, conforme a imagem abaixo.
  https://github.com/MatiasCaccalano/SEL0337_1528/blob/main/Montagem_PWM.jpg </p>
<p> O LEDPWM.py simplismente alterna entre 3 valores de PWM de forma a alterar o brilho do LED, o projeto LEDPWM_stop.py mantém o led desligado. O arquivo PWM_py.service é responsável por permitir que o projeto seja inicializado durante
  o boot da Raspberry Pi, já que ele inicializa o python e também o projeto LEDPWM.py, ativando o projeto LEDPWM_stop.py quando o service é encerrado. </p>
<p> Todos os projetos foram adicionados a branch master, incluindo o arquivo com o histórico do comando do git. Devido a problemas ao tentar realizar o push durante a aula a adição dos arquivos ao GitHub foi realizada posteriormente com 
  uma máquina virtual Ubuntu no desktop pessoal. </p>
</body>
