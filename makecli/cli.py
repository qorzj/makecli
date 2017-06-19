import sys

__all__ = ["Cli", "CliError", "run", "error", "copy", "paste"]


def parse_arg_list(arg_list, fmt_index):
    p = q = 0
    while p < len(arg_list):
        arg = arg_list[p]
        if arg in fmt_index:
            fmt_node = fmt_index[arg]
            if fmt_node[2] == 'b':
                yield (fmt_node, True)
                p += 1
            else:
                if p + 1 >= len(arg_list): raise help()
                yield (fmt_node, arg_list[p + 1])
                p += 2
        else:
            if q not in fmt_index: raise help()
            fmt_node = fmt_index[q]
            q += 1
            yield (fmt_node, arg)
            p += 1


def extract_args(doc_lines, arg_list):
    fmt_index = {}
    arg_dict = {}
    p = 0
    for line in doc_lines:
        if not line: continue
        if ':' not in line: raise error('definition error: ' + line)
        left = line.rsplit(':', 1)[0].strip()
        if not left: raise error('definition error: ' + line)
        segs = left.split()
        if len(segs) > 3: raise error('definition error: ' + line)
        if segs[-1][0] == '<' and segs[-1][-1] == '>':  # '-a --b <c>', '-a <c>', '<c>'
            last_arg = segs.pop()
            if last_arg.endswith(':n>'):
                last_arg = last_arg.rsplit(':', 1)[0] + '>'
                arg_type = 'n'
            else:
                arg_type = 's'
        else:  # '-a --b', '-a'
            last_arg, arg_type = None, 'b'
        fmt_node = (tuple(segs), last_arg, arg_type)
        if segs:  # '-a --b <c>', '-a <c>', '-a --b', '-a'
            for seg in segs:
                fmt_index[seg] = fmt_node
                arg_dict[seg] = False
        else:  # '<c>'
            fmt_index[p] = fmt_node
            p += 1

        if last_arg:  # '-a --b <c>', '-a <c>', '<c>'
            arg_dict[last_arg] = False

    for (segs, last_arg, arg_type), value in parse_arg_list(arg_list, fmt_index):
        if arg_type == 'n': value = int(value)
        for seg in segs:
            arg_dict[seg] = value
        if last_arg:
            arg_dict[last_arg] = value

    return arg_dict


def getdoc(f):
    doc = f.__doc__
    if doc: return doc.strip()
    return f.__name__


class Cli:
    def __init__(self, overview):
        self.overview = overview
        self.workers = []

    def add(self, path, worker):
        assert isinstance(path, str), path
        segs = tuple(path.split()) if path.strip() else tuple()
        self.workers.append((segs, worker))
        return self

    def run(self):
        help_text = 'OVERVIEW\n  {}\n\nUSAGE\n'.format(self.overview) + ''.join(
                ['  %s\n\n' % getdoc(x[1]) for x in self.workers]) \
                + '  -h --help : for more information on a command.\n'
        arg_list = sys.argv[1:]
        if len(arg_list) == 1 and arg_list[0] in ('-h', '--help'):
            print(help_text)
            return
        self.workers.sort(reverse=True)
        try:
            for suffix_tuple, worker in self.workers:
                zip_tuple = list(zip(arg_list, suffix_tuple))
                if all(x[0] == x[1] for x in zip_tuple) and len(zip_tuple) == len(suffix_tuple):
                    doc_lines = getdoc(worker).splitlines()
                    arg_list = arg_list[len(suffix_tuple):]
                    arg_dict = extract_args(doc_lines[1:], arg_list)
                    worker(arg_dict)
                    break
            else:
                raise help()
        except CliError as e:
            if e.is_help:
                print(help_text)
            else:
                print('error: ' + e.message)


def help():
    return CliError(True, '-h --help for help')

def error(message):
    return CliError(False, message)

def copy(text):
    pass

def paste():
    pass


class CliError(Exception):
    def __init__(self, is_help, message):
        self.message = message
        self.is_help = is_help
