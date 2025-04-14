import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def save_plot(fig, filename):
    os.makedirs("outputs/plots", exist_ok=True)
    fig.savefig(f"outputs/plots/{filename}", bbox_inches="tight")
    plt.close(fig)

def plot_assinatura_vs_cancelamento(df):
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="assinatura", hue="cancelou", ax=ax)
    ax.set_title("Assinatura vs Cancelamento")
    save_plot(fig, "assinatura_vs_cancelamento.png")

def plot_sexo_vs_cancelamento(df):
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="sexo", hue="cancelou", ax=ax)
    ax.set_title("Sexo vs Cancelamento")
    save_plot(fig, "sexo_vs_cancelamento.png")

def plot_idade_vs_cancelamento(df):
    fig, ax = plt.subplots()
    sns.histplot(data=df, x="idade", hue="cancelou", kde=True, multiple="stack", ax=ax)
    ax.set_title("Distribuição da Idade vs Cancelamento")
    save_plot(fig, "idade_vs_cancelamento.png")

def plot_callcenter_vs_cancelamento(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="cancelou", y="ligacoes_callcenter", ax=ax)
    ax.set_title("Ligações para o Call Center vs Cancelamento")
    save_plot(fig, "callcenter_vs_cancelamento.png")

def plot_dias_atraso_vs_cancelamento(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="cancelou", y="dias_atraso", ax=ax)
    ax.set_title("Dias de Atraso vs Cancelamento")
    save_plot(fig, "dias_atraso_vs_cancelamento.png")

def gerar_todos_os_graficos(df):
    plot_assinatura_vs_cancelamento(df)
    plot_sexo_vs_cancelamento(df)
    plot_idade_vs_cancelamento(df)
    plot_callcenter_vs_cancelamento(df)
    plot_dias_atraso_vs_cancelamento(df)
