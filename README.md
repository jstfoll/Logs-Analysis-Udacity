# Logs-Analysis-Udacity
Install vagrant and virtual box
then put the newsdata.sql file in the vagrant folder
make sure python is installed with all the required packages(psycopg2)
Then navigate to vagrant folder and make the following commands

vagrant up
vagrant ssh
cd /vagrant

load the database
psql -d news -f newsdata.sql

connecting to database
psql -d news

create view article_view as select title,author,count(*) as views from articles,log where log.path like concat('%',articles.slug) group by articles.title,articles.author order by views desc;

create view error_view as select date(time),round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time) order by "Percent Error" desc;

Then run logs using the following command
python/python3 logs.py
