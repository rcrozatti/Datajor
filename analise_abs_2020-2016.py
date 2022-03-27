#!/usr/bin/env python
# coding: utf-8

# # **Trabalho de Python para Jornalismo de Dados II**
# 
# **Professores:** Rodolfo Viana e Deborah Foroni 
# 
# **Alunos:** Ana Prado e Renato Crozatti

# Análise com o número de abstenções nas eleições municipais de 2020 e 2016:

# In[1]:


import warnings
warnings.filterwarnings("ignore") 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


dados_2020 = pd.read_csv('perfil_comparecimento_abstencao_2020 2.csv', encoding = "ISO-8859-1", sep=";")
dados_2020.head()


# In[3]:


#resumo com todas as colunas e as primeiras 5 linhas do dataframe


# In[4]:


dados_2020.info()
dados_2020.shape 


# Para a nossa análise, vamos remover todas as colunas desnecessárias, incluindo códigos de município e gênero, comparecimento e abstenção por deficiência, entre outros. Manteremos os dados excenciais, como ano, turno, UF, município, gênero, faixa etária, total e abstenções. 

# In[5]:


dados_2020 = dados_2020.drop(columns=['DT_GERACAO', 'HH_GERACAO', 'CD_MUNICIPIO', 'CD_GENERO', 
                                  'CD_ESTADO_CIVIL', 'CD_FAIXA_ETARIA', 'CD_GRAU_ESCOLARIDADE', 'DS_ESTADO_CIVIL',
                                 'QT_COMPARECIMENTO_DEFICIENCIA', 'QT_ABSTENCAO_DEFICIENCIA', 'QT_COMPARECIMENTO_TTE', 
                                  'QT_ABSTENCAO_TTE', 'NR_ZONA'])
dados_2020.head()


# In[6]:


dados_2020.info() 


# Para facilitar a análise e deixar nosso dataframe mais limpo, vamos renomear essas 10 colunas com nomenclaturas mais simples, em letras minúsculas. Essas alterações serão feitas diretamente no dataframe original. 

# In[7]:


dados_2020.rename(columns={'ANO_ELEICAO': 'ano', 'NR_TURNO': 'turno', 'SG_UF': 'uf', 'NM_MUNICIPIO':'municipio', 
                          'DS_GENERO': 'genero', 'DS_GRAU_ESCOLARIDADE':'escolaridade', 
                        'QT_APTOS': 'total', 'QT_COMPARECIMENTO': 'comparecimento', 'QT_ABSTENCAO': 'abstencao',
                         'DS_FAIXA_ETARIA': 'idade'}, inplace=True) 
dados_2020.info()


# Nosso dataframe, referente às abstenções de 2020, ficará assim: 

# In[8]:


dados_2020 


# Agora, vamos selecionar somente as colunas que nos interessam para nossa primeira análise - ano, turno, total de eleitores e abstenção: 

# In[9]:


abs_2020 = dados_2020.loc[:, ['ano', 'turno', 'total', 'abstencao']]
abs_2020


# Agora, vamos selecionar os dados referentes ao 1º turno da eleição - primeiro checaremos se os valores estão corretos e, logo depois, criar um novo dataframe com esse recorte.

# In[10]:


abs_2020['turno'] == 1


# In[11]:


abs_2020_1 = abs_2020[abs_2020['turno'] == 1]
abs_2020_1


# Agora conseguimos fazer nossa primeira etapa da análise: qual o total de eleitores aptos no 1º turno em 2020, o número de abstenções e seu percentual? 

# In[12]:


total_2020_1 = abs_2020_1['total'].sum()
total_2020_1


# In[13]:


abs_2020_1_sum = abs_2020_1['abstencao'].sum()
abs_2020_1_sum


# In[14]:


abs_2020_1_perc = abs_2020_1_sum / total_2020_1 *100
abs_2020_1_perc


# Chegamos aos números que buscávamos: ao todo, o país possuía 147.918.483 de eleitores no 1º turno de 2020. Deles, 34.240.897 não compareceram no dia da votação, o que representa  23,15% do total. Agora, vamos repetir o processo para chegar aos números do 2º turno. 

# In[15]:


abs_2020_2 = abs_2020[abs_2020['turno'] == 2]
abs_2020_2


# In[16]:


total_2020_2 = abs_2020_2['total'].sum()
total_2020_2


# In[17]:


abs_2020_2_sum = abs_2020_2['abstencao'].sum()
abs_2020_2_sum


# In[18]:


abs_2020_2_perc = abs_2020_2_sum / total_2020_2 *100
abs_2020_2_perc


# O 2º turno das eleições municipais no Brasil teve um aumento nas abstenções: dos 38.577.128 eleitores aptos, 11.392.279 não votaram no dia. 
# 
# *É importante destacar que muitos municípios não tiveram 2º turno, por isso a diferença do total em relação ao 1º.* 

# Com os dados gerais das eleições municipais de 2020 no Brasil, verificamos e limpamos a base de dados referente a 2016. Vamos repetir o processo anterior: importar a base de dados e verificá-la para entendê-la através de resumo, tamanho, etc. 

# In[19]:


dados_2016 = pd.read_csv('perfil_comparecimento_abstencao_2016.csv', encoding = "ISO-8859-1", sep=";")


# In[20]:


dados_2016.head()


# In[21]:


dados_2016.info()
dados_2016.shape


# Agora, vamos retirar as colunas desnecessárias para nossa análise e renomear as remanescentes para ficar mais simples e fácil de verificar. 

# In[22]:


dados_2016 = dados_2016.drop(columns=['DT_GERACAO', 'HH_GERACAO', 'CD_MUNICIPIO', 'CD_GENERO', 
                                  'CD_ESTADO_CIVIL', 'NR_ZONA', 'CD_FAIXA_ETARIA', 'CD_GRAU_ESCOLARIDADE', 'DS_ESTADO_CIVIL',
                                 'QT_COMPARECIMENTO_DEFICIENCIA', 'QT_ABSTENCAO_DEFICIENCIA', 'QT_COMPARECIMENTO_TTE', 
                                  'QT_ABSTENCAO_TTE'])
dados_2016.head()


# In[23]:


dados_2016.info()


# In[24]:


dados_2016.rename(columns={'ANO_ELEICAO': 'ano', 'NR_TURNO': 'turno', 'SG_UF': 'uf', 'NM_MUNICIPIO':'municipio', 
                         'NR_ZONA': 'zona', 'DS_GENERO': 'genero', 'DS_FAIXA_ETARIA': 'idade', 
                         'DS_GRAU_ESCOLARIDADE': 'escolaridade', 'QT_APTOS': 'total', 'QT_COMPARECIMENTO': 'comparecimento', 
                         'QT_ABSTENCAO': 'abstencao'}, inplace=True) 
dados_2016.info()


# Nosso dataframe de 2016 ficou assim:

# In[25]:


dados_2016


# Similar ao que fizemos na base de dados de 2020, vamos verificar o número total de eleitores e de abstenção do 1º e 2º turno separadamente. 

# In[26]:


dados_2016_1 = dados_2016[dados_2016['turno'] == 1]
dados_2016_1


# In[27]:


abs_2016_1 = dados_2016_1.loc[:, ['ano', 'turno', 'total', 'abstencao']]
abs_2016_1


# In[28]:


total_2016_1 = abs_2016_1['total'].sum()
total_2016_1


# In[29]:


abs_2016_1_sum = abs_2016_1['abstencao'].sum()
abs_2016_1_sum


# In[30]:


perc_2016_1 = abs_2016_1_sum / total_2016_1 * 100
perc_2016_1


# In[31]:


dados_2016_2 = dados_2016[dados_2016['turno'] == 2]
dados_2016_2


# In[32]:


abs_2016_2 = dados_2016_2.loc[:, ['ano', 'turno', 'total', 'abstencao']]
abs_2016_2


# In[33]:


abs_2016_2_sum = abs_2016_2['abstencao'].sum()
abs_2016_2_sum


# In[34]:


total_2016_2 = abs_2016_2['total'].sum()
total_2016_2


# In[35]:


perc_2016_2 = abs_2016_2_sum / total_2016_2 * 100
perc_2016_2


# Os dados de 2016 nos retornaram as seguintes informações: 
# 1º turno teve um total de 144.088.912 eleitores aptos e 25.333.362 abstenções, o equivalente a 17,58% do total;
# 2º turno contou com um total de 38.577.128 eleitores aptos e 32.986.856 abstenções, o que equivale a 29,53% do total. 

# Agora que temos o total, o número de abstenções e o percentual de cada ano e turno, vamos montar um dataframe novo com esses resultados:
# - Total 2016, turno 1: **144088912**
# - Abstenção 2016, turno 1: **25333362**
# - Percentual abstenção 2016, turno 1: **17.58%**
# - Total 2016, turno 2: **32986856**
# - Abstenção 2016, turno 2: **7109097**
# - Percentual abstenção 2016, turno 2: **21.55%**
# - Total 2020, turno 1: **147918483**
# - Abstenção 2020, turno 1: **34240897**
# - Percentual abstenção 2020, turno 1: **23.15%** 
# - Total 2020, turno 2: **38577128**
# - Abstenção 2020, turno 2: **11392279**
# - Percentual abstenção 2020, turno 2: **29.53%**
# 
# O novo dataframe ficará assim:

# In[36]:


df = pd.DataFrame({
    'ano': ['2016', '2016', '2020', '2020'],
    'turno': ['turno 1', 'turno 2', 'turno 1', 'turno 2'],
    'total': [144088912, 32986856, 147918483, 38577128],
    'abstencao': [25333362, 7109097, 34240897, 11392279],
    'percentual_abs': [17.58, 21.55, 23.15, 29.53]
})
df


# Para facilitar a criação do gráfico para visualizar esses dados, vamos transformar as colunas 'ano' e 'turno' no índice do dataframe. 

# In[37]:


df.set_index(['ano', 'turno'], inplace=True)


# In[38]:


df


# Para a visualização, vamos criar um gráfico em barras na vertical com esse dataframe e, abaixo, a barra horizontal usando o matplotlib e seaborn.

# In[39]:


f, ax = plt.subplots(figsize = (10,5)) 
df['percentual_abs'].plot.bar(title='Abstenção nas eleições municipais - 2016 e 2020')
for container in ax.containers:
    ax.bar_label(container)     
ax.set(ylabel = '% de abstenção', 
       xlabel = 'Ano e turno das eleições municipais' 
)


# In[40]:


df1 = pd.DataFrame({
    'ano_turno': ['2016, 1º turno', '2016, 2º turno', '2020, 1º turno', '2020, 2º turno'],
    'total': [144088912, 32986856, 147918483, 38577128],
    'abstencao': [25333362, 7109097, 34240897, 11392279],
    'percentual_abs': [17.58, 21.55, 23.15, 29.53]
})
f, ax = plt.subplots(figsize = (10,5))
sns.barplot(x ='percentual_abs',
            y = 'ano_turno',
            data = df1,
            label = 'Turno 1',
            ci = None)
for container in ax.containers:
    ax.bar_label(container)
ax.set(xlim = (0, 35), 
       xlabel = '% de abstenção', 
       ylabel = 'Ano e turno das eleições municipais'
)


# # Parte 2 - Analisando o índice de abstenção por cidade

# Agora que temos as médias, vamos analisar quais municípios se destacam nas taxas de abstenção. Desta vez, vamos comparar apenas o primeiro turno, já que as cidades com segundo turno variam a cada eleição. 

# In[41]:


abs_2020_cidade = dados_2020.loc[:, ['ano', 'turno', 'municipio','total', 'abstencao']]


# In[42]:


abs_2020_cidade = abs_2020_cidade.astype({'turno': str, 'ano': str})
abs_2020_cidade.info()


# In[43]:


abs_2020_cidade_1 = abs_2020_cidade[abs_2020_cidade['turno'] == "1"]
abs_2020_cidade_1.head(10)


# In[44]:


abs_2020_cidade_1 = abs_2020_cidade_1.groupby(by='municipio', as_index=False).sum()
abs_2020_cidade_1.head(10)


# In[45]:


abs_2020_cidade_1['taxa_abstencao'] = 100*(abs_2020_cidade_1['abstencao']/abs_2020_cidade_1['total'])
abs_2020_cidade_1


# In[50]:


abs_2020_cidade_1 = abs_2020_cidade_1.sort_values(by=['taxa_abstencao'], ascending=False)
abs_2020_cidade_1.head(10)


# In[47]:


abs_2020_cidade_1.tail(5)


# In[51]:


abs_2016_cidade = dados_2016.loc[:, ['ano', 'turno', 'municipio','total', 'abstencao']]
abs_2016_cidade = abs_2016_cidade.astype({'turno': str, 'ano': str})
abs_2016_cidade_1 = abs_2016_cidade[abs_2016_cidade['turno'] == "1"]
abs_2016_cidade_1 = abs_2016_cidade_1.groupby(by='municipio', as_index=False).sum()
abs_2016_cidade_1['taxa_abstencao'] = 100*(abs_2016_cidade_1['abstencao']/abs_2016_cidade_1['total'])
abs_2016_cidade_1 = abs_2016_cidade_1.sort_values(by=['taxa_abstencao'], ascending=False)
abs_2016_cidade_1.head(10)


# In[49]:


abs_2016_cidade_1.tail(5)


# É possível notar que, embora algumas das cidades com maior abstenção em 2020 já estivessem no top 10 de 2016, essa porcentagem se tornou maior. Além disso, novas cidades entraram no ranking. Uma segunda análise possível, porém bem mais trabalhosa, seria integrar esses dados com os dados de casos de Covid por município no mês de novembro para avaliar se existe uma correlação. 

# ## Parte 3

# Agora, vamos analisar os índices de abstenção por faixa etária. Queremos avaliar se a pandemia influenciou os números, já que o coronavírus representa um risco maior para os mais idosos. Para esta análise, também vamos verificar apenas os resultados do primeiro turno, por ser um universo maior. 
# 

# In[52]:


abs_2020_idade = dados_2020.loc[:, ['ano', 'turno', 'idade','total', 'abstencao']]


# In[53]:


abs_2020_idade = abs_2020_idade.astype({'turno': str, 'ano': str})


# In[54]:


Faixa_etaria = []
for row in abs_2020_idade['idade']:
    if row in ['100 anos ou mais']:
        Faixa_etaria.append('100 anos ou mais')
    elif row in ['90 a 94 anos', '95 a 99 anos']:
        Faixa_etaria.append('90 a 99 anos')
    elif row in ['80 a 84 anos', '85 a 89 anos']:
        Faixa_etaria.append('80 a 89 anos')
    elif row in ['70 a 74 anos', '75 a 79 anos']:
        Faixa_etaria.append('70 a 79 anos')
    elif row in ['60 a 64 anos', '65 a 69 anos']:
        Faixa_etaria.append('60 a 69 anos')
    elif row in ['50 a 54 anos', '55 a 59 anos']:
        Faixa_etaria.append('50 a 59 anos')
    elif row in ['40 a 44 anos', '45 a 49 anos']:
        Faixa_etaria.append('40 a 49 anos')
    elif row in ['30 a 34 anos', '35 a 39 anos']:
        Faixa_etaria.append('30 a 39 anos')
    elif row in ['20 anos', '21 a 24 anos', '25 a 29 anos']:
        Faixa_etaria.append('20 a 29 anos')
    elif row in ['16 anos', '17 anos', '18 anos', '19 anos']:
        Faixa_etaria.append('16 a 19 anos')
    elif row in ['Inválido']:
        Faixa_etaria.append('nulo')
abs_2020_idade['idade'] = Faixa_etaria
abs_2020_idade


# In[55]:


abs_2020_idade_1 = abs_2020_idade[abs_2020_idade['turno'] == "1"]
abs_2020_idade_1


# In[56]:


abs_2020_idade_1 = abs_2020_idade_1.groupby(by='idade', as_index=False).sum()
abs_2020_idade_1


# In[57]:


abs_2020_idade_1['taxa_abstencao'] = 100*(abs_2020_idade_1['abstencao']/abs_2020_idade_1['total'])
abs_2020_idade_1

abs_2020_idade_1 = abs_2020_idade_1.sort_values(by=['taxa_abstencao'], ascending=False)
abs_2020_idade_1


# In[58]:


abs_2016_idade = dados_2016.loc[:, ['ano', 'turno', 'idade','total', 'abstencao']]
abs_2016_idade = abs_2016_idade.astype({'turno': str, 'ano': str})
Faixa_etaria = []
for row in abs_2016_idade['idade']:
    if row in ['100 anos ou mais']:
        Faixa_etaria.append('100 anos ou mais')
    elif row in ['90 a 94 anos', '95 a 99 anos']:
        Faixa_etaria.append('90 a 99 anos')
    elif row in ['80 a 84 anos', '85 a 89 anos']:
        Faixa_etaria.append('80 a 89 anos')
    elif row in ['70 a 74 anos', '75 a 79 anos']:
        Faixa_etaria.append('70 a 79 anos')
    elif row in ['60 a 64 anos', '65 a 69 anos']:
        Faixa_etaria.append('60 a 69 anos')
    elif row in ['50 a 54 anos', '55 a 59 anos']:
        Faixa_etaria.append('50 a 59 anos')
    elif row in ['40 a 44 anos', '45 a 49 anos']:
        Faixa_etaria.append('40 a 49 anos')
    elif row in ['30 a 34 anos', '35 a 39 anos']:
        Faixa_etaria.append('30 a 39 anos')
    elif row in ['20 anos', '21 a 24 anos', '25 a 29 anos']:
        Faixa_etaria.append('20 a 29 anos')
    elif row in ['16 anos', '17 anos', '18 anos', '19 anos']:
        Faixa_etaria.append('16 a 19 anos')
    elif row in ['Inválido']:
        Faixa_etaria.append('nulo')
        
abs_2016_idade['idade'] = Faixa_etaria

abs_2016_idade_1 = abs_2016_idade[abs_2016_idade['turno'] == "1"]

abs_2016_idade_1 = abs_2016_idade_1.groupby(by='idade', as_index=False).sum()

abs_2016_idade_1['taxa_abstencao'] = 100*(abs_2016_idade_1['abstencao']/abs_2016_idade_1['total'])


# In[59]:


abs_2016_idade_1 = abs_2016_idade_1.sort_values(by=['taxa_abstencao'], ascending=False)
abs_2016_idade_1


# É possível notar que o ranking mudou um pouco. Para melhor visualizarmos, vamos criar alguns gráficos:

# In[60]:


abs_2020_idade_1.plot.bar(x='idade', y='taxa_abstencao')
plt.title('Taxa de abstenção nas eleições municipais de 2020')
plt.ylabel("% de abstenção")
plt.xlabel("Faixa etária")
plt.show()


# In[61]:


abs_2016_idade_1.plot.bar(x='idade', y='taxa_abstencao')
plt.title('Taxa de abstenção nas eleições municipais de 2016')
plt.ylabel("% de abstenção")
plt.xlabel("Faixa etária")
plt.show()


# As 4 primeiras faixas etárias do ranking de abstenção não apresentam grandes surpresas, já que é de se esperar que idosos entre 70 e 100+ anos deixem de ir votar (embora seja interessante notar que idosos com 100 anos ou mais compareçam mais às urnas do que aqueles entre 90 e 99 anos). A faixa etária dos 20 aos 29 anos apareceu em seguida (se ignorarmos os dados nulos) em ambos os anos, o que levanta uma ideia de pauta não relacionada à Covid: por que essa idade costuma deixar de votar com mais frequência que outras faixas? 
# 
# A faixa etária de 60 a 69 se ausentou mais em 2020 em comparação com 2016, o que é compreensível, já que eles fazem parte do grupo de risco. Talvez a grande surpresa venha dos jovens entre 16 e 19 anos, cuja taxa saltou de 12% para quase 22%. Por conta da idade, eles não fazem parte do grupo de risco. Será que eles adotaram o distanciamento social com mais afico que outros grupos? Eis uma questão que talvez mereça maior investigação. 
