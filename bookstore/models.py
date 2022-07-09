from django.contrib.auth.models import User
from django.db import models

# Create your models here.

books = [
    {
        'id': 1,
        'title': 'Python Crash Course',
        'released_year': 2016,
        'description': 'Python Crash Course is the world’s best-selling guide to the Python programming language. This fast-paced, '
                         'thorough introduction to programming with Python will have you writing programs, solving problems, and making '
                         'things that work in no time. '
                         'In the first half of the book, you’ll learn basic programming concepts, such as variables, lists, classes, and '
                         'loops, and practice writing clean code with exercises for each topic. You’ll also learn how to make your programs '
                         'interactive and test your code safely before adding it to a project. In the second half, you’ll put your new knowledge '
                         'into practice with three substantial projects: a Space Invaders–inspired arcade game, a set of data visualizations with Python’s '
                         'handy libraries, and a simple web app you can deploy online.',
        'book_cover': 'https://images-na.ssl-images-amazon.com/images/I/51j89lmxnpL._SX377_BO1,204,203,200_.jpg',
        'author_id': 1
    },
    {
        'id': 2,
        'title': 'Python Flash Cards: Syntax, Concepts, and Examples',
        'released_year': 2019,
        'description': 'These colorful programming study cards help new Python coders drill and reinforce the concepts, syntax, and terminology they\'ll '
                         'need to become successful professional programmers. '
                         'Keep your coding skills sharp on the go! Python Flash Cards take a tried-and-tested method and give it a programming makeover. '
                         'Eric Matthes, author of the best-selling Python Crash Course, distills essential Python programming knowledge into this 101-card '
                         'deck you can use anywhere. '
                         'Work through the deck in order or shuffle it up for a new study session every time. You can brush up foundational programming '
                         'principles and vocabulary like data structures, logical control, and program flow, quiz yourself on Python syntax, and test your '
                         'skills against exercises and challenges designed to keep you on your toes -- all in one sitting.',
        'book_cover': 'https://images-na.ssl-images-amazon.com/images/I/51OLKAbLIlL._SX373_BO1,204,203,200_.jpg',
        'author_id': 1
    },
    {
        'id': 3,
        'title': 'Automate the Boring Stuff with Python, 2nd Edition: Practical Programming',
        'released_year': 2019,
        'description': 'Learn how to code while you write programs that effortlessly perform useful feats of automation! '
                         'If you\'ve ever spent hours renaming files or updating spreadsheet cells, you know how tedious tasks like these can be. But what if '
                         'you could have your computer do them for you? Automate the Boring Stuff with Python, 2nd Edition teaches even the technically uninclined '
                         'how to write programs that do in minutes what would take hours to do by hand—no prior coding experience required! '
                         'This new, fully revised edition of Al Sweigart’s bestselling Pythonic classic, Automate the Boring Stuff with Python, covers all the '
                         'basics of Python 3 while exploring its rich library of modules for performing specific tasks, like scraping data off the Web, filling out forms, '
                         'renaming files, organizing folders, sending email responses, and merging, splitting, or encrypting PDFs. There’s also a brand-new chapter on input '
                         'validation, tutorials on automating Gmail and Google Sheets, tips on automatically updating CSV files, and other recent feats of automations that '
                         'improve your efficiency.',
        'book_cover': 'https://images-na.ssl-images-amazon.com/images/I/51B161E04DL._SX342_SY445_QL70_FMwebp_.jpg',
        'author_id': 2
    },
    {
        'id': 4,
        'title': 'Invent Your Own Computer Games with Python, 4th Edition',
        'released_year': 2016,
        'description': 'nvent Your Own Computer Games with Python will teach you how to make computer games using the popular Python programming language—even if you’ve never programmed before! '
                         'Begin by building classic games like Hangman, Guess the Number, and Tic-Tac-Toe, and then work your way up to more advanced games, like a text-based treasure hunting game '
                         'and an animated collision-dodging game with sound effects. Along the way, you’ll learn key programming and math concepts that will help you take your game programming to the next level.',
        'book_cover': 'https://m.media-amazon.com/images/P/B01MS66Y6M.01._SCLZZZZZZZ_SX500_.jpg',
        'author_id': 2
    },
    {
        'id': 5,
        'title': 'The Big Book of Small Python Projects: 81 Easy Practice Programs',
        'released_year': 2021,
        'description': 'Best-selling author Al Sweigart shows you how to easily build over 80 fun programs with minimal code and maximum creativity. '
                       'If you’ve mastered basic Python syntax and you’re ready to start writing programs, you’ll find The Big Book of Small Python Projects '
                       'both enlightening and fun. This collection of 81 Python projects will have you making digital art, games, animations, counting pro- grams, '
                       'and more right away. Once you see how the code works, you’ll practice re-creating the programs and experiment by adding your own custom touches. '
                       'These simple, text-based programs are 256 lines of code or less. And whether it’s a vintage screensaver, a snail-racing game, a clickbait headline '
                       'generator, or animated strands of DNA, each project is designed to be self-contained so you can easily share it online.',
        'book_cover': 'https://m.media-amazon.com/images/I/51eLNoOpXhL.jpg',
        'author_id': 2
    },
    {
        'id': 6,
        'title': 'Learning Python, 5th Edition',
        'released_year': 2013,
        'description': 'Get a comprehensive, in-depth introduction to the core Python language with this hands-on book. Based on author Mark Lutz’s popular training course, '
                       'this updated fifth edition will help you quickly write efficient, high-quality code with Python. It’s an ideal way to begin, whether you’re new to programming '
                       'or a professional developer versed in other languages. '
                       'Complete with quizzes, exercises, and helpful illustrations, this easy-to-follow, self-paced tutorial gets you started with both Python 2.7 and 3.3— the latest '
                       'releases in the 3.X and 2.X lines—plus all other releases in common use today. You’ll also learn some advanced language features that recently have become more common in Python code.',
        'book_cover': 'https://m.media-amazon.com/images/I/51ycFmfAeKL._SX260_.jpg',
        'author_id': 3
    },
    {
        'id': 7,
        'title': 'Programming Python: Powerful Object-Oriented Programming',
        'released_year': 2010,
        'description': 'If you\'ve mastered Python\'s fundamentals, you\'re ready to start using it to get real work done. Programming Python will show you how, with in-depth tutorials on the language\'s primary '
                       'application domains: system administration, GUIs, and the Web. You\'ll also explore how Python is used in databases, networking, front-end scripting layers, text processing, and more. '
                       'This book focuses on commonly used tools and libraries to give you a comprehensive understanding of Python’s many roles in practical, real-world programming. '
                       'You\'ll learn language syntax and programming techniques in a clear and concise manner, with lots of examples that illustrate both correct usage and common idioms. Completely updated for '
                       'version 3.x, Programming Python also delves into the language as a software development tool, with many code examples scaled specifically for that purpose.',
        'book_cover': 'https://m.media-amazon.com/images/I/51JBgWckUWL.jpg',
        'author_id': 3
    },
    {
        'id': 8,
        'title': 'Fluent Python: Clear, Concise, and Effective Programming ',
        'released_year': 2015,
        'description': 'Python’s simplicity lets you become productive quickly, but this often means you aren’t using everything it has to offer. With this hands-on guide, you’ll learn how to write effective, '
                       'idiomatic Python code by leveraging its best—and possibly most neglected—features. Author Luciano Ramalho takes you through Python’s core language features and libraries, and shows you '
                       'how to make your code shorter, faster, and more readable at the same time.'
                       'Many experienced programmers try to bend Python to fit patterns they learned from other languages, and never discover Python features outside of their experience. With this book, '
                       'those Python programmers will thoroughly learn how to become proficient in Python 3.',
        'book_cover': 'https://images-na.ssl-images-amazon.com/images/I/41R+fNX-akL._SX379_BO1,204,203,200_.jpg',
        'author_id': 4
    },
    {
        'id': 9,
        'title': 'Think Python: How to Think Like a Computer Scientist ',
        'released_year': 2015,
        'description': 'If you want to learn how to program, working with Python is an excellent way to start. This hands-on guide takes you through the language one step at a time, beginning with basic programming '
                       'concepts before moving on to functions, recursion, data structures, and object-oriented design.'
                       'Through exercises in each chapter, you’ll try out programming concepts as you learn them. Think Python is ideal for students at the high school or college level, as well as self-learners, '
                       'home-schooled students, and professionals who need to learn programming basics.',
        'book_cover': 'https://images-na.ssl-images-amazon.com/images/I/51yWKSfOcfS._SX379_BO1,204,203,200_.jpg',
        'author_id': 5
    },
    {
        'id': 10,
        'title': 'Modeling and Simulation in Python',
        'released_year': 2022,
        'description': 'Modeling and Simulation in Python teaches readers how to analyze real-world scenarios using the Python programming language, requiring no more than a background in high school math.'
                       'Modeling and Simulation in Python is a thorough but easy-to-follow introduction to physical modeling—that is, the art of describing and simulating real-world systems. Readers are guided '
                       'through modeling things like world population growth, infectious disease, bungee jumping, baseball flight trajectories, celestial mechanics, and more while simultaneously developing a '
                       'strong understanding of fundamental programming concepts like loops, vectors, and functions.',
        'book_cover': 'https://m.media-amazon.com/images/I/51s6KBaWslL.jpg',
        'author_id': 5
    },
]

authors = [
    {
        'id': 1,
        'first_name': 'Eric',
        'last_name': 'Matthes',
        'age': 50
    },
    {
        'id': 2,
        'first_name': 'Al',
        'last_name': 'Sweigart',
        'age': 36
    },
    {
        'id': 3,
        'first_name': 'Mark',
        'last_name': 'Lutz',
        'age': 45
    },
    {
        'id': 4,
        'first_name': 'Luciano',
        'last_name': 'Ramalho',
        'age': 59
    },
    {
        'id': 5,
        'first_name': 'Allen',
        'last_name': 'Downey',
        'age': 55
    },
]


class Authors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    @staticmethod
    def create_authors():
        for i in authors:
            author = Authors(first_name=i['first_name'], last_name=i['last_name'], age=i['age'])
            author.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name }"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Books(models.Model):
    title = models.CharField(max_length=100)
    released_year = models.PositiveIntegerField()
    description = models.TextField()
    book_cover = models.CharField(max_length=150)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, blank=True, null=True)

    @staticmethod
    def create_books():
        for i in books:
            book = Books(title=i['title'], released_year=i['released_year'], description=i['description'], book_cover=i['book_cover'], author_id=i['author_id'])
            book.save()

    def __str__(self):
        return f"{self.title} {self.author}"

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Comments(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.body} {self.author}"
