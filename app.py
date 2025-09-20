
# # # !pip install flask
# # from flask import Flask ,redirect ,url_for


# # app = Flask(__name__)

# # @app.route("/")
# # def home():
# #     return "<h1> Welcome To Home </h1>"

# # @app.route("/courses")
# # def courses():
# #     return "<h1>Welcome To The Courses </h1>"

# # ### dynamic routing
# # #it shows what is typed in url

# @app.route('/<name>')
# def name(name):
#     return f"<h1> Hello {name} </h1>"

# # #redirect url means by clicking on link and it directs to another link

# # @app.route("/admin")
# # def admin():
# #     return redirect("/")

# # #by using url_for we can mention function name to change the address

# # @app.route("/adam")
# # def adam():
# #     return redirect(url_for("home"))

# # # @app.route
# # if __name__ == '__main__':      
# #     app.run(debug = True)
# # ----------------------------------------------
# # from flask import Flask ,render_template

# # app=Flask(__name__)

# # @app.route("/")
# # def home():
# #     return render_template("home.html", content = ['ML' , 'DL' , 'OC','NUMPY','PANDAS'])
# # # @app.route("/index")
# # # def index():
# # #     return render_template("index.html")

# # if __name__=="__main__":
# #     app.run(debug=True)



# # from flask import Flask ,redirect ,render_template ,url_for

# # app = Flask(__name__)

# # @app.route("/")
# # def name():
# #     return "<h1>My Name is MAHESH</h1>"

# # @app.route("/name")
# # def home():
# #     return render_template("home.html")

# # @app.route("/login", methods = ["GET" , "POST"])
# # def login():
# #     return render_template("index.html")


# # if __name__ =="__main__":
# #     app.run(debug = True)

# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Sample data
# books = [
#     {"id": 1, "title": "Concept of Physics", "author": "H.C Verma"},
#     {"id": 2, "title": "Gunahon ka Devta", "author": "Dharamvir Bharti"},
#     {"id": 3, "title": "Problems in General Physsics", "author": "I.E Irodov"}
# ]

# # Get all books
# @app.route('/books', methods=['GET'])
# def get_books():
#     return jsonify(books)

# # Get a single book by ID
# @app.route('/books/<int:book_id>', methods=['GET'])
# def get_book(book_id):
#     book = next((book for book in books if book["id"] == book_id), None)
#     return jsonify(book) if book else (jsonify({"error": "Book not found"}), 404)

# # Add a new book
# @app.route('/books', methods=['POST'])
# def add_book():
#     new_book = request.json
#     books.append(new_book)
#     return jsonify(new_book), 201

# # Update a book
# @app.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     book = next((book for book in books if book["id"] == book_id), None)
#     if not book:
#         return jsonify({"error": "Book not found"}), 404

#     data = request.json
#     book.update(data)
#     return jsonify(book)

# # Delete a book
# @app.route('/books/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     global books
#     books = [book for book in books if book["id"] != book_id]
#     return jsonify({"message": "Book deleted"})

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask ,jsonify ,request

# app=Flask(__name__)

# books=[
#     {"id": 1,"title":"concept of physics","author":"Mahesh"},
#     {"id": 2, "title": "Radio Frequency","author":"Kalyan"},
#     {"id" : 3 ,"title" : "VLSI","author":"Leenu"}
# from flask import Flask, jsonify, request

# app = Flask(__name__)

# books = [
#     {"id": 1, "title": "Concept of Physics", "author": "Mahesh"},
#     {"id": 2, "title": "Radio Frequency", "author": "Kalyan"},
#     {"id": 3, "title": "VLSI", "author": "Leenu"}
# ]

# @app.route("/", methods=["GET"])
# def name():
#     b = [book for book in books if book["id"] == 1]  # filter book with id=2
#     return jsonify(b) if b else (jsonify({"message": "not found"}), 404)

# if __name__ == "__main__":
#     app.run(debug=True)


# @app.route("/books",methods = ["GET"])
# def get_books():
#     return jsonify(books)

# @app.route("/books/<int:book_id>" ,methods=["get"])
# def get_book(book_id):
#     book=next((book for book in books if book ["id"] == book_id),None)
#     return jsonify(book) if book else (jsonify({"error":"Book Not Found"}),404)

# @app.route("/books",methods = ["POST"])
# def add_book():
#     new_book = request.json
#     # print("books")
#     books.append(new_book)
#     return jsonify(new_book)

# @app.route("/",methods = ["GET"])
# def name():
#     b=[ b for b in books if books["id"] == 2]
#     return  jsonify(b) if books_id == 2 else (jsonify ({"not found"}),404)

# @app.route("/books", methods = ["update"])
# def update_books():


# if __name__ == "__main__":
#     app.run(debug = True)

#//////// FLASK OPERATIONS//////////#




# from flask import Flask ,jsonify ,render_template ,request

# app=Flask(__name__)

# @app.route("/")
# def nam():
#     return "<h1> HI TO ALL </h1>.center()"


# @app.route("/<username>")
# def show_name(username):
#     return f"I AM A SUPER STAR {username}"


# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask

app=Flask(__name__)

@app.route("/")
def f1():
    return "<h1> PLEASE ENTER THE NAME </h1>" \
    "<h2> I'AM MAHESH </h2>"\
    "<h4> GOOD MORNING EVERYONE </h4>"


@app.route("/students",methods = ["GET","POST"])
def student():
    # return ("<span><b> NAME </b>: MAHESH</span><br>"\
    # "<span> <b> BRANCH </b> : ECT</span><br>"\
    # "<span> <b>RESULT </b> : PASS</span>"
    # )


    return "MAHESH"
# @app.route("/students")
# def stud():
#     return "Mahesh"
    

if __name__ == "__main__":
    app.run(debug=True)
