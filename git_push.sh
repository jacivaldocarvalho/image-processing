#!/bin/bash

# Verifica se um argumento foi passado para a mensagem do commit
if [ -z "$1" ]; then
  echo "Uso: $0 'mensagem do commit'"
  exit 1
fi

# Adiciona todos os arquivos ao stage
git add .

# Realiza o commit com a mensagem passada como argumento
git commit -m "$1"

# Envia as alterações para o repositório remoto
git push origin main

echo "Alterações enviadas com sucesso!"
