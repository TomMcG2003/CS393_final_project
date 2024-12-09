-- Create Person Table
CREATE TABLE Person (
    person_id VARCHAR(50) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    birthCity VARCHAR(50),
    birthCountry VARCHAR(50),
    weight INT,
    height INT
);

-- Create Team Table
CREATE TABLE Team (
    team_id VARCHAR(50) PRIMARY KEY,
    teamName VARCHAR(50) NOT NULL
);

-- Create TeamStats Table
CREATE TABLE TeamStats (
    teamstats_id SERIAL PRIMARY KEY,
    team_id VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    wins INT NOT NULL,
    losses INT NOT NULL,
    rank INT NOT NULL,
    divWinner VARCHAR(50),
    wcWinner VARCHAR(50),
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
);

-- Create Pitching Table
CREATE TABLE Pitching (
    pitching_id SERIAL PRIMARY KEY,
    person_id VARCHAR(50) NOT NULL,
    team_id VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    wins INT,
    loss INT,
    games INT,
    saves INT,
    shutouts INT,
    strikeouts INT,
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
);

-- Create Batting Table
CREATE TABLE Batting (
    batting_id SERIAL PRIMARY KEY,
    person_id VARCHAR(50) NOT NULL,
    team_id VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    hits INT,
    doubles INT,
    triples INT,
    homeruns INT,
    strikeouts INT,
    atbats INT,
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
);

-- Create Fielding Table
CREATE TABLE Fielding (
    fielding_id SERIAL PRIMARY KEY,
    person_id VARCHAR(50) NOT NULL,
    team_id VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    putouts INT,
    assists INT,
    errors INT,
    doublePlays INT,
    passedBalls INT,
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
);
