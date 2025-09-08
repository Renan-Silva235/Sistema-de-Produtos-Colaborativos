#include <stdio.h>
#include <stdlib.h>
#include <cjson/cJSON.h>
#include <errno.h>


int gerarId(cJSON *json) {
    int id = 0;
    int tamanhoArquivoJson = cJSON_GetArraySize(json);
    for (int i = 0; i < tamanhoArquivoJson; i++) {
        cJSON *item = cJSON_GetArrayItem(json, i);
        cJSON *id_json = cJSON_GetObjectItem(item, "id");
        if (cJSON_IsNumber(id_json) && id_json->valueint > id) {
            id = id_json->valueint;
        }
    }
    return id + 1;
}





void cadastrar(char *filename,  char *json_str) {
    cJSON *produto = cJSON_Parse(json_str);
    if (!produto) return; // erro no parse

    FILE *arquivo;
    long tamanho;
    char *conteudo;
    cJSON *json = NULL;

    // Lê JSON existente
    arquivo = fopen(filename, "r");
    if (arquivo) {
        fseek(arquivo, 0, SEEK_END);
        tamanho = ftell(arquivo);
        rewind(arquivo);

        if (tamanho > 0) {
            conteudo = malloc(tamanho + 1);
            fread(conteudo, 1, tamanho, arquivo);
            conteudo[tamanho] = '\0';
            fclose(arquivo);

            json = cJSON_Parse(conteudo);
            free(conteudo);
            if (!json) json = cJSON_CreateArray();
        } else {
            fclose(arquivo);
            json = cJSON_CreateArray();
        }
    } else {
        json = cJSON_CreateArray();
    }

    // Gera ID automático
    int novo_id = gerarId(json);

    // Cria produto com ID primeiro
    cJSON *produto_com_id = cJSON_CreateObject();
    cJSON_AddNumberToObject(produto_com_id, "id", novo_id);

    // Copia os outros campos
    cJSON *campo = produto->child;
    while (campo) {
        cJSON_AddItemToObject(produto_com_id, campo->string, cJSON_DetachItemFromObject(produto, campo->string));
        campo = produto->child;
    }

    // Adiciona ao array e salva
    cJSON_AddItemToArray(json, produto_com_id);
    char *texto = cJSON_Print(json);

    arquivo = fopen(filename, "w");
    if (arquivo) {
        fputs(texto, arquivo);
        fclose(arquivo);
    }

    free(texto);
    cJSON_Delete(json);
    cJSON_Delete(produto); // libera o produto original
}






