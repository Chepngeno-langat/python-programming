class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

x = int(input())
y = int(input())

x = x % y
x = x % y
y = y % x

print(y)