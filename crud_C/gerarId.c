#include <stdio.h>
#include <cjson/cJSON.h>

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

