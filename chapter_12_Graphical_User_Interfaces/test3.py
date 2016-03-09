def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()


def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue())
    file.close()
