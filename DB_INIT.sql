CREATE TABLE WBL.manager(
    playerID VARCHAR(255) NOT NULL,
    currentYear DATE NOT NULL,
    currentTeam CHAR(3) NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    birthDay DATE,
    PRIMARY KEY(playerID),
    PRIMARY KEY (currentYear)
);

CREATE TABLE WBL.managerStats(
    playerID VARCHAR(255) NOT NULL,
    currentYear DATE NOT NULL,
    team CHAR(3) NOT NULL,
    wins INT,
    losses INT,
    winsToLossPer FLOAT,
    ties INT,
    games INT,
    awards VARCHAR(255),
    PRIMARY KEY(playerID),
    PRIMARY KEY (currentYear),
    FOREIGN KEY(playerID) REFERENCES WBL.manager(playerID)
);

CREATE TABLE WBL.player(
    playerID VARCHAR(255) NOT NULL,
    currentYear DATE NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    team CHAR(3),
    offensiveStats VARCHAR(255),
    defensiveStats VARCHAR(255),
    pitchingStats VARCHAR(255),
    salary FLOAT,
    leauge CHAR(2),
    PRIMARY KEY (playerID),
    PRIMARY KEY (currentYear),
    FOREIGN KEY (offensiveStats) REFERENCES WBL.offsensiveStats (playerID),
    FOREIGN KEY (defensiveStats) REFERENCES WBL.defensiveStats (playerID),
    FOREIGN KEY (pitchingStats) REFERENCES WBL.pitchingStats (playerID)
);

CREATE TABLE WBL.pitchingStats(
    playerID VARCHAR(255) NOT NULL,
    currentYear DATE NOT NULL,
    wins INT,
    losses INT,
    winsToLossPer FLOAT,
    era FLOAT,
    games INT,
    gamesStarted INT,
    gamesFinshed INT,
    completeGames INT,
    shutouts INT,
    saves INT,
    inningsPitched FLOAT,
    strikeOuts INT,
    hbp INT,
    balks INT,
    wildPitches INT,
    br INT,
    eraPlus INT, 
    fip INT,
    whip INT,
    hitsPerNine FLOAT,
    HomeRunsPerNine FLOAT,
    walksPerNine FLOAT,
    strikeOutsPerNine FLOAT,
    strikeOutsToWalks FLOAT,
    awards VARCHAR(255),
    PRIMARY KEY (playerID),
    PRIMARY KEY (currentYear)
);

CREATE TABLE WBL.offensiveStats(
    playerID VARCHAR(255) NOT NULL,
    currentYear DATE NOT NULL,
    age INT,
    games INT,
    plateApp INT,
    atbats INT,
    runs INT,
    hits INT,
    doubles INT,
    triples INT,
    homeRuns INT,
    rbi INT,
    stolenBases INT,
    caughtStealing INT,
    walks INT,
    strikeOUts INT,
    battingEAverage FLOAT,
    onBasePer FLOAT,
    slugging FLOAT,
    ops FLOAT,
    opsLus INT,
    tb INT,
    gdp INT,
    hbp INT, 
    sh INT,
    sf INT,
    intentionalWalks INT,
    pos VARCHAR(255),
    awards VARCHAR(255),
    rOBA FLOAT,
    rBatPlus INT,
    baBIP FLOAT,
    iso FLOAT,
    hrPer FLOAT,
    soPer FLOAT,
    bbPer FLOAT,
    ev FLOAT,
    hardHitPer FLOAT,
    idPer FLOAT,
    bgPer FLOAT,
    gbPer FLOAT,
    fbPer FLOAT,
    gbTofbPer FLOAT,
    pullPer FLOAT,
    centPer FLOAT,
    oppoPer FLOAT,
    wpa FLOAT,
    cWPA FLOAT,
    reTwoFour FLOAT,
    rsPer FLOAT,
    sbPer FLOAT,
    sbPer FLOAT,
    sbtPer FLOAT,
    PRIMARY KEY (playerId),
    PRIMARY KEY (currentYear)
);

CREATE TABLE WBL.defensiveStats(
    playerID VARCHAR(255) NOT NULL,
    currentYear DATE NOT NULL,
    age INT, 
    pos CHAR(3),
    games INT,
    gamesStarted INT,
    completeGames INT,
    innings FLOAT,
    ch INT,
    po INT,
    a INT,
    errors INT,
    n FLOAT,
    fieldingPer FLOAT,
    rtot INT,
    rdrs INT,
    rtotPerYear INT,
    rdrsPerYear INT,
    rfPerNine FLOAT,
    rfPerGame FLOAT,
    lgFLDPer FLOAT,
    lgRFGNine FLOAT,
    pb INT,
    wp INT,
    sb INT,
    csPer FLOAT,
    lgCSPer FLOAT,
    po INT, 
    awards VARCHAR(255),
    PRIMARY KEY (playerID),
    PRIMARY KEY (currentYear)
);

CREATE TABLE WBL.schedule(
    team CHAR(3) NOT NULL,
    currentYear DATE NOT NULL,
    game VARCHAR(255),
    PRIMARY KEY (team),
    PRIMARY KEY (currentYear),
    FOREIGN KEY (game) REFERENCES WBL.games(gameID)
);

CREATE TABLE WBL.games(
    gameID INT NOT NULL AUTO_INCREMENT,
    homeTeam CHAR(3) NOT NULL,
    awayTeam CHAR(3) NOT NULL,
    gameDate DATE,
    homeWinner BOOL,
    homeScore INT,
    awayScore INT,
    innings INT,
    winningPitcher VARCHAR(255),
    loosingPitcher VARCHAR(255),
    savingPitcher VARCHAR(255),
    dayGame BOOL,
    attendance INT,
    cLI INT,
    streak INT,
    PRIMARY KEY (gameID),
    FOREIGN KEY (homeTeam) REFERENCES WBL.teams(teamID),
    FOREIGN KEY (awayTeam) REFERENCES WBL.teams(teamID),
    FOREIGN KEY (winningPitcher) REFERENCES WBL.players(playerID),
    FOREIGN KEY (loosingPitcher) REFERENCES WBL.players(playerID),
    FOREIGN KEY (savingPitcher) REFERENCES WBL.players(playerID)
);

CREATE TABLE WBL.Leauge (
    leaugeID CHAR (2) NOT NULL,
    teamID CHAR(3) NOT NULL,
    PRIMARY KEY (leaugeID),
    FOREIGN KEY (teamID) REFERENCES WBL.teams (teamID)
);

CREATE TABLE WBL.teams(
    teamID CHAR (3) NOT NULL,
    currentYear DATE NOT NULL,
    player VARCHAR(255),
    PRIMARY KEY (teamID),
    PRIMARY KEY (currentYear),
    FOREIGN KEY (player) REFERENCES WBL.players(playerID)
);

CREATE TABLE WBL.career(
    player VARCHAR(255) NOT NULL,
    PRIMARY KEY (player)
);