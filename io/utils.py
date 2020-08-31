import os


class Utils(object):

    def print_file_name(self, file_path):
        file_names = os.listdir(file_path)
        for _name in file_names:
            _path = os.path.join(file_path, _name)
            if os.path.isdir(_path):
                self.print_file_name(_path)
            else:
                print(_path)


if __name__ == '__main__':
    file_path = '/Users/machao/work/inspur/product_support/projects'
    utils = Utils()
    utils.print_file_name(file_path)
