insert into users(user_id, login, password, email, phone, repo_count) values (1, 'test', 'test', 'test', 'test', 1);
insert into users(user_id, login, password, email, phone, repo_count) values (2, 'test1', 'test1', 'test1', 'test1', 2);
insert into users(user_id, login, password, email, phone, repo_count) values (3, 'test2', 'test2', 'test2', 'test', 3);

insert into repo(repo_id, user_id, name, deep_link, related_link, language) values (1, 1, 'test2', 'test2', 'test2', 'python');
insert into repo(repo_id, user_id, name, deep_link, related_link, language) values (2, 1, 'test2', 'test2', 'test2', 'js');
insert into repo(repo_id, user_id, name, deep_link, related_link, language) values (3, 2, 'test2', 'test2', 'test2', 'js');

insert into doc(doc_id, repo_id, path, format) values (1, 1, 'test2', 'test2');
insert into doc(doc_id, repo_id, path, format) values (2, 2, 'test2', 'test2');
insert into doc(doc_id, repo_id, path, format) values (3, 2, 'test2', 'test2');

insert into note(note_id, repo_id, meta_data, body) values (1, 2, 'test2', 'test2');
insert into note(note_id, repo_id, meta_data, body) values (2, 2, 'test2', 'test2');
insert into note(note_id, repo_id, meta_data, body) values (3, 2, 'test2', 'test2');