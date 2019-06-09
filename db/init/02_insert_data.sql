\connect alcohol_suggest higher68

INSERT INTO settings(
  past_length
  , candidate_num
  , alcohol_consumption_lower_limit
  , drink_days_upper_limit
  , ml_of_1glass
  , number_of_output_upper_limit
)
VALUES (
  2    -- past_length: unit=year
  , 5  -- candidate_num unit=prefecture
  , 0  -- alcohol_consumption_lower_limit
  , 7  -- drink_days_upper_limit
  , 350 -- ml_of_1glass
  , 47 -- number_of_output_upper_limit
)
