import ast
import math
import operator


def are_elements_numbers(l: list[str]) -> bool:
    for x in l:
        try:
            float(x)
        except ValueError:
            return False
    return True

def construct_string(l: list[str | list]) -> str:
    return ''.join([construct_string(x) if type(x) is list else x for x in l])



class SafeEval(ast.NodeVisitor):
    def __init__(self, env: dict):
        self.env = env
        self.OPS = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.USub: operator.neg
        }
        self.ALLOWED_FUNCTIONS = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "max": max,
            "min": min,
        }

    def visit_Module(self, node):
        for stmt in node.body:
            self.visit(stmt)

    def visit_Expr(self, node):
        return self.visit(node.value)

    def visit_Assign(self, node):
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            raise ValueError("Invalid assignment")
        name = node.targets[0].id
        self.env['vars'][name] = self.visit(node.value)

    def visit_Num(self, node):
        return node.value

    def visit_Name(self, node):
        if node.id not in self.env['whitelist'] and node.id not in self.env['vars']:
            raise NameError(f"Undefined variable '{node.id}'")
        return self.env['whitelist'][node.id] if node.id in self.env['whitelist'] else self.env['vars'][node.id]

    def visit_Attribute(self, node):
        if type(node.value) is not ast.Name:
            raise ValueError('Attribute should be called from a Name')
        if node.value.id not in self.env['vars']:
            raise ValueError(f'Class {node.value.id} cannot be called')
        if 'attrs' in self.env.keys() and node.attr in self.env['attrs']:
            return getattr(self.env['vars'][node.value.id], node.attr)
        else:
            raise ValueError(f'Attribute {node.attr} cannot be called')

    def visit_UnaryOp(self, node):
        if type(node.op) in [ast.Not, ast.Invert, ast.UAdd]:
            raise ValueError(f'Operator {type(node.op).__name__} is not allowed')
        return operator.neg(self.visit(node.operand))

    def visit_BinOp(self, node):
        if type(node.op) not in self.OPS.keys():
            raise ValueError("Operation not allowed")
        return self.OPS[type(node.op)](self.visit(node.left), self.visit(node.right))

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            method = node.func.attr
            if method not in self.env['whitelist']:
                raise ValueError(f"Method {method} not allowed")
            if method in self.env['whitelist'] and isinstance(self.visit(node.func.value), self.env['class']):
                args = [self.visit(arg) for arg in node.args]
                if type(node.func.value) is ast.Name and node.func.value.id in self.env['vars']:
                    return getattr(self.env['vars'][node.func.value.id], method)(*args)
                else:
                    return getattr(self.visit(node.func.value), method)(*args)

            else:
                raise ValueError(f'{method} cannot be called from {type(self.visit(node.func.value)).__name__}')

        elif isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name not in self.ALLOWED_FUNCTIONS:
                raise ValueError(f"Function '{func_name}' is not allowed")

            args = [self.visit(arg) for arg in node.args]
            return self.ALLOWED_FUNCTIONS[func_name](*args)
        else:
            raise ValueError('Call not allowed.')

    def generic_visit(self, node):
        raise ValueError(f"Disallowed syntax: {type(node).__name__}")

def safe_eval(code: str, env=None):
    if env is None:
        env = {}
    tree = ast.parse(code)
    evaluator = SafeEval(env)
    evaluator.visit(tree)
    try:
        ast.parse(code, mode='eval')
    except SyntaxError:
        exec(code, evaluator.env['vars'])
        return None, evaluator.env
    else:
        return eval(code, evaluator.env['vars']), evaluator.env
