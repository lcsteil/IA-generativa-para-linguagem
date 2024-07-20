# IA-generativa-para-linguagem
Trabalho de IA generativa para linguagem

**Questão 1**: Explique os seguintes conceitos fundamentais dos LLMs, fornecendo exemplos práticos e diagramas onde for relevante:

* Pre-training       

    É a fase inicial do treinamento, o modelo é treinando com uma grande quantidade de dados de texto de maneira 
    não supervisionada. Nesta fase, o modelo aprende a prever a próxima palavara ou preencher palavras faltantes em uma sentença.

    **Exemplo**: Utilizado em um texto ou artigo gigante. O modelo será treinado para prever a próxima palavra em frases como "O gato está em cima do" (Modelo deve prever "teclado")

* Transfer Learning

    É a técnica de aproveitar o modelo pré-treinado em uma tarefa e adapta-lo para uma tarefa específica. Utiliza-se este conceito para que ao invés
    de treinar um modelo do zero, utiliza-se todo o conhecimento adquirido no pré-treino e ajusta-se para a nova tarefa com um conjunto
    menor de dados

    **Exemplo**: Pode ser utilizado em uma empresa que deseja monitorar a percepção de sua marca nas redes sociais. Utilizando  TRANSFER LEARNING  com um modelo pré-treinado como BERT, a empresa pode rapidamente classificar postagens em categorias como "positivo", "negativo" e "neutro".

* Embeddings

    São representações vetoriais de dados, geralmente palavras ou frases usadas em processamento de linguagem natural (NLP) e aprendizado de máquina. Elas permitem que máquinas entendam e manipulem texto de forma mais eficaz, transformando palavras em vetores de números que capturam o significado e as relações semânticas entre elas.

    **Exemplo**: Pode ser utilizado para uma análise de setimentos em um conjunto de avaliações de produtos. A análise  de sentimentos envolve determinarse uma opinião expressa em um texto é positiva, negativa ou neutra.

* Transformers

    São uma arquitetura de modelo de aprendizado profundo que revolucionou o campo do processamento de linguagem natural (NLP) e, mais recentemente, a visão computacional.

    **Exemplo**: Pode ser utilizado para analisar opiniões sobre produtos ou serviços para identificar tendências e preferências dos consumidores.

* Attention

    

* Fine-Tunning

**Questão 2**: Acesse os quizzes dos capítulos 1, 2 e 3 do curso de NLP da Hugging Face através do link: [Curso de NLP](https://huggingface.co/learn/nlp-course/).

1. Resolva os quizzes e capture screenshots dos resultados.
2. Anexe as screenshots a esta avaliação e explique brevemente os conceitos abordados em cada quiz.

* Capítulo 1
    1. Esse capítulo aborda conceitos fundamentais sobre modelos de linguagem natual e suas aplicações. Ele começa identificando que  modelo    *roberta-large-mnli* no Hugging Face Hub é usado para a classificação de texto, determinando se duas setenças têm uma relação lógica.

        Também foi explicado o uso do token *MASK* em modelos de preenchimento de lacunas, utilizado para prever tokens mascarados. Na seção sobre classificação zero-shot, destacou-se que o código falhará se não incluir a variável candidate_labels, necessária para classificar o texto corretamente.

        O conceito de transferência de aprendizado foi abordado, explicando como o conhecimento de um modelo pré-treinado é transferido para uma nova tarefa. O quiz também mencionou que modelos de linguagem geralmente são pré-treinados de maneira auto-supervisionada, sem a necessidade de rótulos explícitos.

        Os termos "modelo", "arquitetura" e "pesos" foram definidos: a arquitetura refere-se a uma sucessão de funções matemáticas, o modelo é construído com essas funções e os pesos são os parâmetros ajustados durante o treinamento. Além disso, modelos decodificadores são indicados para a geração de texto a partir de um prompt, enquanto modelos codificadores são mais adequados para tarefas de classificação de texto, pois geram uma representação da sentença inteira.

        Por fim, o quiz abordou a questão do viés nos modelos, destacando que este pode surgir de várias fontes, incluindo os dados de treinamento e as métricas otimizadas durante o treinamento.
        
    2. [QUIZ](/images/nlp_capitulo_1.png)

* Capítulo 2
    1. O quiz aborda conceitos importantes sobre a pipeline de modelagem de linguagem, tokenização, e técnicas de processamento de sequências. Ele começa descrevendo a pipeline de modelagem de linguagem, onde o tokenizador lida com o texto e retorna IDs. Esses IDs são utilizados pelo modelo para fazer previsões, que podem ser convertidas de volta para texto pelo tokenizador.

        A seguir, discute a dimensionalidade do tensor de saída de um modelo Transformer base, que inclui a sequência de comprimento, o tamanho do lote (batch size) e a dimensão oculta (hidden size).

        O quiz também aborda a tokenização de subpalavras, com exemplos como WordPiece e Unigram, que são técnicas usadas para dividir palavras em subunidades menores.

        O conceito de "model head" é explicado como um componente adicional, geralmente composto por uma ou algumas camadas, usado para converter as previsões do transformador em saídas específicas para a tarefa.

        Em seguida, a AutoModel é descrita como um objeto que retorna a arquitetura correta com base no checkpoint do modelo, apenas precisando saber qual checkpoint utilizar para inicializar a arquitetura correta.

        O quiz também menciona técnicas para lidar com sequências de diferentes comprimentos ao agrupar em lotes, como truncamento, padding e máscaras de atenção (attention masking).

        A função SoftMax é discutida, com o propósito de transformar logits em valores compreensíveis e interpretáveis como probabilidades, com os valores resultantes limitados entre 0 e 1.

        O método principal do tokenizador é descrito como o __call__, que pode codificar texto em IDs e IDs em previsões.

        Além disso, o quiz exemplifica o resultado de um código de tokenização, onde a variável resultante contém uma lista de strings, cada uma sendo um token. É explicado que esses tokens devem ser convertidos em IDs para serem utilizados por um modelo.

        Por fim, foi identificado que o tokenizador e o modelo devem sempre ser do mesmo checkpoint para evitar erros de compatibilidade.
    2. [QUIZ](/images/nlp_capitulo_2.png)

* Capítulo 3
    1. O quiz aborda conceitos importantes de processamento de linguagem natural (NLP) e uso de modelos pré-treinados no Hugging Face. Primeiro, ele explora datasets específicos, como o de emoções do Twitter, que inclui seis emoções básicas (alegria, amor, raiva, surpresa, tristeza e medo) e exclui "confusão". O dataset de sarcasmo suporta a tarefa de classificação de sentimentos.

        Sobre o modelo BERT, o quiz menciona que ele espera pares de sentenças formatados como [CLS] Tokens_da_sentenca_1 [SEP] Tokens_da_sentenca_2 [SEP]. O método Dataset.map() oferece benefícios como armazenamento em cache dos resultados, processamento em mini-batches e economia de memória ao processar elementos individualmente.

        O padding dinâmico ajusta o tamanho do lote ao comprimento máximo das sentenças no lote atual, resultando em batches com diferentes formas. A função de colação garante que todas as sequências em um lote tenham o mesmo comprimento, facilitando o processamento conjunto.

        Quando se instancia classes AutoModelForXxx com um modelo pré-treinado para uma tarefa diferente, a cabeça do modelo pré-treinado é descartada e uma nova cabeça, adequada para a nova tarefa, é instanciada com pesos aleatórios.

        O TrainingArguments contém todos os hiperparâmetros necessários para treinamento e avaliação com a API Trainer. A biblioteca Accelerate facilita o treinamento distribuído, permitindo o uso de múltiplas GPUs e TPUs para acelerar o processo.

        Este resumo sintetiza os principais pontos abordados, incluindo datasets de emoções e sarcasmo, formatação de entrada para modelos, benefícios de métodos de processamento de datasets, padding dinâmico, função de colação, instanciação de modelos pré-treinados, argumentos de treinamento e o uso da biblioteca Accelerate.
    2. [QUIZ](/images/nlp_capitulo_3.png)

 