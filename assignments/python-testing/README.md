# 📘 Assignment: Primeiros Passos com Testes Automatizados

## 🎯 Objetivo

Aprenda a usar `pytest` para verificar funções Python com testes automatizados. Você praticará como escrever casos de teste, conferir resultados esperados e investigar falhas.

## 📝 Tarefas

### 🛠️ Escrever os Primeiros Testes

#### Descrição
Instale o `pytest` com `python -m pip install pytest`. Renomeie o arquivo fornecido `starter-code.py` para `starter_code.py` e crie ao lado dele um arquivo chamado `test_starter_code.py`. Importe `add_numbers` e escreva testes que confirmem a soma de dois números positivos e de um número positivo com um negativo. Execute os testes com `python -m pytest`.

#### Requisitos
O programa concluído deve:

- Instalar e executar `pytest` pelo terminal
- Criar testes cujos nomes comecem com `test_`
- Verificar os resultados de `add_numbers` usando `assert`
- Exibir os testes aprovados ao executar `python -m pytest`

### 🛠️ Testar Resultados Verdadeiros e Falsos

#### Descrição
Adicione testes para `is_even`. Verifique números pares e ímpares, incluindo um número negativo, para confirmar que a função retorna `True` ou `False` como esperado.

#### Requisitos
O programa concluído deve:

- Testar pelo menos dois números pares e dois ímpares
- Incluir pelo menos um número negativo
- Comparar cada resultado esperado com `assert`
- Manter os testes organizados em `test_starter_code.py`

### 🛠️ Investigar uma Falha de Teste

#### Descrição
Inclua um teste para o limite de aprovação da função `is_passing_grade`: uma nota de 59 não passa e uma nota de 60 passa. Altere temporariamente um dos valores esperados para observar um teste falhar, leia a mensagem do `pytest` e depois restaure o valor correto.

#### Requisitos
O programa concluído deve:

- Verificar as notas imediatamente abaixo e no limite de aprovação
- Mostrar uma falha intencional e identificar qual teste falhou
- Restaurar a expectativa correta e executar todos os testes novamente
- Terminar com todos os testes aprovados