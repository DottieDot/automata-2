use antlr_rust::tree::{TerminalNode, ParseTreeVisitor};

use crate::gen::{DotLangParserContextType, DotLangVisitor};

pub struct MyDotLangVisitor<'i> {
  field1: Vec<&'i str>
}

impl<'i> MyDotLangVisitor<'i> {}

impl<'i> ParseTreeVisitor<'i, DotLangParserContextType> for MyDotLangVisitor<'i> {
  fn visit_terminal(&mut self, _node: &TerminalNode<'i, DotLangParserContextType>) {}

  fn visit_error_node(
    &mut self,
    _node: &antlr_rust::tree::ErrorNode<'i, DotLangParserContextType>
  ) {
  }
}

impl<'i> DotLangVisitor<'i> for MyDotLangVisitor<'i> {
  fn visit_compile_unit(&mut self, ctx: &crate::gen::Compile_unitContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_scoped_expr(&mut self, ctx: &crate::gen::Scoped_exprContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_int_literal(&mut self, ctx: &crate::gen::Int_literalContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_function_decl(&mut self, ctx: &crate::gen::Function_declContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_parentheses(&mut self, ctx: &crate::gen::ParenthesesContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_not(&mut self, ctx: &crate::gen::NotContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_comparison(&mut self, ctx: &crate::gen::ComparisonContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_conjunction(&mut self, ctx: &crate::gen::ConjunctionContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_read_variable(&mut self, ctx: &crate::gen::Read_variableContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_multiply_divide(&mut self, ctx: &crate::gen::Multiply_divideContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_function_call(&mut self, ctx: &crate::gen::Function_callContext<'i>) {
    self.visit_children(ctx)
  }

  fn visit_add_subtract(&mut self, ctx: &crate::gen::Add_subtractContext<'i>) {
    self.visit_children(ctx)
  }
}
