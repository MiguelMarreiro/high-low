from flask import Flask
import random

app = Flask(__name__)

target_number = random.randint(0,9)
print(target_number)
@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Guess a number between 0 and 9</h1>'
            '<img style="display: block; margin-left: auto;margin-right: auto;width: 40%;"'
            'src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"> ')


@app.route("/<int:number>")
def output(number):
    if number > target_number:
        return ('<h1 style="text-align: center">Too High!</h1>'
            '<img style="display: block; margin-left: auto;margin-right: auto;width: 40%;"'
            'src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmRyM2lxaDkxZHk0enU1ZGE0ODdpY240ZHM2NDUza3RiazFnNjl3YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UHDB3gcgTHKotMQHiA/giphy.webp"> ')
    elif number < target_number:
        return ('<h1 style="text-align: center">Too Low</h1>'
            '<div style="display: block; margin-left: auto;margin-right: auto;width: 27%;">'
                '<iframe allow="fullscreen" frameBorder="0" height="853" '
                'src="https://giphy.com/embed/wHg7wvRUSzSVYYTftC/video" width="480"></iframe></div>')
    else:
        global target_number
        target_number = random.randint(0, 9)
        return ('<h1 style="text-align: center">Guess a number between 0 and 9</h1>'
            '<img style="display: block; margin-left: auto;margin-right: auto;width: 40%;"'
            'src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTN5Z3c4enV4aHJiaGdxMnExdzMwaDVvOHE4OXN1dDNycG0zcmhqeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kZqbBT64ECtjy/giphy.webp"> ')


if __name__ == '__main__':
    app.run(debug=True)