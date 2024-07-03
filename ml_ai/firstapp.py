import gradio as gr
import random
import time


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


def echo(msg, hist):
    print("history, ", hist)
    time.sleep(.05)
    if 'hello' in msg:
        return f'Hiiee{msg}'
    else:
        return "Say hello"

demo = gr.ChatInterface(
    fn=echo,
    examples=["hello"],
    title="Echo chatbox",
    retry_btn=None
)

demo.launch()
