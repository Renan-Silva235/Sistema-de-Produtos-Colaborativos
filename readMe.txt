Antes de tudo, você precisa instalar as bibliotecas que o programa está usando, siga o passo a passo abaixo:

passo 1:
  crie um ambiente virtual com o seguinte comando abaixo:
  comando: python -m venv .venv


passo 2:
  Ative o ambiente virtual. Dependendo do terminal que você está usando, o camando será diferente:
  - PowerShell:
    comando: .\.venv\Scripts\Activate.ps1

  -Prompt de Comando:
    comando: .venv\Scripts\activate.bat

passo 3: depois de ativar o ambiente virtual, instale todos os recursos do programa.
  comando: pip install -r requirements.txt



OBS:
  lembre-se de criar um gitIgnore para não commitar arquivos desnecessários.
