/*
 * Arquivo: funcaoSalvarJson.c
 *
 * Implementação de funções para salvar dados JSON em arquivos.
 * Contém funções para gerenciar operações de escrita em arquivos JSON,
 * incluindo geração automática de IDs e adição de novos objetos a arquivos JSON existentes.
 *
 * Utiliza a biblioteca cJSON para manipulação de dados JSON.
 */

#include <stdio.h>
#include <stdlib.h>
#include <cjson/cJSON.h>
#include <errno.h>

/*
 * Macro para exportar funções em bibliotecas compartilhadas.
 * No Windows, usa __declspec(dllexport) para exportar a função.
 * Em sistemas Unix/Linux, não é necessário.
 */
#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif



/*
 * Gera um novo ID único para um objeto JSON baseado nos IDs existentes.
 *
 * Percorre todos os itens do array JSON, encontra o maior ID existente
 * e retorna o próximo ID disponível (maior ID + 1).
 * Se o array estiver vazio ou não houver IDs válidos, retorna 1.
 *
 * Recebe: ponteiro para um objeto cJSON do tipo array contendo os dados existentes
 * Retorna: o próximo ID disponível (maior ID encontrado + 1)
 */
int gerarId(cJSON *json) {
    int id = 0;
    int tamanhoArquivoJson = cJSON_GetArraySize(json);

    // Percorre todos os itens do array para encontrar o maior ID
    for (int i = 0; i < tamanhoArquivoJson; i++) {
        cJSON *item = cJSON_GetArrayItem(json, i);
        cJSON *id_json = cJSON_GetObjectItem(item, "id");

        // Atualiza o ID máximo encontrado
        if (cJSON_IsNumber(id_json) && id_json->valueint > id) {
            id = id_json->valueint;
        }
    }

    // Retorna o próximo ID disponível
    return id + 1;
}





/*
 * Salva um novo objeto JSON em um arquivo, gerando automaticamente um ID único.
 *
 * Esta função é responsável por:
 * 1. Ler o conteúdo existente do arquivo JSON (se existir)
 * 2. Gerar um novo ID único para o objeto a ser adicionado
 * 3. Adicionar o objeto ao array JSON existente
 * 4. Salvar o array atualizado de volta no arquivo
 *
 * Se o arquivo não existir ou estiver vazio, cria um novo array JSON.
 * O objeto recebido é parseado a partir de uma string JSON e adicionado ao array.
 *
 * Esta função é exportada para uso em bibliotecas compartilhadas (DLL/SO).
 * A função retorna silenciosamente se houver erro no parse do JSON de entrada.
 * A memória alocada é liberada automaticamente ao final da função.
 *
 * Recebe:
 *   - filename: caminho do arquivo JSON onde os dados serão salvos
 *   - json_str: string JSON contendo o objeto a ser adicionado ao arquivo
 */
EXPORT void salvarNoJson(char *filename, char *json_str) {
    // Faz o parse do objeto JSON recebido como string
    cJSON *produto = cJSON_Parse(json_str);
    if (!produto) return; // Erro no parse: retorna sem fazer nada

    FILE *arquivo;
    long tamanho;
    char *conteudo;
    cJSON *json = NULL;

    // Lê o conteúdo JSON existente do arquivo
    arquivo = fopen(filename, "r");
    if (arquivo) {
        // Obtém o tamanho do arquivo
        fseek(arquivo, 0, SEEK_END);
        tamanho = ftell(arquivo);
        rewind(arquivo);

        if (tamanho > 0) {
            // Aloca memória e lê o conteúdo do arquivo
            conteudo = malloc(tamanho + 1);
            fread(conteudo, 1, tamanho, arquivo);
            conteudo[tamanho] = '\0';
            fclose(arquivo);

            // Faz o parse do conteúdo lido
            json = cJSON_Parse(conteudo);
            free(conteudo);

            // Se o parse falhar, cria um novo array vazio
            if (!json) json = cJSON_CreateArray();
        } else {
            // Arquivo vazio: cria um novo array
            fclose(arquivo);
            json = cJSON_CreateArray();
        }
    } else {
        // Arquivo não existe: cria um novo array
        json = cJSON_CreateArray();
    }

    // Gera um novo ID único baseado nos IDs existentes
    int novo_id = gerarId(json);

    // Cria um novo objeto JSON e adiciona o ID primeiro
    cJSON *produto_com_id = cJSON_CreateObject();
    cJSON_AddNumberToObject(produto_com_id, "id", novo_id);

    // Copia todos os outros campos do objeto original para o novo objeto
    cJSON *campo = produto->child;
    while (campo) {
        cJSON_AddItemToObject(produto_com_id, campo->string,
                              cJSON_DetachItemFromObject(produto, campo->string));
        campo = produto->child;
    }

    // Adiciona o objeto completo ao array JSON
    cJSON_AddItemToArray(json, produto_com_id);

    // Converte o JSON para string formatada
    char *texto = cJSON_Print(json);

    // Salva o array atualizado no arquivo
    arquivo = fopen(filename, "w");
    if (arquivo) {
        fputs(texto, arquivo);
        fclose(arquivo);
    }

    // Libera a memória alocada
    free(texto);
    cJSON_Delete(json);
    cJSON_Delete(produto); // Libera o produto original
}






