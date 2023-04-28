from flask import Flask, render_template, redirect, request, make_response
from flask_login import login_user, LoginManager, login_required, logout_user

from forms.LoginForm import LoginForm
from forms.MainForm import MainForm
from forms.user import RegisterForm
from data import db_session
from data.users import User

import MainClass

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

words = ['avito', 'slando', 'ebay', 'instagram', 'yandex', 'google', 'yahoo', 'skype', 'torrent', 'nvidia',
                      'intel', 'cortana', 'siri', 'amazon', 'comodo', 'java', 'nigma', 'adobe', 'viber', 'ubuntu',
                      'samsung',
                      'xiaomi', 'philips', 'yamaha', 'honda', 'nestle', 'vimeo', 'chevrolet', 'tesla', 'paypal',
                      'epsom',
                      'canon', 'slack', 'disney', 'telegram', 'fornex', 'punto', 'flux', 'aveo', 'amway', 'avon',
                      'panasonic',
                      'lego', 'oracle', 'logitech', 'siemens', 'nokia', 'twitter', 'feedly', 'wiki', 'asus', 'acer',
                      'sony',
                      'xperia', 'nike', 'reebok', 'beeline', 'megafon', 'casio', 'nikon', 'pentium', 'xeon', 'realtec',
                      'hennessy', 'iphone', 'phantom', 'tissot', 'rayban', 'omega', 'polaroid', 'dexp', 'demix', 'audi',
                      'vesta', 'lada', 'cherry', 'apple', 'ford', 'ardo', 'arduino', 'zelmer', 'toshiba', 'rolsen',
                      'sharp',
                      'spersy', 'nintendo', 'tetris', 'trikolor', 'сyrix', 'maxtor', 'hitachi', 'garmin', 'transcend',
                      'symantec', 'explay', 'rover', 'dirol', 'ordit', 'fanta', 'sprite', 'cola', 'mirinda', 'jacobs',
                      'lipton', 'marvel', 'ergotron', 'microsoft', 'sega', 'dendy', 'galaxy', 'ariel', 'lenor', 'mars',
                      'twix', 'snikers', 'bounty', 'picnic', 'mercedes', 'ferrari', 'lamborghini', 'porsche', 'lexus',
                      'toyota', 'renova', 'rexona', 'linux', 'angular', 'react', 'prisma', 'shazam', 'yota', 'retrica',
                      'lamoda', 'qiwi', 'rovio', 'drom', 'djin', 'fingerprint', 'doodle', 'sothebys', 'alibaba',
                      'dadata',
                      'whiskas', 'kinder', 'motorola', 'boeing', 'toster', 'laravel', 'symfony', 'zendesk', 'python',
                      'dropbox', 'valve', 'voximplant', 'selectel', 'jino', 'ucoz', 'kvant', 'priora', 'granta', 'niva',
                      'adwords', 'adsense', 'webmoney', 'guzzle', 'simpex', 'joomla', 'next', 'driver', 'perhaps',
                      'flower',
                      'cartoon', 'music', 'hacker', 'within', 'never', 'jeans', 'river', 'cucumber', 'waterful',
                      'mirror',
                      'forest', 'wireless', 'happyness', 'women', 'start', 'victim', 'excite', 'pleasure', 'pressure',
                      'dragon',
                      'fire', 'criminal', 'introduce', 'square', 'hesitate', 'life', 'company', 'fish', 'trand',
                      'brand',
                      'download', 'school', 'nonsence', 'vertex', 'lead', 'feeling', 'woody', 'trash', 'hotel',
                      'basket',
                      'triple', 'clock', 'mother', 'wind', 'channel', 'dollar', 'motherland', 'carrot', 'wave', 'table',
                      'sunny', 'crecker', 'paper', 'feedback', 'double', 'hostel', 'harmony', 'impossible', 'truth',
                      'figure',
                      'kitchen', 'holiday', 'wonderful', 'below', 'afternoon', 'mommy', 'granny', 'mayflower', 'green',
                      'animal', 'family', 'agreement', 'football', 'moon', 'danger', 'stranger', 'alien', 'shape',
                      'heart',
                      'englishman', 'citizen', 'trace', 'chance', 'icecream', 'cheesecake', 'fairytail', 'potato',
                      'tomato',
                      'expensive', 'forewer', 'together', 'air', 'between', 'lesson', 'smile', 'turbulence', 'sure',
                      'famous',
                      'beach', 'strawberry', 'cherry', 'sugar', 'pepper', 'popcorn', 'simple', 'perfect', 'candy',
                      'memorize',
                      'remember', 'lollypop', 'pool', 'humor', 'drugs', 'about', 'butterfly', 'cock', 'yellow',
                      'perfomance',
                      'public', 'online', 'present', 'childhood', 'rainbow', 'office', 'style', 'godless', 'teeth',
                      'string',
                      'bycicle', 'twice', 'week', 'today', 'tomorrow', 'after', 'dinner', 'currency', 'earth', 'winner',
                      'looser', 'handsome', 'killer', 'baby', 'ready', 'baloon', 'track', 'tablet', 'high', 'level',
                      'village',
                      'center', 'travel', 'taking', 'swimming', 'dream', 'cheater', 'winter', 'bubble', 'russian',
                      'olimpic',
                      'honor', 'golden', 'better', 'attempts', 'mouse', 'mikki', 'anyone', 'happened', 'nothing',
                      'rings',
                      'filter', 'silver', 'monster', 'capital', 'anothet', 'champion', 'runner', 'direct', 'second',
                      'floor',
                      'ocean', 'international',
                      ]

def main():
    db_session.global_init("db/blogs.db")
    app.run()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/", methods=['GET', 'POST'])
def index():

    # Cookies
    cookies_MinLenWord = int(request.cookies.get("ck_MinLenWord", 1))
    cookies_MaxLenWord = int(request.cookies.get("ck_MaxLenWord", 1))
    cookies_Population = int(request.cookies.get("ck_Population", 1))
    cookies_Mutation = int(request.cookies.get("ck_Mutation", 1))

    form = MainForm()
    if form.validate_on_submit():
        print("Submit" if form.submit.data else "Erase")
        if form.submit.data:
            a = MainClass.RandomGen(int(form.min_len_word.data), int(form.max_len_word.data), int(form.population.data),
                                    list(form.Area.data.split("\n")))
            a.Start()
            adw = ''
            for key, val in a.Population().items():
                adw += str(key) + " - " + str(val) + "\n"
            form.Area_out.data = adw

            res = make_response(render_template('form.html', form=form))

            # Cookies
            res.set_cookie("ck_MinLenWord", str(form.min_len_word.data), max_age=60 * 60 * 24 * 365 * 2)
            res.set_cookie("ck_MaxLenWord", str(form.max_len_word.data), max_age=60 * 60 * 24 * 365 * 2)
            res.set_cookie("ck_Population", str(form.population.data), max_age=60 * 60 * 24 * 365 * 2)
            res.set_cookie("ck_Mutation", str(form.mutation.data), max_age=60 * 60 * 24 * 365 * 2)

            return res
        else:
            form.Area_out.data = ""
            return render_template('form.html', form=form)
    l = ''
    for i in words:
        l += i + "\n"

    # Cookies
    form.min_len_word.data = cookies_MinLenWord
    form.max_len_word.data = cookies_MaxLenWord
    form.population.data = cookies_Population
    form.mutation.data = cookies_Mutation

    form.Area.data = l

    return render_template('form.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()
