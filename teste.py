nome_arquivo = 'arquivo_remessa.cnab'
MSG_SUCESSO = 'Lote processado com sucesso'
MSG_ERRO = 'Encontramos erro no lote, analise o relatório de erros!'
MSG_ERRO_LINHA = 'Erro na linha {} no {}'

# estabelecendo os parametros
parametro_registro = '0'
parametro_operacao = '0'
parametro_movimento = 'REMESSA'
parametro_id_servico = '01'
parametro_ext_servico = 'COBRANCA       '


# Extraindo o conteúdo
def parse_linha(linha):
    dic = {
        "tipo_de_registro": linha[0:1],
        "tipo_de_operacao": linha[1:2],
        "id_do_movimento": linha[2:9],
        "id_do_servico": linha[9:11],
        "ext_do_tipo_servico": linha[11:26]
    }
    return dic


def analisa_linha_e_atualiza_relatorio(dic_campos, nome_campo, parametro_teste, index_linha):
    if dic_campos[nome_campo] != parametro_teste:
        return index_linha + 1


def main():
    relatorio_final = {
        "tipo_de_registro": [],
        "tipo_de_operacao": [],
        "id_do_movimento": [],
        "id_do_servico": [],
        "ext_do_tipo_servico": []
    }
    total_linhas = 0
    # abrindo o arquivo e lendo
    with open(nome_arquivo, 'r') as arquivo:
        for index_linha, linha in enumerate(arquivo):
            total_linhas += 1
            dic_campos = parse_linha(linha)

            campo = 'tipo_de_registro'
            parametro = parametro_registro
            relatorio_final[campo] = []
            n = analisa_linha_e_atualiza_relatorio(nome_campo=campo, parametro_teste=parametro, index_linha=index_linha, dic_campos=dic_campos)
            if n:
                relatorio_final[campo] = relatorio_final[campo] + [n]

            campo = 'tipo_de_operacao'
            parametro = parametro_operacao
            relatorio_final[campo] = []
            n = analisa_linha_e_atualiza_relatorio(nome_campo=campo, parametro_teste=parametro, index_linha=index_linha, dic_campos=dic_campos)
            if n:
                relatorio_final[campo] = relatorio_final[campo] + [n]

            campo = 'id_do_movimento'
            parametro = parametro_movimento
            n = analisa_linha_e_atualiza_relatorio(nome_campo=campo, parametro_teste=parametro, index_linha=index_linha, dic_campos=dic_campos)
            if n:
                relatorio_final[campo] = relatorio_final[campo] + [n]

            campo = 'id_do_servico'
            parametro = parametro_id_servico
            n = analisa_linha_e_atualiza_relatorio(nome_campo=campo, parametro_teste=parametro, index_linha=index_linha, dic_campos=dic_campos)
            if n:
                relatorio_final[campo] = relatorio_final[campo] + [n]

            campo = 'ext_do_tipo_servico'
            parametro = parametro_ext_servico
            relatorio_final[campo] = []
            n = analisa_linha_e_atualiza_relatorio(nome_campo=campo, parametro_teste=parametro, index_linha=index_linha, dic_campos=dic_campos)
            if n:
                relatorio_final[campo] = relatorio_final[campo] + [n]

    print('total de linhas', total_linhas)
    if all(value == [] for value in relatorio_final.values()):
        print(MSG_SUCESSO)
    else:
        print(MSG_ERRO)
        print(f'Relatório de erros: {relatorio_final}')


if __name__ == '__main__':
    main()
