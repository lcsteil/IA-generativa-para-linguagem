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

    É uma tecnica usada em redes neurais, particularmente em modelos de linguagem, para focar em partes específicas de entrada (texto) ao gerar uma saída. Ele permite que o modelo dê mais peso a palavras ou tokens importantes, ajudando a capturar dependências e relações contextuais de longa distância.

    **Exemplo**: Condiderando a frase "O gato sentou no tapete". Se quisermos prever a palava "tapete" dada a palavra "gato", a atenção ajudaria a entender que "tapete" é relevante porque "gato" esá "sentado" nele.

* Fine-Tunning

    É o processo de adaptar um modelo pré-treinado (como um LLM) a uma tarefa específica, ajustando seus pesos com base em um conjunto de dados específico da tarea.

    **Exemplo**: Suponha que temos um modelo pré-treinado em um grande corpus de textos gerais e queremos adaptá-lo para detectar spam em e-mails. Utilizamos um conjunto de dados específicos de e-mails marcadaos como spam e não-spam para ajustar o modelo pré-treinado, otimizando-o para essa tarefa.

----------------------------------------------------

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

----------------------------------------------------

 **Questão 3**: Análise de Dados com NER. Baixe o conjunto de dados de notícias disponível em: [Folha UOL News Dataset](https://www.kaggle.com/datasets/marlesson/news-of-the-site-folhauol).

A questão 3 foi desenvolvida no notebook [questao_3.ipynb](questao_3.ipynb), seguindo os passos abaixo:

1. Após importar o CSV, os dados foram filtrados pela categoria "MERCADO" e com dados do primeiro trimestre de 2015
2. Foi utilizado a o TRANSFORMERS, classificando por organizações "ORG" removendo palavras com menos de um caracter e que começam com "##" para limpar um pouco os resultados
3. Em seguida foi feito um contador de frequencia das organizações encontradas
4. Por fim foi ordenado em ordem decrescente para apresentar as organizações com maiores frequências

----------------------------------------------------

 **Questão 4**: Analise os seguintes prompts e identifique por que eles poderiam gerar respostas insatisfatórias ou irrelevantes.

* Exemplo 1: "Escreva sobre cachorros."

    A frase não define o objetivo desejado. É necessário mais detalhes como o que quer que seja escrito sobre cachorros, raça? cuidados? cachorros?, sem mais detalhes a resposta pode ser genérica, incompleta ou irrelevante.

* Exemplo 2: "Explique física."

    Como no exemplo 1, a física é um campo de estudo muito abrangente, com diversas divisões, a falta de detalhes pode ser que retorne uma resposta muito geral, focar em um contexto irrelevante ou retornar uma reposta muito completa para o público-alvo.

----------------------------------------------------

**Questão 5**: O prompt "Descreva a história da internet." foi mal formulado. Aplique técnicas de engenharia de prompts para melhorá-lo. Reformule o prompt para melhorar a especificidade e a qualidade da resposta. Justifique as mudanças feitas e explique como elas contribuem para obter uma resposta mais eficaz e relevante.

O prompt informado é muito vago e aberto, podendo gerar respostas muito amplas e superficiais. Não especifica quais aspectos da história devem ser cobertos, como datas importantes, porsonagens chave, etc. Falta especificar o nível de detalhamento esperado na resposta.

*Prompt reformulado*: Descreva a história da internet, destacando suas principais frases de desenvolvimento, desde a criação da arpanet até o surgimento das redes sociais. Inclua datas importantes, tecnologias chaves e o impacto social econômico ao longo do tempo.

----------------------------------------------------

**Questão 6**: Aplique a técnica de Chain of Thought (CoT) para melhorar o prompt "Explique como funciona a energia solar.", detalhando o raciocínio necessário para que o modelo forneça uma resposta completa e coerente. Explique como a aplicação da técnica CoT melhora a resposta do modelo.

Para utilizar a técnica de Chain of Thought (CoT), precisamos dividir o processo em etapas lógicas que guiem o modelo a fornecer uma reposta completa e coerente. Isso envolve a decomposição da pergunta em subquestões que abordem diferentes aspectos do funcionamento de energia solar.

1. *Definição*: Começar com definição básica do que é energia solar
2. *Principio básico*: Explicar o conceito básico de como a energia solar é convertida em eletrecidade
3. *Componentes principais*: Descrever os componentes principais de uma energia solar, como painéis solares e baterias.
4. *Processo de conversão*: Detalhar o processo de conversão dentro dos painéis solares.
5. *Distribuição de eneregia*: Explicar como a eletrecidade é gerada é distribuidad e utilizada em um sistema residencial ou comercial.
6. *Benefícios e desafios*: Explicar os benefícios e desacios associados ao uso de energia solar.

A divisão do problema em subquestões garante que nenhum aspecto importante seja omitido. Cada etapa permite uma exploração mais profunda de cada componente do funcionamento da energia solar e a estrutura lógica facilita a organização das informações, tornando uma resposta mais fácil de entender e seguir.

*Exemplo e de prompt*: Explique como funciona a energia solar detalhadamente. Inicie definindo o que é energia solar e o princípio básico de como a luz é convertida em eletrecidade. Descreva os componentes principais de um sistema de energia solar, incluindo painéis solares, inversores e baterias. Explique o processo de conversão da luz em eletrecidade dentro dos painéis solares. Detalhe como a eletricidade gerada é distribuída e utilizada em um sistema residencial e comercial. Por fim, discuta os benefícios e desafios associados ao uso da energia solar.

----------------------------------------------------

**Questão 7**: Escolha uma aplicação para desenvolver utilizando Streamlit, LLM e LangChain. Crie um aplicativo interativo que demonstre o uso de LLMs para resolver um problema específico.

1. Descreva a aplicação escolhida e os objetivos principais do projeto.

A aplicação escolhida foi o sumarizador de Artigos.

O objetivo é desenvolver um aplicativo que permita ao usuário inserir o texto de um artigo e obter um resumo conciso do conteúdo.

2. Explique a arquitetura do aplicativo, incluindo como o Streamlit, LLM e LangChain são utilizados.

    1. O StreamLite é utilizado para criar a interface para o usuário informar o texto e a chave do OPENAI.
    2. O LangChain é uma biblioteca utilizada para processar e manipular o texto, bem como carregar o modelo de sumarização.
    3. No LLM, foi utilizado o modelo de linguagem da OpenAI para gerar a sumarização do texto fornecido.   
    4. Fluxo do aplicativo:
        1. O usuário insere o texto a ser resumido e a chave da API do OpenAI
        2. Processamento:
            * O texto é dividido em partes menores
            * Cada parte é encapsulada em um objeto "Document"
            * A cadeia de sumarização é carregada e executada nos documentos
        3. O resultado é gerado e exibido para o usuário na tela.

3. Implemente o aplicativo e forneça o código-fonte, junto com instruções para execução.

O aplicativo foi implementado no arquivo [questao_7.py](questao_7.py)

4. Apresente evidências e exemplos de uso do aplicativo e discuta os resultados obtidos.

Foi utilizado o texto abaixo:

> Sempre que ocorre um entusiasmo com os resultados de uma tecnologia, existe uma tendência da mídia em fornecer definições e explicações, por vezes não muito precisas, dos seus principais aspectos. Isso é, certamente, o que ocorre com a IA nos dias de hoje. Em primeiro lugar, cabe ressaltar que não existe uma definição acadêmica, propriamente dita, do que vem a ser IA. Trata-se certamente de um ramo da ciência/engenharia da computação, e portanto visa desenvolver sistemas computacionais que solucionam problemas. Para tal, utiliza um número diverso de técnicas e modelos, dependendo dos problemas abordados. Portanto, é inadequado utilizar-se expressões como “a IA da empresa X”; mais adequado (porém com menos apelo) seria dizer “um sistema da empresa X que utiliza técnicas de IA"

Retornando:

> The media often provides vague definitions of AI when there is excitement about its results. There is no clear academic definition for AI, but it is a branch of computer science/engineering that aims to solve problems using various techniques and models. It is inappropriate to use phrases like "X company's AI", and it is more accurate to say "a system from X company that utilizes AI techniques".

![Resultado](/images/questao_7.png)


