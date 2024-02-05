from main15 import app, Message


with app.app_context():
    all_messages = Message.query.all()
    print(all_messages)

    #  [Jonas - jonas@mail.com, Antanas - antanas@mail.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]
    message_1 = Message.query.get(1)
    print(message_1)

    # Jonas - jonas@mail.com
    message_antanas = Message.query.filter_by(name="Antanas").all()
    print(message_antanas[0].message)


