CREATE TABLE Task  (id			SERIAL PRIMARY KEY,
    		    name		VARCHAR(20)
		    description		TEXT,
		    stage		VARCHAR(4),
		    startTime		TEXT,
		    exptCompTime	TEXT,
		    actCompTime		TEXT
    );

CREATE TABLE Users (userId	SERIAL PRIMARY KEY,
  		    fname	VARCHAR(10),
		    lname	VARCHAR(10),
		    email	VARCHAR(30),
		    gitname	VARCHAR(20)
    );

CREATE TABLE Logs  (taskId	SERIAL,
  		    contributor	SERIAL REFERENCES Users (userId),
		    action	TEXT,
		    time	TEXT,
		    comments	TEXT,
		    PRIMARY KEY(taskId, time)
    );

ALTER TABLE Logs ADD FOREIGN KEY (taskId) REFRENCES Task(id);

