

def discovery_fs(root_dir, indent_level=1):
    import os

    for name in os.listdir(root_dir):
        if not name.startswith('.'):
            try:
                path = os.path.join(root_dir, name)
                prefix = indent_level * (' ' * 4)
                if os.path.isfile(path):
                    print('{prefix} ({size} bytes)'.format(prefix=prefix + '|__ ' + name,
                                                           size=os.path.getsize(path)))
                else:
                    print(prefix + name + ':')
                    discovery_fs(path, indent_level + 1)
            except Exception as ex:
                print(ex)


discovery_fs("C:\\Users\\Class5-Pc10\\Documents\\frontend-basic_17.07.2020")
