This is a sample for how your article md file should look, (everything below this line)

Title: Post Title
Author: Post Author
Date: Post Date
Category: Post category
Tags: Tags Related to post
Slug: This is how the page will display in the search bar

#Working with Markdown and this website
This site is built using Pelican which is a static site generator built with Python. The beauty about this is that it use Markdown files and automatically renders the markdown files in html. This post will show you what you need for the file to render the way you want on the website. 

#Metadata
This is the first part of the file and contains all the information that will be used to render the files where they should be on the website. 
There are 5 key pieces of information that are needed:

```console
Title: 
Author:
Date:
Category:
Tags:
Slug:
```

Title - This will be the name of your page. It is case sensitive.
Author - This will be the author of the post. While it will not be on the site, it is required and will provide future editors with a name to the original post.
Date: This date will be the date and time that you set it to. It is in the format of YYYY-DD-MM HH:MM:ss
Category: This will be the main theme of your post. For example Scratch, Open CV, Pyhton, Java etc. If you are unsure about this, please talk to Emlyn or Amy about this. This variable is used to display your post under the Tutorials tab.
Tags: These are key words related to the post. These can be anything. Try to add atleast 3 tags.
Slug: This is how the page will appear in the url search bar. Generally if there are spaces it-will-be-broken-like-so.

There are two other metadata keywords that can be used. 

```console
Series: 
Series_index:
```

If your work is part of a greater series you would use these keywords. 
Series: This will be the name of the Series, for example, Beginner Scratch, Introduction to Python etc.
Series_index: this is current file number in the series, for example, if there are 5 parts in the series and this is the first part, Series_index: 1 


#Content
After writing your metadata you can get to work on your page content. In general you can use all markdown features. Below is a list of common commands in Markdown.

Basic markdown examples are shown below

This text is **bold**
This text is also __bold__

This text is *italic*
This text is also _italic_

This text is **_italic and bold_**
This text is also ___bold and italic___
# An h1 heading
## An h2 heading
### An h3 heading...
###### An h6 heading

A list with numbers:
1. One
2. Two
3. Three

A list with bullets:
* Bullet
* Bullet
* Bullet

Here's a blockquote:

&gt; Simple is better than complex

Here's a table:

| Column1 | Column 2 | Column 3|
|-----|-----|-----|
| Value 1 | Value 2 | Value 3 |
| Value 4 | Value 5 | Value 6 |
| Value 7 | Value 8 | Value 9 |





Images can be displayed in Markdown.  
Text within the square brackets is the image name. The path to the image goes between the round brackets.  
The {static} tag indicates the image is stored in the content folder. This setting can be changed in pelicanconf.py.

![python logo]({static}/img/python_icon.png)

Links to downloadable content such as PDF files are written similarly to image files but with no ! symbol at the beginning.

[Pelican Documenation]({static}/pdf/pelican.pdf)

A link to a different blog post on our website is written exactly the same.  
Text within the square brackets can be clicked on to travel to the website between the curly brackets.
The {filename} tag indicates we want to follow the link to a webpage rather than the static file it was generated from.

[First Post]({filename}/articles/first_post.md)

Or we can link to another external website by supplying the web address.

[Python Package Index](https://pypi.org)