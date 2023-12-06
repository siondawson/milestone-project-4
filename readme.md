# Milestone Project 4 - Absolute Zero Viola Quartet

## Purpose

This website was created for Code Institue's Milestone Project 4 assignment. The purpose of the project is to demonstrate an understanding of full stack web development with the creating of a Django app, which will include fully automated e-commerce functioniality. A full list of technologies used can be found in the technologies section fo this readme.

## Absolute Zero Viola Quartet Responsive Website

For this project I have chosen to understake a full redesign of Absolute Zero Viola Quartet's website. Their current website is built with wordpress by one of the band memebers who is not a web developer.

This project will cater to two distinct sets of users needs.

1) Sheetmusic Store:
* To sell their viola quartet arrangements via a fully automated e-commerce store.
2) Web presence for the band:
* Advertise upcoming concerts.
* Promote the band to promoters and concert organisers.
* Information about the band and its musicians.


## Web store

Absolute Zero Viola Quartet create their own arrangements of popular classical pieces. Their current website has a functioning sheet music store where users may select and buy sheet music, with one major issue: once paid for users must wait for a member of the band to email their purchases to them in the form of a pdf file. My redesign will generally improve the webstore user experience and add one key feature:

Once users have paid for an arragement it will be available for them to download. If a user loses the pdf, they may log back in to the website and download again.

The webstore was largely created by following code institutes 'Boutique Ado' project. This was modfied to suit the needs of Absolute Zero.

# Apps

## Band App

An app for all content for the band itself: info, videos, concert listings, biographies.

### Index Page (Home)

On loading the home page users are presented with a banner consisting of a graphic of viola scrolls, the bands name and ensemble type. Immidately below this is an iframe with a embedded youtube video that users may play to know what the band looks and sounds like. Below the video is a sub heading informing users of when the band was formed and a paragraph with some initial information on the band. 

This fulfils users stores x 

The user is presented with a button linking to the 'about' page where they may learn more about the band and its members. 

Below is another sub heading before bootstrap cards present the user with a list of the bands upcoming performances. Each card is populated via the database and contains basic information on each performance: date, time, venue, city/towm and a ticket link. As most venue handle ticket sales internally or via an external ticket source a link is provided to the user. 

This fulfils user stories

### About page

A simple page which provides a space for more in depth information on the band, aswell as an image and personal biography of each member. Member information is populated by the database and can only be modified via the django admin panel.

This fulfils user stories x 

### Band app for superusers

Superusers, defined as a band manager have access to spesific functionality within the band app to add, delete and update concert listings. Superusers are provided a button at the bottom of the page. Think links to the 'add_concert' page where the superuser may fill out the form provided to add a new concert. 

In addition superusers may edit or delete concert listings via the concert listing bootstrap cards themselves. Appropriately colored 'Edit' and 'Delete' buttons are provided so the superuser may easily edit or delete concert listings. The edit button links to a similar form to the 'add_concert' form which is pre populated with the data for the concert they have selected to edit. The delete link is protected with a modal which warns the superuser on click that deleting the concert is pernament. 

This functionality fulfils user stories xx x x x 

## sendemail app

An app to provide users with a simple contact form to send a message or enquiry. Accessible at all times via the main nav bar. The contact form has been designed with a general purpose in mind so all users who wish to send a message can use it, wether they are making a performance enquiry or enquiring about an order or have another question. 

The users name, email address a message are required by the form. The user may also leave their contact number in an optional field. 

This fulfils user stories x x x x xx 

The contact form styling is based on the 'love running' project, a styling I have employed previously in my milestone project 1 submission. 

## sheetmusic app
