#
# Insert a newborn baby opossum into the animals table and verify that it's
# been added. To do this, fill in the rest of SELECT_QUERY and INSERT_QUERY.
#
# SELECT_QUERY should find the names and birthdates of all opossums.
#
# INSERT_QUERY should add a new opossum to the table, whose birthdate is today.
# (Or you can choose any other date you like.)
#
# The animals table has columns (name, species, birthdate) for each individual.
#

SELECT_QUERY ='''
select name, birthdate from animals where species = "opossum";'''

INSERT_QUERY ='''
insert into animals values('Giggles', 'opossum', '2018-03-14');'''
