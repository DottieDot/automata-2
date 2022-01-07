use std::env;
use std::error::Error;
use std::process::Command;

fn main() {
  let antlr_path = "./vendor/antlr4.jar";

  gen_for_grammar("./DotLang.g4", antlr_path, "./src/gen", Some("-visitor"))
    .unwrap();

  println!("cargo:rerun-if-changed=build.rs");

  println!("cargo:rerun-if-changed={}", antlr_path);
}

fn gen_for_grammar(
  grammar_file_name: &str,
  antlr_path: &str,
  output_path: &str,
  additional_arg: Option<&str>
) -> Result<(), Box<dyn Error>> {
  let file_name = grammar_file_name.to_owned();
  let dir = env::current_dir()?;

  let _ = Command::new("java")
    .current_dir(dir)
    .arg("-cp")
    .arg(antlr_path)
    .arg("org.antlr.v4.Tool")
    .arg("-Dlanguage=Rust")
    .arg("-o")
    .arg(output_path)
    .arg(&file_name)
    .args(additional_arg)
    .spawn()?
    .wait_with_output()?;

  println!("cargo:rerun-if-changed={}", file_name);

  Ok(())
}
