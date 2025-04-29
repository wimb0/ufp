class BaseFormatter():
    """
    Base representation of a formatter
    """
    def __init__(self, entries, options):
        self.entries = entries
        self.options = options
        self.hostname_cache = {}

    def get_action_repr(self, parsed_line):
        if self.options.colorize:
            allow = '\u2705'
            block = '\u274C'
            limit = '\u2B55'
        else:
            allow = 'ALLOW'
            block = 'BLOCK'
            limit = 'LIMIT'

        if parsed_line.allowed():
            action = allow
        elif parsed_line.limited():
            action = limit
        else:
            action = block
          
        return action

    def format(self):
        raise NotImplemented
