import customtkinter as ctk
ctk.set_appearance_mode('dark')

def calculo_liberdade():
    try:
        patrimonio_inicial = float(campo_botaopatri.get())
        aporte_mensal = float(campo_botaosala.get())
        taxa_anual = float(campo_botaojuros.get())
        anos = int(campo_botaotempo.get())
        
        i = (taxa_anual / 100) / 12
        n = anos * 12
        
        parte1 = patrimonio_inicial * (1 + i)**n
        
        parte2 = aporte_mensal * (((1 + i)**n - 1) / i)
        
        total = parte1 + parte2
        
        calculo.configure(text=f"Total acumulado: R$ {total:,.2f}")
        
    except ValueError:
        calculo.configure(text="Erro: Preencha todos os campos com números!")
    except ZeroDivisionError:
        calculo.configure(text="A taxa de juros não pode ser zero!")

app = ctk.CTk()
app.title('Calculadora')
app.geometry('400x400')

campo_salario = ctk.CTkLabel(app,text='Aporte Mensal')
campo_salario.pack(pady=5)

campo_botaosala = ctk.CTkEntry(app,placeholder_text='Digite seu Aporte')
campo_botaosala.pack(pady=5)

campo_patrimonio = ctk.CTkLabel(app,text='Patrimônio Investido')
campo_patrimonio.pack(pady=5)

campo_botaopatri = ctk.CTkEntry(app,placeholder_text='Digite seu patrimonio')
campo_botaopatri.pack(pady=5)

campo_taxadejuros = ctk.CTkLabel(app,text='Taxa de juros (Anual)')
campo_taxadejuros.pack(pady=5)

campo_botaojuros = ctk.CTkEntry(app,placeholder_text='Taxa de juros')
campo_botaojuros.pack(pady=5)

campo_tempo = ctk.CTkLabel(app,text='Tempo de investimento (Anos)')
campo_tempo.pack(pady=5)

campo_botaotempo = ctk.CTkEntry(app,placeholder_text='Tempo investido')
campo_botaotempo.pack(pady=5)




botao = ctk.CTkButton(app,text='Calcular',command=calculo_liberdade)
botao.pack(pady=20)

calculo = ctk.CTkLabel(app,text='')
calculo.pack(pady=10)

app.mainloop()
