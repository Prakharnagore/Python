# Stack is a Last In First Out (LIFO) data structure.
browsing_session = []
browsing_session.append(1)
browsing_session.pop()
if not browsing_session:
    browsing_session[-1]
    print("redirect", browsing_session[-1])
print(browsing_session)
