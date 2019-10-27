CREATE TABLE users (
        user_id INTEGER NOT NULL,
        login VARCHAR(20),
        password VARCHAR(20),
        email VARCHAR(20),
        phone VARCHAR(20),
        repo_count INTEGER,
        PRIMARY KEY (user_id)
);

CREATE TABLE repo (
        repo_id INTEGER NOT NULL,
        user_id INTEGER,
        name VARCHAR(30),
        deep_link VARCHAR(50),
        related_link VARCHAR(50),
        PRIMARY KEY (repo_id),
        FOREIGN KEY(user_id) REFERENCES users (user_id)
);

CREATE TABLE note (
        note_id INTEGER NOT NULL,
        repo_id INTEGER,
        meta TEXT,
        body TEXT,
        PRIMARY KEY (note_id),
        FOREIGN KEY(repo_id) REFERENCES repo (repo_id)
);

CREATE TABLE doc (
        doc_id INTEGER NOT NULL,
        repo_id INTEGER,
        path VARCHAR(50),
        format VARCHAR(30),
        PRIMARY KEY (doc_id),
        FOREIGN KEY(repo_id) REFERENCES repo (repo_id)
);
