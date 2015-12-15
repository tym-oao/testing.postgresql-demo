# Presentation notes

1. run demo setup script
1.1 Introduce basic idea: a temp Postgres instance that deletes itself after tests finish
1.2 Show minimal Dockerfile
 
2. su postgres, then python interactive import testing.postgresql and start Postgresql instance.
3. in new tmux window, show that database is setup in /tmp
4. stop the testing instance and show that it's gone.

5. show demo.py PostgresDemo code
6. show test_demo.py
7. run test_demo with -v

8. point out that test_select has insert_fixture in test_select
9. explain and demo the factory class
10. pip install git+https://github.com/tk0miya/testing.postgresql.git
10.1 show test_demo1 code and run

pip3 install --upgrade git+https://github.com/tk0miya/testing.postgresql.git

