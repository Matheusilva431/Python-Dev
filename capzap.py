# Frontend -> usuário vê/interage
# Backend -> lógica por trás do site

# Titulo Capzap
# Botão iniciar o chat
    # Popup
        # Bem vindo ao Capzap
        # Escreve seu nome
        # Entrar no chat
# Chat
    # Matheus entrou no chat
    # Mensagens do usuário
# Campo para enviar mensagem
# Botão de enviar

import flet as ft

def main(pagina):
    
    nome_usuario = ft.TextField(label='Escreva seu nome')
    campo_mensagem = ft.TextField(label='Escreva sua mensagem aqui')
    chat = ft.Column()
    
    def enviar_mensagem_tunel(informacoes):
        # Colocar o nome do usuário na mensagem
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        
        pagina.pubsub.send_all(texto_campo_mensagem)
        # limpar o campo_mensagem
        campo_mensagem.value = ''
        pagina.update()
    
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    def entrar_chat(evento):        
        # Feche o popup
        popup.open = False
        # tire o botão 'Iniciar chat' da tela
        pagina.remove(botao_iniciar)
        # adicionar o nosso chat
        pagina.add(chat)
        # criar o campo de enviar mensagem
        # botão de enviar mensagem
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text('Bem vindo ao Capzap'),
        content=nome_usuario,
        actions=[ft.ElevatedButton('Entrar', on_click=entrar_chat)],
        )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    titulo = ft.Text('Capzap')
    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)


# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)
