# Hackathon Banco Citi 💸

Esse projeto foi desenvolvido durante o hackathon promovido pelo Banco Citi.

A proposta do hackathon era desenvolver uma solução que ajudasse no procesamento de remessas de empresas que solicitam
a geração de QR Code para cobrança, no formato CNAB 750.

O `arquivo_remessa.cnab` foi o arquivo que utilizamos para testar a funcionalidade da aplicação e `teste.py` é o código desenvolvido para nossa aplicação. Também estabelecemos
alguns parâmetros para verificar se a linha correspondente a cada registro, no lote, estava dentro das especificações.

Para fazer essa vefificação de parâmetros, extraimos de cada registro (linha)
os campos conforme o padrão CNAB. 

Após isso, todos os campos de cada linha são analisados
para verificar se estão dentro dos parâmetros especificados. 
Caso alguns erro seja encontrado, esse erro é especificado no relatório final,
indicando em qual campo e em qual registro foi encontrado esse erro.



