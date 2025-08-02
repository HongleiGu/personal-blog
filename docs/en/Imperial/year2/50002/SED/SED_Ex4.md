---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# refactor to builder pattern

the builder pattern happens when we got many nullable parameters to init with, we dont want to pass all of them in the constructor as we need to type a bunch of nulls

so we do this

```java
package ic.doc;

public class BookSearchQueryBuilder {
  private String firstname = null;
  private String surname = null;
  private String title = null;
  private Integer publishedAfter = null;
  private Integer publishedBefore = null;

  public static BookSearchQueryBuilder books() {
    return new BookSearchQueryBuilder();
  }

  public BookSearchQueryBuilder withFirstname(String firstname) {
    this.firstname = firstname;
    return this;
  }

  public BookSearchQueryBuilder withSurname(String surname) {
    this.surname = surname;
    return this;
  }

  public BookSearchQueryBuilder withTitle(String title) {
    this.title = title;
    return this;
  }

  public BookSearchQueryBuilder publishedAfter(Integer publishedAfter) {
    this.publishedAfter = publishedAfter;
    return this;
  }

  public BookSearchQueryBuilder publishedBefore(Integer publishedBefore) {
    this.publishedBefore = publishedBefore;
    return this;
  }

  public BookSearchQuery build() {
    return new BookSearchQuery(firstname, surname, title, publishedAfter, publishedBefore);
  }
}
```

then we can do

```java
List<Book> books = books().withSurname("dickens").build().execute();
```
# singleton
but currently we initialize the db everytime, this would cause alot of unnecessary memory usage

so we also try the singleton pattern

first, we make the constructor private, all the classes and functions should get the singleton with a static method

#

there is still some coupling between the books and the , because we are using the singleton directly

we could

- set a constructor parameter
- set a parameter to the query search

so we extract an interface and pass it in to the function

# mocking, 

but we dont want to really init something, it is costy

so we mock
