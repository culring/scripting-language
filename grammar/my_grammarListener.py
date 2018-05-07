# Generated from my_grammar.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .my_grammarParser import my_grammarParser
else:
    from my_grammarParser import my_grammarParser

# This class defines a complete listener for a parse tree produced by my_grammarParser.
class my_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by my_grammarParser#script.
    def enterScript(self, ctx:my_grammarParser.ScriptContext):
        pass

    # Exit a parse tree produced by my_grammarParser#script.
    def exitScript(self, ctx:my_grammarParser.ScriptContext):
        pass


    # Enter a parse tree produced by my_grammarParser#basic_list.
    def enterBasic_list(self, ctx:my_grammarParser.Basic_listContext):
        pass

    # Exit a parse tree produced by my_grammarParser#basic_list.
    def exitBasic_list(self, ctx:my_grammarParser.Basic_listContext):
        pass


    # Enter a parse tree produced by my_grammarParser#by_slice_list.
    def enterBy_slice_list(self, ctx:my_grammarParser.By_slice_listContext):
        pass

    # Exit a parse tree produced by my_grammarParser#by_slice_list.
    def exitBy_slice_list(self, ctx:my_grammarParser.By_slice_listContext):
        pass


    # Enter a parse tree produced by my_grammarParser#comparator.
    def enterComparator(self, ctx:my_grammarParser.ComparatorContext):
        pass

    # Exit a parse tree produced by my_grammarParser#comparator.
    def exitComparator(self, ctx:my_grammarParser.ComparatorContext):
        pass


    # Enter a parse tree produced by my_grammarParser#or_test.
    def enterOr_test(self, ctx:my_grammarParser.Or_testContext):
        pass

    # Exit a parse tree produced by my_grammarParser#or_test.
    def exitOr_test(self, ctx:my_grammarParser.Or_testContext):
        pass


    # Enter a parse tree produced by my_grammarParser#and_test.
    def enterAnd_test(self, ctx:my_grammarParser.And_testContext):
        pass

    # Exit a parse tree produced by my_grammarParser#and_test.
    def exitAnd_test(self, ctx:my_grammarParser.And_testContext):
        pass


    # Enter a parse tree produced by my_grammarParser#not_test.
    def enterNot_test(self, ctx:my_grammarParser.Not_testContext):
        pass

    # Exit a parse tree produced by my_grammarParser#not_test.
    def exitNot_test(self, ctx:my_grammarParser.Not_testContext):
        pass


    # Enter a parse tree produced by my_grammarParser#comparison.
    def enterComparison(self, ctx:my_grammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by my_grammarParser#comparison.
    def exitComparison(self, ctx:my_grammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by my_grammarParser#number.
    def enterNumber(self, ctx:my_grammarParser.NumberContext):
        pass

    # Exit a parse tree produced by my_grammarParser#number.
    def exitNumber(self, ctx:my_grammarParser.NumberContext):
        pass


    # Enter a parse tree produced by my_grammarParser#simple_literal.
    def enterSimple_literal(self, ctx:my_grammarParser.Simple_literalContext):
        pass

    # Exit a parse tree produced by my_grammarParser#simple_literal.
    def exitSimple_literal(self, ctx:my_grammarParser.Simple_literalContext):
        pass


    # Enter a parse tree produced by my_grammarParser#parameter_set_stmt.
    def enterParameter_set_stmt(self, ctx:my_grammarParser.Parameter_set_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#parameter_set_stmt.
    def exitParameter_set_stmt(self, ctx:my_grammarParser.Parameter_set_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#where_expr.
    def enterWhere_expr(self, ctx:my_grammarParser.Where_exprContext):
        pass

    # Exit a parse tree produced by my_grammarParser#where_expr.
    def exitWhere_expr(self, ctx:my_grammarParser.Where_exprContext):
        pass


    # Enter a parse tree produced by my_grammarParser#simple_lambda.
    def enterSimple_lambda(self, ctx:my_grammarParser.Simple_lambdaContext):
        pass

    # Exit a parse tree produced by my_grammarParser#simple_lambda.
    def exitSimple_lambda(self, ctx:my_grammarParser.Simple_lambdaContext):
        pass


    # Enter a parse tree produced by my_grammarParser#assignment.
    def enterAssignment(self, ctx:my_grammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by my_grammarParser#assignment.
    def exitAssignment(self, ctx:my_grammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by my_grammarParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:my_grammarParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:my_grammarParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#assignment_suite.
    def enterAssignment_suite(self, ctx:my_grammarParser.Assignment_suiteContext):
        pass

    # Exit a parse tree produced by my_grammarParser#assignment_suite.
    def exitAssignment_suite(self, ctx:my_grammarParser.Assignment_suiteContext):
        pass


    # Enter a parse tree produced by my_grammarParser#where_assignment.
    def enterWhere_assignment(self, ctx:my_grammarParser.Where_assignmentContext):
        pass

    # Exit a parse tree produced by my_grammarParser#where_assignment.
    def exitWhere_assignment(self, ctx:my_grammarParser.Where_assignmentContext):
        pass


    # Enter a parse tree produced by my_grammarParser#where_assignemnt_stmt.
    def enterWhere_assignemnt_stmt(self, ctx:my_grammarParser.Where_assignemnt_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#where_assignemnt_stmt.
    def exitWhere_assignemnt_stmt(self, ctx:my_grammarParser.Where_assignemnt_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#parameter_set_suite.
    def enterParameter_set_suite(self, ctx:my_grammarParser.Parameter_set_suiteContext):
        pass

    # Exit a parse tree produced by my_grammarParser#parameter_set_suite.
    def exitParameter_set_suite(self, ctx:my_grammarParser.Parameter_set_suiteContext):
        pass


    # Enter a parse tree produced by my_grammarParser#expr.
    def enterExpr(self, ctx:my_grammarParser.ExprContext):
        pass

    # Exit a parse tree produced by my_grammarParser#expr.
    def exitExpr(self, ctx:my_grammarParser.ExprContext):
        pass


    # Enter a parse tree produced by my_grammarParser#term.
    def enterTerm(self, ctx:my_grammarParser.TermContext):
        pass

    # Exit a parse tree produced by my_grammarParser#term.
    def exitTerm(self, ctx:my_grammarParser.TermContext):
        pass


    # Enter a parse tree produced by my_grammarParser#factor.
    def enterFactor(self, ctx:my_grammarParser.FactorContext):
        pass

    # Exit a parse tree produced by my_grammarParser#factor.
    def exitFactor(self, ctx:my_grammarParser.FactorContext):
        pass


    # Enter a parse tree produced by my_grammarParser#power.
    def enterPower(self, ctx:my_grammarParser.PowerContext):
        pass

    # Exit a parse tree produced by my_grammarParser#power.
    def exitPower(self, ctx:my_grammarParser.PowerContext):
        pass


    # Enter a parse tree produced by my_grammarParser#atom_expr.
    def enterAtom_expr(self, ctx:my_grammarParser.Atom_exprContext):
        pass

    # Exit a parse tree produced by my_grammarParser#atom_expr.
    def exitAtom_expr(self, ctx:my_grammarParser.Atom_exprContext):
        pass


    # Enter a parse tree produced by my_grammarParser#atom.
    def enterAtom(self, ctx:my_grammarParser.AtomContext):
        pass

    # Exit a parse tree produced by my_grammarParser#atom.
    def exitAtom(self, ctx:my_grammarParser.AtomContext):
        pass


    # Enter a parse tree produced by my_grammarParser#trailer.
    def enterTrailer(self, ctx:my_grammarParser.TrailerContext):
        pass

    # Exit a parse tree produced by my_grammarParser#trailer.
    def exitTrailer(self, ctx:my_grammarParser.TrailerContext):
        pass


    # Enter a parse tree produced by my_grammarParser#arglist.
    def enterArglist(self, ctx:my_grammarParser.ArglistContext):
        pass

    # Exit a parse tree produced by my_grammarParser#arglist.
    def exitArglist(self, ctx:my_grammarParser.ArglistContext):
        pass


    # Enter a parse tree produced by my_grammarParser#argument.
    def enterArgument(self, ctx:my_grammarParser.ArgumentContext):
        pass

    # Exit a parse tree produced by my_grammarParser#argument.
    def exitArgument(self, ctx:my_grammarParser.ArgumentContext):
        pass


    # Enter a parse tree produced by my_grammarParser#compound_stmt.
    def enterCompound_stmt(self, ctx:my_grammarParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#compound_stmt.
    def exitCompound_stmt(self, ctx:my_grammarParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#for_stmt.
    def enterFor_stmt(self, ctx:my_grammarParser.For_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#for_stmt.
    def exitFor_stmt(self, ctx:my_grammarParser.For_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#while_stmt.
    def enterWhile_stmt(self, ctx:my_grammarParser.While_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#while_stmt.
    def exitWhile_stmt(self, ctx:my_grammarParser.While_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#loop_suite.
    def enterLoop_suite(self, ctx:my_grammarParser.Loop_suiteContext):
        pass

    # Exit a parse tree produced by my_grammarParser#loop_suite.
    def exitLoop_suite(self, ctx:my_grammarParser.Loop_suiteContext):
        pass


    # Enter a parse tree produced by my_grammarParser#if_stmt.
    def enterIf_stmt(self, ctx:my_grammarParser.If_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#if_stmt.
    def exitIf_stmt(self, ctx:my_grammarParser.If_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#else_stmt.
    def enterElse_stmt(self, ctx:my_grammarParser.Else_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#else_stmt.
    def exitElse_stmt(self, ctx:my_grammarParser.Else_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#stmt.
    def enterStmt(self, ctx:my_grammarParser.StmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#stmt.
    def exitStmt(self, ctx:my_grammarParser.StmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#context_stmt.
    def enterContext_stmt(self, ctx:my_grammarParser.Context_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#context_stmt.
    def exitContext_stmt(self, ctx:my_grammarParser.Context_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#simple_stmt.
    def enterSimple_stmt(self, ctx:my_grammarParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#simple_stmt.
    def exitSimple_stmt(self, ctx:my_grammarParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#import_stmt.
    def enterImport_stmt(self, ctx:my_grammarParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#import_stmt.
    def exitImport_stmt(self, ctx:my_grammarParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#dotted_name.
    def enterDotted_name(self, ctx:my_grammarParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by my_grammarParser#dotted_name.
    def exitDotted_name(self, ctx:my_grammarParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by my_grammarParser#funcdef_stmt.
    def enterFuncdef_stmt(self, ctx:my_grammarParser.Funcdef_stmtContext):
        pass

    # Exit a parse tree produced by my_grammarParser#funcdef_stmt.
    def exitFuncdef_stmt(self, ctx:my_grammarParser.Funcdef_stmtContext):
        pass


    # Enter a parse tree produced by my_grammarParser#suite.
    def enterSuite(self, ctx:my_grammarParser.SuiteContext):
        pass

    # Exit a parse tree produced by my_grammarParser#suite.
    def exitSuite(self, ctx:my_grammarParser.SuiteContext):
        pass


