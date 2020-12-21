# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/19

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- '0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
'

# COMMAND ----------

split_strs <- input %>% str_split("\n\n") %>% unlist() %>% map(read_lines)
split_strs

# COMMAND ----------

rules <-
  split_strs[[1]] %>%
  as_tibble() %>%
  separate(value, c("rule_id", "value"), ": ") %>%
  mutate(
    rule_id = as.integer(rule_id)
  )
rules

# COMMAND ----------

char_rules <-
  rules %>%
  filter(str_detect(value, '"')) %>%
  mutate(value = str_replace_all(value, '"', ""))
char_rules

# COMMAND ----------

nested_rules <-
  rules %>%
  anti_join(char_rules, by = "rule_id") %>%
  mutate(
    value = str_split(value, fixed(" | "))
  ) %>%
  unnest(value) %>%
  mutate(
    value = str_split(value, " ") %>% map(as.integer)
  )
nested_rules

# COMMAND ----------

messages <- split_strs[[2]] %>% enframe(name = "message_id")
messages

# COMMAND ----------

check_match <- function(message_str, check_rule_id) {
  if (check_rule_id %in% char_rules$rule_id) {
    match_char <- char_rules %>% filter(rule_id == check_rule_id) %>% pull(value)
    return(tibble(
      is_match = str_detect(message_str, match_char),
      message_str = str_replace(message_str, match_char, "")
    ))
  }
  
  nested_rules_df <- nested_rules %>% filter(rule_id %in% check_rule_id)
  
  if (nrow(nested_rules_df) == 0) {
    stop(paste0("Unknown rule id: ", check_rule_id))
  }
  
  for (rule_group in seq_len(nrow(nested_rules_df))) {
    cur_message_str <- message_str
    is_done <- TRUE
    
    for (individual_rule in unlist((slice(nested_rules_df, rule_group)$value))) {
      
      message(paste0(individual_rule, ": ", cur_message_str))
      #debug <- paste0(individual_rule, ": ", cur_message_str)
      
      result <- check_match(cur_message_str, individual_rule)
      
      #debug <- paste0(debug, "; ", result$is_match) # This will display stuff out of order
      #message(debug)
      
      if (result$is_match) {
        cur_message_str <- result$message_str
      } else {
        is_done <- FALSE
        break
      }
    }
    if (nchar(cur_message_str) == 0 && is_done) {
      return(tibble(
        is_match = TRUE,
        message_str = cur_message_str
      ))
    }
  }
  
  tibble(
    is_match = FALSE,
    message_str = NA
  )
}
# The issue is that cur_message_str is restoring characters when it shouldnt'. Not sure why though

# COMMAND ----------

# MAGIC %md I think a better approach is to just figure out how many a's etc for each rule.

# COMMAND ----------

check_match(messages$value[[1]], 0)

# COMMAND ----------

message_str <- messages$value[[1]]
rule_group = 0
message_str

# COMMAND ----------

cur_message_str <- message_str
    is_done <- TRUE
    
    for (individual_rule in unlist((slice(nested_rules_df, rule_group)$value))) {
      result <- check_match(cur_message_str, individual_rule)
      
      if (result$is_match) {
        cur_message_str <- result$message_str
      } else {
        is_done <- FALSE
        break
      }
    }
    if (nchar(cur_message_str) == 0 && is_done) {
      return(tibble(
        is_match = TRUE,
        message_str = cur_message_str
      ))
    }

# COMMAND ----------

check_match(messages$value[[1]], 3)

# COMMAND ----------

message_str

# COMMAND ----------

nested_rules_df <- nested_rules %>% filter(rule_id %in% 0)

# COMMAND ----------

unlist((slice(nested_rules_df, 1)$value))

# COMMAND ----------

nested_rules_df

# COMMAND ----------

check_match(messages$value[[1]], 0)

# COMMAND ----------

result <- map_dfr(messages$value, check_match, check_rule_id = 0)

# COMMAND ----------

result