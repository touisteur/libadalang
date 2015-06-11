from langkit.parsers import Grammar
from langkit.compiled_types import abstract, ASTNode

ada_grammar = Grammar()
A = ada_grammar
ada_grammar.main_rule_name = "compilation_unit"


@abstract
class AdaNode(ASTNode):
    """
    Root node class for the Ada grammar. This is good and necessary for several
    reasons:

    1. It will facilitate the sharing of langkit_support code if we ever have
       two libraries generated by LanguageKit in the same application
    2. It allows to insert code specific to the ada root node, without
       polluting every LanguageKit node, and without bringing back the root
       ASTNode in the code templates.
    """
    pass