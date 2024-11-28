# SEL337 - Prática 5
## Serviços de inicialização e uso do git para controle de versão

Alunos:
Allan Victor Santos - 12625458
Matheus Augusto Tavares de Freitas - 10696764

Neste procedimento prático foi criada uma tarefa que realiza o controle de um LED
fazendo-o piscar com um período de 0.4s usando linguagem bash. Foi criado um arquivo
.service  que configura esse serviço para poder ser inicializado juntamente com a
inicialização do sistema operacional. O arquivo de configuração foi copiado para a pasta
apropriada no systemd e foi habilitado pelo systemctl, funcionando perfeitamente na
inicialização do SO.
Outro serviço foi adicionado, realizando os mesmos passos anteriores. No entanto essa tarefa
é executada por meio de um script python, que teve seu interpretador inicializado no início do
script. O serviço também fazia um led piscar mas dessa vez com um período de 1s.
A montagem em protoboard com os dois leds, um para cada tarefa, pode ser vista na imagem a seguir.
![montagem](https://github.com/user-attachments/assets/80696cf8-288d-4e55-9417-ce7a68fa827a)
