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

    **Exemplo**: 

* Embeddings
* Transformers
* Attention
* Fine-Tunning

**Questão 2**: Acesse os quizzes dos capítulos 1, 2 e 3 do curso de NLP da Hugging Face através do link: [Curso de NLP](https://huggingface.co/learn/nlp-course/).

1. Resolva os quizzes e capture screenshots dos resultados.
2. Anexe as screenshots a esta avaliação e explique brevemente os conceitos abordados em cada quiz.

* Capítulo 1
    1. Esse capítulo aborda conceitos fundamentais sobre modelos de linguagem natual e suas aplicações. Ele começa identificando que  modelo *roberta-large-mnli* no Hugging Face Hub é usado para a classificação de texto, determinando se duas setenças têm uma relação lógica.

        Também foi explicado o uso do token *MASK* em modelos de preenchimento de lacunas, utilizado para prever tokens mascarados. Na seção sobre classificação zero-shot, destacou-se que o código falhará se não incluir a variável candidate_labels, necessária para classificar o texto corretamente.

        O conceito de transferência de aprendizado foi abordado, explicando como o conhecimento de um modelo pré-treinado é transferido para uma nova tarefa. O quiz também mencionou que modelos de linguagem geralmente são pré-treinados de maneira auto-supervisionada, sem a necessidade de rótulos explícitos.

        Os termos "modelo", "arquitetura" e "pesos" foram definidos: a arquitetura refere-se a uma sucessão de funções matemáticas, o modelo é construído com essas funções e os pesos são os parâmetros ajustados durante o treinamento. Além disso, modelos decodificadores são indicados para a geração de texto a partir de um prompt, enquanto modelos codificadores são mais adequados para tarefas de classificação de texto, pois geram uma representação da sentença inteira.

        Por fim, o quiz abordou a questão do viés nos modelos, destacando que este pode surgir de várias fontes, incluindo os dados de treinamento e as métricas otimizadas durante o treinamento.
        
    2. [QUIZZ](/images/nlp_capitulo_1.png)

* Capítulo 2
    1. 
    2. [QUIZZ](/images/nlp_capitulo_2.png)

* Capítulo 3
    1. 
    2. [QUIZZ](/images/nlp_capitulo_3.png)

