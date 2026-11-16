CREATE DATABASE R6Impact;

USE R6Impact;

CREATE TABLE matches (
	match_id INT PRIMARY KEY,
    tournament VARCHAR(20),
    match_date DATE,
    source_file TEXT
    );

CREATE TABLE kill_events (
	-- event_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT, -- FK
    map_no INT,
    map TEXT,
    round_no INT,
    elapsed_s REAL,
    clock_left_s INT,
    defuser_clock_left_s INT,
    killer TEXT,
    killer_team TEXT,
    killer_side TEXT,
    killer_operator TEXT,
    victim TEXT,
    victim_team TEXT,
    victim_side TEXT,
    victim_operator TEXT,
    headshot BOOL, -- In CSV this is 1 or 0 so will have to convert to bool using python
    post_plant BOOL,
    Weapon TEXT,
    kill_method TEXT,
    weapon_exact BOOL,
    is_first_kill BOOL,
    traded BOOL,
    traded_by TEXT,
    alive_atk_before INT,
    alive_def_before INT,
    kill_situation TEXT
    );
    
    CREATE TABLE round_results (
    match_id INT,
    map_no INT,
    round_no INT,
    attacking_team TEXT,
    defending_team TEXT,
    winner TEXT,
    win_condition TEXT,
    PRIMARY KEY (match_id, map_no, round_no)
    );
    
    DROP TABLE kill_events;
    
   -- Importing data from pandas dataframe csv output
    LOAD DATA LOCAL INFILE "C:\\Users\\jburj\\R6Impact\\Data\\concatData.csv"
    INTO TABLE kill_events
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
    
  SELECT * FROM kill_events;  
    
    
    