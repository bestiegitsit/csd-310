/*
Title: whatabook_program_queries.sql
Author: Ashley Tharp
Date: 28 February 2022
description: WhatABook program queries
*/

/* select query to view a users wishlist items */
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

/* select query to view the store's location */
SELECT store_id, locale from store;

/* select query to view a full listing of the books offered */
SELECT book_id, book_name, author, details from book;

/* select query to view book listings not already in a wishlist.
The value will change based on the input from the user */
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1);

/* insert statement to add a new book to a users wishlist based on selected values */
INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 9)

/* remove a selected book from the user's wishlist */
DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;