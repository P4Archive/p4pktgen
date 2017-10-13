from enum import Enum

TransitionType = Enum('TransitionType',
                      'PARSER_OP_TRANSITION ACTION_TRANSITION BOOL_TRANSITION')


class Transition(object):
    def __init__(self, transition_type, src, dest):
        self.transition_type = transition_type
        self.src = src
        self.dest = dest


class ParserOpTransition(Transition):
    def __init__(self, op_idx, next_state):
        super(ParserOpTransition,
              self).__init__(TransitionType.PARSER_OP_TRANSITION, None, None)
        self.op_idx = op_idx
        self.next_state = next_state


class ActionTransition(Transition):
    def __init__(self, src, dest, action):
        super(ActionTransition,
              self).__init__(TransitionType.ACTION_TRANSITION, src, dest)
        self.action = action

    def get_name(self):
        return self.action.name

    def __repr__(self):
        # XXX: better output (will need to change test cases)
        return 'u\'{}\''.format(self.action.name)

    def __eq__(self, other):
        return self.action.name == str(other)

    def __hash__(self):
        return hash(self.action.name)


class BoolTransition(Transition):
    def __init__(self, src, dest, val, source_info):
        super(BoolTransition, self).__init__(TransitionType.BOOL_TRANSITION,
                                             src, dest)
        assert isinstance(val, bool)
        self.val = val
        self.source_info = source_info

    def __repr__(self):
        # XXX: hack for test cases
        return '({}, {})'.format(self.val, self.source_info)

    def __eq__(self, other):
        return (self.val, (self.source_info.filename, self.source_info.line,
                           self.source_info.source_fragment)) == other

    def __hash__(self):
        # XXX: hack for test cases
        return hash((self.val, self.source_info))