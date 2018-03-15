-- Find the names of the individual animals that eat fish.
--
-- The animals table has columns (name, species, birthdate) for each individual.
-- The diet table has columns (species, food) for each food that a species eats.

select name from animals, diet where animals.species = diet.species and diet.food = "fish";
