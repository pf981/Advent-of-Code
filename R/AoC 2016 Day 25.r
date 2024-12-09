library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    instruction = str_extract(line, "^\\w+"),
    x = str_extract(line, "(?<= )-?\\w+"),
    y = str_extract(line, "-?\\w+$")
  )
df

Rcpp::cppFunction('
bool is_clock(std::vector<std::string> instructions, std::vector<std::string> xs, std::vector<std::string> ys, int a) { 
    std::unordered_map<std::string, int> registers;
    registers["a"] = a;

    int clock_i = 0;

    auto getValue = [&registers] (const std::string& s) {
      try {
        return std::stoi(s);
      }
      catch (...) {
        return registers[s];
      }
    };

    for(int line = 0; line < instructions.size(); ++line) {
        const std::string& instruction = instructions[line];
        const std::string& x = xs[line];
        const std::string& y = ys[line];

        if (instruction == "cpy") {
           try {
            registers[y] = getValue(x);
          }
          catch (...) {
            // If y is a number (from tgl making an invalid cpy command), dont do anything
          }
          
        }
        else if (instruction == "inc") {
          ++registers[x];
        }
        else if (instruction == "dec") {
          --registers[x];
        }
        else if (instruction == "jnz")  {
          if (getValue(x) != 0) {
            line = line + getValue(y) - 1;
          }
        }
        else if (instruction == "tgl")  {
          int target_i = line + getValue(x);

          if (target_i < 0 || target_i >= instructions.size()) continue;

          std::string& target_instruction = instructions[target_i];
          if (target_instruction == "inc") {
            target_instruction = "dec";
          }
          else if (target_instruction == "dec" || target_instruction == "tgl") {
            target_instruction = "inc";
          }
          else if (target_instruction == "jnz") {
            target_instruction = "cpy";
          }
          else if (target_instruction == "cpy") {
            target_instruction = "jnz";
          }
        }
        else if (instruction == "out")  {
          if (clock_i % 2 != getValue(x)) return false;
          
          if (clock_i >= 100) return true;

          ++clock_i;
        }
    }

    return false;
} 
')

for (answer in seq_len(100000)) {
  if (is_clock(df$instruction, df$x, df$y, i)) break
}
answer

# No puzzle here - just need 49 stars.
